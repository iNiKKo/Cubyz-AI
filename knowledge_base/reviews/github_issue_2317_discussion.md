# [issues/issue_2317.md] - Issue #2317 discussion

**Type:** review
**Keywords:** stone types, shared attributes, tiles, bricks, base, walls, model, rotation, tool materials, folder structure, naming conventions, block migrations, item migrations
**Symbols:** cubyz:slate/base, cubyz:stone/slate/base
**Concepts:** refactoring, naming conventions, folder structure, block migrations, item migrations

## Summary
Refactor stone types to consolidate shared attributes and normalize naming conventions.

## Explanation
The discussion revolves around refactoring the stone types in Cubyz to share common attributes among different block types like tiles, bricks, and base. The walls are an exception due to their unique model and rotation, making them unsuitable as tool materials. Most of the stone attributes are shared within the blocks types (tiles/bricks/base), but the exact folder structure is not specified. Additionally, there's a mention of adding block and item migrations and normalizing tile naming conventions to address issue #2240. The maintainer decided to use `cubyz:slate/base` rather than `cubyz:stone/slate/base`. Block and item migrations will be implemented to ensure compatibility with existing stone types, and their relationship to issue #2240 is that they aim to normalize tile naming conventions.

## Related Questions
- What are the specific attributes being shared among different stone types?
- How will the folder structure change for stone types?
- Why are walls treated as an exception in this refactoring?
- What is the proposed naming convention for tiles?
- Are there any potential performance impacts from this refactoring?
- How will block and item migrations be implemented?
- What are the implications of moving stones into a single folder?
- Will this refactoring affect backwards compatibility with existing stone types?
- How will the new structure improve internal name readability?
- What is the relationship between this refactoring and issue #2240?

*Source: unknown | chunk_id: github_issue_2317_discussion*
