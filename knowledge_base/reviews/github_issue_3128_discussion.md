# [issues/issue_3128.md] - Issue #3128 discussion

**Type:** review
**Keywords:** allocator inconsistency, error handling, Result struct, ListUnmanaged, List, stackAllocator, lifetime management, Zig guidelines, consolidation effort
**Symbols:** ArgParser, errorMessage, ListUnmanaged, List, allocator, stackAllocator
**Concepts:** allocator usage, thread safety, backwards compatibility, memory leak

## Summary
The ArgParser's errorMessages usage is inconsistent between stackAllocator and the passed-in allocator. The discussion suggests using a List instead of ListUnmanaged to avoid allocator misuse.

## Explanation
The issue arises because the interface specifies that `errorMessage` should be allocated with `stackAllocator`, but most code uses the passed-in allocator. This inconsistency can lead to bugs and is hard to catch in reviews. The maintainers discuss potential solutions, including using a `List` instead of `ListUnmanaged` to avoid allocator misuse.

The following code snippet demonstrates this issue:
```zig
var tempErrorMessage: ListUnmanaged(u8) = .{};
defer tempErrorMessage.deinit(main.stackAllocator);

// ... (other code)
if (@typeInfo(field.type) == .optional) {
    @field(result, field.name) = null;
    tempErrorMessage.clearRetainingCapacity();
} else {
    errorMessage.appendSlice(main.stackAllocator, tempErrorMessage.items);
    return error.ParseError;
}
```
The maintainers also mention that using a `Result` struct instead of an out parameter could be another solution. However, they note that this would require allocating and copying the error strings around all the time.

The main concern is maintaining consistency with Zig's guidelines on allocator usage:
> - local lifetime, things that are freed at the end of the scope (including local data structures such as lists) → `main.stackAllocator`
Using `stackAllocator` for `errorMessage` looks like explicitly using `stackAllocator` for a resource that outlives the scope where `stackAllocator` is used. This violates Zig's guidelines.

The maintainers suggest waiting until after other changes are made, such as consolidating ArgParser usages outside the command (e.g., #3073), to resolve this issue more effectively.

## Related Questions
- What is the primary issue with ArgParser's errorMessages usage?
- Why is using a List instead of ListUnmanaged recommended?
- How does the maintainers' discussion suggest resolving the allocator inconsistency?
- What are the potential benefits of using a Result struct for error handling?
- Why might the issue wait until after other changes are made?
- What are the main concerns regarding allocator usage in Zig?

*Source: unknown | chunk_id: github_issue_3128_discussion*
