# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 0

**Type:** implementation
**Keywords:** blueprintMap, StructureBuildingBlock, LocalBlockIndex, GlobalBlockIndex, origin block, child blocks, worldArena, error.MultipleOriginBlocks, error.ChildBlockNotRecognized, error.NoOriginBlock
**Symbols:** structureList, structureMap, blueprintList, blueprintMap, childrenToResolve, originBlockStringId, originBlockNumericId, childBlockNumericIdMap, childBlockName, childBlockNameToLocalIndex, BlueprintIndex, StructureIndex, LocalBlockIndex, GlobalBlockIndex, Blueprints, BlueprintEntry, StructureBlock, isChildBlock
**Concepts:** blueprint parsing, origin block detection, child block resolution, local/global indexing, structure building blocks, error handling, memory arena allocation, block type predicates

## Summary
This chunk defines the server-side terrain structure building block (SBB) system, including blueprint parsing with origin and child block resolution, local/global block indexing, and helper predicates for identifying block types.

## Explanation
The chunk declares global state variables: a list and map of StructureBuildingBlock instances (structureList/structureMap), a list and map of BlueprintEntry instances (blueprintList/blueprintMap), a managed list of childrenToResolve awaiting resolution, originBlockStringId constant, originBlockNumericId counter, childBlockNumericIdMap mapping GlobalBlockIndex to LocalBlockIndex, childBlockName list, and childBlockNameToLocalIndex. It defines two public enum types: BlueprintIndex (u32) with fromId and get methods accessing blueprintMap and blueprintList; StructureIndex (u32) with fromId and get methods accessing structureMap and structureList. It defines LocalBlockIndex (u16) with an origin sentinel value, a name method returning childBlockName items, and a fromName method using childBlockNameToLocalIndex; GlobalBlockIndex is declared as u16. The chunk declares the Blueprints struct containing items (?[4]BlueprintEntry), chance (f32), and BlueprintEntry struct with blueprint, originBlock, and childBlocks fields. StructureBlock is defined inside BlueprintEntry with x, y, z, index (LocalBlockIndex), data (u16) fields; it provides inline direction returning Neighbor via @enumFromInt(self.data), pos returning Vec3i, and id returning the name of self.index. The init function for Blueprints takes a blueprint and stringId, initializes a BlueprintEntry with undefined originBlock and childBlocks, then iterates over blueprint.blocks dimensions to locate origin blocks (setting originBlock if not already found, logging error.MultipleOriginBlocks if duplicate) and child blocks (looking up typ in childBlockNumericIdMap, returning error.ChildBlockNotRecognized if missing, appending to a temporary List(StructureBlock), replacing the block with getVoidBlock). After loops it checks for hasOrigin, logs error.NoOriginBlock if absent. It then dupe's childBlocks into self.childBlocks using main.worldArena. The chunk ends mid-definition of pub fn isChildBlock(block: Block) bool.

## Related Questions
- What is the purpose of childrenToResolve in this chunk?
- How does LocalBlockIndex handle its origin sentinel value?
- Which error is returned when a child block typ is not found in childBlockNumericIdMap?
- Where are origin blocks replaced with void blocks during blueprint init?
- What memory arena is used to dupe the resolved childBlocks array?
- How does StructureIndex.fromId retrieve a structure from the global map?
- Is there any concurrency protection around structureList or blueprintList in this chunk?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_0*
