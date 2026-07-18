# [issues/issue_1852.md] - Issue #1852 discussion

**Type:** review
**Keywords:** vanity equipment slots, chest and legs, cloth texture, second texture layer, clothing model, rendering complexity, armor layers, bulkiness, undergarments, non-revealing clothing
**Concepts:** texture mapping, model rendering, animation handling, user interface design

## Summary
The discussion revolves around adding vanity equipment slots for chest and legs to the Snale model, including how to map textures, handle animations, and decide on the design of the clothing.

## Explanation
The issue proposes adding two vanity equipment slots for chest and legs to the Snale model in Cubyz. The main points of discussion include mapping cloth onto the Snale model using a second texture layer, deciding whether clothes should be cubic or have slopes, and how the client will know what other players are wearing. There is also debate on whether clothes should be separate models or just texture overlays, with concerns about rendering complexity and potential bulkiness if they are separate models. The maintainers suggest that clothes should be their own models to avoid issues seen in Minecraft 1.8 where armor layers became bulky. The discussion touches on practical considerations like the possibility of taking off clothes and the implications of Snale wearing undergarments, with a suggestion to keep them non-revealing but not entirely covering.

## Related Questions
- How does the Snale model currently handle texture mapping?
- What are the potential issues with making clothes a separate model?
- How will the client determine what other players are wearing?
- Can the clothing design be made to have slopes without affecting rendering?
- What is the current status of adding vanity equipment slots in Cubyz?
- Are there any plans to allow customization of Snale's appearance beyond the initial random colors?
- How does the discussion address the practicality of taking off clothes in-game?
- What are the implications of Snale wearing undergarments in the game design?
- Is there a timeline for implementing this feature in Cubyz?
- How will the new clothing system interact with existing animations and movements?

*Source: unknown | chunk_id: github_issue_1852_discussion*
