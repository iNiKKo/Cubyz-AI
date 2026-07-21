# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 1

**Type:** documentation
**Keywords:** allocator, stack allocator, world arena, global allocator, arena, defer, init, deinit, dupe, catch unreachable, NeverFailingAllocator, eager allocation, lazy allocation
**Symbols:** main.stackAllocator, main.worldArena, NeverFailingAllocator
**Concepts:** Memory & Allocator Discipline

## Summary
Section 1 of Cubyz Developer Judgment: memory and allocator discipline -- the single most common category of PR review comment by a wide margin.

## Explanation
Match the allocator to the data's actual lifetime -- this is a summary of the same lifetime-matching principle detailed with the full four-allocator breakdown (`main.globalArena`, `main.worldArena`, `main.stackAllocator`, `main.globalAllocator`) in CONTRIBUTING.md's "Choose the right allocator for the job" section: stack allocator (`main.stackAllocator`) for data that doesn't outlive the current function/scope, world arena (`main.worldArena`) for data that lives as long as the current world/session, and a global-lifetime allocator for data that outlives everything (CONTRIBUTING.md splits "global" into `main.globalArena` for game-lifetime data like mod registry data, versus `main.globalAllocator` for other lifetimes -- these are two distinct allocators, not one). Using a stack allocator for something that needs to persist across frames, or a heap `dupe` for something discarded at function end, are both real, repeatedly-flagged mistakes (PR #2469, #2733, #717).

Never call `.free()` on a slice/pointer that came from an arena allocator -- arenas can only be freed as a whole; freeing a sub-slice individually is either a no-op that misleads the reader or outright corrupts state (PR #2530).

Every `init` needs a matching `deinit`, and the `defer` for that `deinit` belongs immediately after the corresponding acquisition -- not "10 lines later" (PR #3276, #1225). A `defer` placed far from its `init` is flagged even when it's technically still correct, because it's fragile to future edits.

Resource acquisition must be paired with cleanup before any point where the function can exit early -- if parsing/validation can fail and return partway through a function, anything allocated before that point must already be covered by a `defer`, not cleaned up manually at the end (PR #1824, #2195). This is the most common actual memory-leak root cause found in review.

Always `dupe`/copy data whose lifetime you don't control before storing it somewhere longer-lived than the caller's own scope -- e.g. a name string passed into a spawned thread, or a slice captured into a struct that outlives the call (PR #3219, #2886). Zig does not copy strings for you.

`catch unreachable` is the correct idiom, not a hack, when an allocator is structurally guaranteed not to fail (`NeverFailingAllocator`, or a stack allocator sized for a known-small string) -- catching and handling an error that cannot occur is treated as worse than `unreachable`, because it implies a false possibility to future readers (PR #2680, #398, #1125). Conversely, using `unreachable` for a case that genuinely can happen under normal misconfiguration (a missing structure reference, a bad user-supplied ID) is a real bug -- replace it with a proper error return and a logged message (PR #1530).

Eager vs. lazy allocation is a judgment call, not a fixed rule. Lazy/path-based loading is preferred for large or rarely-touched data (entity models: store a path, load on first bind, PR #2680). But eager initialization is explicitly preferred when correctness or synchronization ordering demands it -- e.g. Vulkan resources, where lazy creation would complicate GPU sync (PR #2680 counter-example in the same file). Don't apply "lazy loading is better" as a blanket rule; ask whether deferring the work actually helps here.

Don't allocate more than you know you need -- repeated doubling-growth into an arena wastes space that's never reclaimed until the whole arena drops; if the exact count is knowable upfront, allocate exactly that (PR #2195 -- this exact issue caused a real out-of-bounds bug from a related fix that didn't bound the loop to the actual registered count).

## Related Questions
- How should allocators be matched to data lifetimes in Cubyz?
- Why is calling `.free()` on a slice from an arena allocator wrong in Cubyz?
- Why is placing a `defer` far from its matching `init` flagged in Cubyz review, even if technically correct?
- What is the most common actual memory-leak root cause found in Cubyz review?
- When must you `dupe`/copy data in Cubyz code?
- When is `catch unreachable` the correct way to handle error.OutOfMemory in Cubyz?
- Is eager or lazy allocation preferred in Cubyz code review?
- Why shouldn't you over-allocate into an arena in Cubyz?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_1*
