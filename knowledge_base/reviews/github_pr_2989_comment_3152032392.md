# [src/sync.zig] - PR #2989 review diff

**Type:** review
**Keywords:** MoveToPlayerBag, TakeFromPlayerBag, InventoryAndSlot, serialization, deserialization, refactoring, shift-clicking, hand operations
**Symbols:** MoveToPlayerBag, TakeFromPlayerBag, InventoryAndSlot, Context, BinaryWriter, BinaryReader, Side, main.game.Player.id, @"cubyz:bag".client.getBag, @"cubyz:bag".server.getBag
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added new structs for moving and taking items from player bags, with serialization and deserialization methods.

## Explanation
The changes introduce two new structs, `MoveToPlayerBag` and `TakeFromPlayerBag`, which handle the logic for moving items to and from a player's bag. These structs include methods for running the command, serializing data to a binary writer, and deserializing data from a binary reader. The reviewer suggests using an `Inventories` struct as the destination with a `putItemsInto` method, which could simplify future refactoring efforts. Additionally, there is a suggestion to consider shift-clicking as a fallback for hand operations.

## Related Questions
- What is the purpose of the `MoveToPlayerBag` struct?
- How does the `run` method in `MoveToPlayerBag` handle client and server sides differently?
- Why is there a check for `ctx.user != null` in the `MoveToPlayerBag` run method?
- What is the role of the `serialize` method in `MoveToPlayerBag`?
- How does the `deserialize` method in `TakeFromPlayerBag` handle reading data from a binary reader?
- What is the suggested improvement for using `Inventories` with `putItemsInto`?
- Why is there a suggestion to consider shift-clicking as a fallback for hand operations?

*Source: unknown | chunk_id: github_pr_2989_comment_3152032392*
