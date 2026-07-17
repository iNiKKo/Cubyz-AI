# [src/blocks.zig] - PR #1476 review diff

**Type:** review
**Keywords:** tick function design, enum-based design, VTable approach, modding capabilities, runtime dispatch, tool modifiers, architecture improvement
**Symbols:** Block, tickFunctions, TickFunction, TickFunctions, replaceWithCobble, parseBlock, chunk.ServerChunk
**Concepts:** runtime extensibility, modularity, VTable pattern, function pointers, enums

## Summary
The review suggests replacing the current enum-based tick function design with a VTable approach for better modularity and runtime extensibility.

## Explanation
The reviewer criticizes the existing design of using enums for tick functions, highlighting that it is not runtime extensible, which limits modding capabilities. The alternative proposed is to use a VTable (virtual table) pattern, similar to how other systems in Cubyz are implemented, such as tool modifiers. This change aims to improve the architecture by allowing more flexible and dynamic function handling without compromising performance or correctness.

## Related Questions
- What are the potential performance implications of using a VTable instead of enums for tick functions?
- How does the current enum-based design limit modding capabilities in Cubyz?
- Can you provide examples of how other systems in Cubyz use the VTable pattern?
- What are the benefits of using a VTable over function pointers in this context?
- How can we ensure backward compatibility with existing tick functions when implementing the VTable approach?
- What changes need to be made to the `replaceWithCobble` function to fit into the new VTable design?

*Source: unknown | chunk_id: github_pr_1476_comment_2098735375*
