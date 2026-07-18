# [issues/issue_63.md] - Issue #63 discussion

**Type:** review
**Keywords:** random texture rotation, texture variants, white noise overlay, fully procedural textures, large 2D textures, stochastic texture sampling, CTM, performance cost, mipmapping, anisotropic filtering
**Symbols:** random connected textures, CTM (Connected textures mod), stochastic texture sampling, texture2DGrad(), prefiltering
**Concepts:** texture repetition, performance optimization, procedural generation, mipmapping, anisotropic filtering

## Summary
The discussion revolves around various approaches to reduce texture repetitiveness in Cubyz, including random texture rotation, variants, white noise overlay, fully procedural textures, and large 2D textures. The maintainers suggest exploring 'random' connected textures as a potential solution, while users propose stochastic texture sampling as an alternative.

## Explanation
The issue of repetitive textures is addressed through multiple approaches, each with its own pros and cons. Random texture rotation and variants offer some randomness but have limitations in applicability and matching issues at borders. Fully procedural textures provide high detail but suffer from performance overhead. Large 2D textures can reduce repetition scale but require procedural generation to handle artistically. Stochastic texture sampling is proposed as a more efficient alternative, though it comes with increased computational cost.

## Related Questions
- What are the performance implications of using stochastic texture sampling in Cubyz?
- How can stochastic texture sampling be integrated with mipmapping and anisotropic filtering?
- Can random connected textures effectively reduce texture repetition without significant overhead?
- What are the potential benefits and drawbacks of using large 2D textures for reducing repetition?
- How does fully procedural texture generation compare to other methods in terms of performance and quality?
- Are there any existing libraries or tools that can facilitate stochastic texture sampling implementation in Cubyz?

*Source: unknown | chunk_id: github_issue_63_discussion*
