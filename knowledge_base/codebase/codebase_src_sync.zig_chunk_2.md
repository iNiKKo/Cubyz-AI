# [hard/codebase_src_sync.zig] - Chunk 2

**Type:** serialization
**Keywords:** union variants, InventoryAndSlot, stack size limits, deserialize, ref assignment, update method, client messages, server logic, item manipulation, health energy operations
**Symbols:** Payload, BaseOperationType, BaseOperation, SyncOperationType, SyncOperation, executeFromData
**Concepts:** inventory synchronization, payload union types, base operations, server-side updates, serialization protocol

## Summary
Defines the server-side inventory synchronization protocol, including payload types for client requests and base operations for item manipulation.

## Explanation
This chunk declares a union of PayloadType values (open, close, depositOrSwap, etc.) that represent different kinds of client-to-server messages. It then defines BaseOperationType as an enum with move, swap, delete, create, moveToBag, takeFromBag, useDurability, addHealth, and addEnergy. Each base operation is a union variant containing fields like dest/source InventoryAndSlot, amount u16, item Item, or pointers to User for health/energy changes. A separate SyncOperationType enum (create, delete, useDurability, health, kill, energy) is provided with corresponding union variants that include the inv field and amount/durability values; these are used on the server side to apply updates from serialized data. The executeFromData function begins deserialization logic for create and delete operations, checking item nullness, stack size limits, and updating inventory amounts via ref().item assignment and .update() calls.

## Related Questions
- What payload types are defined for client requests in this chunk?
- How is the BaseOperationType enum structured and what values does it include?
- What fields are present in each variant of the BaseOperation union?
- Is there a separate SyncOperation type and how does it differ from BaseOperation?
- Which operations are included in SyncOperationType for server-side updates?
- Where does executeFromData begin processing deserialized data?
- How does create handle null items versus existing items during execution?
- What validation is performed on stack size before applying an item creation?
- How does delete check whether the removal amount exceeds current inventory contents?
- When does delete set the item to null after removing its quantity?
- Are there any other functions defined in this chunk beyond executeFromData?
- Do these definitions import or reference types from other modules?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_2*
