# [src/argparse.zig, src/server/command/permission/perm.zig] - argparse migration rationale

**Type:** review
**Keywords:** argparse, manual string-splitting, brittle, Helper struct, splitScalar, exact spacing, command parsing
**Symbols:** argparse.Parser, std.mem.splitScalar, Helper.init, Helper.deinit
**Concepts:** command-line/command argument parsing, code review judgment

## Summary
Why Cubyz maintainers migrated server commands (e.g. `/perm`) from manual string-splitting argument parsing to the generic `argparse.Parser` utility.

## Explanation
Before `src/argparse.zig` (introduced PR #1425) existed, individual server commands parsed their own arguments by hand with `std.mem.splitScalar(u8, args, ' ')`, manually walking the resulting iterator and calling `std.ascii.eqlIgnoreCase` to compare each token against expected subcommand names (e.g. "add"/"remove"). This approach was brittle: it assumed exact single-space spacing between arguments (no tolerance for extra whitespace), required a repeated string comparison for every possible subcommand token, and needed a custom per-command `Helper` struct that had to be manually initialized via `Helper.init(source, &split)` and explicitly cleaned up with a matching `deinit()` -- one more manual resource-management step a contributor could get wrong.

The `/perm` command's migration (PR #3112) is a concrete example: the old `execute()` function's manual `split`/`Helper.init`/`deinit` dance was replaced with a declarative `Args` union type describing the command's valid argument shapes (e.g. `/perm <action> <list> <playerIndex> <permissionPath>` vs. `/perm <playerIndex> <permissionPath>`), parsed generically via `argparse.Parser(Args, .{.commandName = "/perm"}).parse(...)`. The generic parser handles tokenization, per-field type parsing, and error-message construction itself, so individual commands no longer duplicate that brittle logic.

## Related Questions
- Why might a Cubyz reviewer suggest replacing manual string-splitting argument parsing with argparse?
- What problems did the old manual `std.mem.splitScalar`-based command parsing have in Cubyz?
- What did the `/perm` command's argument parsing look like before and after PR #3112?
- What is the `Helper` struct pattern that argparse.Parser replaced in Cubyz's server commands?

*Source: unknown | chunk_id: github_pr_argparse_migration_rationale*
