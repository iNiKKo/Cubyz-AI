# [src/server/command/worldedit/blueprint.zig] - PR #3138 review diff

**Type:** review
**Keywords:** refactoring, enum, union(enum), struct, deinit, resource management, command parsing, path handling
**Symbols:** BlueprintSubCommand, Args, FilePath, NeverFailingAllocator
**Concepts:** Resource Management, Structural Design, Command Parsing

## Summary
Refactored BlueprintSubCommand enum into Args union(enum) with specific structs for each subcommand, including deinit methods for resource management.

## Explanation
The refactoring changes the BlueprintSubCommand enum to an Args union(enum), where each subcommand has its own struct. This approach allows for more detailed handling of command-specific parameters and resources. The reviewer points out that while a unified `/blueprint <subCommand> <file-name>` format might seem simpler, it doesn't fit all commands equally due to varying requirements (e.g., 'list' does not need a file name). Additionally, the reviewer suggests using 'path' instead of 'file-name' for consistency and flexibility in handling different types of paths. The deinit methods ensure proper resource management by freeing allocated memory.

## Related Questions
- What is the purpose of the deinit methods in each struct?
- How does the Args union(enum) improve command handling compared to the previous enum?
- Why was it decided to use 'path' instead of 'file-name'?
- What are the potential compatibility issues with the new command format?
- How does this refactoring impact backwards compatibility?
- Can you explain the reasoning behind separating each subcommand into its own struct?

*Source: unknown | chunk_id: github_pr_3138_comment_3329161962*
