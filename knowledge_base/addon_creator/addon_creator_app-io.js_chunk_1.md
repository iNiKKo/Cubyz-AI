# [medium/addon_creator_app-io.js] - Chunk 1

**Type:** ui
**Keywords:** .zig.zon, items, entities, particles, recipes, biomes, extractVal, regex match, brace counting, projectData
**Symbols:** window.projectData.items, window.projectData.entities, window.projectData.particles, window.projectData.recipes, extractVal, extractMinMax, getSideTex, parseIntegerToHexColor
**Concepts:** file parsing, regex extraction, nested JSON handling, project data population, addon blueprint processing

## Summary
This module parses .zig.zon addon files and populates the projectData object with items, entities, particles, recipes, and biomes by extracting values from file contents.

## Explanation
The code handles multiple file paths: blocks (absorbedLightColor, dropAuto, etc.), items (stackSize, foodValue, blockPlacement, tags, texture, colors, baseColor, material), entityModels/models (height, coordinateSystem, model, defaultTexture, tags), particles (speedRange, lifeRange, densityRange, rotRange, dragRange, directionVectorMatch, hasEmission, shape, mode), recipes (inputsParsed, output), and biomes (parsedStructures). It uses extractVal helper for simple key-value extraction, extractMinMax for range values, regex matches for complex structures like tags or inputs, and manual brace counting for nested JSON-like blocks. Each parsed section pushes an object into the corresponding window.projectData array or property.

## Related Questions
- How does the code extract tags from a .zig.zon file?
- What happens if a block file lacks an absorbedLight value?
- How are particle speed ranges parsed from content?
- Where is the entity model ID constructed in the code?
- Does the recipe parser handle quoted input strings?
- How does the biome parser locate structures within nested braces?
- What default values are used when extractVal fails to find a key?
- Is there any validation for texture file existence before pushing items?
- How is the coordinateSystem determined for an entity model?
- Can the particle shape be changed dynamically by editing the .zig.zon?

*Source: unknown | chunk_id: addon_creator_app-io.js_chunk_1*
