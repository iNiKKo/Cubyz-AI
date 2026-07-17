# [easy/codebase_assets_cubyz_tools_axe.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** choppable, matrix multiplication, boolean flags, optional components, massDamage, hardnessDamage, swingSpeed, durability, sum method, average method
**Symbols:** tags, disabled, optional, parameters
**Concepts:** tool configuration, damage matrix parameters, component flags, stat conversion rules

## Summary
Configuration data defining the Axe tool's damage matrix parameters and optional component flags.

## Explanation
This chunk is a static configuration file (`.zon`) that defines the properties of an Axe tool. It contains three main fields: `tags`, which marks the tool as `.choppable` for interaction purposes; `disabled`, a 5x5 boolean matrix indicating which specific damage components are disabled by default, with values like `0, 0, 1, 1, 1` on the first row meaning the first two components are enabled and the rest are disabled; and `optional`, another 5x5 boolean matrix specifying which components can be optionally added to the tool. The chunk also defines a `parameters` field containing an array of six distinct parameter sets. Each set is a struct with fields `.source`, `.destination`, `.matrix`, `.factor`, and `.method`. These parameters define how different stats (like massDamage, hardnessDamage, durability, swingSpeed) are converted into damage or other attributes using matrix multiplication followed by either a sum or average method.

## Related Questions
- What does the .choppable tag signify for an Axe tool?
- How are disabled flags represented in the configuration matrix?
- Which damage components can be optionally added to the Axe?
- What is the purpose of the source and destination fields in each parameter set?
- How does the matrix multiplication affect the final damage value?
- Why are there two different methods (sum vs average) for combining values?
- Can a component be both disabled by default and optional to enable later?
- What is the role of the factor field in each parameter set?
- How many distinct parameter sets are defined for the Axe tool?
- Which stats map directly to themselves (e.g., swingSpeed -> swingSpeed)?
- Are there any parameters that convert durability into maxDurability?
- What is the default state of the first row in the disabled matrix?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_axe.zig.zon_chunk_0*
