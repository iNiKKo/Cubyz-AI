# [issues/issue_99.md] - Issue #99 discussion

**Type:** review
**Keywords:** resolution upscaling, downscaling, shader, fog calculations, nearest-neighbor, linear sampling, powers of 2, viewport size, internal framebuffer, screenbuffer
**Concepts:** resolution scaling, shader handling, fog calculations, nearest-neighbor sampling

## Summary
Discussion on implementing resolution up-/downscaling in Cubyz, focusing on shader handling and sampling techniques.

## Explanation
The discussion revolves around adding a resolution scaling feature to Cubyz, allowing users to adjust the game's rendering scale. The maintainers suggest using a resolution scale from 25% (downscaling) to 200% (upscaling). They propose that fog calculations should be done before downscaling and that a new shader might be needed for manual sampling and interpolation during downscaling. The maintainers also emphasize the use of nearest-neighbor sampling for upscaling, as they prefer it over linear sampling due to its sharpness. Additionally, there's a consideration to limit the scaling factors to powers of 2 (1/4, 1/2, 1, 2) for simplicity and performance reasons.

## Related Questions
- What are the potential performance implications of implementing resolution scaling in Cubyz?
- How does the current shader handle fog calculations, and why is it being reused for upscaling?
- Why is nearest-neighbor sampling preferred over linear sampling for upscaling?
- What are the limitations of limiting the scaling factors to powers of 2?
- How might downscaling affect UI rendering in Cubyz?
- What considerations should be made when implementing a new shader for manual sampling and interpolation during downscaling?

*Source: unknown | chunk_id: github_issue_99_discussion*
