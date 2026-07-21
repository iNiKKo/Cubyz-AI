# [src/server/blocks/migrations.zig] - PR #1125 getOrPut rationale

**Type:** review
**Keywords:** getOrPut, StringHashMap, contains check, insert, atomic, redundant lookup, migrations.zig
**Symbols:** collection.getOrPut, blockMigrations
**Concepts:** memory management, hash map usage, code review judgment

## Summary
Why a Cubyz reviewer suggested using `std.StringHashMap`'s `getOrPut` instead of a separate contains-check plus insert, in the block-migrations registration code (PR #1125).

## Explanation
`migrations.zig` registers block migrations into a `blockMigrations` string hash map. The original code performed a separate existence check (a `contains`-style lookup) before inserting a new entry -- two distinct hash map operations for what is logically one piece of work. The reviewer suggested replacing this with `getOrPut`, which atomically retrieves the entry if it already exists or inserts a new one if it doesn't, in a single hash map operation instead of two separate lookups. This reduces redundant memory accesses and code complexity: instead of hashing the key once to check `contains` and hashing it again to `insert`, `getOrPut` does the check-and-insert as one combined operation.

## Related Questions
- Why might a Cubyz reviewer prefer std.StringHashMap's getOrPut over a separate contains-check plus insert?
- What did PR #1125's migrations.zig code look like before switching to getOrPut?
- Why does getOrPut reduce redundant memory accesses compared to contains-then-insert?

*Source: unknown | chunk_id: github_pr_1125_getorput_rationale*
