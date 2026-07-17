# [hard/addon_creator_app-studio.js] - Chunk 3

**Type:** ui
**Keywords:** biome-form, entity-form, particle-form, block-preset, item-preset, recipe-preset, dynamic-tags, form-population, preset-loading, conditional-fields
**Symbols:** populateBiomeFormValues, populateEntityFormValues, populateParticleFormValues, toggleParticleShapeFields, loadBlockPreset, loadItemPreset, loadRecipePreset
**Concepts:** data-binding, form-population, preset-loading, dynamic-tag-system, conditional-field-toggling, UI-state-management

## Summary
This module contains utility functions to populate form inputs with data from project definitions (biomes, entities, particles) and load preset configurations for blocks, items, and recipes.

## Explanation
The chunk defines several window-scoped functions: populateBiomeFormValues populates a biome configuration form by finding the matching biome in projectData.biomes and setting various input fields including ID, chance, interpolation, radius limits, height limits, roughness, hills, mountains, soil creep, terrain preservation, surface/sub/stone blocks, caves, crystals, music, fog density, beach smoothing, cave spawning, sky/fog colors, climate/humidity/zone/growth/elevation radio buttons, and dynamically rendering structures. populateEntityFormValues fills entity form fields (ID, height, coordinate system, model search, texture search) and initializes the dynamic tag system for entity tags. populateParticleFormValues loads particle data into corresponding inputs (ID, texture, emission flag with warning visibility, speed/size/life/density ranges, rotation velocity, drag, spawn shape, direction mode, directional components, random rotate, collision), toggles shape-specific fields (radius vs size) and direction-specific fields based on the loaded values. toggleParticleShapeFields dynamically builds and shows/hides a wrapper containing either a sphere radius input or cube bounds vector input depending on the particle shape. loadBlockPreset loads predefined block configurations (log, leaves, ore, stone, dirt) into form inputs for health, resistance, rotation, collision, transparency, texture searches for top/front/left/right/up/bottom faces, item icon search, handles rotation change, initializes dynamic tag system for block tags, toggles drop input, marks form as dirty, and schedules a preview update. loadItemPreset loads predefined item configurations (amber, ruby, iron) into inputs for ID, stack size, texture search, material properties (durability, swing speed, roughness, mass damage, hardness damage), modifier strength, base color, modifier type dropdown/search, and initializes dynamic tag system for item tags. loadRecipePreset handles recipe preset loading by setting filename, input/output searches and counts based on the key ('planks' or 'workbench').

## Related Questions
- What happens when populateBiomeFormValues is called with a biome ID that does not exist in projectData.biomes?
- How are the climate and humidity radio buttons populated in the biome form?
- Which fields are conditionally shown or hidden based on particle shape in toggleParticleShapeFields?
- What preset keys are supported by loadBlockPreset and what data do they contain?
- How does loadItemPreset handle modifier types, and where is that information displayed to the user?
- In populateEntityFormValues, how is the coordinate system input initialized if not provided in the entity definition?
- What triggers window.markFormAsDirty when loading a block preset?
- Does populateParticleFormValues initialize any default values for missing particle properties?
- How does loadRecipePreset differentiate between 'planks' and 'workbench' presets in terms of input/output configuration?
- Are there any event handlers attached to the inputs populated by these functions, or are they purely static assignments?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_3*
