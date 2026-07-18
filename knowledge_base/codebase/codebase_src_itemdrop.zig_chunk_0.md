# [hard/codebase_src_itemdrop.zig] - Chunk 0

**Type:** api
**Keywords:** struct, networking, synchronization, item drop, position, velocity
**Symbols:** ItemDrop, ItemDrop.pos, ItemDrop.vel, ItemDrop.rot, ItemDrop.onGround, ItemDrop.itemStack, ItemDrop.despawnTime, ItemDrop.pickupCooldown, ItemDrop.reverseIndex, ItemDropNetworkData, ItemDropNetworkData.index, ItemDropNetworkData.pos, ItemDropNetworkData.vel
**Concepts:** item drops, network synchronization

## Summary
Defines the structure and network data for item drops in the game.

## Explanation
This chunk defines the `ItemDrop` struct, which represents an item drop entity with properties such as position, velocity, rotation, whether it is on the ground, the item stack it contains, despawn time, and pickup cooldown. It also defines the `ItemDropNetworkData` struct, which is used for network communication to synchronize item drops across clients.

## Related Questions
- What are the fields of the ItemDrop struct?
- How is item drop data synchronized over the network?
- What does the ItemDropNetworkData struct contain?
- What is the purpose of the reverseIndex field in ItemDrop?
- How is the position and velocity of an item drop represented?
- What are the conditions for despawning an item drop?

*Source: unknown | chunk_id: codebase_src_itemdrop.zig_chunk_0*
