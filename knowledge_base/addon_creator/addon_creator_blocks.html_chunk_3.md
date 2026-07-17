# [medium/addon_creator_blocks.html] - Chunk 3

**Type:** ui
**Keywords:** texture, slot, upload, png, dropdown, filter, layout, map, cube, face, grid, view
**Symbols:** tex14, tex15, tex14Dropdown, tex15Dropdown, view_up, view_left, view_front, view_right, view_bottom, view_back, window.handleCustomTexture, showDropdown, filterDropdown
**Concepts:** texture-slot-inputs, dropdown-filtering, file-upload-binding, face-layout-map, grid-positioning

## Summary
This HTML chunk defines the texture input controls for slots 14 and 15, including dropdowns and file upload buttons, followed by a visual layout map of the six cube faces with image placeholders.

## Explanation
The UI contains two form groups (Texture Slot 14 and Texture Slot 15). Each group has: <label> text, an <input type="text"> bound to id 'tex14'/'tex15', a hidden dropdown div ('tex14Dropdown'/'tex15Dropdown'), and a file-input-label wrapping a hidden <input type="file" accept=".png"> that triggers window.handleCustomTexture(this, 'tex14') on change. The inputs have onfocus='showDropdown(...)' and oninput='filterDropdown(...)'. Below the slots is a styled div titled 'Texture Layout Map' containing a CSS grid (block-layout-cross-grid) with 3 columns x 4 rows; only specific cells contain layout-face-box elements, each holding an <img> (id view_up, view_left, etc.) and a .face-lbl span. The face images are hidden by default via CSS.

## Related Questions
- What happens when a user focuses the text input for Texture Slot 14?
- How is the custom texture file handler invoked for slot 15?
- Which CSS class controls the visibility of the face images in the layout map?
- Are all six cube faces represented in the layout map, or only some?
- What placeholder text is used for the texture input fields?
- Does the dropdown appear immediately on focus, or after typing?
- Is there any validation logic attached to these inputs besides filtering?
- How are the face labels (e.g., 'Top', 'Left') rendered in the layout map?
- Can a user add multiple PNG files for a single texture slot via this UI?
- What is the purpose of the block-layout-cross-grid CSS rule?

*Source: unknown | chunk_id: addon_creator_blocks.html_chunk_3*
