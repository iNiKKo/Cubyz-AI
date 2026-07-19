# [issues/issue_1220.md] - Issue #1220 discussion

**Type:** review
**Keywords:** Structure Void blocks, behavior inversion, -a flag, -w flag, automatic placement, /replace command, /swap command
**Symbols:** /paste, /replace, /swap
**Concepts:** Command-line interface, Block manipulation, WorldEdit compatibility

## Summary
Discussion about the behavior of Structure Void blocks and potential commands for their manipulation.

## Explanation
The discussion revolves around the behavior of Structure Void blocks in Cubyz, which are similar to those in Minecraft. The maintainers suggest inverting the behavior so that air does not change blocks and void replaces them, making it easier to create structures without large volumes of void blocks. The current `/replace` command (`/replace cubyz:air cubyz:void`) does not work well when both air and void are needed. The maintainers also propose adding `-a` and `-w` flags to the `/paste` command to disable placing air and water blocks, similar to WorldEdit. Additionally, there is a suggestion for an automatic command to place structure void blocks. The maintainers inquire about the difference between `/swap` and `/replace` commands.

## Related Questions
- What is the intended behavior of Structure Void blocks in Cubyz?
- How can the behavior of Structure Void blocks be inverted in Cubyz?
- Why are there suggestions to add `-a` and `-w` flags to the `/paste` command?
- What is the purpose of an automatic command to place structure void blocks?
- Why does the current `/replace` command not work well with both air and void?
- What is the difference between the `/swap` and `/replace` commands in Cubyz?

*Source: unknown | chunk_id: github_issue_1220_discussion*
