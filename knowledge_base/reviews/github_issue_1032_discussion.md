# [issues/issue_1032.md] - Issue #1032 discussion

**Type:** review
**Keywords:** anisotropic filtering, mipmaps, transparency, dithering, flowers, grass, leaves, rendering artifacts, resolution, opacity
**Symbols:** anisotropic filtering, mipmaps, transparency
**Concepts:** texture rendering, mipmap generation, partial transparency

## Summary
The issue was resolved by allowing partial transparency in mipmaps for specific textures, fixing rendering artifacts.

## Explanation
The original problem was caused by the game not supporting partial transparency for certain textures like flowers and grass, leading to dithering patterns at low resolutions. The fix involved modifying the mipmapping process to make pixels transparent if any of their parent pixels are transparent, but only for specific textures (flowers/grass) while keeping leaves opaque in the distance. This change was confirmed to resolve the issue when anisotropic filtering is enabled.

## Related Questions
- What was the original cause of the rendering artifacts?
- How did enabling anisotropic filtering resolve the issue?
- Which textures were modified to support partial transparency in mipmaps?
- Why were leaves not included in the modification for partial transparency?
- What is the impact of this change on memory usage?
- How does this fix affect performance, especially at low resolutions?
- Are there any potential regressions introduced by this change?
- Can you explain the architectural reasoning behind allowing partial transparency only for certain textures?
- How was the correctness of this fix verified?
- What are the implications of this change on future texture rendering optimizations?

*Source: unknown | chunk_id: github_issue_1032_discussion*
