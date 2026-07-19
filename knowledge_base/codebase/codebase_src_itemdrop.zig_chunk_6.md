# [hard/codebase_src_itemdrop.zig] - Chunk 6

**Type:** implementation
**Keywords:** uniform binding, model drawing, light interpolation, voxel model cache, player inventory
**Symbols:** itemModelSSBO, modelData, freeSlots, voxelModels, getModel, bindCommonUniforms, bindLightUniform, bindModelUniforms, drawItem, renderItemDrops, getIndex, blendColors, renderDisplayItems
**Concepts:** item rendering, lighting calculations, model transformations, inventory display

## Summary
Handles rendering of item drops and display items in the game world.

## Explanation
Handles rendering of item drops and display items in the game world. This chunk manages the rendering of both item drops scattered in the world and items displayed on the screen. It initializes resources, binds uniforms, and draws models for these items.

The `renderItemDrops` function updates item drop positions, calculates lighting based on surrounding blocks, and renders each item with appropriate transformations. For each item drop, it retrieves the position, rotation, and block type. If the item is a base item with a default image, it uses the block type to determine the model index and vertices; otherwise, it sets a default scale of 0.5. The function calculates the light values for the surrounding blocks and blends them using the `blendColors` function. It then binds the common uniforms, light uniforms, and model uniforms, constructs the model matrix with translation, rotation, scaling, and final adjustments, and draws the item using the vertex array object.

The `renderDisplayItems` function handles the display of selected items from the player's inventory. It calculates a perspective projection matrix and an identity view matrix, binds common uniforms, retrieves the selected item from the player's inventory, and if it is not null, calculates its position relative to the camera. It then samples light values from surrounding blocks, blends them, and binds the necessary uniforms before drawing the item.

The `deinit` method deinitializes various resources including `itemPipeline`, `itemModelSSBO`, `modelData`, and clears `voxelModels`. It also destroys each free slot in `freeSlots` and deinits `freeSlots` itself. The `getModel` function retrieves or creates a voxel model for a given item using the `voxelModels` cache.

The `bindCommonUniforms` function binds common uniforms such as reflection map size, projection matrix, ambient light, view matrix, contrast, and depth range. Specifically, it sets the reflection map size to `main.renderer.reflectionCubeMapSize`, uploads the projection matrix using `glUniformMatrix4fv`, sets the ambient light using `glUniform3fv`, uploads the view matrix using `glUniformMatrix4fv`, sets the contrast to 0.12, and retrieves the depth range using `glGetFloatv` before uploading it with `glUniform2fv`.

The `bindLightUniform` function calculates and binds lighting based on sun and block light values. It computes the sun light as a fraction of the ambient light multiplied by the normalized light vector from the light array, and similarly for block light. The combined light is then clamped to a maximum value of 1 using `@min` and `@sqrt`, before being uploaded with `glUniform3fv`.

The `bindModelUniforms` function binds model index and block type uniforms using `glUniform1i`. The `drawItem` function sets the model matrix and draws elements using the vertex array object. It uploads the model matrix using `glUniformMatrix4fv` and then calls `glDrawElements` to render the item.

The `getIndex` function calculates an index based on x, y, and z coordinates using the formula `(z*4) + (y*2) + (x)`. The `blendColors` function blends two color arrays with a given interpolation factor by linearly interpolating each component of the color arrays.

The chunk also includes functions for handling item rendering, lighting calculations, model transformations, and inventory display. It ensures that items are rendered correctly based on their positions, orientations, and lighting conditions.

## Code Example
```zig
fn getIndex(x: u8, y: u8, z: u8) u32 {
		return (z*4) + (y*2) + (x);
	}
```

## Related Questions
- What is the purpose of the `getModel` function?
- How does the chunk handle lighting for item drops?
- What resources are initialized in the `deinit` method?
- How are model matrices calculated and applied during rendering?
- What is the role of the `blendColors` function in rendering?
- How does the chunk manage the display of items from the player's inventory?

*Source: unknown | chunk_id: codebase_src_itemdrop.zig_chunk_6*
