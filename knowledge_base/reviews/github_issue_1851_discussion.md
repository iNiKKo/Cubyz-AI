# [issues/issue_1851.md] - Issue #1851 discussion

**Type:** review
**Keywords:** gitignore, whitelist, blacklist, IDE files, contribution guidelines, global .gitignore, Zig philosophy
**Concepts:** version control, gitignore, whitelist strategy, global gitignore

## Summary
Discussion on implementing a whitelist-based .gitignore strategy for Cubyz, with concerns about ignoring all newly created files and suggestions to follow Zig's approach of using global .gitignore for IDE-specific files.

## Explanation
Discussion on implementing a whitelist-based .gitignore strategy for Cubyz, with concerns about ignoring all newly created files and suggestions to follow Zig's approach of using a global .gitignore for IDE-specific files. The maintainer expresses reservations about the proposal, suggesting that it might lead to unintended consequences such as ignoring necessary files. The user proposes aligning with Zig's philosophy by managing IDE-specific files through a global .gitignore file (https://github.com/ziglang/zig/blob/master/.gitignore) and suggests documenting this approach in the contribution guidelines or as a comment within the .gitignore file.

## Related Questions
- What are the potential drawbacks of using a whitelist-based .gitignore strategy?
- How does Zig's approach to managing IDE-specific files differ from Cubyz's current practices?
- Can you provide examples of other projects that use a similar whitelist-based .gitignore strategy?
- What are the benefits and trade-offs of using a global .gitignore for IDE files?
- How can we ensure that contributors understand and follow the guidelines for managing IDE-specific files in Cubyz?
- What impact might ignoring all newly created files have on version control practices?

*Source: unknown | chunk_id: github_issue_1851_discussion*
