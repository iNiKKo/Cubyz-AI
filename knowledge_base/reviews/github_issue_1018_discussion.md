# [issues/issue_1018.md] - Issue #1018 discussion

**Type:** review
**Keywords:** LOD0.5, model faces, remove faces, separate models, face list segmentation
**Concepts:** Level of Detail (LOD), Model Management, Face List Segmentation

## Summary
Discussion about extending LOD0.5 functionality to allow removing specific model faces.

## Explanation
Discussion about extending LOD0.5 functionality to allow removing specific model faces. The current limitation of LOD0.5 is that it only supports making faces opaque or removing what's behind them; specifically, it does not support adding new faces. The user suggests using separate models for different LODs as a potential solution, but the maintainer points out that this would complicate the face list segmentation further by requiring additional segmentation of the face list. The discussion highlights the need to explore alternative approaches to enhance the flexibility of LOD0.5 without introducing additional complexity.

## Related Questions
- What is the current limitation of LOD0.5 regarding model faces?
- Why does the maintainer suggest not adding new faces in LOD0.5?
- How could using separate models for different LODs affect the face list segmentation?
- Are there any alternative approaches to enhance LOD0.5 functionality without complicating the codebase?
- What are the potential benefits of allowing specific model faces to be removed in LOD0.5?
- How might the current implementation impact performance when removing specific model faces?

*Source: unknown | chunk_id: github_issue_1018_discussion*
