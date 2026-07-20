# [src/server/command/worldedit/selection.zig] - PR #3313 review diff

**Type:** review
**Keywords:** worldedit, selection, normalize, cube, pos1, pos2, coordinates, block box, radius, command design
**Symbols:** selection, normalize, cube, Block, command, User, Vec3i
**Concepts:** Command Design, World Editing, Coordinate Management

## Summary
Added new worldedit selection commands for normalization and creating cubes.

## Explanation
The review introduces two new commands under the 'selection' module: 'normalize' and 'cube'. The 'normalize' command ensures that the coordinates of the selected area are set correctly, with pos1 being the minimal and pos2 the maximal. The usage syntax for 'normalize' is `/selection normalize`. The 'cube' command allows creating a cubic selection with a specified radius, where the default radius is 5. The usage syntax for 'cube' is `/selection cube <radius=5>`. The reviewer emphasizes the importance of always working with a full box to avoid awkward situations where only one corner is set. If there is no pos2, it can be assumed that pos2=pos1, but unsettling it afterward is awkward (you can only clear both). It's much more reliable to always work with a full box. The architectural review also notes that the more abstract use case is to help understand how big a block box (e.g., 31x31x31) is in terms of structure limits.

## Related Questions
- How does the 'normalize' command ensure correct coordinate settings?
- What is the purpose of the 'cube' command in world editing?
- Why is it important to always work with a full box in selection operations?
- How does the code handle cases where only one corner (pos1 or pos2) is set?
- Can you explain the architectural reasoning behind adding these new commands?
- What are the potential performance implications of using these new selection commands?

*Source: unknown | chunk_id: github_pr_3313_comment_3556961872*
