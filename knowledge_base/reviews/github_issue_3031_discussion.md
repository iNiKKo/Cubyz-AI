# [issues/issue_3031.md] - Issue #3031 discussion

**Type:** review
**Keywords:** mining pattern, tool slots, side effects, stats impact, multiblock patterns, accessories
**Symbols:** 3x3 mining area, tool type, tool modifier, accessory, armor
**Concepts:** game mechanics, user interface design, statistical modeling

## Summary
Discussion on implementing a 3x3 mining area in Cubyz, exploring tool type, modifier, or accessory options.

## Explanation
Discussion on implementing a 3x3 mining area in Cubyz, exploring tool type, modifier, or accessory options. The maintainer suggests either reducing the impact of some slots on tool stats to zero or conditionally excluding items from stat calculations. Specifically, reducing slot impact to zero would mean that certain slots, such as those for side effects, would not affect the overall tool stats. Conditionally excluding items from stat calculations could involve enabling modifiers that allow specific items to be ignored in the stat math. Another suggestion is using flowers to select multiblock patterns, similar to a previous discussion with Quantum. The maintainer also proposes that this feature could be implemented as an accessory affecting both mining and placement. Additionally, it's mentioned that crouching could limit the mining area to only the selected block, preventing the extra 3x3 area from being mined.

## Related Questions
- What are the potential impacts of adding slots exclusively for side effects in tools?
- How could changing the impact of some slots on tool stats be implemented?
- Can you provide examples of how flowers could be used to select multiblock patterns?
- What are the benefits and drawbacks of implementing this feature as an accessory?
- How would crouching affect the mining area in this implementation?

*Source: unknown | chunk_id: github_issue_3031_discussion*
