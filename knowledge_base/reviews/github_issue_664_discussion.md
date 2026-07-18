# [issues/issue_664.md] - Issue #664 discussion

**Type:** review
**Keywords:** animated water texture, 30 frames, PNG files, absorption, reflectivity, textureInfo, block JSON, sprite sheet, texturepacks, core block properties, animation frames, animation time
**Symbols:** sprite sheet, textureInfo, block json
**Concepts:** file management, animation handling, configuration flexibility

## Summary
Discussion about loading animations from a sprite sheet and consolidating texture information into the block JSON.

## Explanation
The issue discusses the inconvenience of managing multiple files for animated textures, such as water, where each frame requires separate PNGs along with associated metadata like absorption, reflectivity, and textureInfo. The proposal is to load animations from a single sprite sheet file, which would simplify the process. Additionally, there's a suggestion to include texture information directly in the block JSON to allow for easier configuration and future extensions.

## Related Questions
- How can the current system be modified to support loading animations from a sprite sheet?
- What are the potential benefits of consolidating texture information into the block JSON?
- How will extending the textureInfo in the future facilitate easier configuration of animation parameters?
- Are there any backward compatibility concerns with changing how textures and animations are managed?
- What tools or scripts could be developed to automate the creation of sprite sheets from individual frame files?
- How might the performance of loading animations change with the new sprite sheet approach?
- What security implications should be considered when allowing texturepacks to modify core block properties?

*Source: unknown | chunk_id: github_issue_664_discussion*
