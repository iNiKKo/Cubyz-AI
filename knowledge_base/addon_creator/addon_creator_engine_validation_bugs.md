# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk bug_spawn

**Type:** reference
**Keywords:** isValidPlayerSpawn, validPlayerSpawn, field-name-mismatch, addon-creator-bugs, biome-spawn
**Symbols:** Biome.init, saveBiomeToProject, ZonElement.get
**Concepts:** engine-vs-website-mismatch, silent-fallback, biome-validation

## Summary
Documented real bug: the Addon Creator website exports the biome "valid player spawn" checkbox
under a field name the engine doesn't actually read, so the setting silently never takes effect.

## Explanation
The website's `saveBiomeToProject` (`app-save.js`) exports the spawn checkbox as
`.isValidPlayerSpawn`. The engine's `Biome.init()` (`server/terrain/biomes.zig` line 297) reads
`zon.get(bool, "validPlayerSpawn")` -- a different field name (no "is" prefix). Because
`ZonElement.get` returns the `orelse` default (`false`) when a field isn't present, a biome
exported from the website with "spawn" checked will still load with `validPlayerSpawn = false`
in-game. The fix would be renaming the exported field in `app-save.js` to `validPlayerSpawn`, or
hand-editing the exported file to use the correct engine field name.

Precedence rule: where the website and the engine disagree on field names, defaults, or formats,
the engine is the source of truth, not the website -- the website is a convenience tool and can
have bugs. When hand-writing addon files, use the engine-expected field name (`.validPlayerSpawn`)
even where it differs from what the website currently produces.

## Related Questions
- What's the known bug with the 'valid player spawn' checkbox in the Addon Creator?
- Why does a biome exported from the website sometimes not actually count as a valid player spawn?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_bug_spawn*
