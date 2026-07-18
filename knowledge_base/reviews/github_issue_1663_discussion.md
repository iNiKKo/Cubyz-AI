# [issues/issue_1663.md] - Issue #1663 discussion

**Type:** review
**Keywords:** items, physics, friction, buoyancy, air/fluid resistance, implementation, consistency
**Concepts:** physics engine, friction, buoyancy, air/fluid resistance

## Summary
Items should have the same physics as normal entities, including friction, buoyancy, and air/fluid resistance.

## Explanation
The issue highlights a discrepancy where items on the ground do not experience friction, causing them to slide indefinitely. The maintainer emphasizes that any solution must integrate the same physics code used for regular entities to ensure consistency and prevent further divergence in implementations.

## Related Questions
- What is the current implementation of item physics in Cubyz?
- How does the physics code for regular entities differ from that for items?
- Are there any existing workarounds for item friction in the codebase?
- What are the potential impacts of integrating the same physics code for items and regular entities?
- How can we ensure that the integration of physics code for items does not introduce new bugs or regressions?
- What architectural changes, if any, are necessary to achieve consistent physics across different entity types?

*Source: unknown | chunk_id: github_issue_1663_discussion*
