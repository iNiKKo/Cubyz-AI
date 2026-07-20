# [src/utils.zig] - PR #1273 review diff

**Type:** review
**Keywords:** ReadWriteTest, init, deinit, main.zig, builtin.is_test, allocator, test build, thread locals, simplification, future tests
**Symbols:** ReadWriteTest, init, deinit, main.initThreadLocals, main.deinitThreadLocals, builtin.is_test
**Concepts:** thread safety, testing framework, allocator management

## Summary
A new struct `ReadWriteTest` is introduced with initialization and deinitialization functions, but the reviewer suggests modifying `main.zig` to assign testing allocators conditionally during test builds.

## Explanation
**Explanation**

A new struct `ReadWriteTest` is introduced with methods for initializing (`init`) and deinitializing (`deinit`) thread locals. The `init` method calls `main.initThreadLocals()`, while the `deinit` method calls `main.deinitThreadLocals()`. This struct is defined in `src/utils.zig`.

The reviewer suggests modifying `main.zig` to assign testing allocators conditionally during test builds using `if(builtin.is_test)`. This approach would simplify future tests by avoiding repetitive setup code and align with Cubyz's overall testing strategy. The reviewer notes that instead of requiring these initialization and deinitialization functions for every test, the testing allocator should be assigned in `main.zig` if the build is a test build. This change would make the testing framework more efficient by reducing boilerplate code and ensuring consistent allocator management across all tests.

The critical architectural review suggests that instead of requiring these for every test (and every future test for that matter), how about just assigning the `stack`/`globalAllocator`s in `main.zig` the testing allocator if we are in a test build. You can use `if(builtin.is_test)` for this.

*Source: unknown | chunk_id: github_pr_1273_comment_2027141708*

## Related Questions
- How does the `ReadWriteTest` struct impact test execution?
- What is the purpose of using `builtin.is_test` in allocator management?
- Can you explain the benefits of setting up testing allocators in `main.zig`?
- How would modifying `main.zig` affect existing tests?
- What are the potential drawbacks of this architectural change?
- How does this change align with Cubyz's overall testing strategy?

*Source: unknown | chunk_id: github_pr_1273_comment_2027141708*
