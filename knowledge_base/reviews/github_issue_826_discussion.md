# [issues/issue_826.md] - Issue #826 discussion

**Type:** review
**Keywords:** AABB, collision, fences, generated models, rotation, zon file, Model struct
**Symbols:** AABB, Model, zon
**Concepts:** collision detection, model integration, performance optimization

## Summary
Discussion on implementing Axis-Aligned Bounding Boxes (AABBs) for collision detection, focusing on integration with existing models and handling of rotation.

## Explanation
Discussion on implementing Axis-Aligned Bounding Boxes (AABBs) for collision detection, focusing on integration with existing models and handling of rotation. The maintainer questions how to handle generated models and suggests using a separate zon file or suffix for collision models. There is debate on whether bounding boxes should be tied to the model or remain independent. The maintainer ultimately decides that AABBs should be integrated into the Model struct, with each model having its own slice of AABBs.

## Related Questions
- How are AABBs generated from the model?
- What is the impact of tying AABBs to the model on performance?
- Can AABBs be used with all types of models, or are there limitations?
- How does the use of AABBs affect collision detection accuracy?
- What changes need to be made to support rotation in collision models?
- Is there a plan to update existing models to include AABBs?
- How will AABBs interact with other collision shapes in future updates?
- What are the potential benefits and drawbacks of using AABBs for collision detection?
- How does the implementation of AABBs affect memory usage?
- Are there any backward compatibility concerns with this change?

*Source: unknown | chunk_id: github_issue_826_discussion*
