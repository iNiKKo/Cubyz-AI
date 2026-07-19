# [issues/issue_3195.md] - Issue #3195 discussion

**Type:** review
**Keywords:** blocks, tags, items, inventory, tooltip, rendering, irrelevant information, alien blocks, mineable, cuttable
**Concepts:** tagging, inventory management, game mechanics

## Summary
The issue involves blocks not mirroring tags to their items, causing the item's tags to not be displayed in-game.

## Explanation
The issue involves blocks not mirroring tags to their items, causing the item's tags to not be displayed in-game. The user reports that when querying an item's tags in a player's inventory using the `getItemTags` function (as shown in the attached image), only the item index is found, and not the associated tags. The maintainer initially questions whether the queried item actually has tags and notes that block tags and item tags are distinct. Specifically, the maintainer mentions that rendering certain tags such as `.mineable`, `.cuttable`, and `.slate` could fill the tooltip with irrelevant information. However, it turns out that the issue is not about irrelevant information but rather that the tags do not render at all in-game. The user later discovers that they can check if an item has an associated block by querying the item's properties (e.g., `item.hasBlock()`). The maintainer also clarifies that the issue is about the tags not rendering in the first place, as shown in another attached image.

## Related Questions
- What is the current implementation for mirroring block tags to item tags in Cubyz?
- Are there any known issues with tag rendering in the inventory system of Cubyz?
- How does Cubyz differentiate between block tags and item tags?
- Can you provide a code snippet that demonstrates how to check if an item has an associated block in Cubyz?
- What are the potential performance implications of adding more information to tooltips in Cubyz?
- Is there a way to ensure that only relevant tags are displayed in the tooltip without cluttering it?

*Source: unknown | chunk_id: github_issue_3195_discussion*
