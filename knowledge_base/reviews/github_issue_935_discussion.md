# [issues/issue_935.md] - Issue #935 discussion

**Type:** review
**Keywords:** block health, hardness, Moh's Scale, breakingPower, resistance, tool power, damage, balance, simplification
**Symbols:** block health, Moh's hardness, breakingPower, resistance, tool power, damage
**Concepts:** game mechanics, balance, simplification

## Summary
The discussion revolves around adding block health and revising the hardness system in Cubyz. The maintainer proposes renaming existing parameters and simplifying the breaking mechanics for better balance.

## Explanation
The issue aims to introduce a new concept of 'block health' and redefine 'hardness' using the Moh's Scale. The maintainer suggests renaming 'breakingPower' to 'resistance' and 'tool power' to 'damage' to align with the block health system. The breaking mechanics would then be simplified by calculating damage as the maximum of zero or the difference between tool damage and block resistance. This change is proposed to make the game's balance easier to manage compared to the exponential nature of Moh's hardness.

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
