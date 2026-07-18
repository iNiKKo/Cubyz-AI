# [medium/addon_creator_app-io.js] - Chunk 1

**Type:** ui
**Keywords:** absorbedLightColor, dropAuto, hasItemIcon, material properties, callbacks, sides, tags, stackSize, foodValue, blockPlacement, texture, durability, swingSpeed, modifierType, height
**Symbols:** absorbedLightColor, dropAuto, dropSearch, hasItemIcon, itemIconSearch, baseTexture, callbacks, sides, tags, parsedTags, content, extractVal, getSideTex, stackSize, foodValue, blockPlacement, texture, colors, baseColor, material, durability, swingSpeed, textureRoughness, massDamage, hardnessDamage, modifierType, modifierStrength, height, coordinateSystem, model, defaultTexture, speedRange, lifeRange, densityRange, rotRange, dragRange, directionVectorMatch, hasEmission, speedMin, speedMax, lifeMin, lifeMax, densityMin, densityMax, rotVelMin, rotVelMax, dragMin, dragMax, randomRotate, collides, shape, shapeRadius, shapeSize, mode, dirX, dirY, dirZ, inputsParsed, inputsMatch, outputs
**Concepts:** data-binding, file parsing, project data model, regular expressions, configuration extraction

## Summary
This chunk handles the parsing and processing of different types of files (.zig.zon) within an addon project, extracting relevant data and populating it into the corresponding sections of the project's data structure.

## Explanation
The chunk processes various file paths and their content to extract specific configurations and data. It uses regular expressions to parse values from the file content, such as tags, texture paths, material properties, and more. The extracted data is then structured into objects that are pushed into arrays or added to objects within `window.projectData`, which represents the project's overall data model. This includes handling files for blocks, items, entity models, particles, recipes, and biomes.

## Related Questions
- How does the chunk extract and process data from .zig.zon files for blocks?
- What regular expressions are used to parse material properties in item files?
- How is the `callbacks` object populated based on the content of block files?
- What steps are taken to ensure that texture paths are correctly formatted in entity model files?
- How does the chunk handle parsing and storing data for recipes, including inputs and outputs?
- What mechanisms are used to validate or sanitize extracted values before they are added to `window.projectData`?
- How does the chunk manage different coordinate systems specified in entity model files?
- What is the process for extracting and handling speed ranges from particle files?
- How does the chunk ensure that default texture paths are correctly formatted in biomes files?
- What steps are taken to parse and store structure data from biome files?

*Source: unknown | chunk_id: addon_creator_app-io.js_chunk_1*
