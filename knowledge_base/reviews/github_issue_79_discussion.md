# [issues/issue_79.md] - Issue #79 discussion

**Type:** review
**Keywords:** World Creation, Save Files, File Structure, Button Implementation, Documentation
**Symbols:** World Creation Screen, World Selection Screen, saves/Development, world.dat, generatorSettings.json
**Concepts:** File Handling, User Interface Design

## Summary
Discussion about implementing a World Creation Screen and understanding the file structure for saving worlds.

## Explanation
The discussion revolves around the need to add a World Creation Screen where players can choose a name for their new world. The user questions the current state of save files, noting that `saves/Development` contains only `world.dat` and possibly `generatorSettings.json`. There's uncertainty about whether creating a new world involves simply writing these files, suggesting potential complexity in the file handling process.

## Related Questions
- What are the specific requirements for creating a new world in Cubyz?
- How does the current file structure support world creation and saving?
- Are there any existing functions or classes that handle world file creation?
- What documentation exists regarding the format of `world.dat` and `generatorSettings.json`?
- How will the World Creation Screen interact with the existing save system?
- Is there a need for additional files beyond `world.dat` and `generatorSettings.json` during world creation?
- What are the potential implications of adding a new button to the World Selection Screen?
- How can we ensure that the new world creation process is user-friendly and intuitive?
- Are there any security concerns related to file handling in Cubyz?
- How will the implementation of the World Creation Screen affect existing save compatibility?

*Source: unknown | chunk_id: github_issue_79_discussion*
