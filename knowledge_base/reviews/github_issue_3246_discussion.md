# [issues/issue_3246.md] - Issue #3246 discussion

**Type:** review
**Keywords:** reflection shader, highlights, mirroring, screen-space reflections, world-space reflections, performance impact, consistent graphics experience, Vulkan rewrite, asset design, lower settings
**Concepts:** graphics performance, uniform experience, shader optimization

## Summary
Discussion about improving water reflections in Cubyz, with concerns over performance and maintaining a consistent graphics experience across all players.

## Explanation
Discussion about improving water reflections in Cubyz, with concerns over performance and maintaining a consistent graphics experience across all players. The maintainer expresses uncertainty about implementing proper reflections due to potential issues such as screen-space reflections looking bad and world-space reflections being laggy. There is a preference for a uniform graphics experience to simplify implementation effort, especially before the Vulkan rewrite when having too many options complicates development. Future developments may include more graphics options and custom shader support. The maintainer emphasizes that assets should be designed to look good at the lowest settings to ensure consistency across all players.

## Related Questions
- What are the potential performance impacts of implementing proper water reflections in Cubyz?
- Why is maintaining a consistent graphics experience across all players important for the development team?
- How might future developments, such as Vulkan rewrite and custom shader support, address the current limitations of reflection effects?
- What are the benefits and drawbacks of allowing optional graphics options in Cubyz?
- How can assets be designed to look good at lower settings while ensuring a consistent experience for all players?
- What is the reasoning behind the preference for a uniform graphics experience before the Vulkan rewrite?

*Source: unknown | chunk_id: github_issue_3246_discussion*
