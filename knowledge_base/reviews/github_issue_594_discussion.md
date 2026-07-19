# [issues/issue_594.md] - Issue #594 discussion

**Type:** review
**Keywords:** crafting grid, tool type, orientation, restrictions, balance, selection, buttons, settings, detection
**Concepts:** gameplay balance, tool selection, crafting grid restrictions

## Summary
Discussion on restricting the crafting grid based on tool type, with consideration for different orientations.

## Explanation
Discussion on restricting the crafting grid based on tool type, with consideration for different orientations. The proposal involves implementing a pattern-dependent crafting grid where certain slots are mandatory (white fields), optional (gray fields), and prohibited (red fields). For example, in a pickaxe, white fields must be used, gray ones are optional, and red ones cannot be used. This restriction is intended to simplify balancing and make it easier for the player to select the tool they want. Additionally, once pattern-dependent modifiers from #172 are added, restricting the crafting grid could make it more interesting, since it's more of a puzzle to place these pattern-dependent modifiers. For example, in this pickaxe here, you could at most place one modifier with a 3×3 pattern requirement. Of course, it strips away some of the freedom to make broken tools, but I think it still offers enough freedom. The discussion includes suggestions for handling different tool orientations using buttons to switch between left and right facing tools, but detection of orientation is not feasible.

## Related Questions
- How can we implement a crafting grid restriction based on tool type?
- What are the potential benefits of restricting the crafting grid for different tool orientations?
- Can we use buttons to switch between left and right facing tools in the crafting grid?
- Is it possible to detect which side a tool is facing during crafting?
- How can we ensure that the default orientation setting fits both left and right facing tools?

*Source: unknown | chunk_id: github_issue_594_discussion*
