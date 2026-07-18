# [mods/cubyz/rotations.zig] - PR #3266 review diff

**Type:** review
**Keywords:** rotations.zig, go deeper folder, worldedit, commands.zig, helper folders, prefixing with underscore, auto generation
**Symbols:** stairs, no_rotation, texture_pile, ore, hanging, torch, decayable, direction, planar, log, carpet, branch, fence, sign, spawn, paste
**Concepts:** code organization, architectural design, auto-generation, folder naming conventions

## Summary
The review discusses the addition of various rotation modules in Cubyz and proposes an architectural change for folder naming conventions to improve code organization.

## Explanation
The reviewer adds several new modules related to different types of rotations (stairs, no_rotation, texture_pile, etc.) to the `rotations.zig` file. The critical architectural review suggests a naming convention for folders where helper structs reside, by prefixing them with an underscore (_). This would help in distinguishing between main functionality and helper code during auto-generation processes. The reviewer is uncertain about the implementation's feasibility and seeks feedback on its effectiveness.

## Related Questions
- What is the purpose of adding these rotation modules in Cubyz?
- How does the proposed folder naming convention improve code organization?
- Why is there uncertainty about the implementation's feasibility?
- Can you provide an example of how the auto-generation process would work with this new naming convention?
- What are the potential benefits and drawbacks of prefixing helper folders with an underscore?
- How might this change affect mod creators' workflow?

*Source: unknown | chunk_id: github_pr_3266_comment_3447420382*
