# [issues/issue_1622.md] - Issue #1622 discussion

**Type:** review
**Keywords:** two-handed layout, secondary hand, keybindings, UI complexity, dedicated slots, shields, torches
**Concepts:** user interface, game mechanics, player experience

## Summary
The discussion revolves around implementing a two-handed layout feature in Cubyz, where players can use both hands for different items. The maintainer argues that the feature might be unnecessary and could complicate the UI, while the user emphasizes the need for secondary hand functionality for specific actions like using shields or torches.

## Explanation
The discussion centers around adding a two-handed layout feature to Cubyz, allowing players to use both hands for different items. The maintainer raises concerns about the complexity and potential redundancy of this feature, suggesting that it might not be necessary given existing mechanics. They also point out that implementing such a feature could complicate the user interface and require new keybindings.

The proposed layout includes:
- Main hand item use - left click
- Main hand item alternative use - right click
- Secondary hand use - hold alt + left
- Secondary hand alt use - hold alt + right

Holsters provide two additional slots to switch with when pressing tab. The layout is as follows:
1[pickaxe]
2 [torch]
t1[sword]
t2 [_]
After pressing tab, the layout changes to:
1[sword]
2 [_]
t1[pickaxe]
t2 [torch]

The maintainer also mentions that if a player never used secondary hand functionality in games, they likely don't care. However, for those who did use it actively, this is an extra degree of freedom they may not want to let go easily.

Additionally, the maintainer suggests adding dedicated slots for items like shields rather than implementing a full two-handed system. They argue that such a feature could be redundant and complicate the UI with new keybindings.

## Related Questions
- What are the potential benefits and drawbacks of implementing a two-handed layout in Cubyz?
- How might the addition of a secondary hand affect gameplay balance and player experience?
- What alternative solutions could be considered for providing specific actions like using shields or torches?
- How would the implementation of a two-handed system impact modding capabilities in Cubyz?
- What are the potential usability issues with adding new keybindings for a two-handed layout?
- How might the current UI design accommodate additional features like a secondary hand?

*Source: unknown | chunk_id: github_issue_1622_discussion*
