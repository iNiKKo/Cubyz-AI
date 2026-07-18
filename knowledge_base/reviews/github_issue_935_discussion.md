# [issues/issue_935.md] - Issue #935 discussion

**Type:** review
**Keywords:** block health, hardness, Moh's Scale, breakingPower, resistance, tool power, damage, balance, simplification
**Symbols:** block health, Moh's hardness, breakingPower, resistance, tool power, damage
**Concepts:** game mechanics, balance, simplification

## Summary
The discussion revolves around adding block health and revising the hardness system in Cubyz. The maintainer proposes renaming existing parameters and simplifying the breaking mechanics for better balance.

## Explanation
The discussion in issue #935 aims to introduce a new concept of 'block health' and redefine 'hardness' using the Moh's Scale. The maintainer proposes renaming 'breakingPower' to 'resistance' and 'tool power' to 'damage' to align with the block health system. The breaking mechanics would then be simplified by calculating damage as max(0, tool damage - block resistance). This change is proposed because the exponential nature of Moh's hardness makes it difficult to balance effectively. While one maintainer suggested reducing the hardness values of all blocks, this was not universally agreed upon and remains a suggestion rather than a concrete plan. The current status of the Block-Health branch (https://github.com/ikabod-kee/Cubyz/tree/Block-Health) is that it awaits further contributions from maintainers to finalize the implementation.

## Related Questions
- What is the proposed renaming of 'breakingPower'?
- How does the new damage calculation work?
- Why was Moh's hardness deemed too difficult to balance?
- What are the benefits of simplifying the breaking mechanics?
- Who will handle the implementation of these changes?
- When is the next playtest scheduled?
- What is the current status of the Block-Health branch?
- How does the new system compare to the old hardness system?
- Are there any potential regressions with this change?
- What are the expected outcomes of this rebalancing effort?

*Source: unknown | chunk_id: github_issue_935_discussion*
