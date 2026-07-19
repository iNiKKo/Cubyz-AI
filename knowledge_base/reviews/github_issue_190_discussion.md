# [issues/issue_190.md] - Issue #190 discussion

**Type:** review
**Keywords:** grass texture, natural terrain, biome integration, side textures, connected textures, rotation mode, block transitions, ore treatment
**Symbols:** grass, dirt, side textures, connected textures, rotation mode, biomes
**Concepts:** texture mapping, biome design, block interaction

## Summary
Discussion about redesigning the grass texture in Cubyz to improve natural terrain appearance and biome integration.

## Explanation
The issue revolves around redesigning the current grass texture in Cubyz to improve natural terrain appearance and biome integration. The discussion highlights that the current grass texture shows dirt on the sides, which is undesirable for natural terrain. One solution proposed is using full side textures, but this could look bad when placed on top of a regular dirt block. Another suggestion is using a connected textures approach to ensure seamless transitions between grass blocks. The maintainers suggest that grass should use a specific side texture if there isn't another grass block to connect to. Users propose having the grass texture on all sides with transitions controlled by biome settings (Issue #889). This approach allows biomes to control their color palette more effectively and enables players to build with 6-sided grass blocks seamlessly transitioning to any other block type. There is also consideration of treating grass like an ore for better integration, but concerns arise about distinguishing between connecting to a grass layer below or not.

## Related Questions
- How can the grass texture be modified to avoid showing dirt on the sides?
- What are the benefits of using full side textures for grass blocks?
- How does the connected textures approach improve the appearance of grass blocks?
- Why is it important to have unique side textures for grass blocks?
- What are the potential drawbacks of treating grass like an ore in Cubyz?
- How can transitions between grass and other blocks be controlled by biome settings?

*Source: unknown | chunk_id: github_issue_190_discussion*
