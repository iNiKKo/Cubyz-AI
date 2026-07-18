# [issues/issue_1736.md] - Issue #1736 discussion

**Type:** review
**Keywords:** player identification, file naming, UUIDs, hashing, collisions, zon file, mapping, incremental IDs
**Symbols:** zon file, UUID, MD5, SHA-1, hashmap
**Concepts:** uniqueness, file system limits, collision resolution, hash functions

## Summary
The discussion revolves around finding a suitable method for uniquely identifying player files without relying on potentially problematic UUIDs or hash functions.

## Explanation
The issue arises because player names can be too long, exceeding file system limits. The maintainer suggests using a zon file with indexes to map players to directories, while the user proposes using UUIDs similar to Minecraft's approach. The maintainer argues against UUIDs due to their complexity and potential for collisions, suggesting instead a hash-based solution with incremental IDs to resolve collisions. However, the maintainer also expresses concerns about relying solely on hash functions, citing the lack of guarantees about name distribution and the difficulty of migrating files if the hash function proves inadequate. The discussion highlights trade-offs between simplicity, uniqueness, and storage opacity.

## Related Questions
- What are the potential drawbacks of using UUIDs for player identification?
- Why is MD5 considered weak and what alternatives are suggested?
- How does the maintainer propose resolving collisions in player file naming?
- What concerns does the maintainer have about relying on hash functions for player identification?
- What alternative method is proposed to ensure unique player file names without using UUIDs?
- How might a mapping file help prevent issues with hash function failures?

*Source: unknown | chunk_id: github_issue_1736_discussion*
