# [issues/issue_1800.md] - Issue #1800 discussion

**Type:** review
**Keywords:** lock sign, unlock mechanism, sign UI, chest labeling, multiple block entities, text copying, click-through functionality
**Concepts:** user interface, block entities, user experience

## Summary
Discussion about adding a 'lock sign' feature to prevent accidental editing of signs on chests, with considerations for unlocking mechanisms and alternative labeling methods.

## Explanation
Discussion about adding a 'lock sign' feature to prevent accidental editing of signs on chests, with considerations for unlocking mechanisms and alternative labeling methods. The maintainers suggest a way to unlock locked signs without breaking them but do not specify the mechanism. There are concerns about potential impacts on functionality like copying text from signs and the introduction of multiple block entities per block. A suggestion is made to add labels directly inside the chest UI as an alternative solution, but no details are provided on how this would affect user experience. Additionally, a Minecraft mod (clickthrough+) that allows users to click through signs placed on chests unless shift is held is mentioned as a possible solution.

## Related Questions
- How can we implement a lock/unlock mechanism for signs without allowing them to be broken?
- What are the potential impacts on performance if multiple block entities per block are introduced?
- How can we ensure that the 'lock sign' feature does not interfere with existing functionalities like text copying from signs?
- What alternative methods could be explored for labeling chests without using signs?
- How would adding a label inside the chest UI affect the overall user experience?
- Can the click-through functionality from Minecraft mods be integrated into Cubyz to solve this issue?

*Source: unknown | chunk_id: github_issue_1800_discussion*
