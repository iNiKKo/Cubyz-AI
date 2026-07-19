# [issues/issue_1168.md] - Issue #1168 discussion

**Type:** review
**Keywords:** doors, implementation, 2x1 door, big doors, trapdoors, entities, synchronization, block placement, opening mechanism
**Symbols:** door bottom, door top
**Concepts:** block storage, texture mapping, entity-based implementation

## Summary
Discussion on implementing doors in Cubyz, focusing on design choices and potential challenges.

## Explanation
Discussion on implementing doors in Cubyz, focusing on a basic 2x1 door model using two blocks. The bottom half of the door is craftable and spawns an uncraftable top block when placed. When either half is broken, only the bottom block drops. The synchronization between the bottom and top halves involves each half checking for the presence of the other during placement or opening actions to ensure proper updates. Specifically, when placing the first half, it checks if there is a second half above or below and places it accordingly. If the bottom half detects an existing top half, it synchronizes with it by updating its data first to avoid infinite chain of updates. Larger doors (e.g., 3x3) are proposed but would require entity-based implementation due to current limitations in handling overlapping blocks and texture mapping issues.

## Related Questions
- What are the exact names of the door blocks used for crafting and placing?
- How does the placement logic work when placing the bottom half of a door?
- What specific synchronization mechanism is proposed for opening and breaking actions?
- Are there any existing mods or examples that could inspire the door implementation in Cubyz?

*Source: unknown | chunk_id: github_issue_1168_discussion*
