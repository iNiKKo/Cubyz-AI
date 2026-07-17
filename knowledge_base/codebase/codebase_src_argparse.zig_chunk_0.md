# [medium/codebase_src_argparse.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, structs, unions, error handling, tokenization
**Symbols:** Options, ResolveMode, Parser, Parser.parse, Parser.resolve, Parser.resolveStruct, Parser.resolveArgument, Parser.parseUnion
**Concepts:** command-line argument parsing, struct and union handling, error reporting

## Summary
The `Parser` struct provides functionality to parse command-line arguments into a specified type `T`, handling both structs and unions.

## Explanation
The `Parser` struct is designed to parse command-line arguments based on the schema defined by the generic type parameter `T`. It supports parsing of structs and unions, with error handling through an out-parameter `errorMessage`. The `parse` method initiates the parsing process. The `resolve` function determines whether to parse or autocomplete based on the `ResolveMode`. For structs, it tokenizes the input arguments and attempts to resolve each field using `resolveArgument`, which handles different types including optional fields, strings, numbers, enums, and nested structs/unions. If an argument is missing or incorrectly formatted, it appends an error message. The `parseUnion` method starts parsing a union but is incomplete in the provided snippet.

## Code Example
```zig
pub fn parse(allocator: NeverFailingAllocator, args: []const u8, errorMessage: *List(u8)) error{ParseError}!T {
	return resolve(ResolveMode.parse, allocator, args, errorMessage);
}
```

## Related Questions
- How does the `Parser` struct handle parsing of command-line arguments?
- What types are supported by the `resolveArgument` function?
- How is error information returned from the parser?
- What is the purpose of the `ResolveMode` enum?
- How does the `parseUnion` method start its execution?
- What happens if an argument is missing during parsing?

*Source: unknown | chunk_id: codebase_src_argparse.zig_chunk_0*
