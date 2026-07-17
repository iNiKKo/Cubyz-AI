# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 2

**Type:** implementation
**Keywords:** StructureBuildingBlock, initFromZon, postResolutionChecks, blueprints, children, rotation, registerSBB, registerChildBlock, childBlockNumericIdMap, childBlockName, childBlockNameToLocalIndex, main.worldArena
**Symbols:** registerSBB, registerChildBlock
**Concepts:** structure building block registration, blueprint validation, child block configuration checking, ZON asset parsing, rotation parameter handling, map key string duplication, reverse lookup table construction

## Summary
This chunk defines the StructureBuildingBlock struct and its initialization logic from ZON blueprint data, including validation of child blocks against blueprints, rotation parsing, and registration functions for building block assets.

## Explanation
The chunk declares pub fn registerSBB which iterates over an Assets.ZonHashMap to load structure building blocks into a list and map, asserting the structures collection is initially empty. It calls StructureBuildingBlock.initFromZon (defined elsewhere) with each entry's key and value, then duplicates the ZON key string into main.worldArena for use as a map key. After loading all entries, it runs postResolutionChecks on every loaded SBB to validate that blueprint-referenced child blocks have corresponding configuration entries in self.children and that configured children are referenced by at least one blueprint. The chunk also defines pub fn registerChildBlock which registers a new child block given numericId and stringId, asserting numericId is non-zero, computing an index from childBlockNumericIdMap.count(), inserting the mapping into childBlockNumericIdMap, extracting the color name portion of stringId (splitting backwards on '/'), duplicating that color name into main.worldArena, appending it to childBlockName, and registering a reverse lookup in childBlockNameToLocalIndex. The chunk does not define any function bodies or struct/enum definitions within its own raw content; all referenced types like StructureBuildingBlock, Blueprints, BlueprintEntry, LocalBlockIndex, Rotation, Assets.ZonHashMap are declared elsewhere.

## Related Questions
- What does registerSBB do with the input structures ZonHashMap?
- How are child blocks validated against blueprints in postResolutionChecks?
- What happens if a blueprint references a child block without configuration?
- What is the purpose of duplicating the key string into main.worldArena?
- How does registerChildBlock compute the index for a new child block?
- Where are the color names extracted from the stringId in registerChildBlock?
- Why does registerSBB assert that structureList.items.len == 0 before loading?
- What error is logged when initFromZon fails during registration?
- How are reverse lookups for child blocks stored after registration?
- Does this chunk define any public functions besides registerSBB and registerChildBlock?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_2*
