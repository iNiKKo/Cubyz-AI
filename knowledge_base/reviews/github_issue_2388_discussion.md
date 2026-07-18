# [issues/issue_2388.md] - Issue #2388 discussion

**Type:** review
**Keywords:** dispersion, viscosity, flow speed, biome temperature, infinite waterfalls, chain waterfalls, fluid behavior
**Symbols:** dispersion, viscosity, F, V, D, B
**Concepts:** fluid dynamics, realistic physics, biome effects

## Summary
Proposes adding 'dispersion' and 'viscosity' properties to fluids in Cubyz to simulate more realistic behavior, preventing infinite waterfalls and allowing for chain waterfalls.

## Explanation
The proposal introduces two new properties for fluids: 'dispersion' and 'viscosity'. The 'dispersion' property determines the distance after which a fluid begins to break into droplets and vapor, making it unswimmable. This addresses concerns about infinite waterfalls from single source blocks. The viscosity value affects the flow speed of the fluid using the formula F = (100 / V), where F is the flow speed in blocks per second and V is the viscosity value. For example, Minecraft's water has a viscosity of 25, resulting in a flow speed of 4 blocks per second (F = (100 / 25) = 4). Additionally, a dispersal distance D is calculated based on viscosity and biome temperature using the formula D = (V * (1.5 / (B + 0.5)), where B is the biome temperature ranging from 0.00 to 2.00. The constant 1.5 ensures that dispersal acts quicker in hotter biomes and slower in colder ones, while adding 0.5 prevents division by zero issues. Both F and D should be rounded to the nearest integer. The proposal also includes rules for how fluids interact with solid blocks during their fall, allowing for chain waterfalls as long as the liquid makes contact with another solid block after falling a height less than the dispersal distance.

## Related Questions
- How does the viscosity value affect the flow speed of fluids?
- What is the formula used to calculate the dispersal distance D?
- How does the biome temperature influence the dispersal distance?
- What happens when a fluid comes into contact with a solid block during its fall?
- Can this proposal prevent infinite waterfalls in Cubyz?
- How does the dispersion property make fluids unswimmable?
- What is the purpose of the constant 1.5 in the dispersal distance formula?
- How does the viscosity value determine the flow speed of fluids?
- What are the benefits of adding realistic fluid physics to Cubyz?
- How does this proposal address concerns about water on floating sky islands?

*Source: unknown | chunk_id: github_issue_2388_discussion*
