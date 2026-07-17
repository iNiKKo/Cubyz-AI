# [src/server/command/worldedit/replace.zig] - PR #1424 review diff

**Type:** review
**Keywords:** replace, command, worldedit, selection box, block pattern, mask expression, Vec3i, User, Block, Blueprint, Pattern, Mask
**Symbols:** description, usage, Vec3i, User, Block, Blueprint, Pattern, Mask
**Concepts:** worldedit, block replacement, mask expression, pattern

## Summary
Added a new command for replacing blocks in a worldedit selection based on a mask and pattern.

## Explanation
The change introduces a new command `/replace` that allows users to replace blocks within a specified selection box. The command uses a mask expression to identify which blocks to replace and a block pattern to define the replacement blocks. The reviewer suggests refining the description and usage strings for clarity, emphasizing that the operation is limited to the worldedit selection box.

## Related Questions
- What is the purpose of the `/replace` command?
- How does the command identify which blocks to replace?
- What defines the replacement blocks in this command?
- Why was there a suggestion to refine the description and usage strings?
- Does this command operate within a specific selection box?
- What are the dependencies required for this command to function?

*Source: unknown | chunk_id: github_pr_1424_comment_2095907347*
