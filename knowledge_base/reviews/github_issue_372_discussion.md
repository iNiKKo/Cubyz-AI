# [issues/issue_372.md] - Issue #372 discussion

**Type:** review
**Keywords:** item drop shadows, subpixel artifacts, texture contrast, transparency, pixel grid alignment
**Concepts:** visual quality, contrast, pixel grid alignment

## Summary
Discussion about removing or adjusting item drop shadows in Cubyz to improve visual quality and contrast.

## Explanation
The issue revolves around the misalignment of item drop shadows with the pixel grid, causing subpixel artifacts. The maintainer initially made the shadow offset less than one pixel to avoid awkward cutoffs but found that it affects contrast for certain blocks. Users suggested removing the shadow entirely or making it more translucent. The maintainer experimented with increasing contrast and found that higher contrast darkens the world. After updating textures, users preferred no shadow at all, except for tools where further work is needed.

## Related Questions
- What are the potential visual effects of removing item drop shadows in Cubyz?
- How does increasing texture contrast affect the overall world lighting in Cubyz?
- Why was the initial shadow offset less than one pixel, and what were the drawbacks?
- What is the current status of translucent block rendering in Cubyz?
- How can the visual quality of item drops be improved without using drop shadows?
- What are the implications of removing drop shadows on tools in Cubyz?

*Source: unknown | chunk_id: github_issue_372_discussion*
