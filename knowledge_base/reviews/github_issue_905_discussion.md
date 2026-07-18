# [issues/issue_905.md] - Issue #905 discussion

**Type:** review
**Keywords:** stalactite blocks, billboard, dynamic texture, log rotation, chiseling, adjacent block updates, inventory clutter
**Concepts:** block placement, rotation mechanics, texture handling, collision detection

## Summary
Discussion on implementing stalactite blocks with unique placement and rotation mechanics, including potential changes to block support and texture handling.

## Explanation
The discussion revolves around the implementation of stalactite blocks in Cubyz. The primary concerns include the block's ability to be placed on ceilings and floors, its rotation mechanics, and how it interacts with other blocks. Maintainers suggest that the block could be a billboard to save faces and improve appearance, but users argue against this due to potential collision issues and lack of uniqueness compared to Minecraft. There is also discussion about making the block's texture dynamic based on the stone type it's placed on, though this is deemed complex. The team considers adding log rotation for more flexible building options and suggests starting with the largest thickness and allowing chiseling to reduce complexity. Naming conventions are also discussed, with suggestions ranging from 'stalagmite' to 'stem'.

## Related Questions
- What are the potential performance implications of making stalactite textures dynamic?
- How can we implement log rotation without significantly increasing computational complexity?
- Are there any existing examples in Cubyz or other games that handle block support over longer distances?
- What are the benefits and drawbacks of using a billboard for stalactite blocks?
- How can we ensure that the chiseling feature does not introduce new bugs or inconsistencies?
- What is the current state of adjacent block updates in Cubyz, and how could they be improved?

*Source: unknown | chunk_id: github_issue_905_discussion*
