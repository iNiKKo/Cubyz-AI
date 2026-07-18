# [issues/issue_1951.md] - Issue #1951 discussion

**Type:** review
**Keywords:** space check, comments, format.zig, zig fmt, tabs, spacing, modifications, compatibility, future updates
**Symbols:** fmt.zig, main, std.heap.DebugAllocator, std.heap.ArenaAllocator, process.argsAlloc, run
**Concepts:** formatter, tabs vs spaces, backwards compatibility, standard library modifications

## Summary
The maintainer directs the user to implement a space check for comments in `format.zig` and re-enable it for `.zig` files, while explaining that modifications to the zig formatter were made within standard library files to maintain compatibility with future updates.

## Explanation
The discussion revolves around implementing a space check for comments in the Cubyz project's formatter. The user questions the discrepancy between the contributing guidelines and the actual implementation of `fmt.zig`, noting that the custom formatter is only used for `.zon` and shader files, not `.zig`. The maintainer clarifies that modifications to the zig formatter were made within standard library files to ensure compatibility with future updates from the zig compiler. They direct the user to implement the space check in `format.zig` and re-enable it for `.zig` files, emphasizing the need to keep differences minimal to simplify future updates.

## Related Questions
- Where is the space check for comments currently implemented in Cubyz?
- Why are modifications to the zig formatter made within standard library files?
- How can the space check be re-enabled for `.zig` files without affecting future updates?
- What are the potential implications of keeping differences minimal between Cubyz's and zig's formatter implementations?
- How does the current implementation of `fmt.zig` handle doc comments (`///`)?
- Are there any specific guidelines or considerations for updating the formatter to align with future zig compiler changes?

*Source: unknown | chunk_id: github_issue_1951_discussion*
