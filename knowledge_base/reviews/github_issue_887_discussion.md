# [issues/issue_887.md] - Issue #887 discussion

**Type:** review
**Keywords:** leaf rendering, chunk borders, neighbor chunks, LOD, jungle, unnecessary faces
**Concepts:** optimization, performance, visual quality

## Summary
Discussion on optimization of leaf rendering at chunk borders in Cubyz.

## Explanation
The discussion revolves around an optimization decision where leaf rendering is intentionally limited to avoid loading all neighboring chunks. The maintainer argues that this is not a bug but an intentional design choice for performance reasons, especially considering the rule that players should not be inside the terrain. There are concerns about the visual quality of jungles with many leaves and the potential impact on performance. The team considers LOD (Level of Detail) settings as a solution to mitigate these issues. Additionally, it was noted that this optimization also affects areas outside of the terrain.

## Related Questions
- What is the impact of loading all neighboring chunks on performance?
- How does LOD 0.5 affect the visual quality of jungles?
- Are there any plans to implement a more detailed shading model for jungles?
- What are the rules regarding player positioning in Cubyz?
- How can unnecessary faces be reduced without compromising visual detail?
- Is there a way to balance performance and visual fidelity in leaf rendering?

*Source: unknown | chunk_id: github_issue_887_discussion*
