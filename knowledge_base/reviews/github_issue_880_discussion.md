# [issues/issue_880.md] - Issue #880 discussion

**Type:** review
**Keywords:** light spreads down, infinite spread, white glow crystal, caves, daytime, sun emitter, block updates
**Concepts:** light propagation, bug fixing, performance optimization

## Summary
The issue involves light spreading infinitely downwards in caves during daytime, specifically with pure white glow crystals.

## Explanation
The issue involves light from a pure white glow crystal spreading infinitely downwards in cave environments during daytime. The game mistakenly treated all light sources as sun emitters, leading to this behavior. Specifically, the bug only occurs with white glow crystals and spreads down infinitely as long as there are no blocks in the way. It does not occur in the overworld or at night time. When the chunk containing the issue is unloaded, it fixes itself. The fix involves correcting how the game identifies and processes light sources, which also improved block update performance.

## Related Questions
- What specific conditions must be met for this bug to occur?
- How does the game mistakenly treat all light sources as sun emitters during daytime?
- Can you provide more details on the exact behavior of the infinite spread in caves?
- Why doesn't this issue occur in the overworld or at night time?

*Source: unknown | chunk_id: github_issue_880_discussion*
