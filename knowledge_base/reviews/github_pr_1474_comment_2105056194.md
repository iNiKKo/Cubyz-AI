# [src/server/server.zig] - PR #1474 review diff

**Type:** review
**Keywords:** ECS, architecture, separate PR, interpolation, player field, manual data copying
**Symbols:** User, Connection, Entity, utils.TimeDifference, utils.GenericInterpolation
**Concepts:** Entity Component System (ECS), architectural integrity, separation of concerns

## Summary
The review suggests separating changes related to ECS from other modifications, specifically regarding the removal of `player` and `interpolation` fields.

## Explanation
The reviewer is concerned about the architectural integrity of the codebase. They believe that changes affecting the Entity Component System (ECS) should be handled in a separate pull request to allow for thorough examination of their implications. The reviewer also suggests keeping the `interpolation` field and using a stable pointer to manually copy data over during each update, rather than removing it entirely.

## Related Questions
- What are the potential consequences of removing the `player` and `interpolation` fields from the `User` struct?
- How does separating ECS-related changes into a separate PR benefit code review and maintenance?
- Can you explain why manual data copying with a stable pointer is suggested instead of removing the `interpolation` field?
- What are the implications of not following the reviewer's suggestion to handle ECS changes separately?
- How might this change affect the performance or stability of the server component?
- Is there any risk of introducing bugs by separating ECS-related changes into a different PR?

*Source: unknown | chunk_id: github_pr_1474_comment_2105056194*
