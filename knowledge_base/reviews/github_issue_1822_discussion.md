# [issues/issue_1822.md] - Issue #1822 discussion

**Type:** review
**Keywords:** achievements, tips, grindy, callbacks, stats, pickupItem, biomeTagVisited, custom art, GUI, dependencies, DAG, player autonomy, progression management
**Symbols:** Achievements, Tips, callbacks, stats, pickupItem, biomeTagVisited, custom art, GUI, dependencies, DAG
**Concepts:** Player autonomy, Grind prevention, Achievement conditions, Customization, Progression management

## Summary
The discussion revolves around implementing achievements and tips in Cubyz, focusing on player autonomy, avoiding grindy tasks, and defining achievement conditions.

## Explanation
The discussion revolves around implementing achievements in Cubyz, emphasizing player autonomy and avoiding grindy tasks. Achievements should have a name, short description, and custom image. Specific suggestions include breaking/placing blocks, crafting tools, gaining progression-relevant resources, chiseling blocks, sticking ores onto things, reaching the root or sky islands, and digging to certain depths. The maintainers suggest collecting player stats and using callbacks for achievements. Users propose condition types like item pickup and biome visit. Custom art for achievements is also discussed, with textures loaded in the GUI. There's debate about achievement dependencies to prevent players from pursuing unachievable goals. The final decision leans towards simpler depth-related challenges rather than revealing game content. Specific examples of proposed achievements include 'Awakening Wood' (collect wood), 'Hand Me My Shover' (craft a shover), and 'Deeper, Yet Deeper' (dig 1000 blocks below sea level). The syntax for conditions is as follows: ```zig .condition = .{ .stat = .toolsCrafted, .equals = 1, }, ``` for crafting the first tool, and ```zig .condition = .{ .pickupItem = "cubyz:void_stone", } ``` for picking up a specific item. Dependencies between achievements are managed by ensuring that players cannot pursue an achievement if they lack the necessary prerequisites.

## Related Questions
- How are player stats collected for achievements in Cubyz?
- What is the proposed method for implementing achievement callbacks?
- Can multiple conditions be used for a single achievement in Cubyz?
- Where should custom textures for achievements be loaded from?
- How will dependencies between achievements be managed in Cubyz?
- What are the potential drawbacks of having depth-related achievements in Cubyz?

*Source: unknown | chunk_id: github_issue_1822_discussion*
