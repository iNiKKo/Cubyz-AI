# [issues/issue_2409.md] - Issue #2409 discussion

**Type:** review
**Keywords:** Tooltip, Interactable, Block Entities, OnInteract, Visual Impairment, Future Improvements
**Symbols:** .blockentity, .onInteract
**Concepts:** Accessibility, User Experience, Game Mechanics

## Summary
Discussion about adding tooltip descriptions to indicate interactable blocks, focusing on block entities and interaction functions.

## Explanation
The discussion revolves around enhancing the game's accessibility for visually impaired players by providing tooltips that describe whether a block is interactable. The maintainers suggest identifying interactable blocks through the presence of `.blockentity` (like chests and signs) and `.onInteract` methods (like workbenches). There is also a mention that in the future, block entities should be handled via the `onInteract` function to streamline this process.

## Related Questions
- How are block entities currently identified in the game?
- What changes need to be made to handle block entities via `onInteract`?
- Can you provide examples of other blocks that should have tooltips indicating they are interactable?
- How will the tooltip descriptions be implemented for visually impaired players?
- Are there any potential performance implications from adding these tooltip checks?
- What is the current state of block interaction handling in Cubyz?
- How can we ensure that all interactable blocks are correctly identified and described?
- Is there a plan to extend this feature to other types of player impairments?
- What are the architectural considerations for integrating tooltips into the existing game mechanics?
- How will these changes affect backwards compatibility with older versions of Cubyz?

*Source: unknown | chunk_id: github_issue_2409_discussion*
