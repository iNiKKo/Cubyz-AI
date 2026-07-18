# [issues/issue_105.md] - Issue #105 discussion

**Type:** review
**Keywords:** #include, shader support, voxel models, #303, #3335, buffer management
**Concepts:** shader inclusion, code duplication, maintenance

## Summary
The issue proposes adding shader `#include` support, but it has been deemed less critical due to recent changes and potential conflicts.

## Explanation
The issue proposes adding shader `#include` support to reduce code duplication by including common functions. However, due to recent changes in the project (removal of voxel models), this feature is no longer considered critical. The maintainer notes that implementing `#include` could conflict with another ongoing project (#303) and exacerbate existing buffer management issues (#3335). Additionally, there are concerns about potential impacts on autocomplete support due to less structured file naming conventions. Specifically, the maintainer mentions that each included file would need to have the same name as the function they contain to maintain some level of autocomplete functionality.

## Related Questions
- What are the potential impacts of implementing shader `#include` support?
- How does the removal of voxel models affect the necessity for shader inclusion?
- What conflicts might arise between this feature and project #303?
- How could buffer management be improved to prevent future issues?
- Is there a way to implement shader inclusion without compromising autocomplete support?
- What are the current duplicate buffers in the codebase that need maintenance?

*Source: unknown | chunk_id: github_issue_105_discussion*
