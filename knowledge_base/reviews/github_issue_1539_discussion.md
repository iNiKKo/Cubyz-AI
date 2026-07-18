# [issues/issue_1539.md] - Issue #1539 discussion

**Type:** review
**Keywords:** mods directory, simple structure types, procedural generation, structure generator types, vtables, list file
**Concepts:** modding, procedural generation, structure loading

## Summary
The issue proposes allowing loading additional simple structure generator types from the mods directory to enable procedural generation of structures.

## Explanation
The discussion suggests extending the current structure loading mechanism to include simple structure generator types from the mods directory. This would allow for more flexibility in generating structures procedurally, leveraging modding capabilities. The maintainer's comment indicates that this should be straightforward since existing structures are loaded from a list file and utilize vtables.

## Related Questions
- What is the current mechanism for loading structures?
- How are vtables utilized in the existing structure loading process?
- What changes need to be made to allow loading from the mods directory?
- Are there any potential compatibility issues with existing mods?
- How will this feature impact performance?
- What additional generator types should be considered?
- Is there a plan for testing this new functionality?
- How will user-generated structures be integrated into the game world?
- What are the security implications of loading code from external directories?
- Are there any limitations on the complexity of structures that can be generated?

*Source: unknown | chunk_id: github_issue_1539_discussion*
