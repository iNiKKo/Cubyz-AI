# [issues/issue_2777.md] - Issue #2777 discussion

**Type:** review
**Keywords:** block models, zon metadata, orientation, loading, flexibility, mesh metadata
**Concepts:** coordinate systems, metadata, model orientation

## Summary
Discussion on adding support for loading block models with different coordinate systems by including optional zon metadata files.

## Explanation
Discussion on adding support for loading block models with different coordinate systems by including optional zon metadata files. The maintainer suggests introducing optional zon metadata files that specify the model orientation, allowing adjustments during the loading process. Specific examples of orientation values include `.blender_default`, `.blockbench_default`, and `.right_hand_z_up`. This approach would not only address the current issue but also provide flexibility for future enhancements related to mesh metadata.

## Related Questions
- How can the zon metadata files be structured to support multiple coordinate systems?
- What are the potential performance implications of loading models with different orientations?
- Can this solution be extended to handle other types of mesh metadata in the future?
- How will this change impact existing block models that do not have orientation data?
- Are there any backward compatibility concerns with introducing new metadata files?
- What is the process for updating Blockbench to generate these zon metadata files?

*Source: unknown | chunk_id: github_issue_2777_discussion*
