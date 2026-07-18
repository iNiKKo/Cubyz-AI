# [issues/issue_1877.md] - Issue #1877 discussion

**Type:** review
**Keywords:** chest locks, collaborative gameplay, unauthorized access, protector block, issue #81
**Concepts:** thread safety, backwards compatibility

## Summary
Discussion on implementing trivial locks for chests to prevent unauthorized access during collaborative gameplay.

## Explanation
The discussion revolves around adding a feature to lock chests based on player names, aiming to reduce accidental theft in multiplayer environments. Maintainers express concerns about the necessity of this feature after another issue (#81) is addressed, which might mitigate the problem. There's also mention of a protector block that could potentially lock containers, suggesting a broader protection mechanism.

## Related Questions
- What are the potential implications of adding chest locks on multiplayer server performance?
- How does the proposed chest lock feature interact with existing protection mechanisms in Cubyz?
- Can you provide a detailed explanation of how the protector block will lock containers?
- What are the security considerations when implementing player-based chest locks?
- How will the chest lock feature be configured to allow exceptions for certain players or groups?
- What is the expected impact on user experience with the addition of chest locks?

*Source: unknown | chunk_id: github_issue_1877_discussion*
