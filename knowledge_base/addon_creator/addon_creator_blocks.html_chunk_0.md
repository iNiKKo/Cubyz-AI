# [medium/addon_creator_blocks.html] - Chunk 0

**Type:** ui
**Keywords:** block-id, render-mode, collision, light-emission, tags, replaceable, degradable, view-through, backfaces, ore-veins, friction, bounciness, density, terminal-velocity, mobility
**Symbols:** blockPresetSelectorSearch, blockPresetDropdown, loadBlockPreset, blockId, blockHealth, blockResistance, blockRotation, blockRotationSearch, blockRotationDropdown, handleRotationChange, blockCollide, blockTransparent, emittedLightColor, absorbedLightColor, blockTagsContainer, tagTextInput, addDynamicTagPill, blockReplaceable, blockDegradable, blockViewThrough, blockAlwaysViewThrough, blockHasBackFace, blockAllowOres, blockFriction, blockBounciness, blockDensity, blockTerminalVelocity, blockMobility, simpleTouchPreset, simpleTouchPresetSearch, simpleTouchDropdown, handleSimpleTouchChange
**Concepts:** data-binding, form-validation, live-preview, preset-loading, dropdown-selection, tag-management, engine-mapping, physics-configuration, touch-interaction

## Summary
The Block Creator panel provides UI controls for defining block properties including preset loading, ID naming, health/resistance values, render modes, collision/visibility flags, light emission, tags, engine physics parameters (replaceable, degradability, view-through, backfaces, ore allowance), and touch interaction presets.

## Explanation
UI Controls: Text inputs for blockId (with sanitization on input), blockHealth (number), blockResistance (number with step 0.1), emittedLightColor/absorbedLightColor (color pickers), checkboxes for blockCollide, blockTransparent, blockReplaceable, blockDegradable, blockViewThrough, blockAlwaysViewThrough, blockHasBackFace, blockAllowOres, and dropdowns for render modes (blockRotation) and touch presets (simpleTouchPreset). Event Handlers: oninput sanitizes blockId to lowercase alphanumeric; onfocus triggers dropdown visibility; onmousedown on dropdown options sets hidden input values and calls window.loadBlockPreset or window.handleRotationChange or window.handleSimpleTouchChange. Validation: blockId uses placeholder 'ruby_ore' and regex replacement /[^a-z0-9_]/g to strip invalid chars; health/resistance have default values (1/0); render mode dropdowns include descriptive labels like '3D Block (cubyz:stairs)'. Defaults: emittedLightColor defaults #000000, absorbedLightColor #ffffff; blockCollide checked by default. Templates: Dropdown options are inline HTML with padding/cursor-pointer styling; tag container supports dynamic pill addition via window.addDynamicTagPill. Engine Mappings: hidden inputs store engine-specific identifiers (e.g., 'cubyz:stairs', 'cubyz:ore') while visible text shows user-friendly names. Configuration Generation: The UI likely feeds a JSON-like config object built from these fields, passed to the Cubyz addon generation pipeline.

## Related Questions
- What happens when a user clicks on one of the preset dropdown options for block rotation?
- How is the blockId input sanitized and what characters are allowed?
- Which hidden input stores the engine-specific render mode identifier after selection?
- What default values are assigned to emittedLightColor and absorbedLightColor fields?
- Describe the purpose of the addDynamicTagPill function in relation to blockTagsContainer.
- How does the UI handle user interaction with the simpleTouchPreset dropdown?
- Which checkbox controls whether ores can be spawned inside this block type?
- What is the step attribute for blockResistance and why might it be set that way?
- Explain how the blockRotation hidden input value relates to the visible search text.
- Are any of the physics parameters (friction, bounciness) constrained by min/max attributes?
- How does the UI indicate which engine preset is currently loaded for a given block type?
- What event triggers the display of the blockPresetDropdown element?

*Source: unknown | chunk_id: addon_creator_blocks.html_chunk_0*
