# [issues/issue_1177.md] - Issue #1177 discussion

**Type:** review
**Keywords:** bloom, emission, lighting, over-exposure, exposure detection, localized exposure
**Concepts:** bloom shader, emissive blocks, lighting, exposure detection

## Summary
The discussion revolves around enhancing the bloom shader to affect emissive blocks with dull emission and proposes adding a light source in the space occupied by such blocks for better lighting effects.

## Explanation
The issue highlights that currently, the bloom effect does not apply to emissive blocks with dull emission, which is considered incorrect. The maintainer suggests forcing a light in the space of these emissive blocks to improve lighting and create a fake over-exposure effect. However, this proposal requires exposure detection, possibly localized, to prevent the entire surface from blooming uniformly.

## Related Questions
- How does the current bloom shader handle emissive blocks with dull emission?
- What is the proposed method to force a light in the space of emissive blocks?
- Why is localized exposure detection necessary for the proposed lighting effect?
- Can you explain how exposure detection would prevent uniform blooming across surfaces?
- How does adding a light source in the space of emissive blocks improve overall lighting effects?
- What are the potential performance implications of implementing localized exposure detection?

*Source: unknown | chunk_id: github_issue_1177_discussion*
