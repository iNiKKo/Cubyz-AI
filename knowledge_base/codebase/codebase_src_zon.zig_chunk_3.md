# [hard/codebase_src_zon.zig] - Chunk 3

**Type:** serialization
**Keywords:** serialization, JSON-like output, visual formatting, escaping identifiers, object iteration, array rendering, hex number parsing, whitespace skipping, comment handling
**Symbols:** recurseToString, toString, toStringEfficient, parseFromString, skipWhitespaceAndComments, Parser, whitespaces, parseNumber
**Concepts:** serialization, JSON-like output, visual formatting, escaping identifiers, object iteration, array rendering, hex number parsing, whitespace skipping, comment handling

## Summary
This chunk implements the Zon serialization format, providing functions to convert elements to JSON-like strings with optional visual formatting and efficient compact output, as well as parsing logic for whitespace skipping and number tokenization.

## Explanation
The chunk defines a recursive function recurseToString that handles multiple ZonElement variants: list (appends 'true'/'false'/'null'), string (uses enum literals if the value is a valid identifier name, otherwise escapes it), array (iterates items with optional newlines and tab indentation via writeTabs), and object (iterates key-value pairs using an iterator, handling identifier-name keys vs escaped quoted keys). It exposes two public conversion functions: toString which calls recurseToString with visualCharacters=true to produce human-readable output, and toStringEfficient which adds a custom prefix before calling recurseToString with visualCharacters=false for compact serialization. A parseFromString function is provided that first skips whitespace and comments via skipWhitespaceAndComments (which iterates over a whitespaces array of Unicode space characters and handles line comments starting with '//' by advancing past them) then delegates to Parser.parseElement. The chunk also defines the Parser struct containing a const whitespaces array listing all Unicode whitespace code points, and begins implementing parseNumber which handles optional sign ('+' or '-'), detects hexadecimal numbers (starting with '0x') and parses digit-by-digit using base-16 arithmetic, returning an int variant ZonElement.

## Related Questions
- How does recurseToString handle a list element when visualCharacters is true versus false?
- What condition determines whether a string value is emitted as an enum literal or escaped in JSON format?
- Describe the iteration logic used for object serialization and how keys are treated differently based on identifier validity.
- Which Unicode code points are recognized as whitespace by skipWhitespaceAndComments and how does it advance past them?
- How does parseNumber detect a hexadecimal integer and what arithmetic is performed to build its value?
- What role does the prefix argument play in toStringEfficient and why is visualCharacters set to false there?
- Explain the purpose of writeTabs in the array and object branches and how it interacts with tabs parameter.
- How does parseFromString combine whitespace skipping with element parsing before returning a ZonElement?

*Source: unknown | chunk_id: codebase_src_zon.zig_chunk_3*
