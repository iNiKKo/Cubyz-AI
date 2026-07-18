# [easy/addon_creator_particles.html] - Chunk 0

**Type:** ui
**Keywords:** Particle ID, Texture Search, Emission Texture, Spawn Speed, Lifetime, Density, Rotation Speed, Drag, Random Rotation, Collides with World, Spawn Shape, Direction Mode, Direction Vector
**Symbols:** particleId, particleTextureSearch, thumb_particleTextureSearch, particleTextureDropdown, particleHasEmission, emissionWarning, particleSpeedMin, particleSpeedMax, particleLifeMin, particleLifeMax, particleDensityMin, particleDensityMax, particleRotVelMin, particleRotVelMax, particleRandomRotate, particleCollides, particleSpawnShape, particleSpawnShapeSearch, particleSpawnShapeDropdown, shapeParamWrapper, particleDirectionMode, particleDirectionModeSearch, particleDirectionModeDropdown, directionVectorWrapper, particleDirX, particleDirY, particleDirZ
**Concepts:** data-binding, form validation, dropdown management, file handling, conditional display, configuration generation

## Summary
The Particle Creator UI allows users to configure particle properties such as ID, texture, emission settings, and various physical attributes like speed, lifetime, and rotation.

## Explanation
This HTML snippet defines a user interface for creating particles in the Cubyz Addon Studio. The UI includes several form groups for different particle properties:

1. **Particle ID**: An input field where users can enter a unique identifier for the particle, with validation to ensure lowercase letters and numbers only.
2. **Particle Texture**: A dropdown with search functionality that allows users to select a texture for the particle. It also includes an option to upload a custom PNG file.
3. **Emission Texture**: A checkbox to enable emission textures, which are used for lighting effects.
4. **Particle Settings (Min / Max)**: Multiple input fields for configuring various attributes like spawn speed, lifetime, density, rotation speed, and drag. Each attribute has both minimum and maximum values that can be set.
5. **Spawn Shape & Direction**: Dropdowns to select the shape and direction of particle emission. Depending on the selected options, additional fields may appear to specify parameters for these shapes or directions.

The UI also includes a 'Save Particle to Project' button that triggers a function to save the configured particle settings to the project.

**Event Handlers**: The UI uses inline event handlers for input validation, dropdown management, and file handling. For example, `oninput` is used to sanitize the particle ID input, and `onfocus` and `onmousedown` are used to manage dropdown visibility and selection.

**Data Binding**: While not explicitly shown in this snippet, the UI likely uses JavaScript to bind these inputs to a data model that represents the particle configuration. This allows for real-time updates and validation of the particle settings.

**Validation**: The particle ID input includes basic validation to ensure it only contains lowercase letters, numbers, and underscores. There is also conditional display logic for certain fields based on user selections (e.g., emission warning, additional shape parameters).

**Templates**: The dropdown options are hardcoded in the HTML, but the UI could potentially use templates or JavaScript to dynamically generate these options based on available textures or shapes.

**Bindings and Engine Mappings**: The UI controls are directly mapped to specific particle attributes. For example, `particleSpeedMin` and `particleSpeedMax` correspond to the minimum and maximum spawn speed of the particle.

**Configuration Generation**: When the 'Save Particle to Project' button is clicked, the UI likely generates a configuration object based on the current state of the input fields and sends it to the engine for processing.

## Related Questions
- How does the UI handle input validation for the Particle ID?
- What JavaScript functions are triggered when a user selects a texture from the dropdown?
- How is the emission warning displayed or hidden based on user interaction?
- Can users add custom textures to particles, and if so, how is this handled?
- What happens when the 'Save Particle to Project' button is clicked?
- How does the UI manage conditional display of additional fields for spawn shapes and directions?
- Is there any data binding between the UI inputs and a JavaScript object representing the particle configuration?

*Source: unknown | chunk_id: addon_creator_particles.html_chunk_0*
