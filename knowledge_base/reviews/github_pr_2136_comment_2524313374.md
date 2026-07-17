# [src/server/world.zig] - Chunk 2524313374

**Type:** review
**Keywords:** loadWorldSeed, WorldSettings.init, parseSeed, chooseSeed, random seed, settings struct, deterministic, refactor, architectural change
**Symbols:** loadWorldSeed, WorldSettings.init, parseSeed, chooseSeed
**Concepts:** seed initialization, settings struct pattern, deterministic seeding, code refactoring, architectural clarity

## Summary
The reviewer corrects a misunderstanding about parsing: they want to replace `loadWorldSeed` with a call to `WorldSettings.init` to load full settings, and explicitly request removal of any code that initializes the seed randomly.

## Explanation
Architecturally, the change shifts world initialization from a fragmented approach (loading only the seed via `loadWorldSeed`) to a unified settings struct (`WorldSettings`). The reviewer’s concern is that the current implementation mixes parsing and generation in `parseSeed`, which should be renamed to reflect its dual role. By removing random seed initialization, the codebase ensures deterministic seeding behavior consistent with the new settings-driven approach, preventing regressions where seeds might unexpectedly change or be overwritten by random values.

## Related Questions
- What is the current implementation of `loadWorldSeed` in world.zig?
- How does `WorldSettings.init` load settings from a file?
- Where in the codebase is random seed initialization performed?
- Is there any existing usage of `parseSeed` that needs renaming to `chooseSeed`?
- What fields are present in the `WorldSettings` struct after init?
- Does removing random seed init affect backward compatibility with saved worlds?
- Are there tests covering deterministic seeding behavior?
- How does the new settings-driven approach handle missing or corrupted seed files?
- What is the expected signature of `WorldSettings.init`?
- Is there any documentation explaining why `parseSeed` was named that way?

*Source: unknown | chunk_id: github_pr_2136_comment_2524313374*
