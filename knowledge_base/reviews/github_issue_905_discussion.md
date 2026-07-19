# [issues/issue_905.md] - Issue #905 discussion

**Type:** review
**Keywords:** stalactite blocks, billboard, dynamic texture, log rotation, chiseling, adjacent block updates, inventory clutter
**Concepts:** block placement, rotation mechanics, texture handling, collision detection

## Summary
Discussion on implementing stalactite blocks with unique placement and rotation mechanics, including potential changes to block support and texture handling.

## Explanation
The discussion revolves around implementing stalactite blocks in Cubyz with unique placement and rotation mechanics. Stalactites are decorative blocks that drop their stone type when broken and can be crafted from stone at a 1:1 ratio. They have three models: base, middle, and point, which can be changed using the chisel tool. The block's planar-ness allows for player-controllable variation in placement on ceilings or floors. There is discussion about making the texture dynamic based on the stone type it’s placed on but this is deemed complex. Log rotation to allow building them in any direction and starting with the largest thickness before allowing chiseling are suggested features. Naming conventions include 'stalagmite' and 'stem', with 'stem' being proposed as a more consistent term.

## Related Questions
- What are the potential performance implications of making stalactite textures dynamic?
- How can we implement log rotation without significantly increasing computational complexity?
- Are there any existing examples in Cubyz or other games that handle block support over longer distances?
- What are the benefits and drawbacks of using a billboard for stalactite blocks?
- How can we ensure that the chiseling feature does not introduce new bugs or inconsistencies?
- What is the current state of adjacent block updates in Cubyz, and how could they be improved?

*Source: unknown | chunk_id: github_issue_905_discussion*
