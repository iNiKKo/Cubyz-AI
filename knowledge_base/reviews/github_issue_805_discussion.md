# [issues/issue_805.md] - Issue #805 discussion

**Type:** review
**Keywords:** gravity blocks, sand rotation mode, loose rotation mode, block update, solid block, adjacent solid block, block entity, smooth animation, cellular automaton, pyramid, transformation upon impact
**Symbols:** sand, gravel, gravity, block update, solid block, adjacent solid block, block entity, smooth animation, cellular automaton, pyramid
**Concepts:** block physics, animation, entity system, simulation

## Summary
Discussion on implementing gravity for blocks like sand and gravel, including considerations for rendering, animation, and transformation upon impact.

## Explanation
The discussion revolves around how to implement gravity effects for specific blocks such as sand and gravel. The maintainers propose using block entities to render smooth animations during the fall. There is also a suggestion to use a cellular automaton approach to simulate more complex behaviors like piling into pyramids. The transformation of falling blocks back into solid blocks upon hitting the ground is mentioned as a potential feature.

## Related Questions
- What is the proposed condition for a sand block to fall?
- How will the smooth animation of falling blocks be implemented?
- Can you explain the cellular automaton approach mentioned for sand behavior?
- What is the purpose of converting sand to an entity?
- How will the transformation of falling blocks back into solid blocks upon impact be handled?
- What are the potential performance implications of using block entities for gravity effects?

*Source: unknown | chunk_id: github_issue_805_discussion*
