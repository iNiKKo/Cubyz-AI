# [medium/addon_creator_app-io.js] - Chunk 2

**Type:** ui
**Keywords:** import, parse, addon, biome, zig.zon, structures, properties, updateSearchableItems, updateSidebarProjectTree, alert
**Symbols:** inputsParsed, content, parsedStructures, startIdx, openBrace, idx, braceCount, structuresText, sIdx, openObj, subCount, subIdx, objText, lines, attrs, structObj, climate, humidity, zone, growth, elevationType, properties, propMatch, props, groundMatch, surfaceBlock, subBlock, nameToken, extractedSubFolder
**Concepts:** data-binding, file parsing, biome configuration, project data management

## Summary
Handles the import and parsing of addon files, specifically for biomes with '.zig.zon' extension.

## Explanation
This code snippet is responsible for processing imported addon files that are related to biomes. It checks if the file path includes '/biomes/' and ends with '.zig.zon'. If so, it reads the content of the file and extracts various properties such as structures, climate, humidity, zone, growth, elevation type, surface block, sub-block, stone block, and other biome-specific attributes. The extracted data is then added to the `window.projectData.biomes` array. Additionally, it updates searchable items and the sidebar project tree if the respective functions are available.

## Related Questions
- What is the purpose of the `inputsParsed` variable in this code snippet?
- How does the code extract and parse structures from the biome file content?
- What conditions are checked to determine if a file should be processed as a biome file?
- How are climate, humidity, zone, growth, and elevation type properties determined from the file content?
- What is the role of the `updateSearchableItems` function in this code snippet?
- How does the code handle errors during the parsing process?
- What specific attributes are extracted for each structure type (e.g., 'cubyz:simple_tree')?
- How is the surface block and sub-block determined from the file content?
- What is the significance of the `isValidPlayerSpawn` property in the biome configuration?
- How does the code manage to update the sidebar project tree after parsing a new biome file?

*Source: unknown | chunk_id: addon_creator_app-io.js_chunk_2*
