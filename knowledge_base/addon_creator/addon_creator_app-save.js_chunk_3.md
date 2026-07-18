# [hard/addon_creator_app-save.js] - Chunk 3

**Type:** ui
**Keywords:** save, particle, project, configuration, validation, input, state, alert, update, sidebar
**Symbols:** saveParticleToProject, particleId, particleSpawnShape, particleDirectionMode, particleTextureSearch, particleHasEmission, particleSpeedMin, particleSpeedMax, particleLifeMin, particleLifeMax, particleDensityMin, particleDensityMax, particleRotVelMin, particleRotVelMax, particleDragMin, particleDragMax, particleRandomRotate, particleCollides, particleShapeRadius, particleShapeSize, particleDirX, particleDirY, particleDirZ
**Concepts:** data-binding, form validation, conditional logic

## Summary
Handles the saving of a particle configuration to the project data.

## Explanation
The function `saveParticleToProject` is responsible for extracting values from various UI input elements, validating them, and then updating the project's particle data. It ensures that the Particle ID is specified, trims and sanitizes it, and checks if the required fields are filled. The function also handles conditional logic based on the selected shape and direction mode to include additional parameters accordingly. After saving, it updates the global state to reflect changes and alerts the user of successful operation.

## Related Questions
- What is the purpose of the `saveParticleToProject` function?
- How does the function validate the Particle ID before saving?
- What additional parameters are included based on the selected shape and direction mode?
- How does the function handle unsaved changes in the global state?
- What UI elements does the function interact with to gather particle configuration data?
- How is the project's particle data updated after saving a new particle?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_3*
