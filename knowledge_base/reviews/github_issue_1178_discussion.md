# [issues/issue_1178.md] - Issue #1178 discussion

**Type:** review
**Keywords:** emissive blocks, light emission, light sampling, performance cost, visual effect
**Concepts:** lighting, performance

## Summary
The discussion revolves around whether to implement a feature where emissive blocks affect their occupied space by emitting light.

## Explanation
The issue proposes adding functionality that would make emissive blocks emit light in the space they occupy, aiming to enhance lighting effects. However, the maintainer raises concerns about doubling the cost of sampling light values, questioning whether the additional computational expense is justified given the minimal visual impact.

## Related Questions
- What is the current implementation of light emission in Cubyz?
- How does doubling the light sampling affect performance?
- Are there any alternative solutions to achieve similar lighting effects without increasing computational cost?
- What are the potential visual improvements from implementing this feature?
- How would this change impact existing lighting calculations?
- Is there a way to optimize light emission that balances performance and visual quality?

*Source: unknown | chunk_id: github_issue_1178_discussion*
