# [hard/codebase_src_network_protocols.zig] - Chunk 4

**Type:** networking
**Keywords:** BinaryReader, BinaryWriter, conn.send, UpdateType, ZonElement, removeEntity, addEntity, loadFrom, addFromZon, mesh_storage.updateBlock, Block.fromInt, remaining.len
**Symbols:** blockUpdate, entity, genericUpdate, blockUpdate.id, entity.id, genericUpdate.id, blockUpdate.clientReceive, blockUpdate.send, entity.clientReceive, entity.send, genericUpdate.clientReceive
**Concepts:** network protocol, binary serialization, client receive handler, server send handler, ZonElement parsing, block entity data, item drop updates, enum dispatching

## Summary
Defines network protocol handlers for block updates and entity/item state changes via binary serialization.

## Explanation
The chunk declares three public structs: blockUpdate, entity, and genericUpdate. Each struct contains a pub const id field (u8) identifying the protocol message type, and two functions: clientReceive and send. The blockUpdate.clientReceive reads Vec3i position, Block.fromInt(u32), and a slice of block entity data from a BinaryReader until remaining.len == 0; it calls renderer.mesh_storage.updateBlock with those values. blockUpdate.send writes the same fields into a BinaryWriter (initCapacity) and sends via conn.send(.secure). The entity.clientReceive parses a ZonElement array from reader.remaining, handling .int (removeEntity), .object (addEntity), and .null (skip); it also processes item drops by checking for an 'array' child or calling loadFrom/addFromZon. entity.send simply forwards the raw message bytes with conn.send(.secure). The genericUpdate.clientReceive begins a switch on UpdateType read from the reader; only the gamemode case is shown, indicating further cases exist but are not included in this chunk.

## Related Questions
- What does blockUpdate.clientReceive read from the BinaryReader and how does it stop?
- How is the block entity data slice length determined in blockUpdate.send?
- What happens when an unrecognized ZonElement type appears in entity.clientReceive?
- Which UpdateType values are defined inside genericUpdate and which one is implemented here?
- How does entity.clientReceive handle item drops versus other elements in the Zon array?
- What error is returned if a parsed integer cannot be converted to a valid Entity ID?
- Does blockUpdate use .secure or .lossy when sending updates over the connection?
- Where is renderer.mesh_storage.updateBlock invoked and what arguments does it receive?
- How are positions encoded for entities in entity.clientReceive versus genericUpdate?
- What is the purpose of the ZonElement.parseFromString call inside entity.clientReceive?
- Are any of these structs marked pub const or pub fn, and why might that matter to other modules?
- Which fields of blockUpdate are declared as constants and which as functions?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_4*
