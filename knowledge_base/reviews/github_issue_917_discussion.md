# [issues/issue_917.md] - Issue #917 discussion

**Type:** review
**Keywords:** subbiomes, leaking, boundaries, climates, transitions, radius, issue
**Concepts:** subbiomes, biome boundaries, climate transitions

## Summary
Addresses the issue of subbiomes spreading outside their parent biome's boundaries when the biome radius is larger than 32.

## Explanation
The discussion addresses an issue where increasing the biome radius to more than 32 causes subbiomes to spread beyond their parent biome, leading to unexpected transitions between different climates or biomes. The maintainer notes that this problem extends beyond climate-related biomes and affects all subbiomes in general.

## Related Questions
- What is the maximum biome radius (32) that causes subbiomes to leak?
- How does increasing the biome radius affect climate transitions?
- Are there any specific conditions under which subbiomes do not leak?
- Is this issue limited to a particular type of biome or applicable universally?

*Source: unknown | chunk_id: github_issue_917_discussion*
