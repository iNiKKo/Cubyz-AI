# [issues/issue_2980.md] - Issue #2980 discussion

**Type:** review
**Keywords:** charged jump, jump charge, jump animation, platformer-style jump, climb action, tiny jumps
**Concepts:** gameplay mechanics, animation quality, user experience

## Summary
The issue discusses implementing a charged jump mechanic where players hold down the jump key to charge before releasing for a full jump. This is intended to improve animations and gameplay, but there are concerns about its practicality in various scenarios.

## Explanation
The issue discusses implementing a charged jump mechanic where players hold down the jump key to charge before releasing for a full jump. This is intended to improve animations and gameplay, but there are concerns about its practicality in various scenarios. The discussion revolves around the implementation of a charged jump feature where players hold down the jump key to build up power before releasing for a full jump. The primary motivation is to enhance the realism and animation quality of jumps by allowing for a squat-down preparation phase. However, there are concerns about the usability of this mechanic in gameplay scenarios such as climbing hills, where frequent charging might be cumbersome. Specifically, 'tiny jumps' refer to height differences that increase based on how long you hold down the jump key before releasing it. The maintainer suggests alternative behaviors like walking up single blocks without jumping or using climb actions for multiple blocks. This feature aims to provide a more realistic and visually appealing jumping experience.

## Related Questions
- How does the charged jump mechanic affect player movement speed?
- What are the potential performance implications of implementing a charged jump feature?
- Can you provide examples of how the charged jump will be integrated into different game levels?
- How will the charged jump mechanic interact with existing climbing mechanics in the game?
- Are there any plans to implement a cooldown period after using the charged jump?
- What are the potential balance issues that could arise from introducing a charged jump feature?

*Source: unknown | chunk_id: github_issue_2980_discussion*
