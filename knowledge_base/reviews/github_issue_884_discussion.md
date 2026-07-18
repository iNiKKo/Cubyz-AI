# [issues/issue_884.md] - Issue #884 discussion

**Type:** review
**Keywords:** velocity, rotation, camera, update, stored data, synchronization
**Concepts:** camera synchronization, player data storage, state update

## Summary
The issue discusses loading player's velocity and rotation from stored data and sending it to the client, but notes that the camera does not update accordingly.

## Explanation
The discussion highlights a problem where the intended functionality of updating the camera's rotation and velocity based on stored player data is not being achieved. The maintainer points out that despite the implementation, the camera remains unchanged, indicating a potential bug or oversight in how the camera state is being updated or synchronized with the stored player data.

## Related Questions
- Why is the camera not updating with the stored player data?
- Is there a bug in how the camera state is being synchronized?
- How does the system handle loading and sending player data to the client?
- Are there any known issues with camera synchronization in this version of Cubyz?
- What changes need to be made to ensure the camera updates correctly?
- Does the stored player data include all necessary information for camera state?

*Source: unknown | chunk_id: github_issue_884_discussion*
