# [issues/issue_1854.md] - Issue #1854 discussion

**Type:** review
**Keywords:** Zig update, performance workarounds, x86 backend, incremental compilation, 0.15.x branch, deflate compressor
**Symbols:** Zig, 0.15.1, 0.16, array copying, incremental compilation
**Concepts:** performance optimization, versioning, backporting

## Summary
Discussion about updating Zig to version 0.16 or later to benefit from performance improvements and incremental compilation features.

## Explanation
The issue discusses updating Zig to version 0.16 or later to benefit from performance improvements related to array copying and enable incremental compilation on Linux. Specifically, the following pull requests were merged: https://github.com/ziglang/zig/pull/25154 (fixing performance issues with array copying) and https://github.com/ziglang/zig/pull/25299 (enabling incremental compilation on Linux). The team is considering this update after the 0.0.0 release, possibly waiting for another pull request (https://github.com/ziglang/zig/pull/25301) to avoid implementing their own deflate compressor. A user comment notes that certain commits may be specific to Zig 0.16 and suggests backporting them into the 0.15.x branch if needed.

## Related Questions
- What are the specific performance improvements in Zig version 0.16?
- How does incremental compilation work in Zig, and why is it beneficial?
- Can you explain the potential impact of backporting commits from Zig 0.16 to the 0.15.x branch?
- Why might the team wait for another pull request before implementing their own deflate compressor?

*Source: unknown | chunk_id: github_issue_1854_discussion*
