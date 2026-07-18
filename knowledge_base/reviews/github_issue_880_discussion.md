# [issues/issue_880.md] - Issue #880 discussion

**Type:** review
**Keywords:** light spreads down, infinite spread, white glow crystal, caves, daytime, sun emitter, block updates
**Concepts:** light propagation, bug fixing, performance optimization

## Summary
The issue involves light spreading infinitely downwards in caves during daytime, specifically with pure white glow crystals.

## Explanation
The bug was identified where light from a white glow crystal spreads infinitely downwards in cave environments during the day. The game mistakenly treated all light sources as sun emitters, leading to this behavior. The fix involves correcting how the game identifies and processes light sources, which also improved block update performance.

## Related Questions
- What is the condition under which light spreads infinitely downwards?
- How does the game mistakenly treat all light sources as sun emitters?
- What changes were made to fix the issue with light propagation?
- Are there any other light-related bugs that occur during daytime?
- How did fixing this bug impact block update performance?
- Is there a specific time of day when this bug does not occur?
- Can you provide more details on how the game identifies and processes light sources?
- What are the potential consequences if the fix is not applied?
- Are there any other environmental factors that could trigger this bug?
- How can we prevent similar bugs from occurring in the future?

*Source: unknown | chunk_id: github_issue_880_discussion*
