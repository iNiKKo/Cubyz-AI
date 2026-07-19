# [issues/issue_944.md] - Issue #944 discussion

**Type:** review
**Keywords:** wildcards, recipe ingredients, tags, addons, compatibility, zon parser, automatic tag creation, amount specification
**Symbols:** cubyz:*_planks, cubyz:iron_ingot, cubyz:chisel, .planks
**Concepts:** wildcard support, recipe ingredients, tags, addon compatibility, zon parser

## Summary
Discussion on allowing wildcards in recipe ingredients and transitioning to tags for better flexibility and addon compatibility.

## Explanation
The discussion revolves around the implementation of wildcard support in recipe ingredients, specifically addressing how to handle new items added by addons. The maintainer suggests using tags instead of wildcards to ensure that newly added items are automatically included in recipes. However, a user points out that this approach doesn't allow specifying amounts for tagged inputs. The maintainer then proposes treating tags as strings without colons, similar to block IDs, and mentions the possibility of automatically creating tags when they are first defined in an item.

To address the issue of specifying amounts with wildcarded tags, the maintainer suggests using a string format like '4 planks' instead. This allows for flexibility in defining the quantity of each input item without needing to modify the recipe itself.

## Related Questions
- How does the zon parser handle tags without colons?
- What is the process for automatically creating tags in Cubyz?
- Can wildcards be used with amounts in recipe ingredients?
- How does the current implementation of recipe ingredients support addon items?
- What are the potential performance implications of using tags instead of wildcards?
- Is there a way to specify amounts for tagged inputs in recipes?

*Source: unknown | chunk_id: github_issue_944_discussion*
