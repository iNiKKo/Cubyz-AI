# [medium/addon_creator_biomes.html] - Chunk 1

**Type:** ui
**Keywords:** Min Height, Max Height, Smooth Beaches, Roughness Factor, Hills Factor, Mountains Factor, Soil Creep Slip Factor, Keep Original Mix, Ambient Music Track, Fog Thickness Density, Sky Tint, Fog Atmospheric Tint, Valid Spawn, Enable Cave Biome Properties, Cave Density Scale
**Symbols:** bioMinHeight, bioMaxHeight, bioSmoothBeaches, bioMinHeightLimit, bioMaxHeightLimit, bioRoughness, bioHills, bioMountains, bioSoilCreep, bioKeepOriginalTerrain, bioMusic, btnPlayMusic, bioFogDensity, bioSkyColor, bioFogColor, bioSpawn, bioIsCave, caveSettings, bioCaves, bioCaveRadiusFactor, bioCrystals, biomeStructuresContainer
**Concepts:** data-binding, form validation, live preview

## Summary
The UI component in this chunk is responsible for configuring various biome properties such as height limits, terrain factors, environmental settings, and underground cave generation.

## Explanation
This HTML snippet defines a section of the Cubyz Addon Creator's UI where users can configure different aspects of a biome. It includes input fields for numerical values (e.g., Min Height, Max Height), checkboxes (e.g., Smooth Beaches, Valid Spawn), color pickers (e.g., Sky Tint, Fog Atmospheric Tint), and file inputs for custom audio tracks. The UI is organized into sections with headers like 'Environment, Audio & Atmospheric Tints' and 'Underground Cave Gen'. Event handlers are attached to buttons for actions such as playing music previews, adding custom audio files, toggling cave settings visibility, and saving the biome configuration to the project.

## Related Questions
- What is the purpose of the 'bioSmoothBeaches' checkbox in the UI?
- How does the UI handle custom audio file uploads for ambient music?
- What event handler is triggered when the user clicks the 'Save Biome to Project' button?
- How are color values selected and bound in the UI?
- What validation checks are applied to numerical input fields like 'bioMinHeight'?
- How does the UI toggle the visibility of cave settings based on user interaction?
- What is the functionality of the '+ Add Structure Layer' button in the Foliage, Decor & Structures section?
- How does the UI generate a live preview of the biome configuration?
- What data-binding techniques are used to update the project with the configured biome properties?
- How does the UI manage and display dropdown options for music tracks?

*Source: unknown | chunk_id: addon_creator_biomes.html_chunk_1*
