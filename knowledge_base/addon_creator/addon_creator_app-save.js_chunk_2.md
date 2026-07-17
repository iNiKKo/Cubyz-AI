# [hard/addon_creator_app-save.js] - Chunk 2

**Type:** ui
**Keywords:** biome, entity, particle, project data, ZIP export, input fields, validation, texture inclusion, model files
**Symbols:** saveBiomeToProject, saveEntityToProject, saveParticleToProject, exportFullAddon
**Concepts:** data-binding, form validation, file export

## Summary
This chunk handles saving biome, entity, and particle configurations to the project data and exporting the full addon as a ZIP file.

## Explanation
The chunk includes functions for saving biomes, entities, and particles to the project data. Each function retrieves values from input fields, validates them, and updates the corresponding section in `window.projectData`. The `exportFullAddon` function checks if the project is empty, creates a ZIP archive with necessary folders, and writes configuration files based on the project data. It also handles texture and model file inclusion.

## Related Questions
- What is the purpose of the `saveBiomeToProject` function?
- How does the `exportFullAddon` function handle empty projects?
- What validation checks are performed when saving an entity?
- How are textures and models included in the exported ZIP file?
- What happens if a user tries to save a biome without specifying an ID?
- How is the project data updated after saving a particle configuration?
- What is the role of `autoNamespaceBlock` in the biome saving process?
- How does the chunk ensure that only valid IDs are used for entities and particles?
- What steps are taken to prevent duplicate entries when saving configurations?
- How is the sidebar project tree updated after saving a configuration?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_2*
