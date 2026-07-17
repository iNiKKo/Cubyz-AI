# Cubyz Developer Judgment: What a Maintainer Actually Cares About

This document is synthesized from reading all 649 real GitHub PR review threads in this
project's history (crunched into `github_reviews.jsonl`), not from raw code inspection. It is
not a style guide of surface rules -- it's an attempt to internalize the recurring *judgment
patterns* Cubyz maintainers apply, so that responses (code suggestions, reviews of pasted code,
architectural advice) reflect how this specific project actually thinks, not generic "best
practices." Every section below is grounded in multiple independent real review threads; PR
numbers are cited so any claim here can be traced back to its source.

The single biggest meta-pattern across all 649 reviews: **this project strongly prefers
explicit, predictable, allocator-conscious code over clever/generic/automatic solutions**, even
when the generic solution is more DRY. "Magic" is a mild pejorative here. If you're ever unsure
which of two approaches to suggest, the more explicit and more locally-reasoned-about one is
usually the one this project's reviewers would pick.

## 1. Memory & Allocator Discipline

This is the single most common category of review comment by a wide margin. The mental model
to apply:

- **Match the allocator to the data's actual lifetime.** Stack allocator (`main.stackAllocator`)
  for data that doesn't outlive the current function/scope. World arena (`main.worldArena`) for
  data that lives as long as the current world/session. Global allocator for data that outlives
  everything. Using a stack allocator for something that needs to persist across frames, or a
  heap `dupe` for something that's discarded at function end, are both real, repeatedly-flagged
  mistakes (PR #2469, #2733, #717).
- **Never call `.free()` on a slice/pointer that came from an arena allocator.** Arenas can only
  be freed as a whole; freeing a sub-slice individually is either a no-op that misleads the
  reader or outright corrupts state (PR #2530). If code frees only *part* of what an arena owns,
  that's a bug to flag, not a style nit.
- **Every `init` needs a matching `deinit`**, and the `defer` for that `deinit` belongs
  *immediately* after the corresponding acquisition -- not "10 lines later" (PR #3276, #1225).
  A `defer` placed far from its `init` is flagged even when it's technically still correct,
  because it's fragile to future edits.
- **Resource acquisition must be paired with cleanup *before* any point where the function can
  exit early.** If parsing/validation can fail and return partway through a function, anything
  allocated before that point must already be covered by a `defer`, not cleaned up manually at
  the end (PR #1824, #2195). This is the most common actual memory-leak root cause found in
  review.
- **Always `dupe`/copy data whose lifetime you don't control** before storing it somewhere
  longer-lived than the caller's own scope -- e.g. a name string passed into a spawned thread,
  or a slice captured into a struct that outlives the call (PR #3219, #2886). Zig does not copy
  strings for you.
- **`catch unreachable` is the correct idiom, not a hack, when an allocator is structurally
  guaranteed not to fail** (`NeverFailingAllocator`, or a stack allocator sized for a known-small
  string). Catching and handling an error that cannot occur is treated as *worse* than
  `unreachable`, because it implies a false possibility to future readers (PR #2680, #398, #1125).
  Conversely, using `unreachable` for a case that genuinely *can* happen under normal
  misconfiguration (a missing structure reference, a bad user-supplied ID) is a real bug --
  replace it with a proper error return and a logged message (PR #1530).
- **Eager vs. lazy allocation is a judgment call, not a rule.** Lazy/path-based loading is
  preferred for large or rarely-touched data (entity models: store a path, load on first bind,
  PR #2680). But eager initialization is explicitly preferred when correctness or synchronization
  ordering demands it -- e.g. Vulkan resources, where lazy creation would complicate GPU sync
  (PR #2680 counter-example in the same file). Don't apply "lazy loading is better" as a blanket
  rule; ask whether deferring the work actually helps here.
- **Don't allocate more than you know you need.** Repeated doubling-growth into an arena wastes
  space that's never reclaimed until the whole arena drops; if the exact count is knowable
  upfront, allocate exactly that (PR #2195 -- this exact issue caused a real out-of-bounds bug
  from a related fix that didn't bound the loop to the actual registered count).

## 2. Concurrency & Thread Safety

- **Any field touched from more than one thread needs explicit synchronization** (mutex, or a
  genuinely atomic type) -- don't assume "it probably won't race." View-bob player fields (PR
  #665), gamepad state, and player save-on-disconnect (PR #943) were all flagged for exactly
  this.
- **A field is deliberately left non-atomic sometimes, on purpose**, specifically so the thread
  sanitizer will catch a real race during testing rather than the code silently papering over a
  design flaw with an atomic wrapper (PR #943). Don't reflexively suggest "just make it atomic"
  -- ask whether the actual fix is proper synchronization of a *group* of related fields, since
  atomics only protect the single value they wrap, not cross-field consistency.
- **Always use `.load()`/`.store()` on atomic values** -- direct field access on an atomic is
  flagged every time it appears (PR #663, #161).
- **Shutdown/init ordering matters and is a real source of bugs**: initialize subsystems in the
  order their dependents need them (thread pool before audio, since audio's `deinit` touches the
  thread pool -- PR #3219), and don't drain/nuke a shared resource (a whole thread pool) if other
  threads may still be using parts of it -- drain only what's actually safe to drain (PR #3219).
- **Save-on-disconnect must happen after all in-flight updates finish**, not concurrently with
  them -- move save logic into the deinitialization path rather than triggering it eagerly on
  disconnect notice (PR #943).

## 3. Type System & API Design

- **Use `union(enum)` for genuinely distinct cases; don't fake it with an enum plus parallel
  optional fields.** A union variant should represent a real alternative, not "this enum value
  plus sometimes-present data bolted on" (PR #2770, #2987, #3060 -- this exact refactor,
  enum+bool soup → tagged union, recurs across many unrelated PRs).
- **Encode invariants in the type system, not in comments.** The canonical example: a coordinate
  that's sometimes absolute and sometimes relative was originally one struct with a comment
  explaining which; the fix was a tagged union so the distinction is enforced by the compiler,
  not documentation (PR #3103).
- **Prefer optional types (`?T`) over sentinel values or magic numbers for "absent."** A
  `no_value` enum variant, a `0` that secretly means "unset," or a nullable pointer with an
  implicit "null means missing" convention are all weaker than an explicit `?T` unless there's a
  specific memory-layout reason not to (PR #1640).
- **Don't return raw pointers into a struct's internal fields** as a general access pattern --
  it's fragile to layout changes and can produce dangling pointers if the struct moves; prefer
  index-based or accessor-method access, with a separate explicit `getXPtr` only when mutation
  through a pointer is actually required (PR #2891, #1474 -- the latter specifically about a
  `SparseSet`-backed list where pointers can be invalidated by a resize).
- **Return an error or `?T` for a failure that can happen under normal misconfiguration; reserve
  `unreachable`/panics for cases an upstream invariant genuinely guarantees can't happen.** This
  distinction shows up over and over in the structure-building-block loader's evolution (PR
  #1500, #1530, #2195): early versions panicked on a missing blueprint reference, and every
  round of review pushed toward "log an error and return null/error instead," because a bad
  addon config is not the same category of bug as a genuine engine invariant violation.
- **Avoid arbitrary hardcoded limits with no documented reasoning** -- a fixed-size array with a
  magic capacity (a `[20]Node` buffer, a `maxSortedBlockProperties = 100` constant) is flagged
  specifically because *addon content can exceed it* with no growth path (PR #2824, #2063). If a
  limit is genuinely necessary, it needs an explicit justification, not just a round number.
- **Prefer growable/list-based storage over parallel dense arrays** when the active set is much
  smaller than the theoretical maximum (PR #2063's `SortedBlockProperties` refactor away from
  `[maxBlockCount]bool` arrays for properties most blocks don't have).

## 4. Avoiding Over-Engineering

- **Don't add a struct/indirection layer "for future flexibility" without a concrete present
  need.** This is rejected constantly and explicitly -- "may be redundant or harder to maintain,"
  "adds cognitive load... if it needs to grow later, refactoring is still possible" (PR #3103,
  #1207). The bar for adding abstraction is a real current requirement, not a hypothetical one.
- **Reject "magic"/implicit machinery in favor of explicit, locally-readable code** -- this
  project explicitly discussed and rejected a universal automatic struct serializer in favor of
  explicit per-type serialization functions, specifically because implicit introspection-based
  behavior is harder to debug when something goes wrong (PR #1141, #1996 -- an unusually explicit
  and long thread about exactly this tradeoff, worth treating as close to canonical for how this
  project weighs "DRY" against "explicit").
- **Simplicity is a legitimate response to a suggestion, not a cop-out.** Reviewers repeatedly
  defer a "better" approach to a future PR/issue rather than blocking or expanding the current
  one, especially near a known upcoming refactor of the same area (PR #2064, #2482, #2131).
- **"Premature optimization" and "no measurable benefit" are treated as real, valid objections**,
  not hand-waving -- e.g. rejecting a hashmap for a handful of per-frame entries in favor of a
  plain list (PR #1313), rejecting `initCapacity` precomputation that the reviewer showed doesn't
  actually change allocation count (PR #2141), rejecting a lookup table that obscures a single
  shift instruction from the optimizer without benchmark evidence (PR #2482).
- **Context changes the answer.** The same reviewers who reject unnecessary abstraction also
  explicitly *approve* added complexity when it's justified by a real constraint -- e.g. accepting
  a more complex staged/two-phase allocation specifically because the simpler version had a real
  correctness bug (PR #2195). Don't apply "prefer simple" as a dogma that overrides an actual
  demonstrated need.

## 5. Naming & Clarity

- **A name must describe what the thing actually does now, not what it used to do or partially
  resembles.** `loadWorldData` → `loadWorldConfig` because the function only ever touched static
  config, never entity data (PR #2422). `getProperty` → `setProperty` when its behavior changed
  from read to write (PR #2891). Function/variant names get renamed the moment their behavior
  diverges from what the name implies.
- **Don't leave a numeric value's unit ambiguous.** A raw `5_000_000` with no comment saying
  whether it's milliseconds, microseconds, or nanoseconds is flagged every time it appears (PR
  #2191); the preferred fix is a small typed wrapper (e.g. a `TimeDelta`-style struct) over a
  bare integer plus scattered manual conversion helpers.
- **Avoid names that collide with an existing type elsewhere in the codebase**, even in an
  unrelated module -- specifically because Zig tooling with auto-import (ZLS) can silently import
  the wrong one, and that's a real, hard-to-notice bug class, not just a style concern (PR #3104).
- **Casing conventions are enforced deliberately**: snake_case for values, PascalCase for
  types/files-that-represent-a-single-struct (PR #2515, #1237, #1284 -- e.g. a constant named
  `Air` renamed to `air` because it isn't a type).

## 6. Correctness & Defensive Detail

- **Inclusive/exclusive boundary conventions must be applied consistently and are a recurring
  source of real bugs**: `>` vs `>=` creating a dead zone between UI elements (PR #1478), min
  being inclusive while max is exclusive as an established project-wide convention that new code
  must match (PR #3111, #2825).
- **Never trust a declared size/count from network or file input without checking there's
  actually enough remaining data to back it** -- reading a varint count and then allocating based
  on it without verifying the reader has that many bytes left is a real flagged vulnerability
  class (an attacker can claim a huge count with a short payload and force a large allocation or
  crash) (PR #2469).
- **Watch for integer overflow in timestamp/counter arithmetic**; use wrapping-safe subtraction
  (`-%`) where a value could legitimately wrap (PR #2010).
- **Don't use a predictable/low-entropy source (wall-clock time) for anything where
  unpredictability actually matters** -- a world-seed generator that fell back to time-based
  entropy was flagged as trivially brute-forceable (PR #2136).
- **A double-free from mismatched ownership after a conditional reassignment is a real,
  repeatedly-found bug shape**: assign a new value over a variable that still has a pending
  `defer` cleanup pointing at the *old* value, and that old value gets freed twice or the new one
  never gets freed. Trace ownership through every branch, not just the common path (PR #1719).

## 7. PR Scope & Process Discipline

- **Keep PRs to one concern.** Bundling an unrelated rename, a style fix, or a new utility
  function into a PR whose stated purpose is something else gets explicitly split out and
  deferred, even when the added code is fine on its own merits (PR #2121, #1534, #2427, #2381).
  If you're helping someone plan a change, actively flag "this part is unrelated to your stated
  goal, consider a separate PR" the same way these reviewers do.
- **Every code path should end with an explicit, obvious return/result** -- ambiguous fallthrough
  is flagged as an invitation for future mistakes even when current behavior is correct (PR
  #2587).
- **A legitimately good but out-of-scope suggestion gets deferred to a follow-up issue**, not
  silently dropped and not force-fit into the current PR (PR #2422, #2427, #816).

## 8. Backward Compatibility & Data Format Stability

- **A change to a serialized/save format must account for existing saved data.** Adding a new
  union case that changes the byte layout, or allowing a previously-invariant field to take a
  new value (e.g. a "non-null item must have positive amount" invariant being silently broken),
  is treated as a serious issue requiring either a migration path or a redesign -- not something
  to patch around after the fact (PR #2247).
- **Public function signatures are preserved across internal refactors when possible** -- several
  large internal rewrites (thread naming, argument parsing) explicitly note that the *external*
  API/command usage stayed the same even though the internals changed completely (PR #3219,
  #3112). Prefer refactors that don't force every caller to change.

## 9. Comments, Documentation & Attribution

- **New public API surface needs a doc comment explaining purpose and, where relevant, ownership
  semantics** -- who frees what, what a null return means (PR #1425, #1425 doc-comment addition
  for a new `argparse` module).
- **When porting an algorithm from elsewhere (e.g. a ray-triangle intersection routine), link
  back to the source** -- this is about both transparency and licensing, not just courtesy (PR
  #2133).
- **Log message severity and wording must match reality.** Calling an expected, already-handled
  control-flow path an "Internal error" is flagged as actively misleading during future debugging
  -- the fix renamed it to describe what actually happened (PR #2195).
- **Redundant comments that just restate the following line are removed**, not kept for
  "clarity" (PR #1118).

## How to apply this when reviewing or writing Cubyz code

When asked to review pasted code or write new Cubyz code, actually run through these questions
in order, the way these reviewers implicitly do:

1. Does every allocation have a clear, matching, correctly-scoped deallocation? Is the allocator
   choice appropriate to the data's actual lifetime?
2. Is anything here touched from more than one thread without synchronization?
3. Could this have used a tagged union instead of an enum-plus-optional-fields? Is a fallible
   case using `unreachable`/panic where it should return an error, or vice versa?
4. Is there a new abstraction/struct/indirection layer here that isn't earning its complexity
   yet?
5. Do the names still accurately describe current behavior? Is any bare number's unit unclear?
6. Are inclusive/exclusive bounds and untrusted input sizes handled carefully?
7. Is this PR-sized change actually one concern, or does it bundle something unrelated?
8. If this touches a saved/serialized format, does it handle existing data?

This is the actual texture of how this project's maintainer reviews code -- not a generic
checklist, but a specific, consistent, opinionated engineering culture that has now been applied
across hundreds of real PRs.
