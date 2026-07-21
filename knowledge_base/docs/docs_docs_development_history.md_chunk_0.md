# [easy/docs_docs_development_history.md] - Chunk 0

**Type:** documentation
**Keywords:** Cubyz, Development History, Inventory, Terrain Generation, Crafting System, Release Versions, Commit IDs
**Symbols:** Cubyz, Inventory, Terrain Generation, Crafting System, Workbench, Multicolored Lighting System, Block Rotation System, Addons, 0.3.0, 0.2.0, 0.1.1, 0.1.0, 0.0.1, 0.0.0
**Concepts:** Early History, Cubyz Naming Change, Early Development Builds, Great Zig Rewrite, Cubyz Release Versions and Commits

## Summary
Cubyz was created by zenith391 and ZaUserA on August 22 2018 as "Cubz", renamed "Cubyz" on March 17 2019, later rewritten from Java to Zig, and currently maintained by QuantumDeveloper (also known as IntegratedQuantum). Version 0.0.0 released October 5 2025.

## Explanation
Early History: on August 22 2018, zenith391 and ZaUserA created "Cubz" (not a typo -- that was the original name). zenith391 and ZaUserA lost interest sometime in 2020; the project is currently maintained mainly by QuantumDeveloper (also referred to as IntegratedQuantum), with others also contributing. Naming: on March 17 2019 (6:00PM GMT, Sunday), zenith391 suggested renaming the project to "Cubyz" ("they will merge under the new name Cubyz"), and it stuck. Early Development Builds: sometime in 2019, QuantumDeveloper found the Cubz project on GitHub, joined, and implemented Inventory, Terrain Generation, the Crafting System (originally a 2x2 grid like Minecraft), the Workbench (inspired by the Minecraft mod Tinkers Construct), a Multicolored Lighting System, the Block Rotation System, and the Addons system. The Great Zig Rewrite: an earlier attempt to rewrite Cubyz in C++ and Vulkan was abandoned. On November 8 2022, QuantumDeveloper posted a video explaining why Cubyz should be re-coded -- the primary reason was Java's garbage collector: when the upper memory limit was hit, Java would try to free memory, freezing the game for a noticeable time; lag spikes were not his only complaint with Java. Before choosing Zig, QuantumDeveloper considered C++20 (rejected: its new "modules" feature wasn't supported by major compilers like GCC or Clang at the time) and Rust (rejected: found its borrow checker "kind of annoying"). zenith391 then showed QuantumDeveloper the Zig language; the feature that most impressed QuantumDeveloper was Zig's out-of-the-box cross-compilation support, letting him build for Windows and test it under Wine without dealing with Windows-specific build issues. Cubyz 0.0.0: released October 5 2025. After 0.0.0: Cubyz remains in alpha, under active development, with stable releases roughly every three months; no 1.0.0 date is set yet.

## Release Versions
Cubyz releases stable versions roughly every three months, each tagged to a specific commit on GitHub (PixelGuys/Cubyz):
- **0.3.0** (June 30, 2026) -- commit `5c394f953186c662b8c4f6be73bbc61383530212`, "Remove useless alignment parameter from graphics.draw.text/print" (by IntegratedQuantum).
- **0.2.0** (April 2, 2026) -- commit `c4649b1671b458450ed519427143e637846282c3`, "We never unmaped Inventories on Client Side" (#2803).
- **0.1.1** (January 1, 2026) -- commit `29aae45d94e0a2d5838d9a700b03ca57a9bdbba8`, fixes world creation writing `allowCheats`/`defaultGamemode` incorrectly, with a migration path for existing worlds.
- **0.1.0** (December 31, 2025) -- commit `6ce7e0039aad287093688e2ae75d8fcb9fd604a6`, "Fix surface terrain in LOD chunks" (corrects an erosion slope calculation error and an underground chunk-filling issue at chunk boundaries).
- **0.0.1** (November 8, 2025) -- commit `700058f94418592ecf7cdcf6e70faae30a89b15c`, "Stop panic when blueprint doesn't exist for biome" (#2195).
- **0.0.0** (October 5, 2025) -- commit `03db2eb644523c5a08fc12e82459d50498b4fc24`, updated the default background image (credited to @ikabod-kee, issue #1814).

## Related Questions
- What is the initial name of Cubyz?
- When was Cubyz created, and by whom?
- When was the project renamed from Cubz to Cubyz, and who suggested it?
- Who currently maintains Cubyz?
- What alternative name is the current Cubyz maintainer also known by?
- What features were implemented in early development?
- Why was Cubyz rewritten from Java to Zig?
- What alternative languages did the Cubyz maintainer consider before choosing Zig for the rewrite?
- What feature of Zig most impressed the maintainer during the rewrite decision?
- When was Cubyz 0.0.0 released?
- Where can I find the release announcement for Cubyz 0.0.0?
- How did QuantumDeveloper explain why he wanted to re-code Cubyz?
- Where can I find the video explaining why Cubyz should be re-coded?
- What development stage is Cubyz currently in, and how often are stable releases?
- What is the commit ID and commit message for the Cubyz 0.3.0 release?
- What changed in each Cubyz release from 0.0.0 to 0.3.0?

*Source: unknown | chunk_id: docs_docs_development_history.md_chunk_0*
