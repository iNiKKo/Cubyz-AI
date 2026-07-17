# [hard/codebase_src_sync.zig] - Chunk 9

**Type:** serialization
**Keywords:** FillFromCreative, FillAnyFromCreative, DepositOrDrop, serialize, deserialize, run, finalize, canPutInto, gamemode, Inventories, ZonElement, deinit, Context, serverFailure, Vec3d
**Symbols:** FillFromCreative, FillAnyFromCreative, DepositOrDrop
**Concepts:** inventory fill, creative mode checks, serialization, deserialization, ZonElement encoding, context execution, error handling, memory cleanup

## Summary
Defines server-side inventory fill and deposit operations with serialization support.

## Explanation
The chunk declares three structs: FillFromCreative, FillAnyFromCreative, and DepositOrDrop. Each struct contains fields for destinations (InventoryAndSlot or Inventory.Inventories), items, amounts, and drop locations where applicable. All structs implement run methods that execute actions within a Context; they check the gamemode to ensure only creative mode allows these operations. The run implementations use callbacks like canPutInto to validate item placement, delete existing stacks when necessary, and create new stacks with appropriate amounts (using stackSize() if amount is zero). Serialization is provided via serialize and deserialize methods: serialize writes destinations as bytes, an integer amount, and optionally a ZonElement-encoded string for the item; deserialize reads these components back, using ZonElement.parseFromString to reconstruct items when data remains. Finalize methods clean up allocated Inventories by calling deinit on main.globalAllocator. DepositOrDrop also provides init helpers that construct the struct from client inventories or generic Inventory slices, and an initWithInventories variant for server-side deposits. The code uses error handling with !FillFromCreative/!DepositOrDrop return types and errdefer in deserialize to ensure cleanup on failure.

## Related Questions
- How does FillFromCreative validate item placement before adding it to an inventory?
- What happens in the run method when a destination inventory is not empty and the gamemode is creative?
- How are items serialized into the binary format for network transmission?
- What steps occur during deserialization of FillFromCreative when there is remaining data after reading amount?
- Which allocator is used to free Inventories in the finalize methods of these structs?
- How does DepositOrDrop handle server-side deposits versus client-side actions?
- What error type is returned by run and deserialize for FillFromCreative and FillAnyFromCreative?
- Does the chunk provide any public init functions for constructing DepositOrDrop, and what are their signatures?
- How does the serialize method encode an item that is not null in these structs?
- What condition causes the run method to skip processing a stack during deposit operations?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_9*
