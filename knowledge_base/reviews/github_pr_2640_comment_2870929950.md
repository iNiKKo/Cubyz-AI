# [src/lang.zig] - PR #2640 review diff

**Type:** review
**Keywords:** lang.zig, StringHashMapUnmanaged, Category, block, item, label, language, modifier, tag, tool, world_preset, ZonMapEntry, global variable
**Symbols:** std, main, ZonElement, ZonMapEntry, Category, languages
**Concepts:** enum, global variable, string-to-element mapping, efficient data structure

## Summary
Added new language-related constants and structures in src/lang.zig.

## Explanation
The change introduces a new file, src/lang.zig, which defines several constants and structures related to language categories in the Cubyz project. The `Category` enum lists various types of language elements such as blocks, items, labels, etc. A global variable `languages` is declared as an array of `ZonMapEntry`, which uses `StringHashMapUnmanaged` for efficient string-to-element mapping. The reviewer notes that this approach was chosen for simplicity and mentions the possibility of refactoring to use `StringHashMapUnmanaged` in the future.

## Related Questions
- What is the purpose of the `Category` enum in src/lang.zig?
- How does the `languages` array utilize `StringHashMapUnmanaged`?
- Why was `StringHashMapUnmanaged` chosen over other data structures?
- Is there a plan to refactor the use of `StringHashMapUnmanaged` in the future?
- What are the potential benefits and drawbacks of using `StringHashMapUnmanaged`?
- How does the addition of src/lang.zig impact the overall architecture of Cubyz?

*Source: unknown | chunk_id: github_pr_2640_comment_2870929950*
