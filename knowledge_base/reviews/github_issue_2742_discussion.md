# [issues/issue_2742.md] - Issue #2742 discussion

**Type:** review
**Keywords:** /set, force mode, reload mode, chunk loading, real-time processing, world reloading, creative-mode users, selection wand, block placement, unloaded chunks
**Symbols:** /set, force, reload
**Concepts:** command enhancement, user experience, performance optimization

## Summary
The issue discusses adding 'force' and 'reload' modes to the /set command, allowing users to place blocks in unloaded chunks or process selections outside of real-time.

## Explanation
The issue discusses adding 'force' and 'reload' modes to the /set command, allowing users to place blocks in unloaded chunks or process selections outside of real-time. The 'force' mode is specified with the syntax `/set cubyz:sand force`, which allows an addon to the command that force-loads the chunks that are not loaded but included in the selection. This would be particularly useful for creative-mode users building large structures, as it enables them to place blocks across multiple chunks without manually loading each one. The 'reload' mode is specified with the syntax `/set cubyz:sand reload`, which closes the world, processes the selected blocks outside of real-time, and then reloads the world. This could improve performance for complex selections by reducing the load on the system during processing. However, the maintainer emphasizes maintaining the default behavior where blocks are not placed in unloaded chunks to prevent unintended consequences.

## Related Questions
- What is the exact syntax for using 'force' and 'reload' modes with the /set command?
- How does the 'force' mode ensure that only intended chunks are loaded during block placement?

*Source: unknown | chunk_id: github_issue_2742_discussion*
