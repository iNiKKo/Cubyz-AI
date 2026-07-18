# [issues/issue_1156.md] - Issue #1156 discussion

**Type:** review
**Keywords:** BinaryReader, Writer, std.mem.readInt, std.mem.writeInt, network.zig, findIPPort, receiveKeepAlive, flawedReceive, refactoring, binary data handling, code simplification, error handling
**Symbols:** BinaryReader, Writer, std.mem.readInt, std.mem.writeInt, network.zig, findIPPort, receiveKeepAlive, flawedReceive
**Concepts:** refactoring, binary data handling, code simplification, error handling

## Summary
Discussion about replacing `std.mem.readInt` and `std.mem.writeInt` with BinaryReader/Writer across all protocols.

## Explanation
The discussion revolves around the proposal to use BinaryReader/Writer for handling binary data in Cubyz. The maintainer clarifies that this would involve most uses of `std.mem.readInt` and `std.mem.writeInt`. They also inquire about specific implementations in `network.zig`, such as `findIPPort`, `receiveKeepAlive`, and `flawedReceive`. The maintainer suggests that while `keepAlive` could benefit from the change, `findIPPort` should remain unchanged due to its external protocol communication. Additionally, `flawedReceive` is deemed not worth refactoring because it involves only one read operation.

## Related Questions
- What are the potential benefits of using BinaryReader/Writer in all protocols?
- How does the use of BinaryReader/Writer impact error handling?
- Why is `findIPPort` not being refactored to use BinaryReader/Writer?
- Is there a performance difference between `std.mem.readInt/writeInt` and BinaryReader/Writer?
- What are the implications of changing `receiveKeepAlive` to use BinaryReader/Writer?
- How does this change affect backwards compatibility with existing protocols?

*Source: unknown | chunk_id: github_issue_1156_discussion*
