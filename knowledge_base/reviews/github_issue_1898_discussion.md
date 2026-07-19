# [issues/issue_1898.md] - Issue #1898 discussion

**Type:** review
**Keywords:** panic, structure building block, blueprint, crash, error handling, isBroken flag, return errors, drop structures, biome configuration, user feedback
**Symbols:** loadModel, panicWithMessage__anon_112850, init, registerBiome, loadWorldAssets, ServerWorld.init, start, entryFn
**Concepts:** error handling, thread safety, user experience, performance optimization

## Summary
The game crashes when a blueprint is not found due to a panic in `loadModel`.

## Explanation
The game crashes when a blueprint is not found due to a panic in `loadModel`. The issue arises because the `loadModel` function does not handle errors gracefully, leading to a panic with the message 'Could not find structure building block with id '{s}' when a structure building block (SBB) with a specified ID cannot be found. The maintainer suggests either adding an `isBroken` flag to skip generating broken SBBs or modifying the interface to allow returning errors. The current behavior is deemed unacceptable as it crashes the game without providing user feedback. The maintainer also proposes dropping such structures during loading time to prevent runtime issues and improve user experience.

## Related Questions
- How can we modify `loadModel` to handle missing SBBs gracefully?
- What are the potential performance implications of dropping broken structures during loading?
- How can we ensure that users receive meaningful feedback when an SBB is not found?
- Can we implement a mechanism to log these errors without crashing the game?
- What changes are needed in the `init` function to prevent runtime issues with missing SBBs?
- How does the current error handling in `loadModel` impact the overall stability of the game?

*Source: unknown | chunk_id: github_issue_1898_discussion*
