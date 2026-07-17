# [src/sync.zig] - Chunk 2707990592

**Type:** review
**Keywords:** CraftFrom, alloc, free, serialize, deserialize, InventoryId, ItemStack, run, finalize, meta.eql, varInt
**Symbols:** CraftFrom, destinations, sources, resultStack, sourceStacks, init, finalize, run, serialize, deserialize, Inventory, ItemStack, Side, BinaryReader, BinaryWriter
**Concepts:** memory ownership transfer, struct initialization with allocation, resource cleanup via finalize, serialization/deserialization protocol, inventory crafting logic, duplicate item aggregation, partial stack deletion, empty slot selection strategy

## Summary
Added the CraftFrom struct to handle crafting logic with proper memory management and serialization.

## Explanation
The change introduces a new struct 'CraftFrom' in sync.zig to encapsulate the state required for executing a craft command. It includes destinations, sources, resultStack, and sourceStacks fields. The init function allocates copies of inventory pointers (using .super) and duplicates ItemStack arrays to ensure ownership is transferred correctly into the struct. The finalize method frees all allocated memory to prevent leaks. The run method implements the crafting algorithm: it first validates that all involved inventories are normal type, then checks if sufficient source items exist by aggregating amounts across duplicate entries in sourceStacks before iterating over sources to delete required items. It handles partial deletions when a single slot doesn't contain enough of an item, using std.meta.eql for item comparison. After sourcing ingredients, it places the result stack into destination inventories, preferring empty slots and then filling existing stacks up to their max size, with logic to handle overflow by finding another empty slot. The serialize method writes varints for lengths followed by InventoryId enums and ItemStack bytes, while deserialize reads these fields back, returning error.Invalid if sizes are inconsistent or data is truncated.

## Related Questions
- What is the purpose of the .super field access in CraftFrom.init?
- How does CraftFrom.run handle cases where a single source slot contains more items than needed for the recipe?
- In what order are destination slots considered when placing the crafted result stack?
- Does CraftFrom.serialize include any error handling or validation before writing data?
- What happens in deserialize if destinationsSize is zero upon reading the varint length?
- How does the code ensure that no memory leaks occur after a craft command completes?
- Why are duplicate entries in sourceStacks aggregated by item type before iterating sources?
- Is there any assertion or panic used inside CraftFrom.run to guarantee correctness of ingredient consumption?
- What would happen if a destination inventory is not of type .normal when entering CraftFrom.run?
- How does the code decide whether to partially fill an existing stack versus finding an empty slot for the result item?

*Source: unknown | chunk_id: github_pr_2506_comment_2707990592*
