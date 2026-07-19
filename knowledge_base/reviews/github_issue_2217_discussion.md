# [issues/issue_2217.md] - Issue #2217 discussion

**Type:** review
**Keywords:** SDF-based structures, low-resolution cave map, versatile terrain options, regenerating structures, chunk generation cost, multi-pass generation, StructureMap
**Symbols:** CaveMap, StructureMap, SDF
**Concepts:** terrain generation, multi-pass generation, data structure usage

## Summary
Discussion on generating SDF-based structures in a low-resolution version of the cave map to allow more versatile terrain options.

## Explanation
Discussion on generating SDF-based structures in a low-resolution version of the cave map to allow more versatile terrain options. A prototype of this (hardcoded for hemispheres) can be found in the [hemisphere_generator](https://github.com/PixelGuys/Cubyz/tree/hemisphere_generator) branch. But the real solution should allow specifying (more) arbitrary shapes per biome. The maintainer questions the feasibility and cost of regenerating these structures for each chunk, noting that while multi-pass generation is already used, it involves different data structures (each pass uses a different data structure). The current system stores structures in the StructureMap, but the proposed low-resolution SDF-based approach would regenerate structures, which is acceptable given the lower resolution and larger coverage.

## Related Questions
- What is the current data structure used for storing structures in normal chunks?
- How does the proposed SDF-based low-resolution CaveMap differ from the existing cave map implementation?
- Is there a performance impact of regenerating structures for each chunk in the new approach?
- Can you explain how multi-pass generation works in the current terrain generation system?
- What are the benefits and potential drawbacks of using a separate low-resolution version for SDF-based structures?
- How does the proposed change affect memory usage and storage requirements?

*Source: unknown | chunk_id: github_issue_2217_discussion*
