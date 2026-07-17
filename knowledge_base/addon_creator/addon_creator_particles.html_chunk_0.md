# [easy/addon_creator_particles.html] - Chunk 0

**Type:** ui
**Keywords:** Particle Creator, ID, Texture, Emission, Settings, Min/Max, Spawn Shape, Direction, Save, Validation, Dropdown, File Upload, Conditional Fields
**Symbols:** particleId, particleTextureSearch, thumb_particleTextureSearch, particleTextureDropdown, particleHasEmission, emissionWarning, particleSpeedMin, particleSpeedMax, particleLifeMin, particleLifeMax, particleDensityMin, particleDensityMax, particleRotVelMin, particleRotVelMax, particleRandomRotate, particleCollides, particleSpawnShape, particleSpawnShapeSearch, particleSpawnShapeDropdown, shapeParamWrapper, particleDirectionMode, particleDirectionModeSearch, particleDirectionModeDropdown, directionVectorWrapper, particleDirX, particleDirY, particleDirZ
**Concepts:** data-binding, form validation, dropdown selection, file upload, conditional rendering

## Summary
The Particle Creator UI allows users to define particle properties such as ID, texture, emission settings, and various physical attributes like speed, lifetime, and rotation.

## Explanation
This HTML snippet defines a user interface for creating particles in the Cubyz Addon Studio. The UI includes several form groups for different particle properties:

1. **Particle ID**: A text input for specifying the particle's unique identifier (filename), with validation to ensure lowercase alphanumeric characters and underscores.
2. **Particle Texture**: An input field with a dropdown for selecting textures, including an option to upload custom PNG files. The UI also displays a thumbnail preview of the selected texture.
3. **Emission Texture**: A checkbox to enable emission texture support, accompanied by a warning message when enabled.
4. **Particle Settings (Min / Max)**: Multiple input fields for defining particle attributes such as spawn speed, lifetime, density, rotation speed, and drag, with min/max values.
5. **Spawn Shape & Direction**: Dropdowns for selecting the shape and direction of particle spawning, along with additional fields that appear based on the selected options (e.g., direction vector for fixed direction).

The UI also includes a 'Save Particle to Project' button to finalize the particle configuration and add it to the project.

Event handlers are attached to various inputs and dropdowns to manage user interactions, such as filtering texture options, toggling additional fields based on selections, and handling custom file uploads.

## Related Questions
- What is the purpose of the 'particleId' input field?
- How does the UI handle custom texture uploads for particles?
- What validation is applied to the 'particleId' input?
- How are additional fields conditionally rendered based on user selections?
- What event handlers are attached to the dropdowns for spawn shape and direction?
- How does the UI manage the display of emission warnings?
- What is the role of the 'Save Particle to Project' button in the UI?
- How are min/max values handled for particle attributes like speed and lifetime?
- What CSS classes are used for styling the dropdown options?
- How does the UI ensure that only valid characters are entered for the particle ID?

*Source: unknown | chunk_id: addon_creator_particles.html_chunk_0*
