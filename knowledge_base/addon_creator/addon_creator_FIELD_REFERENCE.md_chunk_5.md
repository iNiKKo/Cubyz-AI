# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 5

**Type:** documentation
**Keywords:** entities.html, saveEntityToProject, particles.html, saveParticleToProject, coordinateSystem, spawn shape, emission
**Symbols:** entityId, entityCoordSystem, particleId, particleHasEmission, particleSpawnShape

## Summary
Cubyz Addon Creator: Entities form (`entities.html`) and Particles form (`particles.html`) field-to-export mapping.

## Explanation
**Entities:** Entity ID (`entityId`) becomes the filename. Height (`entityHeight`) exports as `.height`. Coordinate System (`entityCoordSystem`) exports as `.coordinateSystem`, default `.right_handed_z_up`. Model (`entityModelSearch`) and Texture (`entityTextureSearch`) export as `.model`/`.defaultTexture`, both auto-namespaced. Tags export as `.tags = .{...}` -- **the whole block is omitted entirely if there are no tags**.

**Particles:** Particle ID (`particleId`) becomes the filename. Particle Texture (`particleTextureSearch`) exports as `.texture`, auto-namespaced. The "has emission" checkbox (`particleHasEmission`) **doesn't write a field directly** -- it controls whether a companion `{texture}_emission` texture file is also bundled into the export. Speed/Life/Density/Rotation Velocity/Drag min+max pairs export as `.speed`/`.lifeTime`/`.density`/`.rotationVelocity`/`.dragCoefficient = {.min=..., .max=...}`. Random Rotate / Collides checkboxes are direct boolean passthroughs. Spawn Shape (`particleSpawnShape`) exports as `.shape = .{shape}` -- `sphere` adds a `.radius` field (from `particleShapeRadius`); `cube` adds a `.size` field (from `particleShapeSize`). Spawn Direction (`particleDirectionMode`) exports as `.mode = .{mode}` -- `direction` mode adds `.direction = .{x, y, z}` from `particleDirX`/`particleDirY`/`particleDirZ`.

## Related Questions
- What happens to a Cubyz entity's tags block in the Addon Creator export if it has no tags?
- What controls whether a companion "_emission" texture file gets bundled for a Cubyz particle addon?
- What additional field does a Cubyz particle's "sphere" spawn shape add, and where does its value come from?
- What additional field does a Cubyz particle's "cube" spawn shape add?
- What additional field does a Cubyz particle's "direction" spawn mode add?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_5*
