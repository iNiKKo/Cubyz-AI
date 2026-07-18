# [issues/issue_1601.md] - Issue #1601 discussion

**Type:** review
**Keywords:** cactus, wood, leaf, mushroom, axe, sickle, breakByAxe, breakByPickaxe, tags, addons
**Symbols:** cactus, .wood, .leaf, giant mushroom blocks, .mushroom
**Concepts:** tagging system, tool interaction, block properties

## Summary
Discussion about changing cactus back to a `.leaf` block and considering new tagging approaches for blocks.

## Explanation
The discussion revolves around reverting the change made in a previous PR where cactus was changed to a `.wood` block. The maintainers suggest that giant mushroom blocks should also be tagged as `.leaf`. There is a proposal to introduce more specific tags like `.mushroom` for better addon compatibility. The conversation then shifts to questioning whether cactus and mushrooms should break with axes or sickles, highlighting the complexity of balancing tool interactions. A suggestion is made to replace material-based tagging (like `wood`, `leaf`) with tool-specific properties (`breakByAxe`, `breakByPickaxe`), emphasizing that these tags should not dictate which tools can be used to break a block.

## Related Questions
- What was the reason for changing cactus to a .wood block?
- Why is there a suggestion to introduce a .mushroom tag?
- How does the current tagging system affect tool interactions with blocks?
- What are the potential benefits of using tool-specific properties instead of material tags?
- Can you explain the complexity in balancing which tools break cactus and mushrooms?
- Is there any plan to implement the suggested changes to block tagging?

*Source: unknown | chunk_id: github_issue_1601_discussion*
