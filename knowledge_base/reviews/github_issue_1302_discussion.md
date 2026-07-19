# [issues/issue_1302.md] - Issue #1302 discussion

**Type:** review
**Keywords:** red_leaf_pile, old chunks, rotation mode, leaf drop, compatibility
**Symbols:** cubyz:red_leaf_pile
**Concepts:** backwards compatibility, data value, leaf generation

## Summary
The issue discusses red leaf piles generating with an excessively high data value, causing them to drop a large number of leaves upon breaking.

## Explanation
The issue discusses red leaf piles of `cubyz:red_leaf_pile` generating in forests with too high a data value, causing them to drop approximately 17 leaves during breaking. The discussion indicates that this problem arises from old chunks where leaves had an older rotation mode. This suggests a potential compatibility or migration issue between different versions of the game's leaf generation logic.

## Related Questions
- What is the current rotation mode for leaves in Cubyz?
- How does the game handle data value changes between different versions of leaf generation?
- Are there any plans to update old chunks to the new leaf rotation mode?
- Can you provide a code snippet that demonstrates how leaf piles are generated with the old rotation mode?
- What is the expected behavior for red leaf piles in terms of leaf drop when breaking?
- How does the game ensure compatibility between different versions of chunk data?

*Source: unknown | chunk_id: github_issue_1302_discussion*
