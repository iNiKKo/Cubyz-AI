# [hard/codebase_src_particles.zig] - Chunk 4

**Type:** implementation
**Keywords:** struct, union, enum, method, initialization, spawning, configuration parsing
**Symbols:** Emitter, Emitter.typ, Emitter.collides, Emitter.spawnShape, Emitter.properties, Emitter.mode, Emitter.SpawnShape, Emitter.SpawnShape.point, Emitter.SpawnShape.sphere, Emitter.SpawnShape.cube, Emitter.SpawnShape.spawn, Emitter.SpawnShape.parse, Emitter.SpawnPoint, Emitter.SpawnPoint.spawn, Emitter.SpawnPoint.parse, Emitter.SpawnSphere, Emitter.SpawnSphere.radius, Emitter.SpawnSphere.spawn, Emitter.SpawnSphere.parse, Emitter.SpawnCube, Emitter.SpawnCube.size, Emitter.SpawnCube.spawn, Emitter.SpawnCube.parse, Emitter.init, Emitter.initFromZon, Emitter.spawnParticles, ParticleType, ParticleType.frameCount, ParticleType.startFrame, ParticleType.size
**Concepts:** particle system, emitter configuration, spawn shapes, direction modes, collision handling

## Summary
Defines the Emitter and related structures for particle system management.

## Explanation
The code defines an `Emitter` struct that manages particle spawning properties, including shape, speed, direction mode, and collision settings. It includes nested structs like `SpawnPoint`, `SpawnSphere`, and `SpawnCube` to handle different spawn shapes. Each spawn type has a `spawn` method to calculate particle position and velocity based on the emitter's properties and mode. The `Emitter` struct also provides methods for initialization from configuration (`initFromZon`) and for spawning particles (`spawnParticles`). Additionally, it defines a `ParticleType` struct to manage particle visual and behavior properties.

## Code Example
```zig
pub fn spawn(_: SpawnPoint, pos: Vec3d, properties: EmitterProperties, mode: DirectionMode) struct { Vec3d, Vec3f } {
	const particlePos = pos;
	const speed: Vec3f = @splat(properties.speed.get(&main.seed));
	const dir: Vec3f = switch (mode) {
		.direction => |dir| vec.normalize(dir),
		.scatter, .spread => vec.normalize(random.nextFloatVectorSigned(3, &main.seed)),
	};
	const particleVel = dir*speed;

	return .{particlePos, particleVel};
}
```

## Related Questions
- What is the purpose of the `Emitter` struct?
- How does the `spawnParticles` method work?
- What are the different spawn shapes defined in the code?
- How is an `Emitter` initialized from a ZonElement?
- What properties does the `ParticleType` struct manage?
- How do errors during parsing of direction mode and spawn data get handled?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_4*
