# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk bug_skycolor

**Type:** reference
**Keywords:** skyColor, fogColor, u32, vector, format-mismatch, addon-creator-bugs, biome-color
**Symbols:** getHexColorAsRGBVector, u32ToVec3, ZonElement.get
**Concepts:** engine-vs-website-mismatch, silent-fallback, biome-validation

## Summary
Documented likely bug: the Addon Creator website exports biome sky/fog color in a different data
format than the engine actually reads, so a custom sky color set on the website may silently fail
to show up in-game.

## Explanation
The website exports `.skyColor`/`.fogColor` as a 3-component float vector (`.{r, g, b}`, values
0-1) via `getHexColorAsRGBVector()`. The engine reads them with `zon.get(u32, "fogColor")` /
`zon.get(u32, "skyColor")` -- a packed integer (the fallback default is literally `0xffbfe2ff`),
then converts to a vector internally via a separate `u32ToVec3()` helper. A vector literal read
through a `u32` getter is very likely to fail to parse and silently fall back to the default
color rather than crash. This is a format mismatch (vector vs. packed u32 integer), not a
field-name mismatch -- inferred from the type mismatch and the existence of the u32-to-vec3
conversion helper, not fully confirmed against a real in-game test.

Precedence rule: where the website and the engine disagree on field formats, the engine is the
source of truth -- when hand-writing addon files, use the engine-expected packed `u32` color
format even where the website's own export currently produces a vector instead.

## Related Questions
- Why might a biome's custom sky color not show up in-game even though it was set in the Addon Creator?
- What format does the engine actually expect for a biome's fogColor/skyColor fields?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_bug_skycolor*
