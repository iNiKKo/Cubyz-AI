# [src/utils.zig] - PR #1273 review diff

**Type:** review
**Keywords:** ReadWriteTest, init, deinit, main.zig, builtin.is_test, allocator, test build, thread locals, simplification, future tests
**Symbols:** ReadWriteTest, init, deinit, main.initThreadLocals, main.deinitThreadLocals, builtin.is_test
**Concepts:** thread safety, testing framework, allocator management

## Summary
A new struct `ReadWriteTest` is introduced with initialization and deinitialization functions, but the reviewer suggests modifying `main.zig` to assign testing allocators conditionally during test builds.

## Explanation
The change introduces a new struct `ReadWriteTest` with methods for initializing and deinitializing thread locals. The reviewer points out that requiring these initializations for every test is cumbersome and proposes an alternative approach by setting up the testing allocator in `main.zig` when building for tests. This would simplify future tests and avoid repetitive setup code.

## Related Questions
- How does the `ReadWriteTest` struct impact test execution?
- What is the purpose of using `builtin.is_test` in allocator management?
- Can you explain the benefits of setting up testing allocators in `main.zig`?
- How would modifying `main.zig` affect existing tests?
- What are the potential drawbacks of this architectural change?
- How does this change align with Cubyz's overall testing strategy?

*Source: unknown | chunk_id: github_pr_1273_comment_2027141708*
