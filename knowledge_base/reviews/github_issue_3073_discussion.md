# [issues/issue_3073.md] - Issue #3073 discussion

**Type:** review
**Keywords:** argument parser, commands migration, parseCoordinates, Target, clear, gamemode, help, invite, kick, kill, spawn, tickspeed, tp, perm, undo
**Symbols:** parseCoordinates, Target, clear, gamemode, help, invite, kick, kill, spawn, tickspeed, tp, perm, undo, redo, pos1, pos2, deselect, copy, paste, blueprint, mask
**Concepts:** Argument Parsing, Command Migration, Maintainability, Collaboration

## Summary
The issue discusses updating various commands and helper functions to use a new argument parser introduced in #1425. It lists specific commands and helpers that need migration, along with some that are blocked by other issues.

## Explanation
The issue discusses updating various commands and helper functions to use a new argument parser introduced in #1425. The review lists specific commands and helpers that need migration, including `parseCoordinates`, `Target`, `clear`, `gamemode`, `help`, `invite`, `kick`, `kill`, `spawn`, `tickspeed`, `tp`, `perm`, `undo`, `redo`, `pos1`, `pos2`, `deselect`, `copy`, `paste`, and `blueprint`. Additionally, it mentions that the commands `particles` (blocked by #3102), `set`, and `rotate` are pending due to dependencies. The review also notes that certain functions like `parseAxis`, `parseCoordinates`, and `parsePlayerIndexAndIncreaseRefCount` need removal after specific migrations are completed. Furthermore, it states that commands should directly get parameters from type `Args` instead of using `args: []const u8`. The discussion section addresses potential collaboration on further updates, particularly for world edit commands.

## Related Questions
- What is the status of the 'particles' command migration?
- Which commands are still pending migration and why?
- Who is responsible for updating the world edit commands?
- How does the new parser improve command handling in Cubyz?
- Are there any potential performance implications from this migration?
- What changes need to be made after all migrations are complete?

*Source: unknown | chunk_id: github_issue_3073_discussion*
