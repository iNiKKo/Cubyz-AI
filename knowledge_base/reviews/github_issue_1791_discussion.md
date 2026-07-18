# [issues/issue_1791.md] - Issue #1791 discussion

**Type:** review
**Keywords:** global cubyz dir, migrate files, multiple instances, assets/backgrounds, blueprints, gamecontrollerdb.txt, serverAssets
**Concepts:** thread safety, backwards compatibility

## Summary
The discussion revolves around moving certain files and folders from the working directory to a global Cubyz directory location, with concerns about handling multiple instances accessing shared resources simultaneously.

## Explanation
The issue aims to centralize important files like blueprints and assets/backgrounds into a global Cubyz directory. The reviewer raises a critical concern about potential conflicts when multiple instances of Cubyz attempt to access these shared resources concurrently. The maintainer acknowledges the current behavior where processes use the same folders, which could lead to issues, especially with game instances started from different directories. The maintainer also clarifies that assets/backgrounds need to be migrated and suggests addressing this before version 0.0.0.

## Related Questions
- How does the current implementation handle multiple Cubyz instances accessing shared resources?
- What are the potential issues if multiple Cubyz instances try to write to the same global directory simultaneously?
- Is there a proposed solution for ensuring thread safety when accessing shared assets in the global directory?
- How will the migration of important files affect backwards compatibility with existing installations?
- What steps should be taken to prevent data corruption during concurrent access to shared resources?
- How can we ensure that the global Cubyz directory is properly initialized and secured across different operating systems?

*Source: unknown | chunk_id: github_issue_1791_discussion*
