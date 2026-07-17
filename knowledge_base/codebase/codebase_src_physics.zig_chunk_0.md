# [hard/codebase_src_physics.zig] - Chunk 0

**Type:** implementation
**Keywords:** bounding box, collision checking, physical properties, surface interaction, vector calculations
**Symbols:** baseGravity, playerAirTerminalVelocity, airDensity, playerDensity, epsilon, collision, collision.Box, collision.Box.min, collision.Box.max, collision.Box.center, collision.Box.extent, collision.Box.intersects, collision.Direction, collision.collideWithBlock, collision.collides, collision.SurfaceProperties, collision.calculateSurfaceProperties
**Concepts:** collision detection, physics constants, entity interactions, block collisions

## Summary
Defines physics constants and collision detection logic for entities in the Cubyz engine.

## Explanation
This chunk defines various physical constants such as gravity, terminal velocity, and densities. It includes a struct `collision` that handles collision detection between entities and blocks. The `Box` struct within `collision` represents a bounding box with methods to calculate its center, extent, and intersection with other boxes. The `collideWithBlock` function checks for collisions between an entity's bounding box and a block's collision model. The `collides` function determines if an entity collides with blocks in a given direction. Additionally, the `calculateSurfaceProperties` function calculates friction and bounciness properties based on surface interactions.

## Code Example
```zig
pub fn center(self: Box) Vec3d {
	return (self.min + self.max)*@as(Vec3d, @splat(0.5));
}
```

## Related Questions
- What is the base gravity value defined in this chunk?
- How does the `Box` struct calculate its center?
- What function checks for collisions between an entity and a block?
- How is the direction vector determined in the `collides` function?
- What properties are calculated by the `calculateSurfaceProperties` function?
- How is the intersection of two bounding boxes checked?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_0*
