# [issues/issue_372.md] - Issue #372 discussion

**Type:** review
**Keywords:** item drop shadows, subpixel artifacts, texture contrast, transparency, pixel grid alignment
**Concepts:** visual quality, contrast, pixel grid alignment

## Summary
Discussion about removing or adjusting item drop shadows in Cubyz to improve visual quality and contrast.

## Explanation
Discussion about removing or adjusting item drop shadows in Cubyz to improve visual quality and contrast. The issue revolves around subpixel artifacts caused by misalignment of item drop shadows with the pixel grid, leading to floating artifacts on dark items that appear as blobs. Initially, the maintainer set the shadow offset less than one pixel to avoid awkward cutoffs but found this affected contrast for certain blocks like diamond and stone. Users suggested removing the shadow entirely or making it more translucent. The maintainer experimented with increasing texture contrast, noting that higher contrast darkens the world significantly. After updating textures, users preferred no drop shadow at all except for tools where further work is needed to address issues. Screenshots展示了不同对比度级别的效果，包括当前的、更多的和甚至更多的对比度级别。最终决定在更新纹理后移除阴影以提高视觉质量。

## Related Questions
- What are the potential visual effects of removing item drop shadows in Cubyz?
- How does increasing texture contrast affect the overall world lighting in Cubyz?
- Why was the initial shadow offset less than one pixel, and what were the drawbacks?
- What is the current status of translucent block rendering in Cubyz?
- How can the visual quality of item drops be improved without using drop shadows?
- What are the implications of removing drop shadows on tools in Cubyz?

*Source: unknown | chunk_id: github_issue_372_discussion*
