# [issues/issue_1387.md] - Issue #1387 discussion

**Type:** review
**Keywords:** special world type, flat world, structure building blocks, blueprints, UI for viewing blueprints, automagical mechanics, 2D preview, 3D display, void block placement, selection tools, replace wands
**Concepts:** UI design, user experience, structure building blocks, console commands

## Summary
Discussion about adding a special world type in Cubyz to display all available structure building blocks for easier review and refinement.

## Explanation
Discussion about adding a special world type in Cubyz to display all available structure building blocks (SBBs) for easier review and refinement. The maintainers suggest that this could be seen as a workaround for lacking UI features, such as viewing blueprints from assets or editing structures without manual commands. They propose alternative solutions like 2D or 3D previews, using console commands for void block placement, and integrating selection tools with replace wands to improve convenience and accuracy.

The special world type should be a flat world where all root SBBs are pasted with signs describing their paths. Child SBBs should be placed above their respective roots, and contained blueprints should be placed below the root SBBs with frames indicating dimensions. All elements should regenerate upon re-entering the world to allow reuse.

The maintainers suggest that a UI preview would have limitations compared to a 3D display but also note practical issues like looking inside closed structures. They recommend using console commands such as `/mask global !cubyz:air\n/set cubyz:void` or `/replace cubyz:air cubyz:void` for void block placement, and integrating selection tools with replace wands for better precision and convenience.

## Related Questions
- What are the advantages and disadvantages of creating a special world type for reviewing structures?
- How could a UI preview be implemented to enhance structure review in Cubyz?
- What are the potential issues with using console commands like `/mask` and `/set` for void block placement?
- How can selection tools be integrated with replace wands to improve precision and convenience?
- What are the trade-offs between 2D and 3D previews for structure review in Cubyz?
- How could a list-based UI be designed to show multiple structures at once for easier comparison?

*Source: unknown | chunk_id: github_issue_1387_discussion*
