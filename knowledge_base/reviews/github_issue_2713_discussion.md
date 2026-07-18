# [issues/issue_2713.md] - Issue #2713 discussion

**Type:** review
**Keywords:** hotreloading textures, keybind, speed up development, biomes, automatic texture reloading
**Concepts:** hotreloading, keybind, development speed

## Summary
The issue discusses making hotreloading textures a keybind for faster development, with an additional suggestion to extend this feature to biomes.

## Explanation
The discussion revolves around the existing functionality of automatic texture hotreloading in Cubyz. The reporter suggests enhancing this by allowing it to be triggered via a keybind, which could significantly speed up the development process. Additionally, there is a proposal to extend this feature to include biome changes as well. The maintainer notes that the current implementation is supposed to handle texture reloading automatically through anisotropic filtering. However, there is no specific keybind for this feature yet. Extending hotreloading to biomes would involve additional development work to ensure that changes in biome settings are also reflected immediately without needing a full reload. There may be potential performance implications of adding a keybind for texture hotreloading, as frequent reloading could impact game performance if not managed properly. The user experience benefits of making texture hotreloading a keybind include faster iteration during development and reduced downtime caused by manual texture reloads. The configuration file that controls automatic texture reloading in Cubyz is not explicitly mentioned in the issue discussion. However, it is likely related to the game's settings or configuration files where various rendering options are managed.

## Related Questions
- What is the current implementation of hotreloading textures in Cubyz?
- How can we implement a keybind for hotreloading textures?
- Are there any potential performance implications of adding a keybind for texture hotreloading?
- Can you provide more details on how to extend hotreloading to biomes?
- What are the user experience benefits of making texture hotreloading a keybind?
- Is there a configuration file that controls automatic texture reloading in Cubyz?

*Source: unknown | chunk_id: github_issue_2713_discussion*
