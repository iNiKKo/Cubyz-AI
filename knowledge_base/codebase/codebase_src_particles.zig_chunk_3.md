# [hard/codebase_src_particles.zig] - Chunk 3

**Type:** serialization
**Keywords:** ZonElement, enum union, randomization, configuration parsing, error handling
**Symbols:** EmitterProperties, EmitterProperties.speed, EmitterProperties.lifeTime, EmitterProperties.randomizeRotation, EmitterProperties.parse, DirectionMode, DirectionMode.spread, DirectionMode.scatter, DirectionMode.direction, DirectionMode.parse
**Concepts:** particle system configuration, data parsing from configuration files

## Summary
Defines particle emitter properties and direction modes with parsing logic from Zon elements.

## Explanation
The chunk defines two main structures: `EmitterProperties` and `DirectionMode`. `EmitterProperties` includes fields for speed, lifetime, and rotation randomization, each parsed from a Zon element. The `parse` method in `EmitterProperties` initializes these fields using data from the Zon element or default values if parsing fails. `DirectionMode` is an enum union with three variants: spread, scatter, and direction. Each variant has its own parsing logic in the `parse` method, which determines the mode based on a string tag and initializes the appropriate variant's value.

## Code Example
```zig
pub fn parse(zon: ZonElement) EmitterProperties {
	return EmitterProperties{
		.speed = RandomRange(f32).fromZon(zon.getChild("speed")) orelse .init(1, 1.5),
		.lifeTime = RandomRange(f32).fromZon(zon.getChild("lifeTime")) orelse .init(0.75, 1),
		.randomizeRotation = zon.get(bool, "randomRotate") orelse true,
	};
}
```

## Related Questions
- How are the `EmitterProperties` fields parsed from a Zon element?
- What is the default value for `speed` if parsing fails in `EmitterProperties.parse`?
- Which variants does the `DirectionMode` enum union have?
- How is the direction mode determined and initialized in `DirectionMode.parse`?
- What error can be returned by `DirectionMode.parse` if an invalid mode is specified?
- What is the purpose of the `randomizeRotation` field in `EmitterProperties`?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_3*
