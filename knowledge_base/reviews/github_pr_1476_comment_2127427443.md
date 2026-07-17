# [src/blocks.zig] - Chunk 2127427443

**Type:** review
**Keywords:** TickEventVTableMap, vtable, init, deinit, registerEventStruct, named callbacks, auto-registration, std.StringHashMap, main.globalAllocator.allocator, TickEvents
**Symbols:** Block, TickFunction, TickFunctions, replaceWithCobble, TickEventVTableMap, init, deinit, registerEventStruct, vTableMap, main.globalAllocator.allocator, TickEvents
**Concepts:** dynamic dispatch, vtable construction, compile-time reflection, extensibility, memory management, named callbacks, union field iteration, type introspection, zero-copy allocation

## Summary
Replaced a simple global array of tick callbacks with a dynamic vtable map that auto-registers struct fields at init time and supports deinit.

## Explanation
The original code used a static `tickFunctions` named callback table, which required manual wiring for each event type. Reviewers flagged this as fragile: adding new events would require editing the global array, risking missed registrations or stale entries. The refactor introduces `TickEventVTableMap`, a struct containing a `std.StringHashMap(*const TickEvent.VTable)`. At init, it walks over all fields of the `TickEvents` union (or struct), checks that each field is itself a type, and calls `registerEventStruct` to pull the corresponding vtable from the event's definition. This makes registration automatic and deterministic based on the AST layout, eliminating manual updates. The deinit method ensures proper cleanup of the hashmap. Architecturally this improves extensibility (new events need only be added to the union/struct), reduces runtime errors from mismatched registrations, and aligns with Zig’s compile-time reflection capabilities. It also prevents regressions where a new tick event could silently fail if not manually added to `tickFunctions`.

## Related Questions
- What is the type of `tickFunctions` before the refactor and why was it considered fragile?
- How does `registerEventStruct` iterate over fields of a union/struct at compile time?
- Why use `std.StringHashMap(*const TickEvent.VTable)` instead of an array for vtables?
- What happens if a new tick event is added to the union but not manually registered in the old code?
- Does `deinit` guarantee that all allocated vtable entries are freed, and how does it interact with `main.globalAllocator.allocator`?
- Is there any runtime cost for auto-registering events compared to a static array lookup?
- How would you modify this pattern if the tick events were defined in a separate module rather than inline?
- What safeguards prevent double-registration of the same event type during init?
- Can `TickEventVTableMap` be shared across multiple chunks, or is it per-chunk?
- If `@typeInfo(TickEvents)` returns something other than `.struct`, what error is logged and why?
- How does this change affect the ABI of any code that previously called functions in `tickFunctions` directly?
- What is the maximum number of tick events supported by this hashmap approach, and are there limits on key length?

*Source: unknown | chunk_id: github_pr_1476_comment_2127427443*
