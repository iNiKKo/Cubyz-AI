# [src/server/command/_command.zig] - PR #2604 review diff

**Type:** review
**Keywords:** axis parsing, coordinate handling, pointers, Vec3d, error handling, user feedback
**Symbols:** execute, parseAxis, parseCoordinates, User, f64, std.fmt.parseFloat, std.mem.SplitIterator
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added `parseAxis` function to handle axis parsing and updated `parseCoordinates` to use pointers for coordinate values.

## Explanation
The change introduces a new function `parseAxis` that parses an axis argument, which can either be a number or a tilde (`~`) indicating relative positioning. The reviewer suggests using a `Vec3d` instead of pointers for coordinates in the `parseCoordinates` function, advocating for returning a vector object to simplify handling and potential future changes.

## Related Questions
- What is the purpose of the `parseAxis` function?
- Why does the reviewer suggest using a Vec3d instead of pointers?
- How does the `parseCoordinates` function handle invalid input?
- Can you explain the role of the tilde (`~`) in axis parsing?
- What are the potential benefits of returning a Vec3d from `parseCoordinates`?
- How does the code ensure that user feedback is provided for invalid inputs?

*Source: unknown | chunk_id: github_pr_2604_comment_2862596326*
