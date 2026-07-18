# [issues/issue_2192.md] - Issue #2192 discussion

**Type:** review
**Keywords:** Ziplines, Hooks, Cables, Metal Block, Inventory, LODs, 3D Line Curve, Lightweight Entity, Gameplay Mechanics, Item Design, Rendering Optimization, Speed Calculation, Player Interaction, Inventory Management, Balancing
**Symbols:** Ziplines, Hooks, Cables, Metal Block, Inventory, LODs, 3D Line Curve, Lightweight Entity
**Concepts:** Gameplay Mechanics, Item Design, Rendering Optimization, Speed Calculation, Player Interaction, Inventory Management, Balancing

## Summary
The issue discusses the design and implementation of a Zipline feature in Cubyz, including gameplay mechanics, item requirements, rendering, speed calculation, and user interaction methods.

## Explanation
The Zipline feature is proposed as a permanent traversal method between two points with visual appeal. It involves Hooks for attachment and Cables for the zipline itself, which can be extended by chaining multiple hooks. The discussion explores different methods of player interaction, such as using bare hands, existing tools, or dedicated tools, each with its own pros and cons in terms of gameplay balance and inventory management. The rendering is proposed to use lightweight entities representing a 3D line curve between hooks, with LODs for optimization. Speed calculation is based on the angle of the zipline relative to gravity, considering factors like air resistance and friction. The maintainers suggest exploring options like accessory slots or pulley devices for player interaction, emphasizing that the final implementation should balance gameplay and inventory clutter.

## Related Questions
- How does the Zipline feature handle player interaction with different tools?
- What is the proposed method for rendering the zipline in Cubyz?
- How is the speed of the zipline calculated based on its angle?
- What are the potential issues with using bare hands to ride the zipline?
- How can the zipline be extended beyond its maximum length?
- What are the considerations for balancing gameplay and inventory clutter with the Zipline feature?

*Source: unknown | chunk_id: github_issue_2192_discussion*
