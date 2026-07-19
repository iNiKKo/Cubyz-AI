# [src/server/terrain/structures/Lake.zig] - PR #435 review diff

**Type:** review
**Keywords:** bugs, caves, lake bottom, structure interaction, chunk border, map generation, architectural review
**Symbols:** Lake.zig, std
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The reviewer identifies several bugs in the Lake.zig file, including caves visible through lake bottoms and interaction issues with other structures. They suggest generating lakes during map generation to address these problems.

## Explanation
The review highlights critical architectural issues within the Lake structure implementation. The primary concerns are visual artifacts such as caves being visible through the bottom of lakes (as shown in the screenshot at https://github.com/PixelGuys/Cubyz/assets/43880493/c310b7a0-703c-488f-a5ea-a730f0a89bda) and improper interactions with other terrain features, leading to inconsistent rendering (as shown in the screenshots at https://github.com/PixelGuys/Cubyz/assets/43880493/c7f98265-d418-4445-9f4e-07d05a4a8e22, https://github.com/PixelGuys/Cubyz/assets/43880493/2f27949a-8d05-4862-9322-f38b4e904ced, and https://github.com/PixelGuys/Cubyz/assets/43880493/ff2df8ce-e3c9-4967-830a-e9afe640469a). Additionally, there is a noted issue where lakes can abruptly terminate at chunk borders (as shown in the screenshot at https://github.com/PixelGuys/Cubyz/assets/43880493/694b39df-632c-4730-b42a-75d4b8faf62e), disrupting the natural appearance. The reviewer proposes a significant change in approach by integrating lake generation into the map generation process, which would require developing a new structure system specifically for map generation tasks. This architectural shift aims to improve the consistency and quality of terrain features across the game world.

## Related Questions
- What are the specific visual artifacts mentioned in the review?
- How does the current lake generation system interact with other structures?
- Why is there a concern about lakes terminating at chunk borders?
- What new structure system is proposed for map generation?
- What architectural changes are suggested to address the identified issues?
- Are there any plans to maintain backwards compatibility during this change?

*Source: unknown | chunk_id: github_pr_435_comment_1624172620*
