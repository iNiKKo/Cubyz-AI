# [issues/issue_1589.md] - Issue #1589 discussion

**Type:** review
**Keywords:** tool slots, optional slots, texture check, flood fill, balancing, wacky designs, handle, tip, gimmick, viable
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The discussion revolves around making tool slots in Cubyz optional, focusing on the technical implications and potential impact on balancing.

## Explanation
The proposal suggests that only mandatory slots need to be connected based on the tool texture. The maintainer explains that this would involve a flood fill check to ensure all pixels are connected. There is concern about how this might complicate balancing, as it could introduce more 'basic pickaxe' possibilities. The user proposes separating tools into handle and tool_part for clarity, but the maintainer notes that this would not change the location of the tip or handle. The discussion also touches on whether these designs are meant to be viable or just gimmicks, with a potential impact on balance if some designs become viable.

## Related Questions
- What is the technical process for checking if all pixels are connected in the tool texture?
- How might the proposed changes impact the game's balancing?
- Can players create disconnected handles and tips with the new system?
- What are the potential benefits of making tool slots optional?
- How does separating tools into handle and tool_part affect gameplay?
- Are there any memory implications from implementing this feature?

*Source: unknown | chunk_id: github_issue_1589_discussion*
