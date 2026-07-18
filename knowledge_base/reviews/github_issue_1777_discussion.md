# [issues/issue_1777.md] - Issue #1777 discussion

**Type:** review
**Keywords:** shadows, snow, light absorption, ambient occlusion, realism
**Concepts:** lighting, shadows, ambient occlusion

## Summary
The issue discusses the problem of overly strong shadows on snow blocks in Cubyz, suggesting a fix by adjusting light absorption properties.

## Explanation
The discussion revolves around the visual appearance of snow blocks in the game Cubyz, where the shadows are too pronounced. The maintainer suggests reducing the absorption of light to make the snow appear more realistic. A user proposes setting `.absorbedLight = 0x444444` as a potential solution, which seems to yield better results based on provided images.

## Related Questions
- What is the current value of `.absorbedLight` for snow blocks?
- How does changing `.absorbedLight` affect the appearance of shadows on snow blocks?
- Are there any other materials in Cubyz that might require similar adjustments to light absorption?
- What are the potential performance implications of adjusting light absorption properties in real-time?
- How can we ensure that changes to light absorption do not negatively impact other visual aspects of the game?
- Is there a way to make the adjustment to `.absorbedLight` configurable for users?

*Source: unknown | chunk_id: github_issue_1777_discussion*
