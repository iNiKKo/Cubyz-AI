# [issues/issue_2326.md] - Issue #2326 discussion

**Type:** review
**Keywords:** noise-controlled, variable density, biome structures, fullDensityThreshold, minDensityThreshold, minDensity, scale, seed, invert, sub-biomes, SBBS, performance impact, breaking changes
**Symbols:** .fullDensityThreshold, .minDensityThreshold, .minDensity, .scale, .seed, .invert
**Concepts:** biome generation, noise-based density control, resource management, diversity in biomes

## Summary
The issue proposes adding noise-controlled parameters for generating biome structures with variable density, aiming to increase biome diversity.

## Explanation
The issue proposes adding noise-controlled parameters for generating biome structures with variable density to increase biome diversity. The proposal introduces several parameters such as fullDensityThreshold (f32, 0 to 1), minDensityThreshold (f32, 0 to 1), minDensity (f32, 0 to 1), scale (f32), seed (u64), and invert (bool) to control the density of structure spawning based on noise values. The fullDensityThreshold parameter specifies the noise value at which the density of the structure spawning is at its maximum, while minDensityThreshold sets the noise value at which the density is at its minimum. The minDensity parameter defines the minimum density multiplier for structure generation. The scale parameter controls the scale of the noise used to determine structure density, and the seed parameter ensures consistent noise patterns across different structures if specified. The invert parameter allows inverting the output of the noise function, useful for ensuring that a structure only spawns where another does not. The maintainer initially expresses skepticism about the necessity, suggesting alternative methods like sub-biomes and smaller patches. However, the user argues that this approach would make biomes more interesting and easier for addon creators to implement without significant performance impact or breaking changes.

## Related Questions
- How does the noise-controlled density system affect biome generation performance?
- What are potential use cases for the invert parameter in structure generation?
- Can you provide examples of how sub-biomes could be used to achieve similar effects as the proposed noise-based system?
- How might this feature impact compatibility with existing addon systems?
- What is the expected resource consumption increase with the implementation of this feature?
- How does the proposed system compare in terms of complexity to using multiple sub-biomes?
- Can you elaborate on how the seed parameter ensures consistent noise patterns across different structures?

*Source: unknown | chunk_id: github_issue_2326_discussion*
