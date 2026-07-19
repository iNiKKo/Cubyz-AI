# [issues/issue_1528.md] - Issue #1528 discussion

**Type:** review
**Keywords:** Comptime Modding Framework, moddable interfaces, registry, launcher, documentation, trivially moddable, non-trivially moddable, git
**Concepts:** modding framework, registry system, automatic loading, trusted mods

## Summary
The issue discusses the development of a Comptime Modding Framework for Cubyz, including automatic loading of moddable interfaces, creation of a registry for trusted mods, and documentation on modding processes.

## Explanation
The issue discusses the development of a Comptime Modding Framework for Cubyz. The main points include automatically loading lists of all moddable interfaces from a common (`mods`) folder, creating a registry to manage trusted mods with metadata such as name, author, link, and secure hash of the source code, and developing a launcher that downloads and compiles mods from the registry when entering the world or joining a server (requires #1483). The maintainers highlight the distinction between trivially moddable systems (like rotations, block entities, UI) and non-trivially moddable systems (like items/tools, rendering), suggesting that non-trivial changes should be tracked separately. There is also discussion about whether to create a registry system from scratch or base it on existing protocols like git.

## Related Questions
- What are the main features of the Comptime Modding Framework?
- How will the registry system manage trusted mods with name, author, link, and secure hash?
- What is the process for automatically loading moddable interfaces from a common folder?
- Should the registry be created from scratch or based on existing protocols like git?
- Which systems are considered trivially moddable and which are non-trivial?
- What documentation will be provided for modding in Cubyz?

*Source: unknown | chunk_id: github_issue_1528_discussion*
