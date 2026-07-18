# [src/blueprint.zig] - PR #1284 review diff

**Type:** review
**Keywords:** block pattern, mask syntax, tag matching, property matching, inverse match, union enum, stringToEnum
**Symbols:** Mask, Entry, Inner, Tag, Property, initFromString, match
**Concepts:** pattern matching, union types, string parsing, inverse logic

## Summary
Added a new `Mask` struct to handle block pattern matching with tags and properties.

## Explanation
The change introduces a `Mask` struct that allows for more complex block pattern matching by supporting tags, properties, and inverse logic. The `Entry` inner struct uses a union to differentiate between different types of matches (block, block tag, property). The `initFromString` function parses the specifier string to determine the type of match, while the `match` function checks if a given block satisfies the criteria defined by the mask entry. The reviewer suggests a more concise way to handle inverse logic in the `initFromString` method.

## Related Questions
- How does the `Mask` struct handle inverse logic?
- What is the purpose of the `Inner` union in the `Entry` struct?
- How does the `initFromString` function parse a specifier string?
- What are the different types of matches supported by the `Mask` struct?
- How does the `match` function determine if a block satisfies the criteria defined by the mask entry?
- What is the significance of the `separator`, `inverse`, `tag`, and `property` constants in the `Mask` struct?

*Source: unknown | chunk_id: github_pr_1284_comment_2072592455*
