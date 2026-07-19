# [issues/issue_1791.md] - Issue #1791 discussion

**Type:** review
**Keywords:** global cubyz dir, migrate files, multiple instances, assets/backgrounds, blueprints, gamecontrollerdb.txt, serverAssets
**Concepts:** thread safety, backwards compatibility

## Summary
The discussion revolves around moving certain files and folders from the working directory to a global Cubyz directory location, with concerns about handling multiple instances accessing shared resources simultaneously.

## Explanation
The discussion revolves around moving certain files and folders from the working directory to a global Cubyz directory location. Important files that must be migrated include 'blueprints' and 'assets/backgrounds'. Less important files, which do not need to be migrated, are 'gamecontrollerdb.txt', 'gamecontrollerdb.stamp', 'logs', 'serverAssets', 'assets/cubyz/music', and 'assets/cubyz/fonts'. The maintainer acknowledges that both processes use the same folders when multiple instances of Cubyz attempt to access these shared resources concurrently, which could cause issues. This applies especially to game instances started from different directories. Additionally, assets/backgrounds need to be migrated before version 0.0.0.

## Related Questions
- How does the current implementation handle multiple Cubyz instances accessing shared resources?
- What are the potential issues if multiple Cubyz instances try to write to the same global directory simultaneously?
- Is there a proposed solution for ensuring thread safety when accessing shared assets in the global directory?
- Which files and folders need to be migrated, and which ones do not?
- How will the migration of important files affect backwards compatibility with existing installations?

*Source: unknown | chunk_id: github_issue_1791_discussion*
