# [src/server/command/worldedit/pattern.zig] - PR #1237 review diff

**Type:** review
**Keywords:** worldedit, pattern, block, chance, AliasTable, Entry, splitScalar, deinit, stackAllocator
**Symbols:** std, main, AliasTable, Block, ListUnmanaged, NeverFailingAllocator, blocks, Entry
**Concepts:** random selection, weighted probabilities

## Summary
The code introduces a new module for pattern-based world editing in Cubyz, including an `AliasTable` and an `Entry` struct to manage block patterns with weights.

## Explanation
This change adds functionality for more complex world editing patterns by allowing blocks to be selected based on specified chances. The use of `AliasTable` and the `Entry` struct suggests a design aimed at efficient random selection of blocks according to their weights. The `Entry` struct contains two fields: `block`, which is of type `Block`, and `chance`, which is a floating-point number representing the probability of selecting that block. The input string is parsed using `splitScalar` to separate different specifiers, and each specifier is further split to extract the block identifier and its associated chance. Specifically, the input string is split by commas to get individual specifiers, and each specifier is split by a percentage sign (`%`) to separate the block identifier from its weight. The reviewer notes that this is a poor architectural decision, possibly due to inefficiencies or complexity in implementation.

## Related Questions
- What is the purpose of the `AliasTable` in this module?
- How does the `Entry` struct contribute to the pattern-based world editing?
- Why is the use of `splitScalar` for parsing the input string?
- What potential issues might arise from using `NeverFailingAllocator`?
- How does the `weightedEntries` list manage memory allocation and deallocation?
- What architectural concerns are raised by the reviewer regarding this implementation?

*Source: unknown | chunk_id: github_pr_1237_comment_2010868649*
