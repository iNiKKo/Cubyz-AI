# [hard/codebase_src_renderer.zig] - Chunk 1

**Type:** implementation
**Keywords:** projection matrix, viewport update, mesh updating, render loop, camera transformations
**Symbols:** lastWidth, lastHeight, lastFov, updateFov, updateViewport, render, crosshairDirection
**Concepts:** renderer, field of view, viewport, world rendering, crosshair direction calculation

## Summary
Handles rendering operations including updating the field of view, viewport, and performing the main render loop.

## Explanation
This chunk manages various aspects of rendering within the Cubyz engine. It includes functions to update the field of view (`updateFov`) and the viewport (`updateViewport`), which adjust the projection matrix based on new dimensions or field of view settings. The `render` function is the main entry point for rendering the world, handling tasks such as updating item displays, rendering the world itself, and managing mesh updates. Additionally, the `crosshairDirection` function calculates the direction vector from the camera to the crosshair position on the screen, using matrix transformations and trigonometric calculations.

**Variables:**
- `lastWidth`: Stores the last known width of the viewport (type: u31).
- `lastHeight`: Stores the last known height of the viewport (type: u31).
- `lastFov`: Stores the last known field of view (type: f32).

**Functions:**
- `updateFov(fov: f32) void`: Updates the field of view and recalculates the projection matrix if the new field of view is different from the last one.
- `updateViewport(width: u31, height: u31) void`: Updates the viewport dimensions, applies resolution scaling, and recalculates the projection matrix.
- `render(playerPosition: Vec3d, deltaTime: f64) void`: Handles the main rendering loop, including updating item displays, rendering the world, and managing mesh updates.
- `crosshairDirection(rotationMatrix: Mat4f, fovY: f32, width: u31, height: u31) Vec3f`: Calculates the direction vector from the camera to the crosshair position on the screen using matrix transformations and trigonometric calculations.

**Night Color:** The night color is defined as `Vec3f{0.3, 0.4, 0.5}`.

**Ambient Lighting Calculation:** The ambient lighting is calculated based on the night color and the day time's ambient light value using the formula: `ambient = @max(nightColor*@as(Vec3f, @splat(settings.nightBrightness)), @as(Vec3f, @splat(game.world.?.dayTime.ambientLight)))`.

**Resolution Scaling:** The viewport dimensions are scaled by `main.settings.resolutionScale` before being used to update the projection matrix.

**Projection Matrix Update:** When the field of view or viewport dimensions change, the projection matrix is recalculated using the formula: `Mat4f.perspective(std.math.degreesToRadians(fov), @as(f32, @floatFromInt(lastWidth))/@as(f32, @floatFromInt(lastHeight)), zNear, zFar).`

**Item Display Management:** The `itemdrop.ItemDisplayManager.update(deltaTime)` function updates item displays during each frame.

**World Rendering:** The world is rendered using the `renderWorld` function, which takes into account the ambient lighting, fog color, and player position.

**Crosshair Direction Calculation:** The `crosshairDirection` function calculates the direction vector from the camera to the crosshair position on the screen by first calculating the inverse rotation matrix, then determining the camera's direction, up, and right vectors. It uses these vectors along with the field of view and screen dimensions to compute the final direction vector.

**Mesh Updates:** The `mesh_storage.updateMeshes(startTime.addDuration(maximumMeshTime))` function updates the meshes based on the current time and a maximum mesh update duration.

## Code Example
```zig
pub fn updateFov(fov: f32) void {
	if (lastFov != fov) {
		lastFov = fov;
		game.projectionMatrix = Mat4f.perspective(std.math.degreesToRadians(fov), @as(f32, @floatFromInt(lastWidth))/@as(f32, @floatFromInt(lastHeight)), zNear, zFar);
	}
}
```

## Related Questions
- What is the purpose of the `updateFov` function?
- How does the `render` function handle ambient lighting calculations?
- What variables are used to store the last known width and height of the viewport?
- Describe the process of calculating the crosshair direction in the `crosshairDirection` function.
- How is the projection matrix updated when the field of view changes?
- What tasks does the `render` function perform during each frame?
- How are item displays managed within the rendering loop?
- What is the role of the `lastFov` variable in the renderer module?
- How does the renderer handle resolution scaling for the viewport dimensions?
- What steps are taken to ensure the world projection matrix is correctly updated?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_1*
