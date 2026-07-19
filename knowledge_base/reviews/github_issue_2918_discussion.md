# [issues/issue_2918.md] - Issue #2918 discussion

**Type:** review
**Keywords:** attack swings, ECS, pickaxes, scythes, tool swing, slash swing, charged swings, block HP
**Symbols:** pickaxes, scythes, tool swing, slash swing
**Concepts:** Entity Component System (ECS), attack mechanics

## Summary
The issue discusses the implementation of different types of attack swings in the ECS system, specifically generic tool and slash swings, with potential future enhancements like charged swings.

## Explanation
This discussion revolves around defining two primary types of attack swings within the Entity Component System (ECS) framework: a generic tool swing for pickaxes and a generic slash swing for weapons like scythes. The tool swing is described as an overhead motion that corresponds to the tool's swing time and does not affect block health, while the slash swing is an arcing sideways movement that also corresponds to the weapon's swing time and impacts block health, allowing for multiple plant cuts in one swing. The user suggests adding charged swings as a future enhancement to allow for bigger hits or heavier weapon usage.

The generic tool swing used for pickaxes involves an overhead motion that does not affect block health. This means it is primarily used for mining blocks without damaging them. On the other hand, the generic slash swing used for weapons like scythes involves an arcing sideways movement that affects block health, enabling the player to cut down multiple plants in a single swing.

The user has proposed adding charged swings as a potential future enhancement. Charged swings would involve charging up a swing before using it, resulting in bigger hits or heavier weapon usage. This could add more depth and variety to combat scenarios, allowing players to execute powerful attacks when needed.

However, there are limitations to the current attack swing implementations that need to be considered. For instance, the overhead motion of the tool swing may not be suitable for all types of weapons, and the arcing sideways movement of the slash swing might not work well with certain block structures. Additionally, the addition of charged swings could potentially impact performance in combat scenarios, as players would need to manage their charge levels effectively.

To ensure compatibility with existing weapon types, developers must carefully consider how these new attack swing mechanics will interact with current gameplay elements. This includes balancing the power and speed of different weapons, as well as ensuring that the charged swings do not disrupt the overall flow of combat.

## Related Questions
- What are the specific mechanics of the generic tool swing?
- How does the generic slash swing differ from the tool swing?
- Can you explain the potential impact of charged swings on gameplay?
- Are there any limitations to the current attack swing implementations?
- How might the addition of charged swings affect performance in combat scenarios?
- What considerations are involved in ensuring compatibility with existing weapon types?

*Source: unknown | chunk_id: github_issue_2918_discussion*
