# [issues/issue_2938.md] - Issue #2938 discussion

**Type:** review
**Keywords:** block breaking state, hardcoded, engine, synchronization, unique behavior
**Concepts:** block entity, synchronization

## Summary
Discussion about storing block breaking state as a block entity for easier implementation and synchronization.

## Explanation
The discussion revolves around whether the block breaking state should be stored as a block entity. The maintainer initially questions the necessity, suggesting that it might be unique behavior better hardcoded into the engine and noting that saving this state is not required. However, another maintainer argues that storing it would make synchronization easier.

## Related Questions
- What are the potential benefits of storing block breaking state as a block entity?
- Why might it be better to hardcode the block breaking state into the engine?
- How could storing the block breaking state improve synchronization?
- Are there any performance implications of changing how block breaking state is handled?
- What other issues or features are mentioned in relation to this change?
- How does this change relate to issue #2564?

*Source: unknown | chunk_id: github_issue_2938_discussion*
