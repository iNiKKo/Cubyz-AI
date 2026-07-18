# [medium/codebase_src_items_recipes.zig] - Chunk 2

**Type:** implementation
**Keywords:** pattern matching, keys, testing, string manipulation, hash map
**Concepts:** pattern matching, item recipes

## Summary
This chunk contains a test function for pattern matching with keys in item recipes.

## Explanation
The chunk defines a test case that uses the `parsePattern` and `matchWithKeys` functions to match a string against a pattern containing keys. It initializes a pattern from a string, creates a map of keys, matches the input string against the pattern, and checks if the resulting keys match the expected values.

## Related Questions
- What is the purpose of the `parsePattern` function in this chunk?
- How does the test case initialize the keys for pattern matching?
- What is the expected output of the `matchWithKeys` function in this test?
- How are the results of the pattern matching checked in the test?
- What happens to the allocated memory after the test completes?
- What is the role of the `std.StringHashMap` in this chunk?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_2*
