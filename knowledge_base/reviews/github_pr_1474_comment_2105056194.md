# [src/server/server.zig] - PR #1474 review diff

**Type:** review
**Keywords:** ECS, interpolation, architectural review, separate PR, manual data copying
**Symbols:** User, Connection, Entity, utils.TimeDifference, utils.GenericInterpolation
**Concepts:** ECS architecture, thread safety, backwards compatibility

## Summary
The review comments suggest removing fields related to ECS from the User struct and recommends either separating this change into a different PR for closer examination or retaining the interpolation field.

## Explanation
The reviewer points out that the changes made to the User struct are not aligned with the Entity Component System (ECS) architecture. They advise either isolating these changes in a separate pull request to thoroughly assess their impact or preserving the interpolation field, possibly by using a stable pointer and manually copying data during updates. This recommendation aims to maintain architectural integrity and prevent unintended side effects.

## Related Questions
- What are the potential consequences of removing the interpolation field from the User struct?
- How does the ECS architecture impact the design decisions in this code change?
- Why is it recommended to separate this change into a different PR?
- Can you explain the purpose of the manual data copying approach mentioned by the reviewer?
- What are the implications of modifying the User struct without considering the ECS framework?
- How does the removal of the player field affect the overall functionality of the server.zig file?
- What steps should be taken to ensure thread safety when making these changes?
- How can we maintain backwards compatibility while implementing these architectural modifications?

*Source: unknown | chunk_id: github_pr_1474_comment_2105056194*
