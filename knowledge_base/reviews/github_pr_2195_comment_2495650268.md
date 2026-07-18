# [src/server/terrain/simple_structures/SbbGen.zig] - PR #2195 review diff

**Type:** review
**Keywords:** optional pointer, list resize, world arena, memory usage, error handling
**Symbols:** SbbGen, loadModel, ZonElement
**Concepts:** memory management, error handling

## Summary
The function `loadModel` now returns an optional pointer (`?*SbbGen`) instead of a non-optional pointer (`*SbbGen`). The reviewer questions the concern about list storage doubling due to resizes, as the list is discarded after world load.

## Explanation
The change modifies the return type of `loadModel` from `*SbbGen` to `?*SbbGen`, allowing for the possibility of returning null if an error occurs. The reviewer expresses confusion about a concern regarding potential double storage usage (`2N`) due to list resizes, as the list is managed within a world arena and discarded upon world closure, thus preventing any long-term memory issues.

## Related Questions
- What is the purpose of changing `loadModel` to return an optional pointer?
- Why was there a concern about list storage doubling (`2N`) in this context?
- How does the use of `worldArena` affect memory management in this scenario?
- Can you explain the potential impact of returning null from `loadModel`?
- What is the role of `ZonElement` in the `loadModel` function?
- How does the current implementation handle errors during model loading?

*Source: unknown | chunk_id: github_pr_2195_comment_2495650268*
