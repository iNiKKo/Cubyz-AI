# [issues/issue_79.md] - Issue #79 discussion

**Type:** review
**Keywords:** World Creation, Save Files, File Structure, Button Implementation, Documentation
**Symbols:** World Creation Screen, World Selection Screen, saves/Development, world.dat, generatorSettings.json
**Concepts:** File Handling, User Interface Design

## Summary
Discussion about implementing a World Creation Screen and understanding the file structure for saving worlds.

## Explanation
Discussion about implementing a World Creation Screen where players can choose a name for their new world. The user notes that `saves/Development` contains only `world.dat` and possibly `generatorSettings.json`. There is uncertainty whether creating a new world involves simply writing these files, suggesting potential complexity in the file handling process. Specifically, the discussion highlights the need to add a button on the World Selection Screen to create new worlds by generating these files.

## Related Questions
- What are the specific requirements for creating a new world in Cubyz?
- How does the current file structure support world creation and saving?
- Are there any existing functions or classes that handle world file creation?
- What documentation exists regarding the format of `world.dat` and `generatorSettings.json`?
- How will the World Creation Screen interact with the existing save system?

*Source: unknown | chunk_id: github_issue_79_discussion*
