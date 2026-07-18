# [issues/issue_775.md] - Issue #775 discussion

**Type:** review
**Keywords:** carpets, walls, ceilings, corners, 3D placement, modeling
**Symbols:** Carpet RotationMode, Log mode
**Concepts:** 3D modeling, user interface design

## Summary
The maintainer implemented a new Carpet RotationMode that allows placing carpets on walls, ceilings, and filling gaps in corners.

## Explanation
The user requested a feature similar to the Log mode but for carpets, allowing them to cover multiple faces of a block including corners. The maintainer misunderstood initially but clarified that it meant placing carpets on walls and ceilings, akin to moss or vines. The maintainer then implemented this feature without testing with the provided carpet model.

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
