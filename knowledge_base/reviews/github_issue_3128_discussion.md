# [issues/issue_3128.md] - Issue #3128 discussion

**Type:** review
**Keywords:** allocator inconsistency, error handling, Result struct, ListUnmanaged, List, stackAllocator, lifetime management, Zig guidelines, consolidation effort
**Symbols:** ArgParser, errorMessage, ListUnmanaged, List, allocator, stackAllocator
**Concepts:** allocator usage, thread safety, backwards compatibility, memory leak

## Summary
The ArgParser's errorMessages usage is inconsistent between stackAllocator and the passed-in allocator. The discussion suggests using a List instead of ListUnmanaged to avoid allocator misuse.

## Explanation
The issue arises because the interface specifies that errorMessages should be allocated with stackAllocator, but most code uses the passed-in allocator. This inconsistency can lead to bugs and is hard to catch in reviews. The maintainers discuss potential solutions, including using a Result struct instead of an out parameter or returning a dedicated error object. They also mention that this issue could wait until after other changes are made, such as consolidating ArgParser usages outside the command. The main concern is maintaining consistency with Zig's guidelines on allocator usage and avoiding interleaving allocations from different scopes.

## Related Questions
- What is the primary issue with ArgParser's errorMessages usage?
- Why is using a List instead of ListUnmanaged recommended?
- How does the maintainers' discussion suggest resolving the allocator inconsistency?
- What are the potential benefits of using a Result struct for error handling?
- Why might the issue wait until after other changes are made?
- What are the main concerns regarding allocator usage in Zig?

*Source: unknown | chunk_id: github_issue_3128_discussion*
