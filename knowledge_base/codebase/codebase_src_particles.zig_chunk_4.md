# [hard/codebase_src_particles.zig] - Chunk 4

**Type:** api
**Keywords:** spawn, parse, direction mode, seed RNG, ZonElement, collision flag, ParticleTypeLocal, extern struct, capacity cap, RandomRange
**Symbols:** SpawnCube, SpawnCube.spawn, SpawnCube.parse, Emitter, Emitter.init, Emitter.initFromZon, Emitter.spawnParticles, ParticleType, ParticleTypeLocal, Particle, ParticleLocal
**Concepts:** particle emitter, direction mode selection, seeded RNG offset, ZonElement parsing, collision flag, particle lifecycle fields, extern particle struct, capacity capping

## Summary
This chunk defines the core particle emitter API and data structures for spawning particles with configurable size, direction mode (direction/scatter/spread), collision behavior, and per-particle properties including lifetime, rotation velocity, drag coefficient, light index, and type.

## Explanation
The chunk declares SpawnCube as a struct containing pub fn spawn(pos: Vec3d, properties: EmitterProperties, mode: DirectionMode) which computes an offset position using the main seed RNG (random.nextFloatVectorSigned), scales it by self.size, normalizes or samples direction based on mode, and returns particlePos/vel. SpawnCube also has pub fn parse(zon: ZonElement) !SpawnCube that reads a 'size' field from a ZonElement, falling back to f32 parsing then default 1 if missing. Emitter is defined with fields typ (from ParticleManager.particleTypeHashmap lookup), collides, spawnShape, properties, mode; pub fn init(...) initializes these fields directly, while pub fn initFromZon(...) parses directionMode and SpawnShape from zon, handling errors by logging via std.log.err and falling back to .spread or a point-only shape. Emitter has pub fn spawnParticles(self: Emitter, pos: Vec3d, spawnCount: u32) which caps the count against ParticleSystem.maxCapacity - ParticleSystem.particleCount, then iterates calling self.spawnShape.spawn(pos, self.properties, self.mode), retrieves particleTypeLocal and particleType from ParticleManager.typesLocal.items[self.typ] and ParticleManager.types.items[self.typ], and adds each via ParticleSystem.addParticle with collides flag and properties. The chunk also defines ParticleType (frameCount, startFrame, size) and ParticleTypeLocal (density: RandomRange(f32), rotVel: RandomRange(f32), dragCoefficient: RandomRange(f32), loopTime: ?RandomRange(f32)). Particle is an extern struct with pos array aligned 16 bytes, rot default 0, currentFrame default 1, light default 0, typ u32. ParticleLocal contains velAndRotationVel Vec4f, frameRate f32, density f32, dragCoefficient f32, collides bool.

## Code Example
```zig
pub fn parse(zon: ZonElement) !SpawnCube {
	return SpawnCube{
		.size = zon.get(Vec3f, "size") orelse @splat(zon.get(f32, "size") orelse 1),
	};
}
```

## Related Questions
- How does SpawnCube.spawn compute the particle position offset?
- What fallback direction is used when DirectionMode parsing fails in Emitter.initFromZon?
- Which fields are read from ZonElement in SpawnCube.parse and what defaults apply if missing?
- How is the maximum number of particles capped before spawning in Emitter.spawnParticles?
- Where does ParticleSystem.addParticle get its particle type data from for local vs global variants?
- What extern struct layout does Particle use and which fields have default initial values?
- How are RandomRange types represented in ParticleTypeLocal fields?
- What is the purpose of the typ field stored in Emitter when initFromZon runs?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_4*
