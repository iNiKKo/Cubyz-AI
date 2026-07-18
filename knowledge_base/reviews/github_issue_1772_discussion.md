# [issues/issue_1772.md] - Issue #1772 discussion

**Type:** review
**Keywords:** planar rotation bug, facing down, placing backwards, looking up, block orientation
**Concepts:** block placement, player orientation

## Summary
The issue describes a bug where planar blocks are placed backwards when the player is facing down or up.

## Explanation
The problem arises from incorrect handling of block placement orientation based on the player's direction. The reviewer notes that this error occurs not only when facing down but also when looking straight up, indicating a potential issue with how the game determines the correct face for placing blocks in these orientations.

## Related Questions
- What is the current logic for determining block placement based on player orientation?
- Are there any existing tests that cover placing blocks in different orientations?
- How does the game handle block rotation when the player is facing down or up?
- Is there a specific function responsible for calculating the correct face for block placement?
- What changes need to be made to fix the bug where blocks are placed backwards?
- Are there any related issues that might affect block placement in other orientations?

*Source: unknown | chunk_id: github_issue_1772_discussion*
