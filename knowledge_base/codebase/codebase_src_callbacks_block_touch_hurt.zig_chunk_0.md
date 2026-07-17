# [easy/codebase_src_callbacks_block_touch_hurt.zig] - Chunk 0

**Type:** implementation
**Keywords:** dps, DamageType, worldArena, addHealth, deltaTime, ZonElement, stringToEnum, handled, Player.super, client
**Symbols:** dps, damageType, init, run
**Concepts:** hurt callback, block touch damage, damage per second, health synchronization, client-side health update, zon element parsing, error logging on missing fields

## Summary
This chunk defines the HurtCallback data structure and its initialization/run logic for handling damage events triggered by block touch interactions.

## Explanation
The chunk declares a struct (implicitly via pub fn init) with fields dps (damage per second, f32) and damageType (main.game.DamageType). The init function takes a ZonElement zon and a callbacks.Creator, creates an instance in main.worldArena, populates dps by reading the 'dps' string field from zon (converting to f32 via orelse), logs an error and returns null if missing; similarly reads 'damageType' as []const u8, converts to DamageType enum via std.meta.stringToEnum, logs errors for missing or unknown types. The run method asserts that params.entity equals &main.game.Player.super (with a TODO comment indicating server-side implementation is pending), computes damage as self.dps multiplied by deltaTime cast to f32, calls main.sync.addHealth with negative damage and the stored damageType targeting .client side for Player.id, and returns .handled. No other functions or types are declared here.

## Related Questions
- What fields does the HurtCallback struct contain and what are their types?
- How is the dps value extracted from a ZonElement during initialization?
- What error handling occurs if the 'dps' field is missing in the zon element?
- What happens when the damageType enum conversion fails or returns an unknown variant?
- Which assertion is performed inside the run method and what does it check for?
- How is the final damage amount calculated before being applied to health?
- To which side (.client) is the health update sent and why?
- What entity ID is targeted by the addHealth call in this callback?
- What return value indicates successful handling of the hurt event?
- Where is the new HurtCallback instance allocated when init is called?

*Source: unknown | chunk_id: codebase_src_callbacks_block_touch_hurt.zig_chunk_0*
