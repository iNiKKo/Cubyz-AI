# [issues/issue_90.md] - Issue #90 discussion

**Type:** review
**Keywords:** block placement, entity hitbox, sync system, revert local edits, accurate reapplication, position, velocity, timestamp, inputs, frame timestamp, client-side interpolation, teleporting the camera
**Concepts:** synchronization, interpolation, thread safety

## Summary
The issue discusses making block placement illegal inside entity hitboxes, with a focus on addressing similar problems in the 0.1.0 version.

## Explanation
The issue discusses making block placement illegal inside entity hitboxes, which is already handled for the player. The maintainer suggests implementing a full sync system for block placing to revert local edits and ensure accurate reapplication of movement when blocks are placed. This requires that block placing fully goes through the sync system instead of using a bypass protocol. Additionally, the client needs to send various data through this sync system, including position, velocity, timestamp, inputs (very important), and frame timestamp. These details are necessary for accurately reverting and reapplying movement when a block is placed. If necessary, client-side interpolation should be implemented between the last predicted position and the fixed prediction to avoid teleporting the camera. This issue is dependent on another issue (#88) being resolved.

## Related Questions
- What is the current status of issue #90?
- How does the sync system address block placement within entity hitboxes?
- Why is it important to send position, velocity, timestamp, inputs, and frame timestamp through the sync system?
- What are the potential benefits of implementing client-side interpolation in this context?
- How does this solution relate to other similar issues like player knockback and anti-cheat mechanisms?
- What are the implications of fully going through the sync system for block placing?
- Why is issue #88 required for resolving this issue?

*Source: unknown | chunk_id: github_issue_90_discussion*
