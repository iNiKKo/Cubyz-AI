# [src/server/command/_command.zig] - PR #2604 review diff

**Type:** review
**Keywords:** axis parsing, coordinate handling, pointers, Vec3d, relative positioning, error handling
**Symbols:** execute, parseAxis, parseCoordinates, User, sendMessage, std.fmt.parseFloat, f64, std.mem.SplitIterator
**Concepts:** thread safety, backwards compatibility, memory management

## Summary
Added `parseAxis` function to handle axis parsing and updated `parseCoordinates` to use pointers for coordinate values.

## Explanation
The change introduces a new function `parseAxis` that parses an axis argument, handling both numeric values and the '~' character which indicates relative positioning. The reviewer suggests using a `Vec3d` instead of pointers in `parseCoordinates`, but the author justifies keeping pointers for separate access to x, y, and z coordinates.

## Related Questions
- What is the purpose of the `parseAxis` function?
- How does the `parseAxis` function handle invalid input?
- Why are pointers used in the `parseCoordinates` function instead of a vector?
- What is the expected behavior if an invalid number is provided to `parseAxis`?
- How does the `parseCoordinates` function utilize the `parseAxis` function?
- What changes would be necessary to use a `Vec3d` in `parseCoordinates`?

*Source: unknown | chunk_id: github_pr_2604_comment_2862596326*
