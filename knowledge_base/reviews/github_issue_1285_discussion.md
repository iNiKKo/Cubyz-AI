# [issues/issue_1285.md] - Issue #1285 discussion

**Type:** review
**Keywords:** asset file names, ID restrictions, cross-platform compatibility, Windows issues, naming convention, special characters, numbers, versioning, descriptive adjectives, directory organization
**Concepts:** cross-platform compatibility, internal consistency, asset ID system

## Summary
The discussion revolves around restricting asset file names and IDs in Cubyz to improve cross-platform compatibility and internal consistency. The maintainer proposes limiting characters to `a-z`, `A-Z`, and `_`, while excluding numbers, special characters, and reserved Windows file names.

## Explanation
The issue highlights the need for explicit restrictions on asset file names to prevent conflicts with Cubyz's internal parsing logic and ensure compatibility across different operating systems. The maintainer suggests a simplified naming convention using only alphanumeric characters and underscores, which would enforce a consistent style among addons. This approach aims to avoid issues related to special characters that have specific meanings in Cubyz's asset ID system (e.g., `:`, `%`, `,`, etc.). Additionally, the discussion touches on the potential for name collisions due to automatic replacement of restricted characters and the complexity it introduces in handling assets. The maintainer also considers excluding numbers from IDs to prevent confusion with versioning and instead recommends using descriptive adjectives or organizing files within directories.

## Related Questions
- What are the proposed restrictions on asset file names in Cubyz?
- Why is there a need to exclude special characters from asset IDs?
- How does the maintainer suggest handling versioning of assets?
- What is the reasoning behind excluding numbers from asset IDs?
- What alternative naming schemes are discussed for organizing assets?
- How would automatic replacement of restricted characters affect asset management?

*Source: unknown | chunk_id: github_issue_1285_discussion*
