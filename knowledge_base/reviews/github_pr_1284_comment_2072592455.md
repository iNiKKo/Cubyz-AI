# [src/blueprint.zig] - PR #1284 review diff

**Type:** review
**Keywords:** block pattern, mask syntax, tag matching, property matching, inverse match, union enum, stringToEnum
**Symbols:** Mask, Entry, Inner, Tag, Property, initFromString, match
**Concepts:** pattern matching, union types, string parsing, inverse logic

## Summary
Added a new `Mask` struct to handle block pattern matching with tags and properties.

## Explanation
The change introduces a `Mask` struct that allows for more complex block pattern matching by supporting tags, properties, and inverse logic. The `Entry` inner struct uses a union to differentiate between different types of matches (block, block tag, property). The `initFromString` function parses the specifier string to determine the type of match, while the `match` function checks if a given block satisfies the criteria defined by the mask entry. The reviewer suggests a more concise way to handle inverse logic in the `initFromString` method.

The `Mask` struct includes several constants:
- `separator`: A comma (`,`) used to separate entries in the mask.
- `inverse`: An exclamation mark (`!`) used to indicate an inverse match.
- `tag`: A dollar sign (`$`) used to specify a block tag.
- `property`: An at symbol (`@`) used to specify a property.

The `Entry` struct contains an inner union that can be one of three types:
1. **block**: Represents a specific block type with optional data.
2. **blockTag**: Represents a block tag, which is matched against the block's tags.
3. **property**: Represents a property, such as transparency or collision behavior.

The `initFromString` function parses the specifier string to determine the type of match. It supports three types of specifiers:
1. **Block Specifier**: A string representing a block type and optional data (e.g., `stone`, `dirt:2`).
2. **Tag Specifier**: A string starting with `$` followed by a tag name (e.g., `$ore`).
3. **Property Specifier**: A string starting with `@` followed by a property name (e.g., `@transparent`).

The `match` function checks if a given block satisfies the criteria defined by the mask entry. It supports three types of matches:
1. **Block Match**: Checks if the block type and data match the specified values.
2. **Tag Match**: Checks if any of the block's tags match the desired tag.
3. **Property Match**: Checks if the block has the specified property (e.g., `transparent`, `collide`).

The reviewer suggests a more concise way to handle inverse logic in the `initFromString` method by using a single line to determine whether the specifier is an inverse match and then parsing the appropriate substring.

## Related Questions
- How does the `Mask` struct handle inverse logic?
- What is the purpose of the `Inner` union in the `Entry` struct?
- How does the `initFromString` function parse a specifier string?
- What are the different types of matches supported by the `Mask` struct?
- How does the `match` function determine if a block satisfies the criteria defined by the mask entry?
- What is the significance of the `separator`, `inverse`, `tag`, and `property` constants in the `Mask` struct?

*Source: unknown | chunk_id: github_pr_1284_comment_2072592455*
