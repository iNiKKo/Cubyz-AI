# [issues/issue_1822.md] - Issue #1822 discussion

**Type:** review
**Keywords:** achievements, tips, grindy, callbacks, stats, pickupItem, biomeTagVisited, custom art, GUI, dependencies, DAG, player autonomy, progression management
**Symbols:** Achievements, Tips, callbacks, stats, pickupItem, biomeTagVisited, custom art, GUI, dependencies, DAG
**Concepts:** Player autonomy, Grind prevention, Achievement conditions, Customization, Progression management

## Summary
The discussion revolves around implementing achievements and tips in Cubyz, focusing on player autonomy, avoiding grindy tasks, and defining achievement conditions.

## Explanation
The issue discusses the implementation of achievements in Cubyz, emphasizing that they should not be intrusive or grindy. The maintainers suggest collecting player stats and using callbacks for certain achievements. Users propose various condition types like item pickup and biome visit. The maintainers consider multiple conditions but decide to focus on a list style initially. Custom art for achievements is also discussed, with textures loaded in the GUI. There's debate about achievement dependencies to prevent players from pursuing unachievable goals. The final decision leans towards simpler depth-related challenges rather than revealing game content.

## Related Questions
- How are player stats collected for achievements in Cubyz?
- What is the proposed method for implementing achievement callbacks?
- Can multiple conditions be used for a single achievement in Cubyz?
- Where should custom textures for achievements be loaded from?
- How will dependencies between achievements be managed in Cubyz?
- What are the potential drawbacks of having depth-related achievements in Cubyz?

*Source: unknown | chunk_id: github_issue_1822_discussion*
