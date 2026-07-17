# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 1

**Type:** api
**Keywords:** enum, union, FixedRotation, RotationMode, fromZon, sampleRandom, Neighbor, BlueprintIndex
**Symbols:** 0, 90, 180, 270
**Concepts:** rotation system, blueprint parsing, ZON file handling

## Summary
This chunk defines the Rotation system (RotationMode enum, FixedRotation union with string/int/float parsing) and StructureBuildingBlock struct for blueprint initialization from ZON files.

## Explanation
The chunk declares pub const RotationMode as an enum with fixed/random/inherit variants. It then defines a union named Rotation that holds either a FixedRotation (enum u2 with @

## Related Questions
- What are the valid values of RotationMode?
- How does FixedRotation represent rotation angles?
- Which function parses a ZON element into a Rotation value?
- What happens when fromZon receives an int or float input?
- How is random rotation sampled using sampleRandom?
- What error is returned if a blueprint entry lacks an id field?
- Does StructureBuildingBlock store children as pointers?
- Where are blueprints stored inside StructureBuildingBlock?
- Is the Rotation union tagged or untagged?
- Can fromZon handle null ZON elements?
- How does fromZon convert a string to FixedRotation?
- What error is returned if the blueprints field in a ZON element is not an array?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_1*
