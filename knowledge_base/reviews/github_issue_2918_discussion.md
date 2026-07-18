# [issues/issue_2918.md] - Issue #2918 discussion

**Type:** review
**Keywords:** attack swings, ECS, pickaxes, scythes, tool swing, slash swing, charged swings, block HP
**Symbols:** pickaxes, scythes, tool swing, slash swing
**Concepts:** Entity Component System (ECS), attack mechanics

## Summary
The issue discusses the implementation of different types of attack swings in the ECS system, specifically generic tool and slash swings, with potential future enhancements like charged swings.

## Explanation
This discussion revolves around defining two primary types of attack swings within the Entity Component System (ECS) framework: a generic tool swing for pickaxes and a generic slash swing for weapons like scythes. The tool swing is described as an overhead motion that does not affect block health, while the slash swing is an arcing sideways movement that impacts block health, allowing for multiple plant cuts in one swing. The user suggests adding charged swings as a future enhancement to allow for bigger hits or heavier weapon usage.

## Related Questions
- What are the specific mechanics of the generic tool swing?
- How does the generic slash swing differ from the tool swing?
- Can you explain the potential impact of charged swings on gameplay?
- Are there any limitations to the current attack swing implementations?
- How might the addition of charged swings affect performance in combat scenarios?
- What considerations are involved in ensuring compatibility with existing weapon types?

*Source: unknown | chunk_id: github_issue_2918_discussion*
