# [issues/issue_63.md] - Issue #63 discussion

**Type:** review
**Keywords:** random texture rotation, texture variants, white noise overlay, fully procedural textures, large 2D textures, stochastic texture sampling, CTM, performance cost, mipmapping, anisotropic filtering
**Symbols:** random connected textures, CTM (Connected textures mod), stochastic texture sampling, texture2DGrad(), prefiltering
**Concepts:** texture repetition, performance optimization, procedural generation, mipmapping, anisotropic filtering

## Summary
The discussion revolves around various approaches to reduce texture repetitiveness in Cubyz, including random texture rotation, variants, white noise overlay, fully procedural textures, and large 2D textures. The maintainers suggest exploring 'random' connected textures as a potential solution, while users propose stochastic texture sampling as an alternative.

## Explanation
The discussion revolves around various approaches to reduce texture repetitiveness in Cubyz, including random texture rotation, variants, white noise overlay, fully procedural textures, and large 2D textures. The maintainers suggest exploring 'random' connected textures as a potential solution, while users propose stochastic texture sampling as an alternative.

Random texture rotation involves rotating the flat textures like stone but does not work well for all blocks. Random texture variants, as seen on cobblestone in Minecraft's Java version, help reduce repetition but still face matching issues at borders. A random white noise overlay is proposed to add a layer of white noise to noisy textures such as grass/dirt/sand, which would be fairly cheap but only works well for specific types of textures. Fully procedural textures were experimented with in the 'procedural_attempt' branch and an external repository, providing high detail but suffering from poor performance (an extra 4ms per frame) and limitations for certain block types like crystal blocks and cobblestone due to their detailed requirements. Large 2D textures are suggested as a solution where larger textures repeat at a larger scale, though they do not match at the sides and require procedural generation by artists. Stochastic texture sampling is proposed as an alternative approach with performance implications: it is on average 4-5 times costlier than classic texture repetition due to additional look-up table fetches and operations. It works well with mipmapping and anisotropic filtering using texture2DGrad() and prefiltering, though these aspects have not been implemented in experiments.

## Related Questions
- What are the performance implications of using stochastic texture sampling in Cubyz?
- How can stochastic texture sampling be integrated with mipmapping and anisotropic filtering?
- Can random connected textures effectively reduce texture repetition without significant overhead?
- What are the potential benefits and drawbacks of using large 2D textures for reducing repetition?
- How does fully procedural texture generation compare to other methods in terms of performance and quality?

*Source: unknown | chunk_id: github_issue_63_discussion*
