# [issues/issue_877.md] - Issue #877 discussion

**Type:** review
**Keywords:** barren, balanced, overgrown, climate wavelength, temperature, hierarchy, terrain transition, extreme climates
**Concepts:** climate generation, hierarchy, biome tags

## Summary
Discussion on naming and placement of biome lushness tags within the climate generation hierarchy.

## Explanation
The discussion revolves around renaming the biome tags from `.barren`, `.sporting`, and `.lush` to `barren`, `balanced`, and `overgrown`. The maintainer seeks input on the importance of this property and its placement in the climate generation hierarchy. There is also a need for an associated climate wavelength, which should be similar to temperature. The maintainer considers the hierarchy's impact on how different climate zones transition next to each other, with lower positions increasing the likelihood of extreme climates being adjacent. The climate generator transitions terrain through hot-cold, ocean-land, wet-dry, and finally mountains, influencing the placement decision.

## Related Questions
- What are the proposed new names for the biome tags?
- How does the maintainer suggest placing the lushness tags in the hierarchy?
- Why should the climate wavelength be similar to temperature?
- How does the climate generator transition terrain, and what impact does this have on hierarchy placement?
- What is the relationship between the hierarchy position and the likelihood of extreme climates being adjacent?
- Are there any specific considerations for placing lushness tags relative to wet-dry or ocean-land categories?

*Source: unknown | chunk_id: github_issue_877_discussion*
