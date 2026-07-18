# [issues/issue_1449.md] - Issue #1449 discussion

**Type:** review
**Keywords:** code style, automation, linting, tools, review, ownership, zlint, ziglint, zls, Cubyz-linter
**Symbols:** zlint, ziglint, zls, pytest-lsp, Cubyz-linter
**Concepts:** code style enforcement, automated testing, third-party tools, code ownership, linting

## Summary
Discussion on implementing automated code style violation detection for Cubyz using various tools and approaches.

## Explanation
The discussion revolves around automating code style checks to reduce the burden of manual code review. Several tools are mentioned, including zlint, ziglint, and zls. The maintainer expresses interest in creating a custom solution using Zig's tokenizer and parser due to concerns about third-party tool reliability. There is also a suggestion to split code ownership to distribute the review load. The maintainer sets up a dedicated repository for Cubyz-specific linting code.

## Related Questions
- What are the main concerns regarding third-party linters for Cubyz?
- How does the maintainer propose to address code style violations?
- What is the suggested approach for splitting code ownership in Cubyz?
- What tools or libraries are being considered for implementing a custom linter?
- Where can contributors find more information about the proposed linting solution?
- What are the potential benefits and drawbacks of using a LSP-client-like library for linting?
- How does the maintainer view the role of automated tools in code review processes?
- What is the current status of the Cubyz-linter repository, and how can contributors contribute to it?

*Source: unknown | chunk_id: github_issue_1449_discussion*
