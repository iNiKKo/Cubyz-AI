# [issues/issue_2258.md] - Issue #2258 discussion

**Type:** review
**Keywords:** block entities, modular, addons, compatibility, callbacks, data storage, interaction events, click events, interfaces, furnaces, crops, game ticks
**Symbols:** zon, blockentity, inventory, text, onTick, replaceBlock
**Concepts:** modularity, addon compatibility, event system

## Summary
Discussion on making block entities more modular to allow for greater flexibility and addon compatibility.

## Explanation
The issue discusses the current hardcoded nature of block entities in Cubyz, particularly for chests and signs. The proposal is to implement block entities similarly to how items, biomes, and blocks are currently implemented, which would enable more complex behaviors like furnaces and interactive blocks. The discussion includes considerations for modular callbacks, data storage modes, and interaction events. There's also a suggestion to start with implementing click events and interfaces for regular blocks first, as this will be essential for block entities later on.

## Related Questions
- What is the current implementation of block entities in Cubyz?
- How would implementing a modular form of block entity data storage benefit addon developers?
- Can you provide examples of how to use the `onTick` and `replaceBlock` events in a mod?
- What are the potential challenges in making block entities more modular?
- How does the event system currently support complex behaviors like replacing nearby blocks?
- What is the proposed structure for creating interfaces with the zon data structure?
- How would adding an `onGameTick` event enhance the functionality of block entities?
- Can you explain the difference between random ticks and game ticks in Cubyz?
- What are some examples of utility blocks that could benefit from modular block entities?
- How does the current implementation of block entities limit their complexity?

*Source: unknown | chunk_id: github_issue_2258_discussion*
