# [issues/issue_896.md] - Issue #896 discussion

**Type:** review
**Keywords:** hue shifting, lighting, 4 color channels, RGB, darkness scale, lightmaps, tonemaps, color space, vivid colors, desaturated colors
**Concepts:** lighting, hue shifting, color channels, lightmaps, tonemaps, floodfill lighting

## Summary
The discussion revolves around improving lighting in Cubyz to avoid hue shifting, exploring options like adding an extra color channel or using lightmaps/tonemaps. The maintainers propose a solution involving lightmaps to adjust the color space and prevent hue shifts.

## Explanation
The issue primarily concerns the hue shifting that occurs at the edge of light sources in Cubyz, which affects the visual fidelity of lighting. The user suggests adding an extra color channel to differentiate between colors like red and orange more effectively. However, this approach is criticized for increasing memory load and computational complexity. Instead, the maintainers propose using lightmaps or tonemaps to adjust the color space without altering the underlying data format. This solution aims to provide artistic control over lighting while avoiding hue shifts. The discussion also touches on the limitations of floodfill lighting and the challenges in maintaining consistent color mixing across different light sources.

## Related Questions
- How does adding an extra color channel affect memory load in the vertex shader?
- What are the potential issues with using HSV for color mixing in floodfill lighting?
- Can lightmaps be used to prevent hue shifts without altering the underlying data format?
- What is the impact of changing the light radius on the visual appearance of lights?
- How does the current floodfill lighting algorithm handle color mixing across different light sources?
- What are the limitations of using a single u32 for storing light data in the vertex shader?

*Source: unknown | chunk_id: github_issue_896_discussion*
