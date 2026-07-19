# [src/assets.zig] - PR #1229 review diff

**Type:** review
**Keywords:** asset string IDs, dots in file extensions, whitespace in IDs, regex constraint, block names, parameter parsing, case sensitivity, Windows to Unix transfer
**Symbols:** createAssetStringID, NeverFailingAllocator
**Concepts:** file extension conventions, parameter parsing, case sensitivity, operating system compatibility

## Summary
The review discusses the creation of asset string IDs and raises concerns about using dots in file extensions and allowing whitespace in IDs.

## Explanation
**Explanation**
The reviewer is concerned about the use of dots in file extensions, suggesting that they are arbitrary separators and proposing a regex constraint for block names to include only alphanumeric characters, hyphens, and underscores (`[a-zA-Z0-9-_]+`). The reviewer also points out potential issues with case sensitivity in block IDs when transferring between Windows and Unix systems. For example, `addon:Stone` and `addon:stone` behave differently on these operating systems. Allowing whitespace in IDs complicates parameter parsing, as commands must account for this during parsing. The proposed regex constraint simplifies reasoning about how block names should be parsed.

## Related Questions
- What are the potential issues with using dots as separators in file extensions?
- How does allowing whitespace in IDs affect parameter parsing?
- Why is it suggested to constrain block names to a specific regex pattern?
- What are the implications of case sensitivity in block IDs for cross-platform compatibility?
- Can you provide examples of how to handle case sensitivity issues when transferring files between Windows and Unix systems?
- How does the proposed regex constraint simplify reasoning about ID parsing?

*Source: unknown | chunk_id: github_pr_1229_comment_2009152223*
