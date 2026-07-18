# [issues/issue_456.md] - Issue #456 discussion

**Type:** review
**Keywords:** texture reads, anisotropic filtering, shader optimization, performance issues, game speed
**Concepts:** performance optimization, fragment shader, texture management

## Summary
The issue discusses excessive texture reads in the fragment shader, slowing down the game. Possible solutions include using separate shaders for textures with reflectivity/emission, merging emission and reflectivity textures into a single texture, or conditionally reading textures only if needed.

## Explanation
The discussion highlights that anisotropic filtering exacerbates performance issues related to too many texture reads in the fragment shader. Disabling anisotropic filtering is suggested as a temporary workaround to improve game speed. The maintainers propose several architectural changes to optimize texture usage, focusing on reducing the number of texture reads and improving overall performance.

## Related Questions
- How does anisotropic filtering affect texture read performance in the fragment shader?
- What are the potential benefits and drawbacks of using separate shaders for reflectivity/emission textures?
- Can merging emission and reflectivity textures into a single texture significantly improve performance?
- How can conditional texture reading be implemented to optimize shader performance?
- What impact does disabling anisotropic filtering have on overall game performance?
- Are there any potential regressions associated with the proposed solutions for reducing texture reads?

*Source: unknown | chunk_id: github_issue_456_discussion*
