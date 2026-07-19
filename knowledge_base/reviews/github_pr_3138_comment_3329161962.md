# [src/server/command/worldedit/blueprint.zig] - PR #3138 review diff

**Type:** review
**Keywords:** enum, union, struct, deinit, FilePath, NeverFailingAllocator, subcommand, file-name, path, resource management, memory leak prevention, architectural consistency, backwards compatibility
**Symbols:** BlueprintSubCommand, Args, FilePath, NeverFailingAllocator
**Concepts:** resource management, memory leak prevention, architectural consistency, backwards compatibility

## Summary
Refactored BlueprintSubCommand enum into Args union with struct members for each subcommand, adding deinit methods for resource management.

## Explanation
The change refactors the BlueprintSubCommand enum into an Args union containing structs for each subcommand. Each struct corresponds to a specific subcommand ('save', 'delete', 'load') and includes a `path` field of type FilePath. The addition of deinit methods ensures proper resource management, preventing potential memory leaks. The reviewer raises concerns about architectural consistency and naming conventions, suggesting that the struct fields should align with the command parameters. The refactoring maintains backward compatibility by preserving the existing command structure while preparing for more complex operations like file path handling in save and load commands.

The specific subcommands and their parameters are as follows:
- `/blueprint save <file-name>`: Saves a blueprint to a specified file path.
- `/blueprint delete <file-name>`: Deletes a blueprint from a specified file path.
- `/blueprint load <file-name>`: Loads a blueprint from a specified file path.

The reviewer suggests that the struct fields should be named 'path' instead of 'file-name' to align with the command parameters and to allow for paths rather than just file names. The refactoring also prepares for future evolution paths where each command might have different expected operations, such as compatibility parameters or skipping entities.

## Related Questions
- What is the purpose of the deinit methods added to each struct in the Args union?
- How does this refactoring impact backward compatibility with existing commands?
- Why was it decided to use a union instead of an enum for handling subcommands?
- What are the potential future evolution paths for each command as mentioned by the reviewer?
- How does this change align with the architectural goals of maintaining consistency between command parameters and struct fields?
- What specific resource management issues does the addition of deinit methods address?

*Source: unknown | chunk_id: github_pr_3138_comment_3329161962*
