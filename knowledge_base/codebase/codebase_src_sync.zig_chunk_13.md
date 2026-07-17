# [hard/codebase_src_sync.zig] - Chunk 13

**Type:** implementation
**Keywords:** UpdateBlock, AddHealth, cmpxchgBlock, blockUpdate, canBeChangedInto, useDurability, delete, dropLocation, getUserListAndIncreaseRefCount, freeUserListAndDecreaseRefCount, serialize, deserialize
**Symbols:** UpdateBlock, AddHealth
**Concepts:** block modification, inventory changes, atomic block swap, client protocol messages, item drops, health addition, user list resolution, gamemode checks, binary serialization

## Summary
Defines UpdateBlock and AddHealth structs with their run/serialize/deserialize methods for block modification and health addition logic.

## Explanation
The chunk declares two top-level structs: UpdateBlock and AddHealth. UpdateBlock contains fields source, pos, dropLocation (normalDir, min, max), oldBlock, newBlock. Its run method checks costOfChange via a switch on ctx.gamemode and self.oldBlock.canBeChangedInto; if allowed it performs atomic cmpxchgBlock on the server world, sends blockUpdate protocol messages to clients, applies inventory changes using ctx.execute (useDurability or delete), and drops items from self.dropLocation.drop. It also includes serialize/deserialize methods that write/read Vec3i/Vec3f/u32 via BinaryWriter/BinaryReader. AddHealth contains fields target, health, cause; its run method resolves the target user on the server side by iterating a userList obtained via main.server.getUserListAndIncreaseRefCount (with defer to freeUserListAndDecreaseRefCount), returns error.serverFailure if not found or if gamemode is creative, and executes ctx.execute(.{.addHealth = ...}). The chunk uses main.random.nextFloatVectorSigned/nextFloat for drop randomness, vec.normalize/cross for direction vectors, and @bitCast/@floatCast for type conversions.

## Related Questions
- What fields does UpdateBlock contain and how are they used in its run method?
- How does the chunk determine whether a block change is allowed before modifying it?
- Describe the sequence of operations performed when ctx.side == .server inside UpdateBlock.run.
- What error is returned if the atomic cmpxchgBlock fails or if the target user is not found in AddHealth.run?
- How are inventory changes applied after a successful block modification in UpdateBlock?
- Explain how item drops are generated and filtered by dropLocation.drop in UpdateBlock.
- What role does main.random.nextFloatVectorSigned play in the drop direction calculation?
- How is the target user resolved from the server userList in AddHealth.run?
- Under what conditions does AddHealth.run skip execution without modifying health?
- What are the exact steps performed by UpdateBlock.serialize and UpdateBlock.deserialize for binary I/O?
- Which protocol message is sent to clients when a block change occurs on the server side?
- How does the chunk handle procedural items versus regular items during inventory changes?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_13*
