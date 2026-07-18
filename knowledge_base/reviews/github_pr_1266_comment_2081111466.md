# [src/server/Entity.zig] - PR #1266 review diff

**Type:** review
**Keywords:** Entity, climbing, touchingClimbable, server-side, client-side, architectural review, data storage
**Symbols:** Entity, climbing, touchingClimbable
**Concepts:** architectural design, client-server architecture, data encapsulation

## Summary
Added `climbing` and `touchingClimbable` fields to the Entity struct.

## Explanation
The reviewer notes that these new fields (`climbing` and `touchingClimbable`) should only be stored in the client-side player struct. This architectural decision is likely aimed at maintaining a clear separation between server-side and client-side data, ensuring that the server does not need to manage state related to client-specific interactions like climbing.

## Related Questions
- Why are `climbing` and `touchingClimbable` fields being added to the Entity struct?
- What is the architectural reason for storing these fields only on the client-side?
- How might this change affect the synchronization between server and client states?
- Are there any potential performance implications of adding these fields to the Entity struct?
- What are the consequences if the server starts managing `climbing` state?
- How does this change impact backwards compatibility with existing clients?

*Source: unknown | chunk_id: github_pr_1266_comment_2081111466*
