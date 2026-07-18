# [issues/issue_3303.md] - Issue #3303 discussion

**Type:** review
**Keywords:** swords, plants, leaves, collection, tool tags, cuttable, sliceable, cactus, mushroom blocks, axes, items drop
**Symbols:** .cuttable, .sliceable
**Concepts:** Tool Tags, Block Interaction, Item Collection

## Summary
Discussion on adding tool tags to allow swords to break plants and leaves while preventing collection.

## Explanation
Discussion on adding tool tags to allow swords to break plants and leaves while preventing collection. The discussion revolves around implementing two tool tags: one for determining if a block can be broken (`.sliceable`) and another for whether items drop (`.cuttable`). The user proposes using `.cuttable` for sickles and `.sliceable` for swords, aiming to differentiate between breaking blocks and collecting their items. There is also consideration for special cases like cactus and giant mushrooms, where both axes and sickles are effective, and the decision is made to allow swords to be effective against them as well, ensuring they drop items. Additionally, there is a suggestion to make certain blocks drop Rupees sometimes.

## Related Questions
- What are the proposed tool tags for sickles and swords?
- How do the tool tags differentiate between breaking blocks and collecting items?
- Are there any special cases mentioned for cactus and giant mushrooms?
- What is the decision regarding the effectiveness of swords against woody blocks like mushroom blocks and cactus?
- Does the discussion include any consideration for making certain blocks drop Rupees sometimes?

*Source: unknown | chunk_id: github_issue_3303_discussion*
