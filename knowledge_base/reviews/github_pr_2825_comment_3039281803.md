# [src/server/command/_command.zig] - PR #2825 review diff

**Type:** review
**Keywords:** Blueprint.capture, Selection, init, min/max, refactor, encapsulation, code organization, redundancy reduction, Vec3i, capture
**Symbols:** Blueprint.capture, Selection, init, minPos, maxPos, Vec3i
**Concepts:** Code Refactoring, Structural Improvements, Encapsulation, Redundancy Reduction

## Summary
The reviewer suggests improving the `Blueprint.capture` function by changing its parameter to a `Selection` struct that includes methods for initialization and size calculation, reducing redundancy in min/max operations.

## Explanation
The reviewer proposes architectural improvements to the `Blueprint.capture` function. Currently, the function accepts raw positions and performs min/max calculations internally. The suggestion is to encapsulate these positions within a `Selection` struct defined in `blueprint.zig`. This struct would include an `init` method that automatically handles min/maxing of the provided positions. By doing so, the redundancy of min/max operations within the `capture` function can be eliminated. Additionally, adding a `size` method to the `Selection` struct could further simplify related logic in other parts of the codebase. This change aims to enhance code organization and reduce duplication.

## Related Questions
- How does the proposed `Selection` struct improve code readability?
- What are the potential performance implications of using a `Selection` struct instead of raw positions?
- Can you provide an example of how the `size` method in the `Selection` struct could be implemented?
- How might this change affect existing code that calls `Blueprint.capture`?
- What are the benefits of encapsulating selection logic within a dedicated struct?
- How does this refactoring align with the overall architecture of the Cubyz project?

*Source: unknown | chunk_id: github_pr_2825_comment_3039281803*
