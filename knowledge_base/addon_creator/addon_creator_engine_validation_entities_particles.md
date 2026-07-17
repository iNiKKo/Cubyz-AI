# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk entities_particles

**Type:** reference
**Keywords:** height, coordinateSystem, right_handed_z_up, texture, rotationVelocity, degrees, radians, particle-defaults, entity-defaults
**Symbols:** entityModel.zig, EntityModel.init, particles.zig, register, EmitterProperties, SpawnShape, DirectionMode
**Concepts:** engine-default-values, validation-errors, silent-fallback

## Summary
Exact engine-side default values and error messages for Cubyz entity model and particle fields,
read directly from `entityModel.zig: EntityModel.init()` and
`particles.zig: register()`/`EmitterProperties`/`SpawnShape`/`DirectionMode`.

## Explanation
**Entities** (`entityModel.zig: EntityModel.init()`):
- `.model`: `null` if missing, no error logged
- `.height`: `1` if missing (the website's own form defaults to `2.0` instead -- different, this only diverges for hand-written files since the website always writes a value)
- `.coordinateSystem`: `.right_handed_z_up` if missing (matches the website's own default)
- `.tags`: empty list -- a special `playerModel` tag exists (registers the entity as a selectable player skin), not exposed by the website form
- `.defaultTexture`: empty path if missing; format is `"mod:name"`, split on `:`, texture path resolved as `{assetFolder}/{mod}/entity_models/textures/{name}.png`, falling back to `assets/{mod}/entity_models/textures/{name}.png`. No error logged if both are missing -- the failure only surfaces later when the model actually tries to load.

**Particles** (`particles.zig: register()` + `EmitterProperties`/`SpawnShape`/`DirectionMode`):
- `.texture`: REQUIRED, no default. Missing logs `"Particle texture id was not specified for {id}"` and the particle type fails to register entirely -- a hard failure, not a soft fallback, unlike every other particle field.
- Texture dimensions: the base texture's height must be an exact multiple of its width (used to slice animation frames), or the engine logs
  `"Particle base texture has incorrect dimensions ({w}x{h}) expected height to be multiple of width..."`.
  If an emission texture (`_emission.png`) is present, its frame count must match the base texture's or the engine logs a frame-count-mismatch error.
- `.rotationVelocity` (`{min, max}`): default `{20, 60}` if missing (matches website). Values are interpreted as DEGREES on the website/in the file, and the engine converts them to radians internally after loading -- the stored file value itself still matches what you typed in degrees.
- `.density` (`{min, max}`): default `{2, 3}` (matches website)
- `.dragCoefficient` (`{min, max}`): default `{0.5, 0.6}` (matches website)
- `.loopTime` (`{min, max}`): no default -- not exposed by the website form
- `.speed` (`{min, max}`): default `{1, 1.5}` (matches website); parsed separately via `EmitterProperties.parse`, not in `register()`
- `.lifeTime` (`{min, max}`): default `{0.75, 1}` (matches website); same note
- `.randomRotate`: default `true`, though the website always writes an explicit value so this default rarely applies in practice
- `.mode` (`spread`/`scatter`/`direction`): default `spread` if missing; an invalid string logs `"Error while parsing direction mode"` and falls back to `spread`
- `.direction` (Vec3f): default `{0, 0, 1}` (matches website's dirZ=1.0 default)
- `.shape` (`point`/`sphere`/`cube`): default `point` if missing; an invalid string logs `"Error while parsing particle spawn data"` and falls back to a point shape

Structural note: `.texture`/`.rotationVelocity`/`.density`/`.dragCoefficient` are validated once,
at particle-type registration time (`register()`, called when the addon loads).
`.speed`/`.lifeTime`/`.shape`/`.mode`/`.direction` are emitter properties, parsed separately
whenever something actually spawns this particle type -- so a broken emitter-side field won't
cause an error at world-load time, only when something in the world actually triggers that
particle effect.

## Related Questions
- What does a Cubyz entity model's .height field default to if omitted, and how does that differ from the website?
- What coordinate system does a Cubyz entity model default to?
- What happens if a Cubyz particle definition is missing its .texture field?
- What's the dimension requirement for a Cubyz particle's base texture?
- What unit are particle rotation velocity fields in on the Addon Creator website versus internally in the engine?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_entities_particles*
