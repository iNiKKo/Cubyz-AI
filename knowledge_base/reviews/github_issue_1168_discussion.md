# [issues/issue_1168.md] - Issue #1168 discussion

**Type:** review
**Keywords:** doors, implementation, 2x1 door, big doors, trapdoors, entities, synchronization, block placement, opening mechanism
**Symbols:** door bottom, door top
**Concepts:** block storage, texture mapping, entity-based implementation

## Summary
Discussion on implementing doors in Cubyz, focusing on design choices and potential challenges.

## Explanation
The discussion revolves around the implementation of doors in Cubyz. The maintainers propose a basic 2x1 door model using two blocks, where one block is craftable and spawns an uncraftable top block when placed. They also consider alternative approaches such as single-block tall doors and larger 3x3 doors. The main challenge highlighted is how to manage the relationship between the bottom and top halves of a door, especially in terms of synchronization during placement and opening. The maintainers suggest that this approach would work best for simple 2x1 doors but that larger doors would require entity-based implementation due to current limitations.

## Related Questions
- How does the current block storage system handle overlapping blocks?
- What are the potential issues with texturing a single-block tall door model?
- Can you explain how the synchronization between the bottom and top halves of a door is intended to work?
- What are the prerequisites for implementing doors as entities in Cubyz?
- How would the placement logic for a 2x1 door be implemented?
- What challenges arise from implementing larger doors (e.g., 3x3) without entity support?
- How does the current engine handle block interactions during placement and breaking?
- Are there any existing mods or examples that could inspire the door implementation in Cubyz?
- What are the potential performance implications of using entities for door implementation?
- How would the crafting recipe for doors be defined to ensure proper functionality?

*Source: unknown | chunk_id: github_issue_1168_discussion*
