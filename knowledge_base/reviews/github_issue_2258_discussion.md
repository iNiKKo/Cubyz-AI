# [issues/issue_2258.md] - Issue #2258 discussion

**Type:** review
**Keywords:** block entities, modular, addons, compatibility, callbacks, data storage, interaction events, click events, interfaces, furnaces, crops, game ticks
**Symbols:** zon, blockentity, inventory, text, onTick, replaceBlock
**Concepts:** modularity, addon compatibility, event system

## Summary
Discussion on making block entities more modular to allow for greater flexibility and addon compatibility.

## Explanation
Discussion on making block entities more modular to allow for greater flexibility and addon compatibility. The issue highlights that currently, block entities are hardcoded for chests and signs, which limits the ability of addon developers to add new block entities or complex behaviors like furnaces. Proposals include implementing a zon data structure for creating interfaces, defining modular callbacks for these interfaces, and establishing different modes of block entity data storage (e.g., 'inventory' or 'text'). Additionally, there is a suggestion to start with click events and interfaces for regular blocks first, as this will be essential for block entities later on. The discussion also mentions the potential benefits of adding an `onGameTick` event and specific callbacks for when blocks are interacted with in various ways. Examples include crops that grow over time until they can be harvested or utility blocks that replace nearby blocks with themselves every tick, though it is noted that such behaviors may already be achievable through existing events like `onTick`. The current implementation of block entities limits their complexity and addon compatibility.

## Related Questions
- What are the specific requirements for implementing a modular form of block entity data storage?
- How would adding an `onGameTick` event enhance the functionality of block entities?
- Can you provide examples of how to use the `onTick` and `replaceBlock` events in a mod?

*Source: unknown | chunk_id: github_issue_2258_discussion*
