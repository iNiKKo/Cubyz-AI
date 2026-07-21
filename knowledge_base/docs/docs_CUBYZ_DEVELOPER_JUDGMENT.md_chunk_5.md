# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 5

**Type:** documentation
**Keywords:** naming, unit ambiguity, name collisions, ZLS, casing conventions, snake_case, PascalCase
**Symbols:** loadWorldData, loadWorldConfig, getProperty, setProperty, TimeDelta, ZLS, Air
**Concepts:** Naming & Clarity

## Summary
Section 5 of Cubyz Developer Judgment: naming and clarity judgment patterns.

## Explanation
A name must describe what the thing actually does now, not what it used to do or partially resembles. `loadWorldData` was renamed to `loadWorldConfig` because the function only ever touched static config, never entity data (PR #2422). `getProperty` was renamed to `setProperty` when its behavior changed from read to write (PR #2891). Function/variant names get renamed the moment their behavior diverges from what the name implies.

Don't leave a numeric value's unit ambiguous. A raw `5_000_000` with no comment saying whether it's milliseconds, microseconds, or nanoseconds is flagged every time it appears (PR #2191); the preferred fix is a small typed wrapper (e.g. a `TimeDelta`-style struct) over a bare integer plus scattered manual conversion helpers.

Avoid names that collide with an existing type elsewhere in the codebase, even in an unrelated module -- specifically because Zig tooling with auto-import (ZLS) can silently import the wrong one, and that's a real, hard-to-notice bug class, not just a style concern (PR #3104).

Casing conventions are enforced deliberately: snake_case for values, PascalCase for types/files-that-represent-a-single-struct (PR #2515, #1237, #1284 -- e.g. a constant named `Air` renamed to `air` because it isn't a type).

## Related Questions
- Why was `loadWorldData` renamed to `loadWorldConfig` in Cubyz?
- Why should a numeric value's unit never be left ambiguous in Cubyz code?
- Why does Cubyz avoid names that collide with an existing type elsewhere in the codebase?
- What casing conventions does Cubyz enforce for values versus types?
- Why was a constant named `Air` renamed to `air` in Cubyz?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_5*
