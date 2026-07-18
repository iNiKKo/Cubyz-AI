# [medium/docs_CONTRIBUTING.md] - Chunk 2

**Type:** documentation
**Keywords:** style guide, naming conventions, camelCase, PascalCase, snake_case, line limit, comments, imports, magic constants, const correctness, pull request size
**Concepts:** contributing guidelines, style guide, pull request scope

## Summary
The specific style-guide rules from Cubyz's CONTRIBUTING.md: naming conventions, line limits, comment policy, file-size guidance, and pull request size limit.

## Explanation
Naming conventions: camelCase for variables, constants, and functions (no ALL-CAPS constants); CapitalCamelCase (PascalCase) for types; snake_case for files and namespaces; abbreviations count as one word (e.g. `zon`/`ZonElement`, not `ZON`/`ZONElement`). Line limit: there is no fixed line limit -- if a line needs ~200 characters, consider splitting it or adding well-named helper variables instead. Comments: don't write comments unless something non-obvious needs explaining; prefer readable code with descriptive names over comments, since comments naturally degrade as surrounding code changes; when a comment is written, it should explain the why, not the what or how. Imports: import aliasing is fine, but don't alias functions (so a bare function name can be assumed local); imports/aliases go at the top of the file, and an alias should keep the original name (e.g. never alias `main.stackAllocator` to `allocator`). File organization: don't use files as structs without good reason; split unrelated things apart and keep interacting things together; the sweet-spot file size is very roughly 1000 lines; interface implementations (GuiWindow, *Generator, Command) go in separate files in one directory. Magic constants: all non-trivial constants should be named, especially physical/mathematical ones. Const correctness: prefer `const` by default, `var` only as a fallback. Pull request size: a good PR should be no more than 200 lines -- the maintainer may refuse to review larger ones; don't bundle multiple unrelated changes (including introducing non-trivial helpers or refactors) into one PR, since a mistake in one part forces a review cycle on the whole thing and increases merge-conflict risk as other work lands in parallel.

## Related Questions
- What naming convention does Cubyz use for variables and functions?
- What naming convention does Cubyz use for types?
- What naming convention does Cubyz use for files and namespaces?
- Does Cubyz enforce a maximum line length for code?
- What is Cubyz's policy on writing code comments?
- What's the recommended sweet-spot file size (in lines) for a Cubyz source file?
- What's the maximum recommended size for a Cubyz pull request?
- Why shouldn't multiple unrelated changes go into one Cubyz pull request?
- What does CONTRIBUTING.md say about aliasing imports in Cubyz?

*Source: unknown | chunk_id: docs_CONTRIBUTING.md_chunk_2*
