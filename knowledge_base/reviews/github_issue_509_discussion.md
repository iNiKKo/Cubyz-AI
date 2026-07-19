# [issues/issue_509.md] - Issue #509 discussion

**Type:** review
**Keywords:** water animation, fade effect, minecraft campfire, prismarine block, Super Mario Galaxy, texture scrolling, procedural liquids
**Concepts:** animation, fading effect, liquid rendering, procedural generation

## Summary
Discussion about implementing a fading option for block animations, focusing on its application to water and other liquid rendering.

## Explanation
Discussion about implementing a fading option for block animations, focusing on its application to water and other liquid rendering. The maintainer initially presents a quick and dirty prototype of water with smooth animation but finds it unsatisfactory due to the frames not being designed for smooth transitions (e.g., https://github.com/user-attachments/assets/9591d351-38d6-4a53-87b8-94a42574f02c) and the entire surface moving in unison, which looks weird. Suggestions include using large textures that scroll over the liquid (e.g., https://www.youtube.com/watch?v=8rCRsOLiO7k&ab_channel=Jasper) or procedural generation techniques, inspired by examples like those seen in Super Mario Galaxy (e.g., https://www.youtube.com/watch?v=pGOLstWBCDA). The user provides successful fading effect examples from Minecraft, specifically mentioning the glowing charcoal on campfires (https://minecraft.wiki/images/Campfire_JE2_BE2.gif?742be) and the prismarine block.

## Related Questions
- What are the specific issues with the current water animation prototype?
- How can large textures be used to improve liquid rendering in Cubyz?
- Can procedural generation techniques be effectively applied to render liquids like water in Cubyz?
- What examples of successful fading effects from Minecraft were mentioned in the discussion?
- Why is synchronized movement of the entire water surface considered problematic for animation?

*Source: unknown | chunk_id: github_issue_509_discussion*
