# [issues/issue_105.md] - Issue #105 discussion

**Type:** review
**Keywords:** #include, shader support, voxel models, #303, #3335, buffer management
**Concepts:** shader inclusion, code duplication, maintenance

## Summary
The issue proposes adding shader `#include` support, but it has been deemed less critical due to recent changes and potential conflicts.

## Explanation
The original request was to implement a custom `#include` directive for shaders to reduce code duplication. However, the maintainer notes that this feature is no longer as pressing due to the removal of voxel models. Additionally, there are concerns about compatibility with another ongoing project (#303) and the potential exacerbation of existing buffer management issues (#3335). The discussion highlights the trade-offs between adding new features and maintaining codebase integrity.

## Related Questions
- What are the potential impacts of implementing shader `#include` support?
- How does the removal of voxel models affect the necessity for shader inclusion?
- What conflicts might arise between this feature and project #303?
- How could buffer management be improved to prevent future issues?
- Is there a way to implement shader inclusion without compromising autocomplete support?
- What are the current duplicate buffers in the codebase that need maintenance?

*Source: unknown | chunk_id: github_issue_105_discussion*
