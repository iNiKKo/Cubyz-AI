# [issues/issue_1285.md] - Issue #1285 discussion

**Type:** review
**Keywords:** asset file names, ID restrictions, cross-platform compatibility, Windows issues, naming convention, special characters, numbers, versioning, descriptive adjectives, directory organization
**Concepts:** cross-platform compatibility, internal consistency, asset ID system

## Summary
The discussion revolves around restricting asset file names and IDs in Cubyz to improve cross-platform compatibility and internal consistency. The maintainer proposes limiting characters to `a-z`, `A-Z`, and `_`, while excluding numbers, special characters, and reserved Windows file names.

## Explanation
The discussion revolves around restricting asset file names and IDs in Cubyz to improve cross-platform compatibility and internal consistency. The maintainer proposes limiting characters to `a-z`, `A-Z`, and `_`, while excluding numbers, special characters, and reserved Windows file names. Additionally, the exclusion of leading underscores in addon IDs is also considered to avoid potential name collisions and ensure a consistent naming style among addons.

## Related Questions
- What are the proposed restrictions on asset file names in Cubyz?
- Why is there a need to exclude special characters from asset IDs?
- How does the maintainer suggest handling versioning of assets?
- What is the reasoning behind excluding numbers from asset IDs?
- What alternative naming schemes are discussed for organizing assets?
- How would automatic replacement of restricted characters affect asset management?

*Source: unknown | chunk_id: github_issue_1285_discussion*
