# [issues/issue_3235.md] - Issue #3235 discussion

**Type:** review
**Keywords:** localized aquifers, biome feature, minHeight, maxHeight, radius, blockID, chance, SDF implementation, stone shell, air exposure
**Symbols:** minHeight, maxHeight, radius, minRadius, maxRadius, blockID, chance
**Concepts:** Biome Feature, SDF Implementation, Thread Safety, Backwards Compatibility, Memory Leak

## Summary
Discussion on adding localized aquifers as a biome feature in Cubyz, including properties like minHeight, maxHeight, radius, blockID, and chance. Maintainer suggests generating a stone shell at the bottom to prevent air exposure.

## Explanation
The discussion revolves around enhancing Cubyz by introducing localized aquifers as a biome feature. The proposed implementation includes various properties such as minimum and maximum height, radius, block ID, and generation chance. A maintainer comment suggests adding a stone shell at the bottom of the aquifer to ensure it does not spill into air spaces, addressing potential issues with air exposure.

## Related Questions
- What properties are proposed for localized aquifers?
- How does the maintainer suggest preventing air exposure in aquifers?
- Are there any concerns about backwards compatibility with existing biome features?
- What is the role of SDF implementation in this feature proposal?
- How might adding a stone shell at the bottom affect performance?
- Is there a risk of memory leaks associated with generating new biome features?

*Source: unknown | chunk_id: github_issue_3235_discussion*
