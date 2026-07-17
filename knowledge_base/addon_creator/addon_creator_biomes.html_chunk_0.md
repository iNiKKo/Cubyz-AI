# [medium/addon_creator_biomes.html] - Chunk 0

**Type:** ui
**Keywords:** biome, presets, terrain, climate, humidity, environment, flora, elevation, blocks, dropdowns, validation, defaults
**Symbols:** biomePresetSelectorSearch, biomePresetDropdown, biomeId, biomeChance, bioInterpolationSearch, bioInterpolationDropdown, bioInterpolation, bioSurfaceBlock, bioSurfaceDropdown, bioSubBlock, bioSubDropdown, bioStoneBlock, bioStoneDropdown, bioMinRadius, bioMaxRadius, bioMinHeight, bioMaxHeight, bioSmoothBeaches, bioMinHeightLimit, bioMaxHeightLimit
**Concepts:** data-binding, form-validation, live-preview, dropdown-selection, segmented-controls, preset-loading, block-recipe-filtering

## Summary
The Biome Creator panel provides a UI for defining biome generation parameters, including preset loading, terrain size/shape constraints, climate/humidity/environment settings via segmented controls, and ground layer block selection with live recipe dropdowns.

## Explanation
UI Controls: Text inputs (biomeId, biomeChance, bioInterpolationSearch, bioSurfaceBlock, bioSubBlock, bioStoneBlock, bioMinRadius, bioMaxRadius, bioMinHeight, bioMaxHeight, bioMinHeightLimit, bioMaxHeightLimit) with validation via oninput handlers; Dropdowns (biomePresetDropdown, bioInterpolationDropdown) triggered by focus/mousedown events; Segmented radio controls for Climate (.hot/.temperate/.cold), Humidity (.wet/.neither/.dry), Environment (.inland/.land/.ocean), Flora (.barren/.balanced/.overgrown), Elevation Type (.lowTerrain/.balanced/.mountain/.antiMtn); Checkbox (bioSmoothBeaches). Event Handlers: onfocus on preset selector opens dropdown and sets value; onmousedown on dropdown options updates the readonly search input, calls window.loadBiomePreset('type'), and hides dropdown; oninput on block inputs filters a recipe dropdown via window.filterDropdown and shows it via window.showRecipeDropdown when focused. Defaults: biomeId placeholder 'ruby_valleys' (auto-lowercased, alphanumeric+underscore only); bioInterpolation default '.square'; Climate temperate, Humidity neitherWetNorDry, Environment inland, Flora balanced, Elevation Type balanced; Smooth Beaches checked. Templates: none explicitly defined in this chunk. Engine Mappings: window.loadBiomePreset maps preset name to biome type string; window.filterDropdown filters block recipes by input value; window.showRecipeDropdown renders a dropdown list of matching blocks. Configuration Generation: The UI constructs a biome config object (not shown here) from the collected values, likely using the IDs as property names and the segmented control names as grouped fields.

## Related Questions
- What happens when a user clicks on a preset option in the dropdown?
- How does the UI enforce alphanumeric-only input for biomeId?
- Which segmented control is used to set the default climate value?
- What triggers the display of the block recipe dropdowns for surface/subsurface layers?
- Are there any hidden inputs that store the actual biome configuration values?
- How does the UI handle the checkbox for Smooth Beaches in terms of defaults and user interaction?

*Source: unknown | chunk_id: addon_creator_biomes.html_chunk_0*
