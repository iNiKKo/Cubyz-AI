# [issues/issue_2477.md] - Issue #2477 discussion

**Type:** review
**Keywords:** migrations, ore data, blueprints, block ids, rotation modes, VTable, to string method, full string representation, numerical IDs, header mapping
**Concepts:** migrations, blueprints, block ids, rotation modes, VTable

## Summary
The discussion revolves around fixing an issue where ore data in blueprints is not affected by migrations, leading to broken blueprints. The proposed solution involves adding a 'to string' method to the rotation mode VTable to store block information as full strings instead of numeric values.

## Explanation
The core problem identified is that ore rotation stores host block information using its data value, which is not updated during migrations. This results in blueprints that use such combinations becoming invalid. The maintainer suggests adding a 'to string' method to the rotation mode VTable to convert blocks into their full string representation (e.g., `cubyz:slate`) instead of storing them as numeric internal values (`typ`). The user proposes an alternative approach where the blueprint header maps block text IDs to numerical IDs, using these numerical IDs within the blueprint's block section. This would avoid storing redundant text IDs for each block instance. The maintainer notes that a similar mapping already exists but does not account for block data.

## Related Questions
- How does the current implementation handle block data in blueprints?
- What is the proposed solution to ensure block data compatibility across migrations?
- Why is it suggested to store block information as full strings instead of numeric values?
- How would mapping block text IDs to numerical IDs within the blueprint header improve performance?
- Does the existing mapping mechanism support block data, and if not, why?
- What are the potential implications of changing the way block data is stored in blueprints?

*Source: unknown | chunk_id: github_issue_2477_discussion*
