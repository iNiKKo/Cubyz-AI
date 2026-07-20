# [src/blocks.zig] - PR #1476 review diff

**Type:** review
**Keywords:** tick function, enum, runtime dispatch, VTable, modular design, performance, extensibility
**Symbols:** Block, tickFunctions, TickFunction, TickFunctions, replaceWithCobble, parseBlock
**Concepts:** runtime extensibility, modularity, VTable, function pointers, enums

## Summary
The review suggests replacing the current enum-based tick function design with a VTable approach for better modularity and runtime extensibility.

## Explanation
The reviewer criticizes the current implementation of `TickFunction` in `blocks.zig`, which uses an enum to define block-specific tick behaviors. The reviewer argues that this approach is problematic because enums are not runtime-extensible, limiting the ability to add new block types through mods. Additionally, using function pointers introduces runtime dispatch overhead. The reviewer proposes a VTable-based design similar to how other systems in Cubyz handle events, such as tool modifiers, to improve modularity and performance.

The `TickFunction` signature has been updated to include an additional parameter `_param: ?*anyopaque`, which allows for more flexible function calls. A new enum `FunctionName` with values `null` and `replaceWith` has been introduced to manage different tick behaviors.

The `replaceWithCobble` function, which was previously defined in the `TickFunctions` struct, now logs a debug message indicating that cobblestone will replace the block at the specified coordinates. The function then parses the block type "cubyz:cobblestone" and performs the replacement.

## Related Questions
- What are the potential performance implications of using a VTable instead of enums for tick functions?
- How does the current enum-based design limit modularity in Cubyz?
- Can you provide examples of how other systems in Cubyz use VTables for event handling?
- What are the benefits of using function pointers with runtime dispatch in this context?
- How can we ensure backward compatibility when changing from enums to a VTable approach?
- What are the trade-offs between using enums and VTables for defining block behaviors?

*Source: unknown | chunk_id: github_pr_1476_comment_2098735375*
