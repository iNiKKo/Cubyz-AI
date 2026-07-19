# [issues/issue_805.md] - Issue #805 discussion

**Type:** review
**Keywords:** gravity blocks, sand rotation mode, loose rotation mode, block update, solid block, adjacent solid block, block entity, smooth animation, cellular automaton, pyramid, transformation upon impact
**Symbols:** sand, gravel, gravity, block update, solid block, adjacent solid block, block entity, smooth animation, cellular automaton, pyramid
**Concepts:** block physics, animation, entity system, simulation

## Summary
Discussion on implementing gravity for blocks like sand and gravel, including considerations for rendering, animation, and transformation upon impact.

## Explanation
The discussion focuses on implementing gravity for blocks like sand and gravel, including detailed conditions under which these blocks fall and their behavior during and after falling.

Specifically, blocks with 'Sand Rotation Mode' will fall if there is no solid block directly underneath them. Blocks with 'Loose Rotation Mode' will fall if they are not connected to an adjacent solid block. The maintainers propose using a block entity system for rendering smooth animations during the fall and suggest using the same mechanism as branches and leaves to detect when sand should fall.

Additionally, there is a suggestion that falling blocks could transform back into solid blocks upon hitting the ground. This transformation would be part of the implementation details discussed in the issue.

## Related Questions
- What are the conditions for a block with Sand Rotation Mode to start falling?
- What are the conditions for a block with Loose Rotation Mode to start falling?
- How will smooth animations during the fall of gravity blocks be implemented?
- Can you explain how the system used for branches and leaves can detect when sand should fall?
- What is the proposed mechanism for transforming falling blocks back into solid blocks upon impact?

*Source: unknown | chunk_id: github_issue_805_discussion*
