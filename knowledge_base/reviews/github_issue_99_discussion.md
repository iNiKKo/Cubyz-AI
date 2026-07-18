# [issues/issue_99.md] - Issue #99 discussion

**Type:** review
**Keywords:** resolution upscaling, downscaling, shader, fog calculations, nearest-neighbor, linear sampling, powers of 2, viewport size, internal framebuffer, screenbuffer
**Concepts:** resolution scaling, shader handling, fog calculations, nearest-neighbor sampling

## Summary
Discussion on implementing resolution up-/downscaling in Cubyz, focusing on shader handling and sampling techniques.

## Explanation
Discussion on implementing resolution up-/downscaling in Cubyz, focusing on shader handling and sampling techniques. The maintainers suggest using a resolution scale from 25% (downscaling) to 200% (upscaling). For downscaling, the viewport size is adjusted proportionally; for example, if the window size is 800x600, a 75% downscale would result in a viewport size of 600x450. Fog calculations should be done before downscaling to avoid issues with linear interpolation. A new shader might be needed for manual sampling and interpolation during downscaling due to the complexity of fog calculations. The maintainers emphasize using nearest-neighbor sampling for upscaling, as they prefer it over linear sampling because it looks sharper. They also consider limiting scaling factors to powers of 2 (1/4, 1/2, 1, 2) for simplicity and performance reasons.

## Related Questions
- What are the potential performance implications of implementing resolution scaling in Cubyz?
- How does the current shader handle fog calculations, and why is it being reused for upscaling?
- Why is nearest-neighbor sampling preferred over linear sampling for upscaling?
- What are the limitations of limiting the scaling factors to powers of 2?
- How might downscaling affect UI rendering in Cubyz?
- What considerations should be made when implementing a new shader for manual sampling and interpolation during downscaling?

*Source: unknown | chunk_id: github_issue_99_discussion*
