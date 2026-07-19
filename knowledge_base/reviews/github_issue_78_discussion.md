# [issues/issue_78.md] - Issue #78 discussion

**Type:** review
**Keywords:** chunk data, separate files, zon format, binary format, string IDs, numeric IDs, global item palette
**Concepts:** inventory management, data storage, file formats, item identification

## Summary
Discussion on storing inventories for each chunk in Cubyz, considering storage format (chunk data vs. separate files) and item ID representation (string vs. numeric).

## Explanation
Discussion on storing inventories for each chunk in Cubyz, considering storage format (chunk data vs. separate files) and item ID representation (string vs. numeric). The maintainers concluded that files not requiring human-editability should be stored in binary format. There is also a debate on how items should be identified—through string IDs for human readability or numeric IDs for efficiency. The maintainers conclude that a global item palette, similar to the existing systems for blocks and biomes, using numeric IDs, is the preferred approach. Additionally, the issue is marked as complete due to #1060.

## Related Questions
- What are the advantages and disadvantages of storing inventories as part of chunk data versus separate files?
- Why is a binary format preferred for files that do not require human-editability?
- How does the global item palette improve inventory management in Cubyz?
- What considerations should be made when choosing between string IDs and numeric IDs for items?
- How does the decision to use a global item palette align with Cubyz's existing systems for blocks and biomes?
- What potential performance impacts could arise from storing inventories separately?

*Source: unknown | chunk_id: github_issue_78_discussion*
