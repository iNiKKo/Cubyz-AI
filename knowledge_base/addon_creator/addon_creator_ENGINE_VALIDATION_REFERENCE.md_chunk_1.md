# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 1

**Type:** ui
**Keywords:** model properties, particle effects, validation rules, default values, texture dimensions, emitter properties, registration time, parse separately, hard failure, soft fallback
**Symbols:** .model, .height, .coordinateSystem, .tags, .defaultTexture, .texture, .rotationVelocity, .density, .dragCoefficient, .loopTime, .speed, .lifeTime, .randomRotate, .mode, .direction, .shape
**Concepts:** data-binding, form validation, engine defaults, particle registration, texture validation

## Summary
This chunk outlines validation rules and default values for various fields in the Cubyz Addon Creator, focusing on model properties and particle effects.

## Explanation
This chunk outlines validation rules and default values for various fields in the Cubyz Addon Creator, focusing on model properties and particle effects. For models, it specifies that `.model` defaults to `null`, `.height` defaults to `1` (with a website form default of `2.0`), `.coordinateSystem` defaults to `.right_handed_z_up`, and `.tags` are empty by default but can include a special `playerModel` tag which is not exposed in the website form. The `.defaultTexture` field has no default value but logs no error if both specified paths are missing, resolving to `{assetFolder}/{mod}/entity_models/textures/{name}.png` or falling back to `assets/{mod}/entity_models/textures/{name}.png`. For particles, it specifies that the `.texture` field is required and must have a texture with dimensions where height is an exact multiple of width. The frame count for emission textures must match the base texture's frame count. Default values for particle properties include `.rotationVelocity` set to `{20, 60}` (interpreted as degrees internally), `.density` set to `{2, 3}`, and `.dragCoefficient` set to `{0.5, 0.6}`. The `.speed`, `.lifeTime`, `.shape`, `.mode`, and `.direction` fields are parsed separately when the particle effect is triggered, with specific fallback behaviors for invalid values like `spread` for missing or invalid `.mode`. Additionally, `.loopTime` is not exposed by the website form.

## Related Questions
- What is the default value for .height in the Cubyz Addon Creator?
- How does the engine handle missing .texture fields for particles?
- What happens if the base texture dimensions are incorrect for particles?
- Are there any specific defaults for particle properties like .rotationVelocity?
- How are emitter properties validated compared to particle type registration?
- What is the fallback behavior for invalid .mode values in particle effects?
- How does the engine resolve paths for .defaultTexture if both specified paths are missing?
- Are there any specific validation rules for .direction and .shape fields?
- What happens if a required field like .texture is not provided during registration?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_1*
