# [issues/issue_1736.md] - Issue #1736 discussion

**Type:** review
**Keywords:** player identification, file naming, UUIDs, hashing, collisions, zon file, mapping, incremental IDs
**Symbols:** zon file, UUID, MD5, SHA-1, hashmap
**Concepts:** uniqueness, file system limits, collision resolution, hash functions

## Summary
The discussion revolves around finding a suitable method for uniquely identifying player files without relying on potentially problematic UUIDs or hash functions.

## Explanation
The issue arises because player names can be too long, exceeding file system limits. The maintainer suggests using a zon file containing a list of players to map them to directories. A user proposes using UUIDs similar to Minecraft's approach, but the maintainer argues against this due to complexity and potential for collisions. Instead, the maintainer recommends using a hash-based solution with incremental IDs appended to player name hashes to resolve collisions. The maintainer also expresses concerns about relying solely on hash functions, citing the lack of guarantees about name distribution and the difficulty of migrating files if the hash function proves inadequate. To prevent issues where mapping gets corrupted, an additional file in each player folder containing their player name is suggested for recovery purposes. The recommended hash function is SHA-1 due to MD5 being considered weak.

## Related Questions
- What are the potential drawbacks of using UUIDs for player identification?
- Why is MD5 considered weak and what alternatives are suggested?
- How does the maintainer propose resolving collisions in player file naming?
- What concerns does the maintainer have about relying on hash functions for player identification?
- What alternative method is proposed to ensure unique player file names without using UUIDs?
- How might a mapping file help prevent issues with hash function failures?

*Source: unknown | chunk_id: github_issue_1736_discussion*
