# [src/server/Entity.zig] - PR #1266 review diff

**Type:** review
**Keywords:** Entity, climbing, touchingClimbable, client-side, server-side, architectural review, data separation
**Symbols:** Entity, climbing, touchingClimbable
**Concepts:** client-server architecture, data encapsulation

## Summary
Added `climbing` and `touchingClimbable` fields to the Entity struct.

## Explanation
The reviewer notes that these new fields, `climbing` and `touchingClimbable`, should only be stored in the client-side player struct for now. This architectural decision is likely aimed at maintaining a clear separation between server-side and client-side data, ensuring that the server does not inadvertently manage state intended solely for the client's rendering or input handling.

## Related Questions
- Why are the `climbing` and `touchingClimbable` fields being added to the Entity struct?
- What is the architectural rationale behind storing these fields only on the client-side?
- How might this change affect the synchronization between server and client states?
- Are there any potential performance implications of adding these boolean fields?
- What steps should be taken to ensure that the server does not use these fields for logic processing?
- How will this change impact the existing codebase, particularly in terms of data handling and state management?

*Source: unknown | chunk_id: github_pr_1266_comment_2081111466*
