# [issues/issue_521.md] - Issue #521 discussion

**Type:** review
**Keywords:** player hitbox, nearest empty location, last stored position, random direction, block collision
**Concepts:** player movement, block placement, teleportation

## Summary
Discussion on handling player placement inside blocks, suggesting alternatives like moving to an empty location or using the last stored position.

## Explanation
The issue revolves around players being teleported in random directions when placing a block inside their hitbox. The maintainers suggest two potential solutions: either preventing block placement within the player's hitbox or teleporting the player to the nearest empty location, preferably moving upwards if no such location is available. Additionally, another suggestion is to use the server-stored last position of the player as a fallback.

## Related Questions
- How can we prevent block placement within the player's hitbox?
- What algorithm should be used to find the nearest empty location for teleportation?
- How does the server store and retrieve last positions of players?
- What are the potential performance implications of checking for empty locations during block placement?
- How can we ensure that teleportation does not cause additional issues like falling through blocks?
- What is the current implementation for handling player collisions with blocks?

*Source: unknown | chunk_id: github_issue_521_discussion*
