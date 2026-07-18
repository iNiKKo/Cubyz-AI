# [issues/issue_1581.md] - Issue #1581 discussion

**Type:** review
**Keywords:** /sbb, blueprint, structure building block, save, delete, list, load, place, --world, --no-inline, --seed
**Symbols:** /sbb, <id>, --no-inline, --world, place, x, y, z, --seed
**Concepts:** Command-Line Interface (CLI), Modular Design, World Assets Management

## Summary
The `/sbb` command is introduced to allow players to save and manage structure building blocks (SBBs) along with their blueprints. It includes subcommands for saving, deleting, listing, loading, and placing SBBs.

## Explanation
The `/sbb` command extends the functionality of Cubyz by providing a comprehensive toolset for managing complex structures. The `--world` option allows users to save SBBs directly into world-specific assets, which is preferred over game-wide assets. This change ensures that structures are more modular and can be easily managed per-world, enhancing flexibility and organization within the game environment.

## Related Questions
- What is the purpose of the `--world` option in the `/sbb save` command?
- How does the `/sbb place` command differ from the `/paste` command?
- Can you explain the functionality of the `--no-inline` flag in the `/sbb save` command?
- What is the intended use case for the `--seed` parameter in the `/sbb place` command?
- How does the `/sbb` command handle child configurations when saving an SBB?
- What are the benefits of using world-specific assets instead of game-wide assets for SBBs?

*Source: unknown | chunk_id: github_issue_1581_discussion*
