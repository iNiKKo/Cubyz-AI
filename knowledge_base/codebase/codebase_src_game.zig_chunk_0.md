# [hard/codebase_src_game.zig] - Chunk 0

**Type:** implementation
**Keywords:** thread safety, position management, velocity tracking, bounding box, friction state, volume properties, mutex locking
**Symbols:** camera, camera.rotation, camera.direction, camera.viewMatrix, camera.moveRotation, camera.updateViewMatrix, Gamemode, DamageType, Player, Player.EyeData, Player.EyeData.pos, Player.EyeData.vel, Player.EyeData.coyote, Player.EyeData.step, Player.EyeData.box, Player.EyeData.desiredPos, Player.super, Player.eye, Player.crouching, Player.id, Player.gamemode, Player.isFlying, Player.isGhost, Player.hyperSpeed, Player.mutex, Player.inventorySize, Player.inventory, Player.selectedSlot, Player.defaultBlockDamage, Player.selectionPosition1, Player.selectionPosition2, Player.friction, Player.volumeProperties, Player.onGround, Player.jumpCooldown, Player.jumpCoyote, Player.jumpCooldownConstant, Player.jumpCoyoteTimeConstant, Player.standingBoundingBoxExtent, Player.crouchingBoundingBoxExtent, Player.crouchPerc, Player.outerBoundingBoxExtent, Player.outerBoundingBox, Player.jumpHeight, Player.loadFrom, Player.setPosBlocking, Player.getPosBlocking, Player.getVelBlocking, Player.getEyePosBlocking, Player.getEyeVelBlocking
**Concepts:** player management, camera control, gamemodes, damage types, inventory management

## Summary
Defines player structure and related functionalities including camera control, gamemodes, damage types, and inventory management.

## Explanation
This chunk defines the `Player` struct which encapsulates all properties and methods related to a player in the game. It includes nested structures like `EyeData` for eye-specific data. The chunk also defines enums for `Gamemode` and `DamageType`, each with associated methods. Functions such as `moveRotation` and `updateViewMatrix` manage camera rotation and view matrix updates. Player position, velocity, and other properties are managed with thread-safe functions like `setPosBlocking` and `getPosBlocking`. The chunk imports various modules for functionalities like assets, network, particles, graphics, renderer, settings, blocks, physics, and keyboard.

## Code Example
```zig
pub fn getPosBlocking() Vec3d {
	mutex.lock();
	defer mutex.unlock();
	return super.pos;
}
```

## Related Questions
- How does the camera rotation work in the game?
- What are the different gamemodes available in the game?
- How is player position managed with thread safety?
- What methods are available for managing player inventory?
- How does the damage type enum handle sending messages?
- What is the purpose of the `EyeData` struct within the Player struct?
- How is the jump cooldown and coyote time calculated for the player?
- What role does the mutex play in the Player struct methods?
- How are bounding boxes defined for standing and crouching players?
- What functions are used to load player data from a ZonElement?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_0*
