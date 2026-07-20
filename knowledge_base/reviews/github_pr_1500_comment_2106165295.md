# [src/server/terrain/structure_building_blocks.zig] - PR #1500 review diff

**Type:** review
**Keywords:** initInline, inline structures, child blocks, blueprintCache, error.MissingBlueprint, addon creators, .zig.zon file
**Symbols:** StructureBuildingBlock, initInline, blueprintCache, std.log.err
**Concepts:** API design, Error handling, User guidance

## Summary
Added an `initInline` function to the `StructureBuildingBlock` struct for initializing inline structures. The function checks if the blueprint has child blocks and logs an error if it does, suggesting that addon creators should create a `.zig.zon` file instead.

## Explanation
The change introduces a new method `initInline` in the `StructureBuildingBlock` struct to handle the initialization of inline structures. The primary concern is ensuring that inline structures do not contain child blocks, as this could lead to unexpected behavior or errors. The function checks if the blueprint has child blocks and logs an error message: `'['{s}'] Inline structures cannot contain child blocks.'`. If a missing blueprint is encountered, it logs an error message: `'['{s}'] Could not find blueprint '{s}'` and returns `error.MissingBlueprint`. The reviewer points out that addon creators might be unclear about what an 'inline structure' means and suggests providing clearer guidance on how to properly define such structures by creating a `.zig.zon` file when child blocks are required. This change aims to improve the clarity of the API and prevent potential misuse.

To create a '.zig.zon' file for defining structures with child blocks, addon creators should follow these steps:
1. Create a new file named `structure_name.zig.zon` in the appropriate directory.
2. Define the structure using the `.zig.zon` syntax, ensuring that it does not contain any child blocks.
3. Save the file and ensure it is correctly referenced in the project.

## Related Questions
- What steps should addon creators follow to define structures with child blocks using a '.zig.zon' file?

*Source: unknown | chunk_id: github_pr_1500_comment_2106165295*
