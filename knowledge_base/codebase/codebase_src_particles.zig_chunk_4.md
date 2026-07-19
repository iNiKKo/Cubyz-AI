# [hard/codebase_src_particles.zig] - Chunk 4

**Type:** implementation
**Keywords:** struct, union, enum, method, initialization, spawning, configuration parsing
**Symbols:** Emitter, Emitter.typ, Emitter.collides, Emitter.spawnShape, Emitter.properties, Emitter.mode, Emitter.SpawnShape, Emitter.SpawnShape.point, Emitter.SpawnShape.sphere, Emitter.SpawnShape.cube, Emitter.SpawnShape.spawn, Emitter.SpawnShape.parse, Emitter.SpawnPoint, Emitter.SpawnPoint.spawn, Emitter.SpawnPoint.parse, Emitter.SpawnSphere, Emitter.SpawnSphere.radius, Emitter.SpawnSphere.spawn, Emitter.SpawnSphere.parse, Emitter.SpawnCube, Emitter.SpawnCube.size, Emitter.SpawnCube.spawn, Emitter.SpawnCube.parse, Emitter.init, Emitter.initFromZon, Emitter.spawnParticles, ParticleType, ParticleType.frameCount, ParticleType.startFrame, ParticleType.size
**Concepts:** particle system, emitter configuration, spawn shapes, direction modes, collision handling

## Summary
Defines the Emitter and related structures for particle system management.

## Explanation
The code defines an `Emitter` struct that manages particle spawning properties, including shape, speed, direction mode, and collision settings. It includes nested structs like `SpawnPoint`, `SpawnSphere`, and `SpawnCube` to handle different spawn shapes. Each spawn type has a `spawn` method to calculate particle position and velocity based on the emitter's properties and mode.

- **SpawnPoint**: The `spawn` method for `SpawnPoint` calculates the particle position as the same as the emitter's position (`pos`) and generates a random direction vector (`dir`). The speed is determined by the emitter's properties, and the particle velocity (`particleVel`) is calculated by multiplying the direction vector by the speed.

- **SpawnSphere**: The `spawn` method for `SpawnSphere` calculates the particle position within a sphere defined by the radius. It generates a random offset vector (`offsetPos`) within a unit sphere and scales it by the radius to get the final particle position. The speed is determined by the emitter's properties, and the direction vector (`dir`) is calculated based on the mode (direction, scatter, spread).

- **SpawnCube**: The `spawn` method for `SpawnCube` calculates the particle position within a cube defined by the size. It generates a random offset vector (`offsetPos`) within a unit cube and scales it by the size to get the final particle position. The speed is determined by the emitter's properties, and the direction vector (`dir`) is calculated based on the mode (direction, scatter, spread).

The `Emitter` struct also provides methods for initialization from configuration (`initFromZon`) and for spawning particles (`spawnParticles`). Additionally, it defines a `ParticleType` struct to manage particle visual and behavior properties.

Error handling during parsing of direction mode and spawn data is managed by logging an error message and providing default values. For example, if the direction mode cannot be parsed, it defaults to `.spread`. If the spawn shape cannot be parsed, it defaults to a `SpawnPoint`.

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
