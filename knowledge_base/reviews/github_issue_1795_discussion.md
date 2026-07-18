# [issues/issue_1795.md] - Issue #1795 discussion

**Type:** review
**Keywords:** fade ambient occlusion, LOD effect, shader, depth manipulation, lighting contrast, reflection, uniform normals, performance, visual depth, silhouette effect
**Concepts:** ambient occlusion, lighting interpolation, level of detail (LOD), shader programming, transparency, normal mapping, performance optimization

## Summary
The discussion revolves around improving the visual quality of distant terrain in Cubyz by fading out ambient occlusion (AO) and other effects like lighting contrast and reflections. The goal is to create a more realistic silhouette effect as objects move further away from the player.

## Explanation
The maintainers and users discuss various approaches to achieve this effect, including using shaders to manipulate depth and transparency, adjusting light interpolation, and experimenting with different curves for fading out effects based on distance. The main concerns are maintaining visual depth, avoiding unwanted artifacts, and optimizing performance. The maintainers also suggest uniformizing normals to reduce issues from reflection and other normal-based effects. A hacky prototype is shared, demonstrating the potential improvements. The discussion highlights the need for balancing visual fidelity with computational efficiency.

## Related Questions
- How can the shader be modified to handle transparency correctly?
- What is the impact of uniformizing normals on reflection effects?
- Can you provide a detailed explanation of how the distance dimming curve affects visual quality?
- How does adjusting the exponent and start values in the fading effect improve the silhouette appearance?
- What are the potential performance implications of implementing these visual changes?
- How can shadows be made softer and blurrier to better mask LOD artifacts?

*Source: unknown | chunk_id: github_issue_1795_discussion*
