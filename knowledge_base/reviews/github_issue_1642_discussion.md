# [issues/issue_1642.md] - Issue #1642 discussion

**Type:** review
**Keywords:** item migration, player inventories, human-readable, binary format, base64 encoding, nullability handling, permission system, management commands
**Symbols:** Item, player inventories, palette indices, base64 encoded binary data, ItemStack
**Concepts:** data migration, human-readable format, binary format, cheating prevention, performance optimization

## Summary
The discussion revolves around the migration of player inventories in Cubyz from a human-readable format to a binary format, with considerations for cheating prevention, performance, and maintainability.

## Explanation
The issue centers on how to handle item migrations in player inventories while maintaining readability for manual inspection. The maintainer suggests using base64-encoded binary data under `.playerInventory` and `.hand` keys as a compromise between human-readable format and efficiency. This approach involves toggling a boolean when any migration (items, blocks) is applied and looping through all saved inventories to load, substitute, and save them. For now, tools are ignored due to their lower priority compared to items and blocks.

The discussion also touches on the need for a permission system and management commands but concludes that these should be deferred until later stages of development due to complexity and potential risks. The final decision is to proceed with base64 encoding while addressing related issues like nullability handling in item stacks, which uses amount to indicate empty slots.

The recommended order of execution includes resolving dependencies such as #1443 (introduce ItemStack without ?Item) and #1290 (handle inventory storage). This ensures a seamless transition path for multiple storage formats. The feasibility of implementing a permission system is evaluated, but it is deemed more important to focus on getting Cubyz closer to version 0 than fixing broken systems.

Specifically, the maintainer proposes checking if any palette entries were migrated before applying further migrations and ignoring tools due to their lower priority compared to items and blocks. The discussion also highlights that introducing a permission system is complex and potentially risky, so it should be deferred until later stages of development.

## Related Questions
- What is the proposed solution for item migration in player inventories?
- Why was base64 encoding chosen as the storage format?
- How does the discussion address the issue of cheating prevention?
- What are the concerns regarding the implementation of a permission system?
- What is the recommended order of execution for related issues?
- How will nullability handling in item stacks be addressed?
- What are the potential benefits and drawbacks of using base64 encoding?
- How does the discussion balance performance optimization with maintainability?
- What steps are taken to ensure backward compatibility during migration?
- How is the feasibility of implementing a permission system evaluated?

*Source: unknown | chunk_id: github_issue_1642_discussion*
