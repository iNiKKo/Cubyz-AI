# [issues/issue_2794.md] - Issue #2794 discussion

**Type:** review
**Keywords:** inventory ID, distinct types, misuse prevention, shared structs, architectural challenge
**Symbols:** Inventory
**Concepts:** type safety, data structure design

## Summary
The change introduces distinct types for server and client inventory IDs to prevent misuse.

## Explanation
The reviewer points out that while the intention of making it harder to misuse inventory IDs by introducing distinct types is noble, the implementation faces challenges. The issue arises because the ID is present in shared structs like Inventory, which complicates the separation of server and client inventory IDs. This highlights a potential architectural challenge where shared data structures need careful handling to maintain consistency across different components.

## Related Questions
- How does the current implementation handle shared inventory structs?
- What are the potential impacts of introducing distinct types for server and client inventory IDs?
- Can you provide examples of how misuse might occur with the current ID system?
- How can the shared Inventory struct be modified to accommodate distinct server and client IDs?
- What are the implications for performance if we introduce separate types for each component?
- Are there any backward compatibility concerns with this change?

*Source: unknown | chunk_id: github_issue_2794_discussion*
