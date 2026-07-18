# [issues/issue_3095.md] - Issue #3095 discussion

**Type:** review
**Keywords:** translation, rotation, coordinate space, SDF, chaining
**Concepts:** local coordinate space, global coordinate space, SDF (Signed Distance Function)

## Summary
Discussion about adding local coordinate space translation to allow for chaining rotations or changing the rotation point of an SDF.

## Explanation
The issue discusses the need to implement local coordinate space translation in addition to the existing global coordinate space translation. This would enable more flexible transformations, such as chaining rotations and rotating around different points. The maintainer acknowledges the request and suggests that it involves distinguishing between local and global coordinate spaces.

## Related Questions
- What is the current implementation of translation in Cubyz?
- How would adding local coordinate space translation affect existing transformations?
- Can you provide examples of how chaining rotations could be useful in Cubyz?
- What are the potential performance implications of implementing local coordinate space translation?
- Are there any backward compatibility concerns with this change?
- How does the current SDF implementation handle rotation around different points?

*Source: unknown | chunk_id: github_issue_3095_discussion*
