# [src/server/command/worldedit/blueprint.zig] - Chunk 3329167717

**Type:** review
**Keywords:** blueprint, save, delete, load, union, enum, deinit, FilePath, boilerplate, recursive, parser
**Symbols:** BlueprintSubCommand, Args, save, delete, load, unknown, empty, FilePath, deinit
**Concepts:** enum to union refactoring, boilerplate reduction, recursive deinitialization, type safety, command pattern, memory management, parser interface consistency

## Summary
Refactored BlueprintSubCommand enum into a union of Args with per-command structs to hold path and deinit logic, addressing reviewer concern about boilerplate.

## Explanation
The original code used an enum BlueprintSubCommand where each variant implicitly carried no data; the parser returned the enum directly. Reviewers noted that this forced repetitive struct definitions for each command just to store a FilePath and provide a deinit method. The change introduces a union Args containing three distinct structs: one for save, delete, and load commands (each tagged with an enum value indicating the action) plus a placeholder for unknown/empty cases. Each struct now explicitly holds a path field of type FilePath and defines its own deinit method that calls self.path.deinit(allocator). This pattern mirrors the recursive nature of the parser: just as parse returns a union that can be recursively deinitialized, the new Args union allows ArgParser.deinit(result) to walk through each variant’s deinit function in one clean interface. The refactor reduces boilerplate by consolidating common fields and providing a uniform cleanup path, while preserving type safety for each command variant.

## Related Questions
- What is the type of the path field in each Args variant?
- How does ArgParser.deinit handle the new union structure?
- Why was BlueprintSubCommand changed to a union instead of remaining an enum?
- Which commands are represented by the save, delete, and load tags inside Args?
- What happens if an unknown or empty command is parsed under this new design?
- Does the deinit method in each struct call any external allocator functions?
- How does this refactor affect memory layout compared to the original enum approach?
- Is there a corresponding change in how the parser returns results before and after this diff?
- What implications does having per-variant deinit have for cleanup order?
- Could the union be extended with additional command types without breaking existing code?

*Source: unknown | chunk_id: github_pr_3138_comment_3329167717*
