# [medium/addon_creator_blocks.html] - Chunk 2

**Type:** ui
**Keywords:** texture slots, custom textures, PNG upload, top view, left view, front view, right view, bottom view, back view
**Symbols:** div, input, label, img, span
**Concepts:** Texture Configuration, File Upload, Dropdown Menu, Grid Layout, 3D Model Textures

## Summary
The provided HTML snippet is a user interface for configuring texture slots and viewing a layout map of textures. It includes input fields for selecting textures, file upload options for adding custom PNGs, and a grid displaying different views (top, left, front, right, bottom, back) with associated images.

## Explanation
This HTML code represents a section of a web application designed to manage texture configurations for 3D models or similar applications. The interface is structured into two main parts: the texture configuration area and the texture layout map.

1. **Texture Configuration Area**:
   - This section contains multiple input fields, each labeled with 'Texture Slot' followed by a number (6 to 15). These slots are used for selecting textures.
   - Each input field has an associated dropdown menu (`div` with class `dropdown-options`) that appears when the user focuses on the input or types in it. This dropdown is populated dynamically based on the user's input, allowing them to select from a list of available textures.
   - Next to each input field, there's a label styled as a button ('+ Add PNG') which, when clicked, allows users to upload custom PNG files for their texture slots. The file input is hidden and triggered by clicking on the label.

2. **Texture Layout Map**:
   - This section provides a visual representation of how the textures are laid out across different faces of an object (top, left, front, right, bottom, back).
   - It consists of a grid (`div` with class `block-layout-cross-grid`) where each face is represented by a box (`div` with class `layout-face-box`). Each box contains an image element (`img`) and a label (`span` with class `face-lbl`) indicating the corresponding face.

The overall design emphasizes usability and visual clarity, using consistent styling for input fields, dropdowns, and labels. The use of grid layouts ensures that the interface is organized and easy to navigate, making it suitable for applications where precise texture management is required.

## Code Example
```zig
<div class="form-group texture-select-wrapper" style="margin-bottom:0;">
    <label style="font-size:11px; color:#888;">Texture Slot 6</label>
    <input type="text" id="tex6" placeholder="" autocomplete="off" onfocus="showDropdown('tex6Dropdown')" oninput="filterDropdown('tex6', 'tex6Dropdown')">
    <div id="tex6Dropdown" class="dropdown-options"></div>
    <label class="file-input-label" style="color: #3794ff;">+ Add PNG <input type="file" accept=".png" style="display:none" onchange="window.handleCustomTexture(this, 'tex6')"></label>
</div>
```

## Related Questions
- How does the texture configuration area work?
- What is the purpose of the dropdown menus in the texture slots?
- Can users upload custom textures to any slot?
- How is the texture layout map organized?
- What are the different views represented in the layout map?
- Is there a limit to the number of texture slots available?

*Source: unknown | chunk_id: addon_creator_blocks.html_chunk_2*
