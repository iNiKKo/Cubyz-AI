# [easy/codebase_assets_cubyz_world_presets_structure_world.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** preset, configuration, generators, disabled, enabled, climate, wavelengths, biome, mapgen, cave, structure
**Symbols:** climateGenerator, mapGenerator, generators, caveGenerators, structureMapGenerators, climateWavelengths
**Concepts:** world preset configuration, generator state management, biome selection, map generation identifiers, climatic wavelength parameters

## Summary
This chunk defines a world preset configuration containing climate generator settings, map generation identifiers, and lists of enabled/disabled ore, cave, and structure generators with their respective wavelength parameters.

## Explanation
The chunk declares a single top-level struct (unnamed in the provided snippet) that serves as a data container for world preset values. It contains fields: climateGenerator (a struct with id and biome), mapGenerator (struct with id), generators (map of ore generator identifiers to state enums), caveGenerators (map of cave generator identifiers to state enums), structureMapGenerators (map of structure generator identifiers to state enums), and climateWavelengths (struct holding numeric wavelength values for hot_cold, land_ocean, wet_dry, vegetation, mountain). All maps use string keys with the 'cubyz:' namespace prefix. The state field in each map entry is an enum variant either .disabled or .enabled. No executable logic is present; this chunk functions purely as configuration data.

## Related Questions
- What is the identifier assigned to the climate generator in this preset?
- Which biome string is configured for the world preset?
- How many ore generators are defined and what is their state?
- List all cave generators present and indicate which ones are enabled.
- Identify the structure map generators included and their enablement status.
- What numeric value is assigned to the hot_cold wavelength parameter?
- Retrieve the land_ocean wavelength setting from this configuration.
- Which generator has its state set to .enabled in the caveGenerators map?
- Are any ore generators currently enabled or are they all disabled?
- Does the structureMapGenerators section contain any enabled entries besides the default?

*Source: unknown | chunk_id: codebase_assets_cubyz_world_presets_structure_world.zig.zon_chunk_0*
