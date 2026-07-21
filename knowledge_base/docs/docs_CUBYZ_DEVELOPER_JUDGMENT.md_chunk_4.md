# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 4

**Type:** documentation
**Keywords:** over-engineering, abstraction, magic, simplicity, premature optimization, no measurable benefit
**Symbols:** N/A
**Concepts:** Avoiding Over-Engineering

## Summary
Section 4 of Cubyz Developer Judgment: how Cubyz maintainers push back on unnecessary complexity.

## Explanation
Don't add a struct/indirection layer "for future flexibility" without a concrete present need. This is rejected constantly and explicitly -- "may be redundant or harder to maintain," "adds cognitive load... if it needs to grow later, refactoring is still possible" (PR #3103, #1207). The bar for adding abstraction is a real current requirement, not a hypothetical one.

Reject "magic"/implicit machinery in favor of explicit, locally-readable code -- this project explicitly discussed and rejected a universal automatic struct serializer in favor of explicit per-type serialization functions, specifically because implicit introspection-based behavior is harder to debug when something goes wrong (PR #1141, #1996 -- an unusually explicit and long thread about exactly this tradeoff, worth treating as close to canonical for how this project weighs "DRY" against "explicit").

Simplicity is a legitimate response to a suggestion, not a cop-out. Reviewers repeatedly defer a "better" approach to a future PR/issue rather than blocking or expanding the current one, especially near a known upcoming refactor of the same area (PR #2064, #2482, #2131).

"Premature optimization" and "no measurable benefit" are treated as real, valid objections, not hand-waving -- e.g. rejecting a hashmap for a handful of per-frame entries in favor of a plain list (PR #1313), rejecting `initCapacity` precomputation that the reviewer showed doesn't actually change allocation count (PR #2141), rejecting a lookup table that obscures a single shift instruction from the optimizer without benchmark evidence (PR #2482).

Context changes the answer. The same reviewers who reject unnecessary abstraction also explicitly approve added complexity when it's justified by a real constraint -- e.g. accepting a more complex staged/two-phase allocation specifically because the simpler version had a real correctness bug (PR #2195). Don't apply "prefer simple" as a dogma that overrides an actual demonstrated need.

## Related Questions
- Why would Cubyz reject adding an abstraction layer "for future flexibility"?
- Why did Cubyz reject a universal automatic struct serializer?
- Why is "premature optimization" treated as a valid objection in Cubyz review, not hand-waving?
- Why would a Cubyz reviewer push back on using a Hashmap for random indexing into tickable blocks?
- When does Cubyz accept added complexity despite normally preferring simplicity?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_4*
