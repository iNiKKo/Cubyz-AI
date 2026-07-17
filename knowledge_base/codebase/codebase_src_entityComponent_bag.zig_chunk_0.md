# [easy/codebase_src_entityComponent_bag.zig] - Chunk 0

**Type:** api
**Keywords:** SparseSet, BagInventory, BinaryReader, BinaryWriter, entityComponentVersion, init, deinit, load, unload, getBag
**Symbols:** entityComponentID, entityComponentVersion, playerBagSizeLimit, client, server
**Concepts:** entity component system, sparse set storage, binary serialization, versioning checks, lifecycle management, client server separation

## Summary
This chunk defines the entity component system for player bags, providing separate client and server implementations with sparse set storage, binary serialization, versioning checks, and lifecycle management (init/deinit/load/unload).

## Explanation
The chunk declares a global entityComponentID and version constant. It exposes two public structs: client and server. The client struct contains a Component with a BagInventory field and a SparseSet mapping Entity to Component; it provides init, deinit, clear, getBag (returns pointer or null), load (reads binary data after version check), and unload (removes from sparse set and deallocates). The server struct similarly defines a Component with a BagInventory and a save method that writes bytes only for disk or playerHimself audiences; it includes init, deinit, get, getBag, loadFromData (adds component if missing, reads binary data), loadEmpty (adds empty component), and unload. Both structs use main.globalAllocator for allocations. The chunk imports various types from other modules but does not define any functions or methods beyond those inside the client/server structs.

## Related Questions
- What is the default size limit for a player bag?
- How does the client load function handle version mismatches?
- Which audience types trigger actual binary writes on the server side?
- Does the client struct provide a method to clear all components?
- What happens when getBag returns null in the client implementation?
- Is there any difference between load and loadFromData on the server?
- How are components allocated during initialization on both sides?

*Source: unknown | chunk_id: codebase_src_entityComponent_bag.zig_chunk_0*
