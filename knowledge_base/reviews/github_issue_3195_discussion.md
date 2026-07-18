# [issues/issue_3195.md] - Issue #3195 discussion

**Type:** review
**Keywords:** blocks, tags, items, inventory, tooltip, rendering, irrelevant information, alien blocks, mineable, cuttable
**Concepts:** tagging, inventory management, game mechanics

## Summary
The issue involves blocks not mirroring tags to their items, causing the item's tags to not be displayed in-game.

## Explanation
The user reports that when querying an item's tags in a player's inventory, only the item index is found, and not the associated tags. The maintainer initially questions whether the queried item actually has tags and notes that block tags and item tags are distinct. The user clarifies that they believe such information could be relevant, especially for identifying tools needed to break alien blocks. However, it turns out that the issue is not about irrelevant information but rather that the tags do not render at all in-game.

## Related Questions
- What is the current implementation for mirroring block tags to item tags in Cubyz?
- Are there any known issues with tag rendering in the inventory system of Cubyz?
- How does Cubyz differentiate between block tags and item tags?
- Can you provide a code snippet that demonstrates how to check if an item has an associated block in Cubyz?
- What are the potential performance implications of adding more information to tooltips in Cubyz?
- Is there a way to ensure that only relevant tags are displayed in the tooltip without cluttering it?

*Source: unknown | chunk_id: github_issue_3195_discussion*
