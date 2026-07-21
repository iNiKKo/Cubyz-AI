# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 6

**Type:** documentation
**Keywords:** exportFullAddon, Export Full Addon button, zig.zon, zip, app-save.js
**Symbols:** exportFullAddon, window.projectData

## Summary
Cubyz Addon Creator Studio: what "Export Full Addon" does (step 2 of the save/export/import pipeline). This chunk covers EXPORT only -- for the reverse (import) operation, see the sibling import chunk.

## Explanation
Clicking "Export Full Addon" calls **`exportFullAddon()`**, which walks every object in `window.projectData` and writes it out as a `.zig.zon` file (via template-string concatenation) inside a zip, organized into the standard Cubyz addon folder layout (`blocks/`, `items/`, `biomes/`, `entityModels/`, `particles/`, `recipes/`).

## Related Questions
- What does clicking "Export Full Addon" do in the Cubyz Addon Creator?
- What function handles exporting a full addon in the Cubyz Addon Creator, and what does it iterate over?
- What folder layout does an exported Cubyz addon zip use?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_6*
