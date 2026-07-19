# [issues/issue_3316.md] - Issue #3316 discussion

**Type:** review
**Keywords:** custom limited world sizes, X & Y axis parameters, entity spawn conditions, custom dimensions, ring worlds, modders, engine groundwork
**Concepts:** engine capabilities, modding, world generation, architectural changes

## Summary
The issue discusses potential enhancements to Cubyz's engine capabilities for creators, including custom limited world sizes, X & Y axis parameters, entity spawn conditions, and custom dimensions. Maintainers express concerns about the impact on existing engine groundwork and suggest alternative approaches like using mods or new world types.

## Explanation
The issue discusses potential enhancements to Cubyz's engine capabilities for creators, including custom limited world sizes (X, Y, and Z), X & Y axis parameters (ring worlds with climate properties based on map type), entity spawn conditions, and custom dimensions. Maintainers express concerns about the impact of these changes on existing engine groundwork and suggest alternative approaches like using mods or new world types. Specifically, they clarify that certain features such as custom dimensions are unlikely to be implemented due to their significant impact on the engine's foundation. The discussion includes details on how ring worlds could be implemented with climate properties based on map type rather than just wavelength, and mentions that entity spawn conditions would involve setting specific conditions for when entities can spawn in the world. Additionally, it is mentioned that custom limited world sizes (X, Y, and Z) will fit in with #310, and X & Y Axis Layers are similar to layers of the Z-axis.

## Related Questions
- What are the potential impacts of implementing custom limited world sizes on Cubyz's engine?
- How can modders achieve similar effects to custom dimensions without altering the base engine?
- What alternative approaches were suggested for adding X & Y axis parameters (ring worlds) to Cubyz?
- Why is there a concern about rewriting the engine for features that won't be used in the base game?
- Can ring worlds be implemented as an alternative to custom dimensions in Cubyz, and how would climate properties work?
- How might entity spawn conditions be integrated into the existing world generation system?

*Source: unknown | chunk_id: github_issue_3316_discussion*
