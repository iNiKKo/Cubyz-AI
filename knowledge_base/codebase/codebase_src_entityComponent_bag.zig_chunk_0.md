# [easy/codebase_src_entityComponent_bag.zig] - Chunk 0

**Type:** implementation
**Keywords:** entityComponentID, entityComponentVersion, playerBagSizeLimit, client, server, Entity, ServerChunk, game, graphics, ZonElement, renderer, settings, utils, BinaryReader, BinaryWriter
**Symbols:** entityComponentID, entityComponentVersion, playerBagSizeLimit, client, server, Entity, ServerChunk, game, graphics, ZonElement, renderer, settings, utils, BinaryReader, BinaryWriter, vec, Mat4f, Vec3d, Vec3f, Vec4f, Vec3i, NeverFailingAllocator, blocks, World, ServerWorld, items, ItemStack, random
**Concepts:** entity component, inventory management, sparse set, serialization, deletion

## Summary
Entity component for managing player bags

## Explanation
This chunk defines the entity component for managing player bags. It includes client and server-specific implementations of bag management, including initialization, deinitialization, clearing, loading, saving, and unloading. The bag is stored in a sparse set using an allocator and has a size limit of 120 items.

### Client-Specific Implementation:
- **Component Structure:**
  ```zig
  pub const client = struct {
    const Component = struct {
      bag: items.Inventory.BagInventory,
    };
  };
  ```
- **Initialization and Deinitialization:**
  ```zig
  pub fn init() void {}
  pub fn deinit() void {
    components.deinit(main.globalAllocator);
  }
  ```
- **Clearing the Component Set:**
  ```zig
  pub fn clear() void {
    components.clear();
  }
  ```
- **Getting Bag Inventory:**
  ```zig
  pub fn getBag(entity: Entity) ?*items.Inventory.BagInventory {
    return &(components.get(entity) orelse return null).bag;
  }
  ```
- **Loading from Data:**
  ```zig
  pub fn load(entity: Entity, reader: *utils.BinaryReader, version: u32) main.entity.EntityComponentLoadError!void {
    if (version != entityComponentVersion) return error.InvalidComponentVersion;
    const bag = &components.add(main.globalAllocator, entity).bag;
    bag.* = .init(main.globalAllocator, playerBagSizeLimit);
    bag.fromBytes(reader) catch return error.UnreadableComponentData;
  }
  ```
- **Unloading Bag Data:**
  ```zig
  pub fn unload(entity: Entity) void {
    const bag = components.fetchRemove(entity) catch return;
    bag.bag.deinit();
  }
  ```

### Server-Specific Implementation:
- **Component Structure:**
  ```zig
  pub const server = struct {
    pub const Component = struct {
      bag: items.Inventory.BagInventory,
      pub fn save(self: Component, writer: *utils.BinaryWriter, audience: main.entity.AudienceInfo) main.entity.ComponentSaveBehaviour {
        if (audience != .disk and audience != .playerHimself) return .discard;
        self.bag.toBytes(writer);
        return .save;
      }
    };
  };
  ```
- **Initialization and Deinitialization:**
  ```zig
  pub fn init() void {
    components = .{};
  }
  pub fn deinit() void {
    components.deinit(main.globalAllocator);
  }
  ```
- **Getting Bag Inventory:**
  ```zig
  pub fn get(entity: Entity) ?Component {
    return (components.get(entity) orelse return null).*;
  }
  pub fn getBag(entity: Entity) ?*items.Inventory.BagInventory {
    return &(components.get(entity) orelse return null).bag;
  }
  ```
- **Loading from Data:**
  ```zig
  pub fn loadFromData(entity: Entity, reader: *utils.BinaryReader, version: u32) main.entity.EntityComponentLoadError!void {
    if (version != entityComponentVersion) return error.InvalidComponentVersion;
    const bag = &components.add(main.globalAllocator, entity).bag;
    bag.* = .init(main.globalAllocator, playerBagSizeLimit);
    bag.fromBytes(reader) catch return error.UnreadableComponentData;
  }
  ```
- **Loading Empty Bag:**
  ```zig
  pub fn loadEmpty(entity: Entity) void {
    const bag = &components.add(main.globalAllocator, entity).bag;
    bag.* = .init(main.globalAllocator, playerBagSizeLimit);
  }
  ```
- **Unloading Bag Data:**
  ```zig
  pub fn unload(entity: Entity) void {
    const bag = components.fetchRemove(entity) catch return;
    bag.bag.deinit();\n  }
  ```

## Code Example
```zig
pub fn init() void {}
```

## Related Questions
- What is the purpose of the entityComponentID variable?
- How many symbols are defined in this chunk?
- What is the size limit for player bags?
- Where is the client-specific bag management implemented?
- What is the server-specific bag management implementation?
- What is the default save behavior for the server's bag component?
- What happens if an invalid version number is encountered during loading?
- How is the bag data read from a binary reader?
- What is the purpose of the loadFromData function?
- What is the purpose of the loadEmpty function?
- What does the unload function do for a player's bag?
- Where is the client-specific bag management initialized?

*Source: unknown | chunk_id: codebase_src_entityComponent_bag.zig_chunk_0*
