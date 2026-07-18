# [issues/issue_1910.md] - Issue #1910 discussion

**Type:** review
**Keywords:** branch end, missing face, stairs, full block, chiseled, occluded, boolean flags, rendering
**Concepts:** Rendering, Visibility, Block Occlusion

## Summary
The issue involves a missing visible face of a branch end when connected to stairs. The discussion suggests checking if there is a full face on the opposite block and not removing the face if it isn't present.

## Explanation
The problem arises when a branch is connected to a full block, which is then chiseled, resulting in a missing face at the end of the branch. The maintainer indicates that there are boolean flags for each direction indicating whether a face is fully occluded. This suggests that the issue might be related to how these flags are being set or interpreted during rendering.

## Related Questions
- What is the current logic for determining if a face should be removed when chiseling a full block?
- How are the boolean flags for occlusion being set in the code?
- Are there any known issues with how occlusion flags are handled during rendering?
- Can you provide a test case that consistently reproduces the missing face issue?
- What changes need to be made to ensure that the opposite block's face is not removed if it isn't fully occluded?
- How will these changes affect performance, especially in scenes with many branches and chiseled blocks?

*Source: unknown | chunk_id: github_issue_1910_discussion*
