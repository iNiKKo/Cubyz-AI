# [medium/docs_CONTRIBUTING.md] - Chunk 0

**Type:** documentation
**Keywords:** AI/LLMs, Zig, formatter, pull requests, issues tab, Discord server, error handling, allocators, defer, errdefer
**Symbols:** zig, Cubyz-formatter, main.globalAllocator, main.stackAllocator, std.log.err, std.debug.assert, main.List, utils.NeverFailingAllocator, MemoryPool, allocator.create-destroyArena()
**Concepts:** contributing guidelines, programming in Zig, code quality, error handling, resource management, performance optimizations, style guide

## Summary
This document provides guidelines for contributing to Cubyz, covering topics such as using AI for pull requests, learning Zig, disabling Zig's formatter, selecting what to work on, writing code quality, error handling, resource management, performance optimizations, and following the style guide.

## Explanation
AI/LLM policy: don't use AI/LLMs to make pull requests -- narrow AI is trained to produce code matching its training data rather than being good at programming, likely won't follow this project's conventions, and (unlike a human) can't learn from a mistake to avoid repeating it; contributors should invest their own time and learn to code properly instead. Formatter: Cubyz uses a modified `zig fmt` (tabs, different spacing rules) -- the default Zig formatter must be disabled (e.g. in the VSCode Zig extension settings) or it will reformat every file; the correct formatter is downloadable from the Cubyz-formatter GitHub releases. Selecting work: start with the issues tab (look for the "Contributor friendly" label and milestones) or ask on Discord; start small, since a first-time contributor's code often needs more review cycles -- splitting into smaller PRs and asking direction first saves rework. Error handling: explicitly handle all errors, usually by logging via `std.log.err` with file path/error string and continuing with a sensible default, or bubbling up with `try`. `error.OutOfMemory` cannot happen with the standard allocators (`main.globalAllocator`, `main.stackAllocator`), so `catch unreachable` is the correct way to handle it there specifically -- not as a general habit. Use `std.debug.assert`/`.?`/`[]`/`unreachable`/`@panic` for programmer mistakes (should produce a stacktrace), and `std.log.err` for user-facing errors that should let the game keep running. Allocators: match the allocator to lifetime -- `main.globalArena` for global/game-lifetime data (e.g. mod registry data), `main.worldArena` for world-lifetime data (assets/addons, freed when the player exits the world), `main.stackAllocator` for local/scope-lifetime data (freed at end of scope), `main.globalAllocator` for other lifetimes. `utils.NeverFailingAllocator` is a separate allocator interface that cannot return `error.OutOfMemory`; `main.List` and other `utils` structures built on it should be preferred over standard-library data structures since they simplify the code. Resource cleanup: everything allocated must be freed, everything `init`ed must be `deinit`ed, everything locked must be unlocked -- including on error paths -- normally via `defer`/`errdefer` placed immediately after the resource is created. Keep it simple: don't generalize a thing with only one variant; use the language's syntax sugar; extract a helper function once code is duplicated; reuse existing codebase/stdlib functionality (`std.mem`, `std.meta`, `std.math`, `main.utils`); use the simplest data structure for the job (e.g. a slice instead of a List if the size is known upfront); don't make things public unless they need to be. Performance: follows Casey Muratori's non-pessimization philosophy (avoid needlessly making things worse) -- use the right/simplest data structure, keep dependencies flat/minimal, use `f32` over `f64` when the extra precision isn't needed, avoid unnecessary human-readable (zon) storage, lock mutexes in the tightest possible scope, and always measure real optimizations rather than assuming they help.

## Related Questions
- What is the recommended approach for contributing to Cubyz?
- Why should AI/LLMs not be used to create pull requests in Cubyz?
- How do you disable Zig's automatic formatter in Cubyz?
- What are Cubyz's four main allocators and their intended lifetimes?
- When is `catch unreachable` the correct way to handle error.OutOfMemory in Cubyz?
- What is utils.NeverFailingAllocator in Cubyz?
- How should error handling be implemented in Cubyz code?
- What is the importance of keeping code simple in Cubyz development?
- Whose optimization philosophy does Cubyz's CONTRIBUTING.md say to follow?
- What data-structure guidance does CONTRIBUTING.md give when a collection's size is known upfront?

*Source: unknown | chunk_id: docs_CONTRIBUTING.md_chunk_0*
