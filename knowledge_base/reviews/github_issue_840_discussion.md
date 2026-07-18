# [issues/issue_840.md] - Issue #840 discussion

**Type:** review
**Keywords:** tag, spawn above water, underwater, everywhere, enum, surface, issue #570, architecture, dependencies
**Concepts:** feature addition, enum usage, structure generation, dependency management

## Summary
Discussion about adding a tag to specify structure spawning locations (above water, under water, or both). Maintainer suggests waiting for issue #570.

## Explanation
The discussion revolves around the addition of a new feature that allows structures to be tagged with their spawning conditions relative to water levels. The user proposes using an enum with values 'surface', 'underwater', and 'everywhere' to provide flexibility in structure generation. However, the maintainer expresses caution about implementing this feature immediately, suggesting it should wait until after issue #570 is resolved. This indicates that there might be dependencies or architectural considerations related to issue #570 that need to be addressed first.

## Related Questions
- What is the proposed enum for structure spawning locations?
- Why is the maintainer suggesting to wait for issue #570?
- Are there any potential architectural implications of adding this feature?
- How might the new tag affect existing structure generation logic?
- What dependencies does issue #570 have on this feature addition?
- Can you explain the reasoning behind using an enum for specifying spawning locations?

*Source: unknown | chunk_id: github_issue_840_discussion*
