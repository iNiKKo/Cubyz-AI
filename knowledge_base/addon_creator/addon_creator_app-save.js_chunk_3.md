# [hard/addon_creator_app-save.js] - Chunk 3

**Type:** ui
**Keywords:** save, particle, project, configuration, validation, input, state, alert, update, sidebar
**Symbols:** saveParticleToProject, particleId, particleSpawnShape, particleDirectionMode, particleTextureSearch, particleHasEmission, particleSpeedMin, particleSpeedMax, particleLifeMin, particleLifeMax, particleDensityMin, particleDensityMax, particleRotVelMin, particleRotVelMax, particleDragMin, particleDragMax, particleRandomRotate, particleCollides, particleShapeRadius, particleShapeSize, particleDirX, particleDirY, particleDirZ
**Concepts:** data-binding, form validation, conditional logic

## Summary
Handles the saving of a particle configuration to the project data.

## Explanation
The function `saveParticleToProject` is responsible for extracting values from various UI input elements, validating them, and then updating the project's particle data. It ensures that the Particle ID is specified, trims and sanitizes it, and checks if the required fields are filled. The function also handles conditional logic based on the selected shape and direction mode to include additional parameters accordingly. After saving, it updates the global state to reflect changes and alerts the user of successful operation.

**Specific Details:**
- **Particle ID (`particleId`)**: Must be specified; trimmed, sanitized, and converted to lowercase. If not provided, an alert is shown.
- **Shape (`particleSpawnShape`)**: Determines additional parameters like `shapeRadius` for 'sphere' or `shapeSize` for 'cube'.
- **Direction Mode (`particleDirectionMode`)**: Determines additional direction parameters like `dirX`, `dirY`, and `dirZ` if set to 'direction'.
- **Texture (`particleTextureSearch`)**: Texture path; trimmed.
- **Emission (`particleHasEmission`)**: Boolean indicating emission status.
- **Speed (`particleSpeedMin`, `particleSpeedMax`)**: Minimum and maximum speed values with default 1.0 and 1.5 respectively if not provided.
- **Life (`particleLifeMin`, `particleLifeMax`)**: Minimum and maximum life values with default 0.75 and 1.0 respectively if not provided.
- **Density (`particleDensityMin`, `particleDensityMax`)**: Minimum and maximum density values with default 2.0 and 3.0 respectively if not provided.
- **Rotation Velocity (`particleRotVelMin`, `particleRotVelMax`)**: Minimum and maximum rotation velocity values with default 20.0 and 60.0 respectively if not provided.
- **Drag (`particleDragMin`, `particleDragMax`)**: Minimum and maximum drag values with default 0.5 and 0.6 respectively if not provided.
- **Random Rotate (`particleRandomRotate`)**: Boolean indicating random rotation status.
- **Collides (`particleCollides`)**: Boolean indicating collision status.

## Related Questions
- What is the purpose of the `saveParticleToProject` function?
- How does the function validate the Particle ID before saving?
- What additional parameters are included based on the selected shape and direction mode?
- How does the function handle unsaved changes in the global state?
- What UI elements does the function interact with to gather particle configuration data?
- How is the project's particle data updated after saving a new particle?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_3*
