# [issues/issue_985.md] - Issue #985 discussion

**Type:** review
**Keywords:** player fall damage, threshold adjustment, game.zig, line 1099, height before damage, fractional values
**Symbols:** Player, gravity
**Concepts:** fall damage mechanics, game physics

## Summary
The player fall damage threshold is being adjusted to occur at 5 or 6 block falls instead of the current 4 blocks.

## Explanation
The discussion revolves around modifying the fall damage mechanics in the game. The maintainer suggests that the developer should experiment with different values and make a pull request with the preferred setting. The relevant code snippet is located at line 1099 in `game.zig`, where the current threshold for starting fall damage is set to 3 blocks. The maintainer encourages trying fractional values as well, such as 3.5, to find the optimal height for initiating fall damage.

## Related Questions
- What is the current value for the fall damage threshold in game.zig?
- How can I modify the fall damage threshold to 5 blocks?
- Can fractional values be used for the fall damage threshold?
- Where is the fall damage calculation implemented in the code?
- What are the potential impacts of changing the fall damage threshold on gameplay balance?
- Is there a specific reason why the current threshold is set at 3 blocks?

*Source: unknown | chunk_id: github_issue_985_discussion*
