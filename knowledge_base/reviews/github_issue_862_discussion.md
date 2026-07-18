# [issues/issue_862.md] - Issue #862 discussion

**Type:** review
**Keywords:** ~/.config/cubyz, ~/.cubyz, XDG Base Directory Specification, Linux, Minecraft, configuration files, game saves, executables
**Concepts:** backwards compatibility, user experience, file system organization

## Summary
Discussion about changing the configuration directory from ~/.cubyz to ~/.config/cubyz on Linux.

## Explanation
The discussion revolves around the proposed change of the configuration directory for the Cubyz game on Linux systems. The user suggests moving the configuration files to ~/.config/cubyz, arguing that it adheres to the XDG Base Directory Specification by placing configuration files in a designated config folder. The maintainer questions this change, pointing out that other games, including Minecraft, store their data in the home directory and that the proposed directory will also contain game saves, executables, and future launcher components.

## Related Questions
- What is the XDG Base Directory Specification?
- Why do other games like Minecraft store their data in the home directory?
- How does changing the configuration directory affect backwards compatibility?
- What are the potential benefits of following the XDG Base Directory Specification?
- How will the proposed change impact future game updates and components?
- Are there any known issues with storing game saves and executables in the same directory as configuration files?

*Source: unknown | chunk_id: github_issue_862_discussion*
