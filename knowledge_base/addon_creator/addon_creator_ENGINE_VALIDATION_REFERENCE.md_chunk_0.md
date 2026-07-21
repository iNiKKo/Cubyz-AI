# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 0

**Type:** documentation
**Keywords:** precedence rule, isValidPlayerSpawn bug, skyColor bug, fogColor bug, u32ToVec3, getHexColorAsRGBVector
**Symbols:** validPlayerSpawn, isValidPlayerSpawn, zon.get, u32ToVec3

## Summary
Intro to Cubyz's engine-side addon validation reference: the precedence rule between website and engine, and two likely real bugs found in the website's export logic.

## Explanation
This is the companion to FIELD_REFERENCE.md. That document covers what the Addon Creator *website* exports; this one covers what the *game engine* actually reads back when loading a `.zig.zon` addon file, compiled by reading the real Zig loader functions in full: `blocks.zig:register()`, `items.zig:BaseItem.init()`/`Material.init()`/`registerProceduralItem()`, `items/recipes.zig:parseRecipe()`, `server/terrain/biomes.zig:Biome.init()`, `entityModel.zig:EntityModel.init()`, and `particles.zig:register()`/`EmitterProperties`/`SpawnShape`/`DirectionMode`.

**Precedence rule**: where this reference and FIELD_REFERENCE.md disagree (field names, defaults, formats), the engine is the source of truth, not the website -- the website is a convenience tool and can have bugs. When generating new example addon code, use the engine-expected field name/format even where it differs from what the website currently produces. Only describe the website's actual (buggy) behavior when specifically explaining why something exported from the website isn't working.

**Bug 1, biome player-spawn flag field name mismatch**: the website's `saveBiomeToProject` (`app-save.js`) exports the spawn checkbox as `.isValidPlayerSpawn`. The engine's `Biome.init()` (`server/terrain/biomes.zig` line 297) reads `zon.get(bool, "validPlayerSpawn")` -- a different field name. Because `ZonElement.get` returns the `orelse` default (`false`) when a field isn't present, a biome exported from the website with "spawn" checked will still load with `isValidPlayerSpawn = false` in-game.

**Bug 2, biome sky/fog color format mismatch (likely, not fully confirmed)**: the website exports `.skyColor`/`.fogColor` as a 3-component float vector (`.{r, g, b}`, values 0-1) via `getHexColorAsRGBVector()`. The engine reads them with `zon.get(u32, "fogColor")` / `zon.get(u32, "skyColor")` -- a packed integer (e.g. the fallback default is literally `0xffbfe2ff`), then converts to a vector internally via a separate `u32ToVec3()` helper. A vector literal being read through a `u32` getter looks very likely to fail to parse and silently fall back to the default color rather than crash.

## Related Questions
- What's the overall precedence rule when Cubyz's Addon Creator website and the game engine disagree on a field name or default?
- What is the known bug with the 'valid player spawn' checkbox in the Addon Creator?
- What's the likely bug with Cubyz's biome sky/fog color export?
- What six Zig loader functions does this engine validation reference document?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_0*
