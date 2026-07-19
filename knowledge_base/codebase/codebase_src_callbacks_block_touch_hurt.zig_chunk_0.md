# [easy/codebase_src_callbacks_block_touch_hurt.zig] - Chunk 0

**Type:** implementation
**Keywords:** callback, dps, damageType, health, sync addHealth
**Symbols:** init, run
**Concepts:** callbacks, block touch, hurt event, damage points, damage type, health management

## Summary
Handles block touch hurt events

## Explanation
This chunk initializes and runs a hurt event callback for blocks. The `init` function parses the damage points (`dps`, which is a float32) and damage type (`damageType`, which is of type `main.game.DamageType`) from the ZonElement, logs errors if fields are missing or unknown, and then applies damage to the player's health. The `run` function calculates the damage based on the parsed values and updates the player's health using the `sync.addHealth` function. It also includes a debug assertion to ensure that the entity is the player.

## Code Example
```zig
pub fn run(self: *@This(), params: main.callbacks.BlockTouchCallback.Params) main.callbacks.Result {
	std.debug.assert(params.entity == &main.game.Player.super); // TODO: Implement on the server side
	const damage = self.dps*@as(f32, @floatCast(params.deltaTime));
	main.sync.addHealth(-damage, self.damageType, .client, main.game.Player.id);
	return .handled;
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the `run` function handle block touch hurt events?
- What are the required fields for initializing a hurt event callback?
- Where is the health management logic implemented?
- What type of error handling is used if fields are missing or unknown?
- Is there any server-side implementation needed for the `init` function?
- How does the damage calculation work in the `run` function?
- What data structure is used to store and manage player health?
- Where is the `sync.addHealth` function called from?
- What is the purpose of the `.client` parameter in the `sync.addHealth` call?
- What is the `id` parameter used for in the `sync.addHealth` call?
- How does the `std.debug.assert` statement work in the `run` function?

*Source: unknown | chunk_id: codebase_src_callbacks_block_touch_hurt.zig_chunk_0*
