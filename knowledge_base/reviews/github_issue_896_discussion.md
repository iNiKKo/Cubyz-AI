# [issues/issue_896.md] - Issue #896 discussion

**Type:** review
**Keywords:** hue shifting, lighting, 4 color channels, RGB, darkness scale, lightmaps, tonemaps, color space, vivid colors, desaturated colors
**Concepts:** lighting, hue shifting, color channels, lightmaps, tonemaps, floodfill lighting

## Summary
The discussion revolves around improving lighting in Cubyz to avoid hue shifting, exploring options like adding an extra color channel or using lightmaps/tonemaps. The maintainers propose a solution involving lightmaps to adjust the color space and prevent hue shifts.

## Explanation
The discussion revolves around improving lighting in Cubyz to avoid hue shifting, exploring options like adding an extra color channel or using lightmaps/tonemaps. The maintainers propose a solution involving lightmaps to adjust the color space and prevent hue shifts.

The issue primarily concerns the hue shifting that occurs at the edge of light sources in Cubyz, affecting visual fidelity. With 3 color channels (R, G, B), there are 8 base colors: black, white, red, green, blue, yellow, cyan, and magenta. Adding a fourth channel would allow for 16 base colors but introduces performance challenges due to increased memory load and computational complexity in the vertex shader. The maintainers propose using lightmaps or tonemaps to adjust the color space without altering the underlying data format, aiming to provide artistic control over lighting while avoiding hue shifts. Lightmaps contain every light color in Cubyz within a 5-bit color spectrum, allowing for adjustments like making lights more vibrant and polarizing or desaturating as they dim.

The user suggests adding an extra color channel to differentiate between colors like red and orange more effectively. However, this introduces performance challenges due to increased memory load and computational complexity in the vertex shader. The maintainers also propose using lightmaps or tonemaps to adjust the color space without altering the underlying data format, aiming to provide artistic control over lighting while avoiding hue shifts.

The discussion also highlights limitations of floodfill lighting, where colors decrease at the same rate, preventing effective color mixing without significant changes to the algorithm. The user suggests halving the light radius or adding an extra bit to distinguish orange from red, but this is not feasible due to performance and memory load considerations.

## Related Questions
- How does adding an extra color channel affect memory load in the vertex shader?
- What are the potential issues with using HSV for color mixing in floodfill lighting?
- Can lightmaps be used to prevent hue shifts without altering the underlying data format?
- What is the impact of changing the light radius on the visual appearance of lights?
- How does the current floodfill lighting algorithm handle color mixing across different light sources?
- What are the limitations of using a single u32 for storing light data in the vertex shader?

*Source: unknown | chunk_id: github_issue_896_discussion*
