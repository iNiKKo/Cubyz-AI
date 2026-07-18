# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 1

**Type:** ui
**Keywords:** model properties, particle effects, validation rules, default values, texture dimensions, emitter properties, registration time, parse separately, hard failure, soft fallback
**Symbols:** .model, .height, .coordinateSystem, .tags, .defaultTexture, .texture, .rotationVelocity, .density, .dragCoefficient, .loopTime, .speed, .lifeTime, .randomRotate, .mode, .direction, .shape
**Concepts:** data-binding, form validation, engine defaults, particle registration, texture validation

## Summary
This chunk outlines validation rules and default values for various fields in the Cubyz Addon Creator, focusing on model properties and particle effects.

## Explanation
The chunk provides detailed validation rules and default values for different fields used in the Cubyz Addon Creator. It includes specific constraints for fields like `.model`, `.height`, `.coordinateSystem`, and `.tags`. For particles, it specifies required fields such as `.texture` and validates dimensions and frame counts of textures. The chunk also notes that certain fields are validated at registration time while others are parsed separately when the particle effect is triggered.

## Related Questions
- What is the default value for `.height` in the Cubyz Addon Creator?
- How does the engine handle missing `.texture` fields for particles?
- What happens if the base texture dimensions are incorrect for particles?
- Are there any specific defaults for particle properties like `.rotationVelocity`?
- How are emitter properties validated compared to particle type registration?
- What is the fallback behavior for invalid `.mode` values in particle effects?
- How does the engine resolve paths for `.defaultTexture` if both specified paths are missing?
- Are there any specific validation rules for `.direction` and `.shape` fields?
- What happens if a required field like `.texture` is not provided during registration?
- How does the Cubyz Addon Creator handle errors in particle texture frame counts?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_1*
