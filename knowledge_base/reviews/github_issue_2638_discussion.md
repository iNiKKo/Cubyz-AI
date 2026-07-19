# [issues/issue_2638.md] - Issue #2638 discussion

**Type:** review
**Keywords:** locks, blockentity rework, material keys, tool-based locks, transparency lock, high-tier lock, protector blocks, chest contents
**Concepts:** locks, block interactions, keys, tools, transparency, chest contents

## Summary
Discussion about implementing various types of locks for blocks in Cubyz, including material-based keys, tool-based locks, transparency locks, and high-tier locks. Maintainer notes that chest locks were previously rejected due to planned protector blocks.

## Explanation
Discussion about implementing various types of locks for blocks in Cubyz, including material-based keys (e.g., a gold key unlocks a default gold lock), tool-based locks where specific tools are required to unlock the block without considering durability or player identity, transparency locks allowing interaction with the block behind the locked one, and high-tier locks preventing chests from spilling their contents by either stopping the block from being broken or setting defenses/health very high. The maintainer notes that chest locks were previously rejected due to planned protector blocks which serve a similar purpose but are based on knowledge rather than physical keys. Users suggest that locks could still be useful in servers where protector blocks are disabled or as an alternative solution for certain structures.

## Related Questions
- What specific materials and tools can be used as keys?
- How does the transparency lock work?
- Under what conditions do high-tier locks prevent chests from spilling their contents?

*Source: unknown | chunk_id: github_issue_2638_discussion*
