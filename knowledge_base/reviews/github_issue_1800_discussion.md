# [issues/issue_1800.md] - Issue #1800 discussion

**Type:** review
**Keywords:** lock sign, unlock mechanism, sign UI, chest labeling, multiple block entities, text copying, click-through functionality
**Concepts:** user interface, block entities, user experience

## Summary
Discussion about adding a 'lock sign' feature to prevent accidental editing of signs on chests, with considerations for unlocking mechanisms and alternative labeling methods.

## Explanation
The discussion revolves around the addition of a 'lock sign' toggle in the Cubyz game to prevent users from accidentally opening the sign UI when interacting with chests. The maintainers express concerns about how to unlock locked signs without breaking them, as well as the potential impact on functionality like copying text from signs. There is also a suggestion for adding labels directly inside the chest UI as an alternative solution. The conversation touches on architectural considerations such as handling multiple block entities per block and user experience improvements.

## Related Questions
- How can we implement a lock/unlock mechanism for signs without allowing them to be broken?
- What are the potential impacts on performance if multiple block entities per block are introduced?
- How can we ensure that the 'lock sign' feature does not interfere with existing functionalities like text copying from signs?
- What alternative methods could be explored for labeling chests without using signs?
- How would adding a label inside the chest UI affect the overall user experience?
- Can the click-through functionality from Minecraft mods be integrated into Cubyz to solve this issue?

*Source: unknown | chunk_id: github_issue_1800_discussion*
