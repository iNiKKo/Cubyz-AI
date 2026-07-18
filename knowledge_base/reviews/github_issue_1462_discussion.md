# [issues/issue_1462.md] - Issue #1462 discussion

**Type:** review
**Keywords:** brushes, set mode, place mode, sphere, cuboid, cylinder, blueprint, SBB, pattern, whitelist, blacklist, undo, redo
**Concepts:** user interface, command-line interface, block editing

## Summary
The issue discusses the implementation of world edit brushes in Cubyz, detailing their modes, commands for creation and editing, and the rationale behind separating pattern and mask settings into separate commands.

## Explanation
The discussion centers around the design and implementation of world edit brushes in Cubyz. The primary focus is on the 'set' and 'place' modes, each with specific sub-modes like sphere, cuboid, cylinder for 'set', and blueprint or SBB placement for 'place'. The commands for creating these brushes are designed to be simple and intuitive, with separate commands for setting patterns and masks to avoid command length limitations. This design is intended to mimic the user experience of configuring brushes through a dedicated UI in the future. The use of whitelist and blacklist masks allows for flexible block editing without needing a separate replace brush.

## Related Questions
- What are the two main modes of world edit brushes in Cubyz?
- How do you create a sphere brush in Cubyz?
- Why are pattern and mask settings separated into different commands?
- Can you explain the purpose of whitelist and blacklist masks in brush editing?
- How can users undo or redo brush placements in Cubyz?
- What is the intended future user interface for configuring brushes in Cubyz?

*Source: unknown | chunk_id: github_issue_1462_discussion*
