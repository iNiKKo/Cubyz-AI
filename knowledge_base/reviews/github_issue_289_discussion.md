# [issues/issue_289.md] - Issue #289 discussion

**Type:** review
**Keywords:** crystals, translucent, lighting calculations, texture, sunroof, light scattering, stained
**Concepts:** translucency, floodfill lighting, texture opacity

## Summary
The proposal aims to simulate crystal translucency by treating them as transparent for floodfill lighting calculations while keeping their texture opaque. This allows crystals to act like sunroofs and potentially get stained by neighboring block colors if light scattering is implemented.

## Explanation
The issue proposes a method to make crystals in the game appear translucent, similar to real-life giant crystals where impurities diffuse light. The approach involves using floodfill lighting calculations to simulate this effect while keeping the crystal texture opaque to prevent the image behind from being visible. This change would enable crystals to function as sunroofs and could potentially get stained by neighboring block colors if light scattering is implemented, enhancing realism.

## Related Questions
- How does the floodfill lighting calculation simulate crystal translucency?
- What is the purpose of keeping the crystal texture opaque?
- Can crystals function as sunroofs with this proposed change?
- How might light scattering affect the appearance of crystals?
- What are the potential benefits of simulating crystal translucency in the game?
- Are there any limitations to this approach for achieving realistic crystal effects?

*Source: unknown | chunk_id: github_issue_289_discussion*
