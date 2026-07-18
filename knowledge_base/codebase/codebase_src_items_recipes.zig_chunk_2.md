# [medium/codebase_src_items_recipes.zig] - Chunk 2

**Type:** implementation
**Keywords:** pattern matching, keys, testing, string manipulation, hash map
**Concepts:** pattern matching, item recipes

## Summary
This chunk contains a test function for pattern matching with keys in item recipes.

## Explanation
This chunk contains a test function for pattern matching with keys in item recipes. The test initializes a pattern from the string 'foo:{bar}/{baz}' using the `parsePattern` function and creates a map of keys where 'bar' is set to '1/2'. It then matches the input string 'foo:1/2/3' against this pattern, expecting the output to be a single key set with 'bar' mapped to '1/2' and 'baz' mapped to '3'. The test checks if these values match the expected results using `std.testing.expectEqualStrings`. After completing the test, all allocated memory is freed.

## Related Questions
- What is the purpose of the `parsePattern` function in this chunk?
- How does the test case initialize the keys for pattern matching?
- What is the expected output of the `matchWithKeys` function in this test?
- How are the results of the pattern matching checked in the test?
- What happens to the allocated memory after the test completes?
- What is the role of the `std.StringHashMap` in this chunk?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_2*
