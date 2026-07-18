# [medium/addon_creator_app-io.js] - Chunk 1

**Type:** ui
**Keywords:** absorbedLightColor, dropAuto, hasItemIcon, material properties, callbacks, sides, tags, stackSize, foodValue, blockPlacement, texture, durability, swingSpeed, modifierType, height
**Symbols:** absorbedLightColor, dropAuto, dropSearch, hasItemIcon, itemIconSearch, baseTexture, callbacks, sides, tags, parsedTags, content, extractVal, getSideTex, stackSize, foodValue, blockPlacement, texture, colors, baseColor, material, durability, swingSpeed, textureRoughness, massDamage, hardnessDamage, modifierType, modifierStrength, height, coordinateSystem, model, defaultTexture, speedRange, lifeRange, densityRange, rotRange, dragRange, directionVectorMatch, hasEmission, speedMin, speedMax, lifeMin, lifeMax, densityMin, densityMax, rotVelMin, rotVelMax, dragMin, dragMax, randomRotate, collides, shape, shapeRadius, shapeSize, mode, dirX, dirY, dirZ, inputsParsed, inputsMatch, outputs
**Concepts:** data-binding, file parsing, project data model, regular expressions, configuration extraction

## Summary
This chunk handles the parsing and processing of different types of files (.zig.zon) within an addon project, extracting relevant data and populating it into the corresponding sections of the project's data structure.

## Explanation
This chunk handles the parsing and processing of different types of files (.zig.zon) within an addon project, extracting relevant data and populating it into the corresponding sections of the project's data structure. It uses regular expressions to parse values from the file content, such as tags, texture paths, material properties, and more. The extracted data is then structured into objects that are pushed into arrays or added to objects within `window.projectData`, which represents the project's overall data model.

For blocks:
- Extracts `absorbedLightColor` using `parseIntegerToHexColor(extractVal(content, 'absorbedLight', '16777215'), '#ffffff')`
- Checks for `.dropAuto`, `.dropSearch`, `.hasItemIcon`, and `.itemIconSearch` based on content matches
- Sets `callbacks.touchType` to "hurt" if `.onTouch` is present, otherwise sets it to "none"
- Sets `callbacks.touchMode` to "heal" if `.damageType = .heal` is present, otherwise sets it to "damage"
- Extracts `touchDps`, `touchVariant`, `updateType`, `tickType`, `breakType`, and `interactType` using regex matches
- Sets `callbacks.interactWindowName` based on content match for `.onInteract`
- Defines sides (`front`, `left`, `right`, `up`, `bottom`) using `getSideTex('texture2')`, etc.

For items:
- Extracts `stackSize`, `foodValue`, and `blockPlacement` from the file content
- Parses tags from `.tags = .{ ... }`
- Sets texture based on `extractVal(content, 'texture', 'stone').replace('.png', '')`
- Defines material properties such as `durability`, `swingSpeed`, `textureRoughness`, `massDamage`, `hardnessDamage`, and `modifierType` using regex matches

For entity models:
- Extracts `height` from the file content
- Sets coordinate system to `.left_handed_y_up` if `.coordinateSystem = .left_handed_y_up` is present, otherwise sets it to `.right_handed_z_up`
- Defines model and default texture paths using `extractVal(content, 'model', '')` and `extractVal(content, 'defaultTexture', '')`

For particles:
- Extracts speed range, life time range, density range, rotation velocity range, drag coefficient range from the file content
- Sets direction vector components based on `.direction = .{ ... }`
- Defines properties such as `hasEmission`, `speedMin`, `speedMax`, `lifeMin`, `lifeMax`, `densityMin`, `densityMax`, `rotVelMin`, `rotVelMax`, `dragMin`, `dragMax`, `randomRotate`, and `collides` using regex matches
- Sets shape, mode, radius, size based on file content

For recipes:
- Extracts inputs from `.inputs = .{ ... }`
- Defines output based on `extractVal(content, 'output', '').replace(/"/g, '')`

For biomes:
- Parses structures using regex to extract and format structure data within the biome file content

## Related Questions
- How does the chunk extract and process data from .zig.zon files for blocks?
- What regular expressions are used to parse material properties in item files, such as `durability`, `swingSpeed`, etc.?
- How is the `callbacks` object populated based on the content of block files, including specific regex patterns like `.damageType = .heal`?
- What steps are taken to ensure that texture paths are correctly formatted in entity model files using `extractVal(content, 'model', '')` and similar methods?
- How does the chunk handle parsing and storing data for recipes, including inputs and outputs based on regex matches like `.inputs = .{ ... }`?
- What mechanisms are used to validate or sanitize extracted values before they are added to `window.projectData`, such as replacing double quotes with empty strings in output extraction?
- How does the chunk manage different coordinate systems specified in entity model files using conditional checks for `.coordinateSystem`?
- What is the process for extracting and handling speed ranges from particle files, including setting properties like `speedMin`, `speedMax`, etc.?
- How does the chunk ensure that default texture paths are correctly formatted in biomes files using regex to extract structure data?

*Source: unknown | chunk_id: addon_creator_app-io.js_chunk_1*
