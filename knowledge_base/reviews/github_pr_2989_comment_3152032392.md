# [src/sync.zig] - PR #2989 review diff

**Type:** review
**Keywords:** MoveToPlayerBag, TakeFromPlayerBag, run, serialize, deserialize, InventoryAndSlot, Context, BinaryWriter, BinaryReader, Side, main.server.User, Inventories, putItemsInto, shift clicking, hand fallback
**Symbols:** MoveToPlayerBag, TakeFromPlayerBag, run, serialize, deserialize, InventoryAndSlot, Context, BinaryWriter, BinaryReader, Side, main.server.User
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added MoveToPlayerBag and TakeFromPlayerBag structs with run, serialize, and deserialize methods.

## Explanation
The changes introduce two new command structs, `MoveToPlayerBag` and `TakeFromPlayerBag`, which handle moving items between player bags. The reviewer suggests using the `Inventories` struct as a destination for these operations, potentially simplifying future refactoring. They also propose that shift clicking should have the hand as a fallback, enhancing user interaction.

## Related Questions
- What is the purpose of the `MoveToPlayerBag` struct?
- How does the `run` method in `MoveToPlayerBag` handle different sides (client/server)?
- Why is there a check for `ctx.user != null` in the `run` method?
- What does the `serialize` method do in `MoveToPlayerBag`?
- How is the `deserialize` method implemented in `MoveToPlayerBag`?
- What are the potential benefits of using `Inventories` as destinations?
- Why is there a suggestion for shift clicking to have the hand as a fallback?

*Source: unknown | chunk_id: github_pr_2989_comment_3152032392*
