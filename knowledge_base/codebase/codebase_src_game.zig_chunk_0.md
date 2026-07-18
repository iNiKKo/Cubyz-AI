# [hard/codebase_src_game.zig] - Chunk 0

**Type:** implementation
**Keywords:** camera rotation, view matrix update, game modes, damage messages, enum handling
**Symbols:** camera, camera.rotation, camera.direction, camera.viewMatrix, camera.moveRotation, camera.updateViewMatrix, Gamemode, DamageType, DamageType.heal, DamageType.kill, DamageType.fall, DamageType.heat, DamageType.spiky, DamageType.sendMessage
**Concepts:** camera controls, gamemodes, damage types

## Summary
Defines detailed camera control logic including precise rotation limits based on mouse input, gamemodes (survival and creative), and damage types with corresponding message handling methods.

## Explanation
This chunk defines the camera control logic in Cubyz. The `camera` struct contains variables for rotation (`rotation`) and direction (`direction`). The `moveRotation` function updates these based on mouse input, ensuring that the x-axis rotation is clamped between -π/2 + 0.001 and π/2 - 0.001 to prevent gimbal lock issues. The `updateViewMatrix` function calculates the view matrix using the current camera rotation values.

The chunk also declares an enum for game modes (`Gamemode`) with two options: survival (0) and creative (1). Additionally, it defines an enum for damage types (`DamageType`) including heal (0), kill (1), fall (2), heat (3), and spiky (4). Each `DamageType` has a method `sendMessage` that sends specific messages to the server when a player is affected by different types of damage.

The exact message strings for each damage type are:
- heal: `{s}§#ffffff was healed`
- kill: `{s}§#ffffff was killed`
- fall: `{s}§#ffffff died of fall damage`
- heat: `{s}§#ffffff burned to death`
- spiky: `{s}§#ffffff experienced death by 1000 needles`

## Code Example
```zig
pub fn moveRotation(mouseX: f32, mouseY: f32) void {
		// Mouse movement along the y-axis rotates the image along the x-axis.
		rotation[0] += mouseY;
		const bound = std.math.pi/2.0 - 0.001;
		rotation[0] = std.math.clamp(rotation[0], -bound, bound);
		// Mouse movement along the x-axis rotates the image along the z-axis.
		rotation[2] += mouseX;
	}
```

## Related Questions
- How does the camera rotation work in this chunk, including specific bounds?
- What are the defined game modes and their values?
- Can you explain how damage types handle message sending with exact examples?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_0*
