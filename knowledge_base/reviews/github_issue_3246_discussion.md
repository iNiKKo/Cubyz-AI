# [issues/issue_3246.md] - Issue #3246 discussion

**Type:** review
**Keywords:** reflection shader, highlights, mirroring, screen-space reflections, world-space reflections, performance impact, consistent graphics experience, Vulkan rewrite, asset design, lower settings
**Concepts:** graphics performance, uniform experience, shader optimization

## Summary
Discussion about improving water reflections in Cubyz, with concerns over performance and maintaining a consistent graphics experience across all players.

## Explanation
The issue revolves around enhancing the current reflection shader to include highlights and mirroring effects. The maintainer expresses uncertainty about the feasibility of proper reflections due to potential performance issues, such as screen-space reflections looking bad and world-space reflections being laggy. There is a preference for a uniform graphics experience across all players to simplify implementation, especially before the Vulkan rewrite. However, there is an acknowledgment that future developments may include more graphics options and custom shader support. The maintainer also emphasizes the importance of designing assets to look good at lower settings to ensure consistency.

## Related Questions
- What are the potential performance impacts of implementing proper water reflections in Cubyz?
- Why is maintaining a consistent graphics experience across all players important for the development team?
- How might future developments, such as Vulkan rewrite and custom shader support, address the current limitations of reflection effects?
- What are the benefits and drawbacks of allowing optional graphics options in Cubyz?
- How can assets be designed to look good at lower settings while ensuring a consistent experience for all players?
- What is the reasoning behind the preference for a uniform graphics experience before the Vulkan rewrite?

*Source: unknown | chunk_id: github_issue_3246_discussion*
