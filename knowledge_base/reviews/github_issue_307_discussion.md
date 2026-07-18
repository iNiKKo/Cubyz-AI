# [issues/issue_307.md] - Issue #307 discussion

**Type:** review
**Keywords:** mesh intersection, block placement, air, simultaneous clicks, intended feature, Minecraft
**Concepts:** mesh intersection, game world modification, user interaction

## Summary
The issue arises from the mesh intersection not being refreshed after placing or breaking a block, leading to unintended block placement in the air.

## Explanation
The problem stems from a failure to update the mesh intersection data immediately after modifying the game world by placing or breaking a block. This oversight causes the game to incorrectly determine the target location for subsequent interactions, such as placing another block, resulting in blocks being created in unintended positions like mid-air. The discussion suggests that this behavior might be intentional, similar to Minecraft's handling of simultaneous left and right clicks.

## Related Questions
- What is the current mechanism for refreshing mesh intersections in Cubyz?
- How does Cubyz handle simultaneous left and right mouse button clicks?
- Is there a configuration option to disable this behavior if it's intended?
- Can you provide a code snippet where mesh intersection refresh is triggered?
- Are there any known performance implications of frequent mesh intersection updates?
- How does this issue affect multiplayer gameplay, if at all?

*Source: unknown | chunk_id: github_issue_307_discussion*
