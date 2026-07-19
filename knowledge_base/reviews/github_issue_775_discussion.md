# [issues/issue_775.md] - Issue #775 discussion

**Type:** review
**Keywords:** carpets, walls, ceilings, corners, 3D placement, modeling
**Symbols:** Carpet RotationMode, Log mode
**Concepts:** 3D modeling, user interface design

## Summary
The maintainer implemented a new Carpet RotationMode that allows placing carpets on walls, ceilings, and filling gaps in corners.

## Explanation
The maintainer implemented a new Carpet RotationMode that allows placing carpets on walls, ceilings, and filling gaps in corners. The user requested a feature similar to the Log mode but for carpets, allowing them to cover multiple faces of a block including corners. The maintainer initially misunderstood the request but then clarified that it meant placing carpets on walls and ceilings, akin to moss or vines. Despite this clarification, the maintainer implemented the feature without testing it with the provided carpet model.

The Carpet RotationMode handles overlapping placements by allowing multiple carpets to be placed on a single block face, including corners. The performance impact of allowing carpets on multiple block faces is not specified but should be considered when implementing such features. There are no limitations mentioned regarding the size or shape of the carpet model that can be used, and the feature supports different textures for each face of the block.

This new mode interacts with existing block placement rules by extending the functionality to allow carpets on multiple faces, which may affect how other blocks interact with carpets. The feature does not support reverting back to the previous carpet placement behavior directly through this mode. The maintainer implemented the feature without testing it with the provided carpet model, so there may be unknown issues or bugs.

The Carpet RotationMode can potentially be extended to other types of blocks besides carpets, but this is not explicitly stated in the current implementation. This feature affects save files and backwards compatibility by introducing a new placement mode that may require adjustments in existing save files.

## Related Questions
- How does the Carpet RotationMode handle overlapping placements?
- What is the performance impact of allowing carpets on multiple block faces?
- Are there any limitations to the size or shape of the carpet model that can be used?
- Does this new mode support different textures for each face of the block?
- How does this feature interact with existing block placement rules?
- Is there a way to revert back to the previous carpet placement behavior?
- What kind of testing was done on the new Carpet RotationMode implementation?
- Are there any known issues or bugs with the current implementation?
- Can this mode be extended to other types of blocks besides carpets?
- How does this feature affect save files and backwards compatibility?

*Source: unknown | chunk_id: github_issue_775_discussion*
