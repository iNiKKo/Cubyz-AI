# [issues/issue_1805.md] - Issue #1805 discussion

**Type:** review
**Keywords:** structure table, biome tags, modular design, asset loading, flexible structure spawning, biome tagging, hashing functions, maintenance of existing system, force push, code organization
**Symbols:** structure_table, biomeTags, structures, zon file, src/server/terrain/biomes.zig, src/utils/hash.zig, src/server/terrain/hash.zig
**Concepts:** modular design, asset loading, flexible structure spawning, biome tagging

## Summary
The discussion revolves around modifying the structure table system in Cubyz to be biome-independent, allowing for more flexible and generic structure spawning across different biomes using tags.

## Explanation
The proposal introduces a new structure table type that includes an ID, biome tags (like 'cubyz:cold'), and structures. Biomes will no longer directly store structure tables but instead use biome tags to associate with structure tables. During asset loading, structure tables are loaded from specific directories such as `assets/cubyz/structure_tables` or `assets/<addon_name>/structure_tables`. The system builds a list of structure table IDs for lookup later.

Biomes concatenate relevant structure tables based on matching biome tags or lack thereof during the asset loading process. If a structure table has a biometag that matches the biome, or if it has no biometag, its contents are concatenated to the biome's internal structure table. The total chance is added as before and normalized if greater than 1.

The maintainer emphasizes that this change is intended to extend the existing system rather than replace it, allowing for structures not tied to specific biomes. There's a suggestion to maintain both versions of the system if feasible. Additionally, hashing functions may need to be moved out of `src/server/terrain/biomes.zig` and into `src/utils/hash.zig` or `src/server/terrain/hash.zig`, depending on usage.

The revised proposal includes the following steps:
- New structure table type that encapsulates: id, biomeTags (cubyz:cold, cubyz:hot, etc), structures (biomes.structures as we currently know it)
- Biomes now store a biomeTags element to associate structure tables to biomeTags
- During asset loading:
  - Structure Tables
    - Load each available .zon in assets/cubyz/structure_tables (or assets/addon_name/structure_tables)
    - Builds a `[][] const u8` of the structure table IDs to lookup later
  - Biomes
    - Load structures as we did before, then:
      - Loop through all loaded structure tables (via the ID list from earlier, Structure Tables would need a getById or something)
      - If a structure table has a biometag that matches the biome, or the structure table has no biometag, concatenate the contents of that structure table to the biome's internal structure table
      - Add totalChance as we did before, normalize if greater than 1 as we did before.

The revised proposal aims to maintain both versions of the system if feasible. The maintainer suggests moving hashing functions out of `src/server/terrain/biomes.zig` and into `src/utils/hash.zig` or `src/server/terrain/hash.zig`, depending on usage.

Regarding backward compatibility, the new system is designed to extend rather than replace the existing structure table system. This means that existing biomes with their own structure tables will continue to function as they do now. The revised proposal does not explicitly address potential performance impacts but suggests that careful consideration should be given to ensure efficient asset loading and processing.

## Related Questions
- What is the purpose of the new structure table type in Cubyz?
- How does the revised proposal handle biome-specific structure tables?
- Where are structure tables loaded from during asset loading?
- Why is it important to maintain both versions of the system if feasible?
- What changes are needed in the hashing functions for this implementation?
- How does the new system ensure backward compatibility with existing biomes?
- What potential performance impacts might arise from the new structure table system?
- How does the revised proposal address the issue of unorganized structures in biome files?
- What is the role of biome tags in associating structure tables to biomes?
- How does the system handle cases where a structure table has no biome tag?

*Source: unknown | chunk_id: github_issue_1805_discussion*
