# [issues/issue_1604.md] - Issue #1604 discussion

**Type:** review
**Keywords:** tool-specific, material tags, adjectives, is-a relationship, block definitions
**Symbols:** breakWithAxe, wood, leaf, ferrock
**Concepts:** grammar, semantics, block definition

## Summary
Discussion about replacing material tags with tool-specific break methods to improve grammar and semantics in block definitions.

## Explanation
The discussion revolves around the use of specific tool methods like `breakWithAxe` instead of general material tags such as `wood` or `leaf`. The maintainer argues that using adjectives like `pickaxe-breakable` would better convey the relationship between blocks and tools, aligning with a more natural 'is-a' relationship. This change aims to improve the clarity and correctness of block definitions in the game.

## Related Questions
- What are the potential impacts of changing material tags to tool-specific break methods on existing block definitions?
- How does the use of adjectives like `pickaxe-breakable` improve the semantic clarity of block definitions?
- Are there any performance implications associated with this change in how blocks are broken?
- Can you provide examples of other games that use a similar approach to defining block breakability?
- What steps should be taken to ensure backwards compatibility when implementing this change?
- How does this change affect the maintainability of the codebase, particularly in terms of adding new tools or materials?

*Source: unknown | chunk_id: github_issue_1604_discussion*
