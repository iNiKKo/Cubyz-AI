# [issues/issue_564.md] - Issue #564 discussion

**Type:** review
**Keywords:** configurable, generation mode, simple vegetation, ceiling mode, cave vines, flexibility, limitation
**Symbols:** GenerationMode, SimpleVegetation
**Concepts:** configurability, structure generation

## Summary
The discussion revolves around making the GenerationMode configurable for structures like SimpleVegetation, specifically to support ceiling mode for cave vines.

## Explanation
The discussion revolves around making the GenerationMode configurable for structures like SimpleVegetation, specifically to support ceiling mode for cave vines. The maintainer acknowledges that allowing the GenerationMode to be configurable would provide more flexibility but points out a current limitation: SimpleVegetation does not handle cases where generation should occur on ceilings, such as for cave vines. This means that currently, SimpleVegetation will generate into the ceiling regardless of whether it is intended to do so or not.

## Related Questions
- What is the current behavior of SimpleVegetation when generating structures in ceiling mode?
- How can the GenerationMode be made configurable for SimpleVegetation?
- Are there any potential performance implications of making GenerationMode configurable?
- What other structures might benefit from having a configurable GenerationMode?
- Is there a risk of introducing bugs by changing how SimpleVegetation handles generation modes?
- How will this change affect backwards compatibility with existing world generation?

*Source: unknown | chunk_id: github_issue_564_discussion*
