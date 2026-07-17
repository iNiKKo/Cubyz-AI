# [hard/codebase_src_sync.zig] - Chunk 11

**Type:** implementation
**Keywords:** Inventory.Inventories, BinaryReader, BinaryWriter, Side, Context, recipe validation, client-server serialization, item bag retrieval, procedural item generation
**Symbols:** TakeFromPlayerBag, CraftFrom, CraftProceduralItem
**Concepts:** inventory crafting, recipe validation, client-server serialization, item bag retrieval, procedural item generation

## Summary
This chunk defines three public structs for inventory crafting operations: TakeFromPlayerBag (taking items from a player's bag), CraftFrom (crafting using recipe ingredients), and CraftProceduralItem (crafting procedurally generated items).

## Explanation
The chunk declares TakeFromPlayerBag with fields destinations and amount, providing init, finalize, run, serialize, and deserialize methods. Its run method asserts ctx.side is client or user exists, retrieves the player bag via @

## Related Questions
- What are the public fields of TakeFromPlayerBag?
- How does TakeFromPlayerBag.run handle client versus server contexts?
- What error is returned if a player bag cannot be retrieved in TakeFromPlayerBag.run?
- Which methods must be called to finalize TakeFromPlayerBag before dropping it?
- What does CraftFrom.validate check regarding the recipe result item?
- How are source ingredients consumed during CraftFrom.run?
- What happens if CraftProceduralItem cannot hold the resulting procedural item?
- Does CraftProceduralItem.run call ctx.cmd.removeProceduralItemCraftingIngredients?
- Which types are used for serialization in all three structs?
- How does deserialize handle allocation failures with errdefer?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_11*
