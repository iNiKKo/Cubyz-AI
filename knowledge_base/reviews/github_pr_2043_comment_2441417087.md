# [src/game.zig] - PR #2043 review diff

**Type:** review
**Keywords:** folder name validation, duplicate check, stack allocation, parameter refactoring, API cleanliness
**Symbols:** findValidFolderName, main.heap.NeverFailingAllocator, main.stackAllocator, std.fmt.allocPrint, main.files.cubyzDir().hasDir
**Concepts:** string manipulation, file system interaction, parameter encapsulation, API design

## Summary
Added a function `findValidFolderName` to sanitize and check for duplicate folder names. The reviewer suggests refactoring parameters of `flawedCreateWorld` into a `WorldSetting` struct.

## Explanation
The change introduces a new function `findValidFolderName` which processes the input world name by removing illegal ASCII characters and ensuring uniqueness by appending an index if necessary. This function uses stack allocation for intermediate strings and returns a duplicated string using the provided allocator. The reviewer points out that the current parameters of `flawedCreateWorld` are numerous, suggesting encapsulation into a struct to maintain clean API design and ease future parameter additions.

## Related Questions
- What is the purpose of the `findValidFolderName` function?
- How does the function handle illegal ASCII characters in the input name?
- What mechanism ensures the uniqueness of the folder name?
- Why is the reviewer suggesting to refactor parameters into a struct?
- How does the use of stack allocation impact memory management in this context?
- What potential issues could arise from not encapsulating parameters into a struct?

*Source: unknown | chunk_id: github_pr_2043_comment_2441417087*
