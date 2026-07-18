# [issues/issue_2574.md] - Issue #2574 discussion

**Type:** review
**Keywords:** relative notation, /tp command, directional teleportation, creative mode wand, implementation details
**Concepts:** relative notation, teleportation, creative mode wand

## Summary
Discussion about implementing relative notation in the /tp command, including directional teleportation.

## Explanation
Discussion about implementing relative notation in the /tp (teleport) command in Cubyz, similar to Minecraft. The user initially suggests adding directional teleportation as a feature, but the maintainer proposes using a creative mode wand instead for this purpose. The exact syntax and behavior of the relative notation are specified: `/tp ~a b c` adds `a` to x, assigns `b` to y, and assigns `c` to z; `/tp ^a ^b ^c` adds `a`, `b`, and `c` rotated by facing direction to x, y, and z respectively. The user clarifies their confusion and still wants to know about the implementation details. The maintainer explains how a creative mode wand could work: right-clicking teleports you a fixed number of blocks in the direction you are looking; left-clicking and dragging allows configuring the distance in some way. A new issue (#2628) is created to track the development of directional teleportation.

## Related Questions
- How does the /tp command currently handle relative coordinates?
- What is the proposed implementation for directional teleportation in Cubyz?
- Why was a creative mode wand suggested instead of adding directional teleportation to the /tp command?
- Can you explain how the creative mode wand would allow configuring the distance of teleportation?
- How does the new issue (#2628) plan to address the implementation of directional teleportation?

*Source: unknown | chunk_id: github_issue_2574_discussion*
