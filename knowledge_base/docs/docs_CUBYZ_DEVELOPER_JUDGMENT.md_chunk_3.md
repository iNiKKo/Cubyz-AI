# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 3

**Type:** documentation
**Keywords:** union(enum), optional types, tagged union, raw pointers, SparseSet, unreachable, hardcoded limits, growable storage
**Symbols:** union(enum), ?T, SparseSet, getXPtr
**Concepts:** Type System & API Design

## Summary
Section 3 of Cubyz Developer Judgment: type system and API design judgment patterns.

## Explanation
Use `union(enum)` for genuinely distinct cases; don't fake it with an enum plus parallel optional fields. A union variant should represent a real alternative, not "this enum value plus sometimes-present data bolted on" (PR #2770, #2987, #3060 -- this exact refactor, enum+bool soup to tagged union, recurs across many unrelated PRs).

Encode invariants in the type system, not in comments. The canonical example: a coordinate that's sometimes absolute and sometimes relative was originally one struct with a comment explaining which; the fix was a tagged union so the distinction is enforced by the compiler, not documentation (PR #3103).

Prefer optional types (`?T`) over sentinel values or magic numbers for "absent." A `no_value` enum variant, a `0` that secretly means "unset," or a nullable pointer with an implicit "null means missing" convention are all weaker than an explicit `?T` unless there's a specific memory-layout reason not to (PR #1640).

Don't return raw pointers into a struct's internal fields as a general access pattern -- it's fragile to layout changes and can produce dangling pointers if the struct moves; prefer index-based or accessor-method access, with a separate explicit `getXPtr` only when mutation through a pointer is actually required (PR #2891, #1474 -- the latter specifically about a `SparseSet`-backed list where pointers can be invalidated by a resize).

Return an error or `?T` for a failure that can happen under normal misconfiguration; reserve `unreachable`/panics for cases an upstream invariant genuinely guarantees can't happen. This distinction shows up over and over in the structure-building-block loader's evolution (PR #1500, #1530, #2195): early versions panicked on a missing blueprint reference, and every round of review pushed toward "log an error and return null/error instead," because a bad addon config is not the same category of bug as a genuine engine invariant violation.

Avoid arbitrary hardcoded limits with no documented reasoning -- a fixed-size array with a magic capacity (a `[20]Node` buffer, a `maxSortedBlockProperties = 100` constant) is flagged specifically because addon content can exceed it with no growth path (PR #2824, #2063). If a limit is genuinely necessary, it needs an explicit justification, not just a round number.

Prefer growable/list-based storage over parallel dense arrays when the active set is much smaller than the theoretical maximum (PR #2063's `SortedBlockProperties` refactor away from `[maxBlockCount]bool` arrays for properties most blocks don't have).

## Related Questions
- When should Cubyz use `union(enum)` instead of an enum plus optional fields?
- Why should invariants be encoded in the type system rather than in comments?
- When should Cubyz prefer optional types (`?T`) over sentinel values?
- Why shouldn't Cubyz return raw pointers into a struct's internal fields?
- When is `unreachable`/panic appropriate versus returning an error in Cubyz?
- Why are arbitrary hardcoded limits with no documented reasoning flagged in Cubyz?
- When should Cubyz prefer growable/list-based storage over parallel dense arrays?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_3*
