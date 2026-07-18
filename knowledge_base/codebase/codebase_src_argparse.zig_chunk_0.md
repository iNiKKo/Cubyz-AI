# [medium/codebase_src_argparse.zig] - Chunk 0

**Type:** api
**Keywords:** struct, enum, command name, parse mode, autocomplete mode
**Symbols:** Options, Options.commandName, ResolveMode
**Concepts:** command-line arguments, argument parsing

## Summary
Defines the structure for command-line argument parsing options and resolve modes.

## Explanation
This chunk defines a public `Options` struct with a field `commandName` of type `[]const u8`, which is used to store the name of the command being parsed. It also declares an enum `ResolveMode` with two variants: `parse` and `autocomplete`. These definitions are part of the argument parsing logic within the Cubyz engine.

## Related Questions
- What is the purpose of the `Options` struct?
- How many variants are in the `ResolveMode` enum?
- What type is the `commandName` field in the `Options` struct?
- Where is the `NeverFailingAllocator` imported from?
- What does the `List` type represent in this context?
- Which module provides utility functions used here?

*Source: unknown | chunk_id: codebase_src_argparse.zig_chunk_0*
