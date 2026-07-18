# [issues/issue_2389.md] - Issue #2389 discussion

**Type:** review
**Keywords:** heightmap, rivers, grid boundaries, climate map, terrain adjustment
**Concepts:** heightmap, river generation, climate map

## Summary
The discussion revolves around generating rivers that adhere to a heightmap by either splitting the heightmap into large grids or sampling heights from a climate map.

## Explanation
The issue proposes two methods for river generation in Cubyz. The first method involves dividing the heightmap into large grids (e.g., 2048x2048 blocks) to ensure rivers do not cross grid boundaries. The second method suggests sampling heights from a climate map instead, allowing rivers to deviate slightly from the exact height profile and adjusting surrounding terrain to match the river's desired height. The maintainer comments that restricting rivers to specific grids is unnecessary and proposes using the climate map for more flexibility.

## Related Questions
- What are the potential benefits of splitting the heightmap into large grids for river generation?
- How does sampling heights from a climate map differ from following the exact height profile?
- What are the implications of adjusting surrounding terrain to match the river's desired height?
- Why is the maintainer concerned about restricting rivers to specific grid boundaries?
- Can you explain how the climate map can provide more flexibility in river generation?
- What are the potential drawbacks of using a climate map for river height sampling?

*Source: unknown | chunk_id: github_issue_2389_discussion*
