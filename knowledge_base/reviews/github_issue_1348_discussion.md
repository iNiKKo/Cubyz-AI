# [issues/issue_1348.md] - Issue #1348 discussion

**Type:** review
**Keywords:** recipes, tags, mapping, UI, boilerplate reduction, named symbols, addon support
**Symbols:** .wood, cubyz:coal, cubyz:torch, cubyz:planks
**Concepts:** recipe definitions, tags, input/output mapping, UI display

## Summary
Discussion on implementing tags in recipe definitions to reduce boilerplate and improve flexibility.

## Explanation
The discussion revolves around allowing tags in recipes to specify inputs and outputs, reducing the need for duplicating recipes for different item types like wood. The main concerns include how to map input types to correct output types and how to display these recipes in the UI. The maintainer suggests using a mapping option within recipe definitions to explicitly specify the relationship between input and output types. Additionally, there are proposals for using named symbols in recipe inputs and outputs to maintain consistency with the current system.

## Related Questions
- How does the proposed mapping option work in recipe definitions?
- What are the potential issues with allowing mismatching items in recipes?
- How will the UI display recipes that use tags for inputs and outputs?
- What is the impact of using named symbols on recipe consistency?
- How can addon support be integrated into the tag-based recipe system?
- What are the advantages and disadvantages of generating all recipes eagerly versus using tags?
- How does the proposed solution address the issue of mixing different wood types in recipes?
- What are the potential technical challenges in implementing dedicated crafting stations with single input slots?
- How can the mapping option be extended to support more complex patterns or rules?
- What is the relationship between this tag-based recipe system and the concept of dedicated crafting stations?

*Source: unknown | chunk_id: github_issue_1348_discussion*
