# [easy/addon_creator_FIELD_REFERENCE.md] - Chunk 0

**Type:** documentation
**Keywords:** app-save.js, app-io.js, projectData, saveXToProject, pipeline overview
**Symbols:** window.projectData, saveXToProject

## Summary
Overview of the Cubyz Addon Creator Studio's save/export/import pipeline, and the first step: saving a form to the project.

## Explanation
This document maps every Addon Creator Studio form field to its internal `projectData` property and its exact serialized `.zig.zon` output, compiled by reading `app-save.js` (the save/export logic) in full, cross-checked against `app-io.js`'s import logic. The pipeline has three steps, covered individually in sibling chunks: saving a form to the project (this chunk), exporting the full addon (see the dedicated export chunk), and importing an existing addon (see the dedicated import chunk).

**Step 1 -- Save to Project:** the user fills in a form (`blocks.html`, `items.html`, etc.); clicking "Save to Project" calls the matching `saveXToProject()` function in `app-save.js`, which reads the DOM fields by ID and pushes a plain object into `window.projectData.X`.

## Related Questions
- What function does the Cubyz Addon Creator call when "Save to Project" is clicked?
- Where does the Cubyz Addon Creator store form data after "Save to Project" is clicked?
- What are the three steps of the Cubyz Addon Creator's save/export/import pipeline?

*Source: unknown | chunk_id: addon_creator_FIELD_REFERENCE.md_chunk_0*
