# [hard/codebase_src_blueprint.zig] - Chunk 5

**Type:** api
**Keywords:** Mask.initFromString, match method, voidType field, Block struct, std.testing.expectError, defer cleanup, error.MissingExpression, assert invariant, test isolation
**Symbols:** registerVoidBlock, getVoidBlock
**Concepts:** mask parsing, block matching, error handling, test isolation, public API surface

## Summary
Test suite for Mask parsing and matching logic, plus public API functions to register and retrieve a void block.

## Explanation
The chunk contains nine test cases that validate Mask.initFromString under various error conditions (empty string, trailing '|', leading '&', trailing '&', leading '|') expecting error.MissingExpression, and three successful match tests covering inverse (!), exact data matching, and OR-type matching. Each test temporarily replaces Test.parseBlockLikeTest with a mock parser returning null or specific block types to simulate parsing failures without affecting the real parser state; after each test it restores the original value via defer. The mask.match method is exercised against Block structs with explicit .typ and .data fields, asserting expected boolean results. Two public functions are declared: registerVoidBlock takes a Block argument, stores its typ into the global voidType field, and asserts that voidType != 0; getVoidBlock returns a new Block constructed from the current voidType value (with data set to 0). Both functions use std.debug.assert for invariant checking. No other declarations or logic appear in this chunk.

## Related Questions
- What error is returned when Mask.initFromString receives an empty string?
- How does the test suite ensure that parsing failures do not affect subsequent tests?
- Which public functions are exposed by this chunk for block registration and retrieval?
- What invariant is checked inside registerVoidBlock after storing a block's type?
- How does mask.match behave when given an inverse pattern like '!addon:dummy'?
- What Block fields are used in the match assertions to verify type and data equality?
- Why is std.debug.assert used instead of returning an error in these public functions?
- Does this chunk define any new types or only use existing ones from other modules?
- How many test cases cover negative (error) scenarios versus positive (success) scenarios?
- What global variable does registerVoidBlock modify to store the void block type?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_5*
