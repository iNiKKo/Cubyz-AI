# [hard/codebase_src_zon.zig] - Chunk 8

**Type:** implementation
**Keywords:** parseFromString, join, preferLeft, preferRight, activeTag, deinit, get, getChild, stringOwned, array
**Symbols:** ZonElement, ZonElement.parseFromString, ZonElement.join, ZonElement.deinit, ZonElement.get, ZonElement.getChild
**Concepts:** JSON parsing, element merging, tagged unions, memory management, test assertions

## Summary
Tests ZonElement parsing from strings and join semantics with preferLeft/right flags.

## Explanation
This chunk contains only test code that exercises the ZonElement parser by constructing elements from string literals, then joining them using .preferLeft or .preferRight. It verifies activeTag values for different types (object, float, stringOwned, array, int) and checks that nested structures are merged correctly: when preferLeft is used, left-side keys take precedence; when preferRight is used, right-side keys take precedence. The tests also validate getChild navigation across joined elements and ensure proper deinit calls to free allocated memory.

## Related Questions
- What does ZonElement.parseFromString return when given a string literal?
- How does the preferLeft flag affect key merging during join?
- How does the preferRight flag affect key merging during join?
- Which activeTag is returned for an object element parsed from a string?
- Which activeTag is returned for a float element parsed from a string?
- What happens to keys that exist in both left and right elements when joining with preferLeft?
- What happens to keys that exist in both left and right elements when joining with preferRight?
- How does getChild navigate into nested objects after join operations?
- Is ZonElement.get type-checked or does it return a union of possible types?
- Does deinit free memory allocated by parseFromString?

*Source: unknown | chunk_id: codebase_src_zon.zig_chunk_8*
