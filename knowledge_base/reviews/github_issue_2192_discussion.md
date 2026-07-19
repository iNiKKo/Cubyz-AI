# [issues/issue_2192.md] - Issue #2192 discussion

**Type:** review
**Keywords:** Ziplines, Hooks, Cables, Metal Block, Inventory, LODs, 3D Line Curve, Lightweight Entity, Gameplay Mechanics, Item Design, Rendering Optimization, Speed Calculation, Player Interaction, Inventory Management, Balancing
**Symbols:** Ziplines, Hooks, Cables, Metal Block, Inventory, LODs, 3D Line Curve, Lightweight Entity
**Concepts:** Gameplay Mechanics, Item Design, Rendering Optimization, Speed Calculation, Player Interaction, Inventory Management, Balancing

## Summary
The issue discusses the design and implementation of a Zipline feature in Cubyz, including gameplay mechanics, item requirements, rendering, speed calculation, and user interaction methods.

## Explanation
The Zipline feature is proposed as a permanent traversal method between two points with visual appeal. It involves Hooks for attachment and Cables crafted from Metal Blocks (1 ingot yields 8 cables). The amount of cable used depends on the distance between hooks, up to a maximum length. To extend beyond this limit, additional hooks can be added in sequence. Player interaction methods include bare hands, existing tools like pickaxes, or dedicated zipline tools/accessories. Bare hand use is easy but risky and slow; using tools provides better control but consumes durability. The rendering uses lightweight entities representing 3D line curves between hooks with LODs for optimization. Speed calculation considers the angle of the curve relative to gravity, accounting for air resistance and friction. The maintainers suggest exploring options like accessory slots or pulley devices for player interaction, emphasizing that the final implementation should balance gameplay and inventory clutter.

## Related Questions
- How many cables are produced from one metal ingot?
- What is the maximum length a zipline can cover without additional hooks?
- How does extending a zipline with multiple hooks work?
- What are the exact speed calculation factors for a zipline based on its angle?
- What are the pros and cons of using bare hands versus tools to ride a zipline?

*Source: unknown | chunk_id: github_issue_2192_discussion*
