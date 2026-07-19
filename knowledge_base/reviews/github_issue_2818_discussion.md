# [issues/issue_2818.md] - Issue #2818 discussion

**Type:** review
**Keywords:** tool restrictions, crafting grids, hover, item, modifier activation, slots, green and red indicators, secondary tooltip, player inventory interactions, subtle visual cues
**Symbols:** crafting grids, hover, item, modifier activation, slots
**Concepts:** user experience (UX), visual feedback, interaction design

## Summary
Discussion on improving tool restriction display in crafting grids by visualizing relevant slots and tooltips.

## Explanation
The issue revolves around enhancing user understanding of tool restrictions in the game's crafting interface. The maintainer suggests a complex solution involving visual cues like colored slots and additional icons to indicate positive or neutral contributions to modifier activation when an item is held in the hand slot and hovered over a crafting grid slot. Specifically, green indicators would show for slots that contribute positively, while red indicators would denote neutral contributions. Additionally, the maintainer proposes displaying secondary tooltips with more detailed information about these interactions when hovering over slots in crafting inventory. Another suggestion involves subtle visual cues such as small circles (3x3 pixels) in the top left corner for every modifier that would interact with currently held items to indicate potential interactions. The complexity arises from handling multiple modifiers with different restrictions, which complicates the implementation.

## Related Questions
- How can we implement colored slots and icons for positive or neutral contributions to modifier activation?
- What are the exact visual cues proposed for player inventory interactions?
- Can you provide a mockup of how these visual cues would look in practice?

*Source: unknown | chunk_id: github_issue_2818_discussion*
