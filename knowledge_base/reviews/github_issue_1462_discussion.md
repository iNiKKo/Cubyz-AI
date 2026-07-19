# [issues/issue_1462.md] - Issue #1462 discussion

**Type:** review
**Keywords:** brushes, set mode, place mode, sphere, cuboid, cylinder, blueprint, SBB, pattern, whitelist, blacklist, undo, redo
**Concepts:** user interface, command-line interface, block editing

## Summary
The issue discusses the implementation of world edit brushes in Cubyz, detailing their modes, commands for creation and editing, and the rationale behind separating pattern and mask settings into separate commands.

## Explanation
The issue discusses the implementation of world edit brushes in Cubyz, detailing their modes, commands for creation and editing, and the rationale behind separating pattern and mask settings into separate commands. The primary focus is on the 'set' mode with sub-modes like sphere, cuboid, cylinder, and the 'place' mode for blueprint or SBB placement. Commands for creating these brushes include `/brush new sphere <radius>`, `/brush new cuboid <size>`, `/brush new cylinder <radius> <height>`, and `/brush new place <sbb|blueprint> <id>`. Separate commands are used to set patterns (`/brush pattern <pattern>`), whitelist (`/brush whitelist <mask>`), and blacklist (`/brush blacklist <mask>`). The use of whitelist and blacklist masks allows for flexible block editing without needing a separate replace brush. Brush placements can be undone or redone with `/undo` and `/redo` commands.

## Related Questions
- What are the two main modes of world edit brushes in Cubyz?
- How do you create a sphere brush in Cubyz?
- Why are pattern and mask settings separated into different commands?
- Can you explain the purpose of whitelist and blacklist masks in brush editing?
- How can users undo or redo brush placements in Cubyz?
- What is the intended future user interface for configuring brushes in Cubyz?

*Source: unknown | chunk_id: github_issue_1462_discussion*
