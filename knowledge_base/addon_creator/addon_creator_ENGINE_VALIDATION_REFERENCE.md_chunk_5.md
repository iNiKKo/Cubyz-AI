# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 5

**Type:** documentation
**Keywords:** entityModel.zig, EntityModel.init, particles.zig, register, EmitterProperties, SpawnShape, DirectionMode, playerModel tag
**Symbols:** EntityModel.init(), particles.zig register()

## Summary
Engine-side default values and error messages for Cubyz entity model and particle fields, read directly from `entityModel.zig: EntityModel.init()` and `particles.zig: register()`/`EmitterProperties`/`SpawnShape`/`DirectionMode`.

## Explanation
**The Zig function that registers a Cubyz particle type is named `register()`, and it is defined in `particles.zig` (as a method on the `ParticleManager` struct there). There is no other, differently-named registration function -- `register()` in `particles.zig` is the complete and only correct answer.**

**Entities**: `.model` defaults to `null`, no error logged. `.height` defaults to `1` (website form defaults to `2.0` -- different). `.coordinateSystem` defaults to `.right_handed_z_up`, matching the website. `.tags` defaults to empty -- **a special `playerModel` tag exists, which registers the entity as a selectable player skin** -- this tag is **not exposed by the website form**. `.defaultTexture` (format `"mod:name"`) defaults to an empty path; split on `:`, texture path resolved as `{assetFolder}/{mod}/entity_models/textures/{name}.png`, falling back to `assets/{mod}/entity_models/textures/{name}.png` if the first doesn't exist -- no error logged here if both are missing, the failure surfaces later when the model actually tries to load.

**Particles**: `.texture` is **required** -- missing logs `"Particle texture id was not specified for {id}"` and the particle type fails to register entirely (hard failure, not a soft fallback). Texture dimensions: base texture height must be an exact multiple of its width (used to slice animation frames) or logs `"Particle base texture has incorrect dimensions ({w}x{h}) expected height to be multiple of width..."`; if an emission texture (`_emission.png`) is present, its frame count must match the base texture's or logs a frame-count-mismatch error. `.rotationVelocity` defaults to `{min:20, max:60}`, matching the website; values are interpreted as degrees and converted to radians internally. `.density` defaults to `{min:2, max:3}`. `.dragCoefficient` defaults to `{min:0.5, max:0.6}`. `.loopTime` has no default and is **not exposed by the website form**. `.speed` defaults to `{min:1, max:1.5}`, parsed separately via `EmitterProperties.parse`. `.lifeTime` defaults to `{min:0.75, max:1}`, same note. `.randomRotate` defaults to `true` (website always writes an explicit value, so this default rarely applies). `.mode` defaults to `spread` if missing; an invalid string logs `"Error while parsing direction mode"` and falls back to `spread`. `.direction` defaults to `{0, 0, 1}`, matching the website. `.shape` defaults to `point` if missing; an invalid string logs `"Error while parsing particle spawn data"` and falls back to a point shape.

Important structural note: `.texture`/`.rotationVelocity`/`.density`/`.dragCoefficient` are validated once, at particle-*type* registration time (**`register()`, defined in `particles.zig`**, called when the addon loads). `.speed`/`.lifeTime`/`.shape`/`.mode`/`.direction` are **emitter** properties, parsed separately (`EmitterProperties.parse`/`SpawnShape.parse`/`DirectionMode.parse`) whenever something actually spawns this particle type -- so a broken emitter-side field won't cause an error at world-load time, it only surfaces when something in the world actually triggers that particle effect.

## Related Questions
- What does a Cubyz entity model's .model/.height/.coordinateSystem field default to if omitted?
- What special tag exists for Cubyz entity models that isn't exposed by the website form, and what does it do?
- What Zig function registers a Cubyz particle type, per the engine validation reference?
- How does the Cubyz engine resolve an entity's default texture file path?
- What happens if a Cubyz particle's .texture field is missing?
- What happens if a Cubyz particle's emission texture frame count doesn't match its base texture's?
- What does a Cubyz particle's .rotationVelocity/.density/.dragCoefficient/.speed/.lifeTime/.randomRotate/.direction field default to?
- What's the structural difference between a Cubyz particle's type-level and emitter-level properties?
- What Zig function registers a Cubyz particle type?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_5*
