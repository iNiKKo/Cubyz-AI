# [issues/issue_2615.md] - Issue #2615 discussion

**Type:** review
**Keywords:** player index, commands, unique identifier, name conflicts, autocomplete, toggle, tablist, permission layer
**Symbols:** User, server.zig
**Concepts:** unique identifier, player index, autocomplete, name conflicts

## Summary
Discussion on adding a unique identifier for players in commands, focusing on using player indices instead of names due to potential name conflicts.

## Explanation
The discussion revolves around the need for a unique identifier for players when executing commands. Initially proposed was adding a formatting-stripped version of the player's name to the User struct in server.zig. However, maintainers pointed out that names alone are insufficient due to potential duplicates. The consensus shifted towards using player indices as identifiers, with autocomplete to help users select the correct index. Users discussed various ways to display these indices, such as prefixing names in-game or chat, adding them to the tablist, or rendering them behind names through a toggle. The primary concern is ensuring that players can be uniquely identified for commands, especially when dealing with similar names.

## Related Questions
- How can we implement a toggle to render player indices behind their names in-game?
- What are the potential performance implications of adding player indices to the tablist?
- How can we ensure that autocomplete for player indices is efficient and user-friendly?
- What changes need to be made to the permission layer to support unique player identification?
- How can we handle cases where multiple players have the same name in-game?
- What are the security implications of using player indices as command identifiers?

*Source: unknown | chunk_id: github_issue_2615_discussion*
