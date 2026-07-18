# [hard/codebase_src_game.zig] - Chunk 0

**Type:** implementation
**Keywords:** camera rotation, view matrix update, game modes, damage messages, enum handling
**Symbols:** camera, camera.rotation, camera.direction, camera.viewMatrix, camera.moveRotation, camera.updateViewMatrix, Gamemode, DamageType, DamageType.heal, DamageType.kill, DamageType.fall, DamageType.heat, DamageType.spiky, DamageType.sendMessage
**Concepts:** camera controls, gamemodes, damage types

## Summary
Defines camera controls, gamemodes, and damage types with message handling.

## Explanation
This chunk defines the camera control logic, including rotation based on mouse input and updating the view matrix. It also declares an enum for game modes (survival and creative) and another enum for damage types with a method to send messages corresponding to each type of damage.

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
- How does the camera rotation work in this chunk?
- What are the defined game modes in this code?
- How is damage type handled and what messages are sent?
- What is the purpose of the `updateViewMatrix` function?
- Which libraries or modules are imported at the beginning of this file?
- Can you explain the bounds set for camera rotation in the `moveRotation` function?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_0*
