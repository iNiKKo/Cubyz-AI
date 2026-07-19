# [issues/issue_2340.md] - Issue #2340 discussion

**Type:** review
**Keywords:** branches, LOD, appearance, flicker, disappear, enlarge
**Concepts:** Level of Detail (LOD), Rendering, Visual Design

## Summary
Discussion on whether branches should appear as full blocks in LODs or disappear due to their thinness.

## Explanation
Discussion on whether branches should appear as full blocks in Level of Detail (LOD) representations. The maintainers note that branches are quite thin, suggesting it would make more sense to make them disappear rather than enlarge them by a factor of 4× due to flickering issues when viewed from a distance.

## Related Questions
- What are the potential visual effects of making branches disappear in LODs?
- How does the current implementation of branch rendering contribute to flickering issues?
- What are the trade-offs between making branches appear as full blocks and disappearing them in LODs?
- Could adjusting the LOD settings for branches mitigate the flickering problem without changing their appearance?
- Is there a way to dynamically adjust branch visibility based on distance to improve visual consistency?
- How might the decision impact performance when rendering large worlds with many branches?

*Source: unknown | chunk_id: github_issue_2340_discussion*
