# [issues/issue_2432.md] - Issue #2432 discussion

**Type:** review
**Keywords:** addon content, in-game content, duplicate names, vanilla content, modding systems, namespace conflicts, backward compatibility
**Concepts:** modding systems, namespace conflicts, backward compatibility

## Summary
The issue discusses prioritizing addon content over in-game content when duplicate names are found, raising concerns about modding systems and potential conflicts.

## Explanation
The issue proposes that the game should prioritize addon content over in-game content when duplicate names are found. Specifically, if an addon biome with the same name as a vanilla biome is found, only the addon biome should generate, allowing addon creators to overhaul existing features. This would allow for far greater creativity and enable addon creators to edit vanilla content. However, this approach raises concerns about modding systems and potential conflicts when playing multiple addons simultaneously.

The maintainer argues against this idea, stating that it can already be achieved by using the same addon name and placing it in the per world assets folder. Additionally, having separate namespaces for addons is crucial to avoid conflicts when using multiple addons, as it ensures that different mods do not interfere with each other.

Currently, if an addon biome with the same name as a vanilla biome is found, only the addon biome will generate. This behavior can be achieved by placing the addon in the per world assets folder and ensuring it has the same name as the vanilla content. The game uses separate namespaces for addons to prevent conflicts when multiple mods are used simultaneously.

## Related Questions
- How can the game be modified to prioritize addon content over in-game content without causing namespace conflicts?
- What are the potential risks of allowing addon creators to overwrite vanilla content?
- How can a robust modding system be developed to handle multiple addons without interference?
- What is the current mechanism for handling duplicate names between addon and in-game content?
- How does the game currently manage namespaces for different mods?
- What are the implications of prioritizing addon content on backward compatibility?

*Source: unknown | chunk_id: github_issue_2432_discussion*
