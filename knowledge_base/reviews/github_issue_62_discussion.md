# [issues/issue_62.md] - Issue #62 discussion

**Type:** review
**Keywords:** fluids, gases, simulation, performance, rendering, exponential growth, gas types, vector representation, globules, hierarchical node approach
**Concepts:** fluid dynamics, gas simulation, performance optimization, rendering efficiency

## Summary
The discussion revolves around designing a fluid/gas system for Cubyz, focusing on how to handle multiple gas types and fluid dynamics without causing performance issues.

## Explanation
The discussion revolves around designing a fluid/gas system for Cubyz, focusing on how to handle multiple gas types and fluid dynamics while preventing excessive computational load. The main goals include ensuring heavy liquids flow downwards, light gases flow upwards, biomes have associated liquid/fog blocks that fill gaps when broken, fluids exist in separate memory from voxels, and fluids do not propagate endlessly. Relaxations allow for non-realistic flow and infinite bodies of water like oceans. Mixing gases is problematic due to exponential growth in gas types and complex rendering requirements with transparent faces at borders between different gas densities. Users propose treating gases as vectors, grouping fluids into globules, and using a hierarchical node approach. The maintainers note that the issue remains open until someone implements and tests a viable solution.

## Related Questions
- What are the main goals for the fluid/gas system in Cubyz?
- How do relaxations impact the design of the fluid/gas system?
- Why is mixing gases problematic in terms of computational load and rendering complexity?
- What specific solutions have been proposed to address these issues?

*Source: unknown | chunk_id: github_issue_62_discussion*
