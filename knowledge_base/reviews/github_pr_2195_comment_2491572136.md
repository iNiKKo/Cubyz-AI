# [src/server/terrain/biomes.zig] - PR #2195 review diff

**Type:** review
**Keywords:** internal error, recoverable error, logging level, descriptive message, structure model
**Symbols:** SimpleStructureModel, vtable.loadModel
**Concepts:** error handling, logging

## Summary
The reviewer suggests modifying the error message to be more descriptive and less critical.

## Explanation
The original code logs an internal error when failing to load a structure model, which might not accurately reflect the situation. The reviewer proposes changing the log level from 'err' to a more appropriate level that indicates a recoverable error. This change aims to improve clarity and avoid misleading developers about the severity of the issue.

The specific suggested change is to modify the error message from `std.log.err("Couldn't find structure model with id {s}", .{id});` to `std.log.err("Error occurred while loading structure with id '{s}'. Dropping model from biome.", .{id});`. This new message provides more context and clarity about what went wrong, helping developers understand that the issue is recoverable rather than critical.

## Related Questions
- What is the purpose of the 'vtable.loadModel' function in this context?
- How does changing the logging level affect error handling in Cubyz?
- Why is it important to have descriptive error messages in software development?
- Can you explain the difference between internal and recoverable errors in software systems?
- What are the potential consequences of not accurately representing error severity in logs?
- How might this change impact debugging and maintenance processes in Cubyz?

*Source: unknown | chunk_id: github_pr_2195_comment_2491572136*
