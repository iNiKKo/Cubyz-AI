# [issues/issue_2742.md] - Issue #2742 discussion

**Type:** review
**Keywords:** /set, force mode, reload mode, chunk loading, real-time processing, world reloading, creative-mode users, selection wand, block placement, unloaded chunks
**Symbols:** /set, force, reload
**Concepts:** command enhancement, user experience, performance optimization

## Summary
The issue discusses adding 'force' and 'reload' modes to the /set command, allowing users to place blocks in unloaded chunks or process selections outside of real-time.

## Explanation
The discussion centers around enhancing the /set command with two new modes: 'force' and 'reload'. The 'force' mode aims to allow block placement in chunks that are not currently loaded, which would be particularly useful for creative-mode users building large structures. The 'reload' mode suggests closing the world, processing the selected blocks outside of real-time, and then reloading the world, potentially improving performance for complex selections. The maintainer emphasizes maintaining the default behavior where blocks are not placed in unloaded chunks to prevent unintended consequences.

## Related Questions
- What are the potential performance implications of adding a 'reload' mode to the /set command?
- How does the 'force' mode affect memory usage and chunk management?
- Can you provide examples of how the 'force' mode would be used in practice?
- What security concerns might arise from allowing block placement in unloaded chunks?
- How does the current default behavior ensure thread safety during block placement?
- Is there a risk of data corruption if the world is reloaded while processing selections?
- Can you explain how the 'reload' mode would handle large selections efficiently?
- What are the potential compatibility issues with existing addons or plugins?
- How does the addition of these modes impact backwards compatibility with older versions of Cubyz?
- Are there any specific architectural changes required to implement the 'force' and 'reload' modes?

*Source: unknown | chunk_id: github_issue_2742_discussion*
