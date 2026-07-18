# [issues/issue_1909.md] - Issue #1909 discussion

**Type:** review
**Keywords:** XDG_CACHE_HOME, XDG_DATA_HOME, XDG_CONFIG_HOME, XDG_STATE_HOME, application data, dot folders, home directory, Linux, Windows
**Concepts:** XDG Base Directory Specification, data directories, cross-platform consistency

## Summary
Discussion on implementing XDG Base Directory Specification for data directories on Linux, with concerns about maintaining existing directory structures and cross-platform consistency.

## Explanation
The issue revolves around the outdated practice of storing application data in dot folders within the $HOME directory. The proposal suggests adhering to the XDG Base Directory Specification, which recommends specific environment variables for different types of data (cache, configuration, logs) with fallbacks to traditional locations. Maintainers are hesitant about changing the current structure, citing familiarity and time constraints. Users propose making changes but acknowledge the complexity of migrating existing data.

## Related Questions
- What are the benefits of using XDG Base Directory Specification?
- How does the current implementation handle data storage on Windows?
- What challenges arise from migrating existing data directories?
- Why is maintaining the current directory structure important to some maintainers?
- How can cross-platform consistency be achieved while adhering to platform-specific conventions?
- What are the potential drawbacks of using XDG Base Directory Specification?

*Source: unknown | chunk_id: github_issue_1909_discussion*
