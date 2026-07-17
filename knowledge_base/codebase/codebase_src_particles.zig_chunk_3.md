# [hard/codebase_src_particles.zig] - Chunk 3

**Type:** configuration
**Keywords:** RandomRange, parse, spawn, Vec3d, Vec3f, main.seed, normalize, stringToEnum, orelse
**Symbols:** EmitterProperties, DirectionMode, SpawnShape, SpawnPoint, SpawnSphere, SpawnCube
**Concepts:** particle emitter configuration, ZON file parsing, random seeded generation, union enum dispatch

## Summary
Defines the particle emitter data structures (EmitterProperties, DirectionMode, SpawnShape/SpawnPoint/SpawnSphere/SpawnCube) and their parse functions for loading from ZON files.

## Explanation
This chunk declares several public constants defining the structure of particle emitters. EmitterProperties contains speed and lifeTime as RandomRange values plus a randomizeRotation boolean, with a parse function that reads these fields from a ZonElement using orelse defaults. DirectionMode is a union enum with spread, scatter, and direction variants; its parse function reads a 'mode' string field and converts it via std.meta.stringToEnum, returning an error.InvalidDirectionMode on unknown values. SpawnShape is a union enum containing point, sphere, and cube variants, each with their own nested struct definitions (SpawnPoint, SpawnSphere, SpawnCube). Each spawn variant implements a spawn method that takes position, properties, and mode to return a {Vec3d, Vec3f} tuple of particle position and velocity. The spawn implementations use random.nextFloatVectorSigned seeded by main.seed for scatter/spread modes, normalize direction vectors where needed, and compute velocities by multiplying speed with the normalized or generated direction. Each spawn variant also has a parse method that reads its specific fields from ZonElement (point is empty, sphere reads radius, cube reads size as Vec3f with fallback to scalar size). The chunk does not define Emitter itself here; it only declares the nested types and their parsing logic.

## Related Questions
- What are the default values used when a ZON field is missing for EmitterProperties?
- How does DirectionMode parse handle an unknown mode string value?
- Which spawn shape variant has no fields to read from ZON?
- How is the random seed accessed in the spawn implementations?
- What type does the spawn method return for all SpawnShape variants?
- Are any of the spawn methods marked pub const or pub fn?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_3*
