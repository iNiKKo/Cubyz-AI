# [hard/codebase_src_blueprint.zig] - Chunk 4

**Type:** implementation
**Keywords:** initFromString, deinit, clone, match, parseBlockLike, OrList, AndList, Entry, Inner, error.MissingExpression
**Symbols:** Mask, Mask.initFromString, Mask.deinit, Mask.clone, Mask.match, parseBlockLike, Test, AndList, OrList, Entry, Inner
**Concepts:** OR-of-AND expressions, mask parsing, block matching, error handling, unit testing

## Summary
This chunk defines the Mask struct and its parsing logic, including initFromString for building OR/AND expression trees from string literals, deinit for cleanup, clone for copying, match for evaluating blocks against an OR-of-ANDs rule set, parseBlockLike helper function with test stubs, and multiple unit tests covering valid masks, empty/half-or/half-and error cases.

## Explanation
The Mask struct is declared as a public type containing entries (an OrList of AndLists). It provides initFromString which splits the source string by 'or_' to get OR expressions, then each sub-expression is split by 'and_' to build AndStorage lists; it asserts non-empty results and returns error.MissingExpression on empty tokens. deinit iterates over entries and calls their deinit methods. clone creates a new Mask with allocated capacity copies of the OrList and inner AndLists using appendAssumeCapacity, deferring insertion into orListCopy before returning. match evaluates an OR-of-ANDs: it loops over each AND list (andedExpressions), inside which it loops over entries; if any entry does not match the block it breaks to false, otherwise after all entries pass it returns true for that AND list; if no AND list matches it returns false. The parseBlockLike function is a helper that either delegates to Test.parseBlockLikeTest when running in test mode or calls main.blocks.getBlockById and main.blocks.getBlockData to construct an Inner enum variant with block type and optional data, returning error.IdParsingFailed on missing ID or error.DataParsingFailed on missing data. The Test struct holds a mutable pointer to the active parseBlockLike implementation (defaultParseBlockLike is unreachable) and defines several test functions: defaultParseBlockLike returns .{.blockType = 1} for any input; @

## Related Questions
- How does Mask.initFromString handle empty tokens and what error is returned?
- What is the purpose of the defer in Mask.clone and how does it relate to orListCopy?
- In Mask.match, under which condition does an AND list return false versus true?
- When parseBlockLike runs outside tests, how are block IDs resolved and what errors can occur?
- Why is defaultParseBlockLike marked unreachable in the Test struct?
- What enum variants does Inner have and when is each used by parseBlockLike?
- How do AndList and OrList relate to Mask.entries and what types are they?
- Does Mask.clone allocate new memory or reuse existing capacity, and how is that expressed?
- What happens if initFromString receives a string with only 'or_' separators and no entries?
- Are there any assertions in this chunk and where do they trigger errors?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_4*
