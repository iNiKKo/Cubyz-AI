# [easy/codebase_src_server_Entity.zig] - Chunk 0

**Type:** implementation
**Keywords:** entity, ZonElement, component, memory management, serialization
**Symbols:** Entity, loadFrom, clone, save, deinit
**Concepts:** entity management, serialization

## Summary
Entity management and serialization

## Explanation
This chunk defines the Entity struct, which represents a game entity with position, velocity, rotation, health, energy, name, and ID. It provides functions to load, clone, save, and deinitialize entities from and to ZonElement format, handling component loading and saving, as well as memory management for names.

## Code Example
```zig
pub fn loadFrom(self: *@This(), id: main.entity.Entity, zon: ZonElement, comptime side: main.sync.Side) !void {
    self.id = id;
    self.pos = zon.get(Vec3d, "position") orelse .{0, 0, 0};
    self.vel = zon.get(Vec3d, "velocity") orelse .{0, 0, 0};
    self.rot = zon.get(Vec3f, "rotation") orelse .{0, 0, 0};
    self.health = zon.get(f32, "health") orelse self.maxHealth;
    self.energy = zon.get(f32, "energy") orelse self.maxEnergy;
    if (zon.getChildOrNull("components")) |components| {
        try main.entity.loadComponentsFromBase64(components.as([]const u8) orelse "", self.id, side);
    }

    if (zon.getChildOrNull("name")) |name| {
        if (self.name) |oldname| {
            main.globalAllocator.free(oldname);
        }
        self.name = main.globalAllocator.dupe(u8, name.as([]const u8) orelse "invalid name");
    }
}
```

## Related Questions
- What is the purpose of the `loadFrom` function?
- How does the `clone` function work?
- What data is saved when calling the `save` function?
- Under what conditions are components loaded and saved?
- What happens if an entity has a name, and how is it managed?
- How is memory allocated for names in this codebase?
- What side-specific actions are taken during deinitialization?
- Where is the global allocator used in this codebase?
- What does the `componentsToBase64` function do?
- How are components removed from entities on client and server sides?
- What happens if an entity's name is updated after loading?
- Is there any error handling or validation in these functions?

*Source: unknown | chunk_id: codebase_src_server_Entity.zig_chunk_0*
