# [issues/issue_888.md] - Issue #888 discussion

**Type:** review
**Keywords:** shadows, shadow maps, ambient occlusion, floodfill lighting, Cubyz, lighting engine, entity shadows, contrast, realism, performance impact
**Symbols:** shadow maps, ambient occlusion, floodfill lighting, chunk_meshing.zig
**Concepts:** realism, performance, visual quality, atmosphere

## Summary
Discussion about implementing shadow maps in Cubyz to enhance visual depth, with considerations for performance and entity shadows.

## Explanation
The discussion revolves around adding shadow maps to Cubyz to improve the visual appearance by casting realistic shadows from sunlight. The maintainers explore various methods, including ambient occlusion and floodfill lighting, but ultimately decide that shadow maps are the most suitable solution due to their potential for enhancing realism without significant performance impact. There is a debate about whether to apply shadow maps to entities, with concerns raised about potential lag and visual quality. The team also discusses adjusting block contrast to improve the overall atmosphere of the game.

## Related Questions
- What are the potential performance implications of implementing shadow maps in Cubyz?
- How can the contrast adjustment be optimized to enhance visual depth without affecting performance?
- Why was ambient occlusion considered but ultimately rejected for shadow implementation?
- What specific changes were made to the lighting engine to improve block shading?
- How does the team plan to handle entity shadows in relation to shadow maps?
- Can you provide a detailed explanation of how shadow maps will be integrated into Cubyz's rendering pipeline?

*Source: unknown | chunk_id: github_issue_888_discussion*
