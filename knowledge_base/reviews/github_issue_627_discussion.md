# [issues/issue_627.md] - Issue #627 discussion

**Type:** review
**Keywords:** buckets, crafting, durability, fluids, capacity, onRightClick, interactions, tool system, attributes, dependencies
**Symbols:** buckets, tool crafting system, durability, flammability, capacity, fluids, water, lava, onRightClick
**Concepts:** crafting system integration, item interactions, fluid handling

## Summary
Discussion on implementing buckets in Cubyz using the tool crafting system, focusing on durability and potential capacity features.

## Explanation
The discussion revolves around integrating buckets into Cubyz's tool crafting system. Key points include the need for durability attributes to account for different fluid types (e.g., water vs. lava) and the possibility of varying bucket capacities based on size. The team identifies dependencies such as selecting specific fluids when holding a bucket and implementing an `onRightClick` callback for items. There is also mention of ongoing work in #2898 that will expand to include this functionality.

## Related Questions
- How does the tool crafting system currently handle item interactions?
- What are the current limitations of fluid handling in Cubyz?
- How will the `onRightClick` callback be integrated into the existing system?
- What specific attributes will be assigned to buckets for durability and flammability?
- How will bucket capacity be determined and implemented?
- What dependencies need to be resolved before implementing bucket functionality?
- How does #2898 relate to the `onRightClick` callback implementation?
- What are the potential challenges in integrating fluid-specific interactions with buckets?
- How will the procedural crafting part be set up for future enhancements?
- What is the current status of the fluid system implementation (#62)?

*Source: unknown | chunk_id: github_issue_627_discussion*
