# [issues/issue_1906.md] - Issue #1906 discussion

**Type:** review
**Keywords:** block contrast, adjacent blocks, surface normals, ambient occlusion, UI element, menu control
**Concepts:** user feedback, feature request, visual rendering

## Summary
Discussion on adding an option to increase block contrast in the game, clarifying that it refers to contrast between adjacent blocks with different normals.

## Explanation
The discussion revolves around implementing a feature request for players who prefer stronger visual differentiation between adjacent blocks. The maintainers clarify that 'contrast between faces' specifically means the contrast between blocks that have different surface normals, which is achieved using ambient occlusion. This distinction is important as it affects how the game renders block edges and surfaces, potentially enhancing the overall visual experience. Users also inquired about adding a UI element to control the contrast in a menu. The maintainers did not provide a direct answer regarding whether there are any existing UI elements that could be repurposed for this purpose.

The current method for calculating block contrast in Cubyz is based on ambient occlusion, which affects the visual appearance of blocks with different normals. There is currently no means to control block contrast through a UI element. The maintainers did not specify whether there are any existing UI elements that could be repurposed for this purpose.

## Related Questions
- What is the current method for calculating block contrast in Cubyz?
- How does ambient occlusion affect the visual appearance of blocks with different normals?
- Are there any existing UI elements that could be repurposed to control block contrast?
- What are the potential performance implications of adding a dynamic block contrast feature?
- How will this new feature impact compatibility with existing game content?
- Can you provide examples of how other games handle block contrast adjustments?

*Source: unknown | chunk_id: github_issue_1906_discussion*
