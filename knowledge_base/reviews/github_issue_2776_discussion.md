# [issues/issue_2776.md] - Issue #2776 discussion

**Type:** review
**Keywords:** force, group, all, targeting options, selector symbols, filtering, offline players, permission groups, entities, versatile commands
**Symbols:** Target, _command.zig
**Concepts:** Command System, Targeting Options, Selector Symbols, Filtering

## Summary
Discussion on adding more targeting options for commands in Cubyz, including suggestions like 'force', 'group', and 'all'. The proposal includes new selector symbols for players, entities, groups, and filtering.

## Explanation
Discussion on adding more targeting options for commands in Cubyz, including suggestions like 'force', 'group', and 'all'. The proposal includes new selector symbols for players ('@'), entities ('&'), groups ('$'), and filtering ('?'). Specific examples include selecting all entities within a range (`&?r=5`), offline players (`!&`), and filtering based on criteria (`&?x=20,dx=10,y=200,dy=3,z=50,dz=20`). The proposal aims to increase the versatility of commands while avoiding direct imitation of Minecraft's command syntax. However, certain symbols like `#`, `*`, `__`, `~~`, and `§` are blocked due to formatting issues. There is also a discussion about replacing `#` with `&` or other special characters to avoid confusion.

## Related Questions
- What are the proposed new targeting options for commands in Cubyz?
- How do the proposed selector symbols differentiate between targets?
- Can offline players be targeted with the proposed 'force' option?
- What is the purpose of the '?' symbol in the filtering mechanism?
- Are there any limitations on using special characters as selector symbols?
- How does the proposal ensure compatibility with existing command syntax?
- What are the potential performance implications of adding more targeting options?
- Can entities be targeted without specifying a range or criteria?

*Source: unknown | chunk_id: github_issue_2776_discussion*
