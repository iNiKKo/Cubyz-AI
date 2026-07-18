# [issues/issue_1912.md] - Issue #1912 discussion

**Type:** review
**Keywords:** stripes, ground structure, zon notation, DSL, readability, consistency, syntax highlighting, documentation, context-aware snippets, Cubyz Dev Kit
**Symbols:** .stripes, cubyz:chalk/pink, cubyz:cloth/brown, cubyz:air, zon notation
**Concepts:** readability, consistency, declarative languages, DSL (Domain Specific Language), ZON notation

## Summary
The discussion revolves around improving the readability and verbosity of Cubyz's configuration files by proposing changes to the stripes and ground structure definitions. The maintainer argues against introducing nested declarative languages within ZON notation, citing issues with readability and consistency.

## Explanation
The user proposes a more concise way to define stripes using arrays of blocks instead of individual structures. However, the maintainer rejects this idea, emphasizing that embedding structured data within a blob of characters without syntax highlighting reduces readability. The maintainer also expresses concern about the potential for creating multiple DSLs on top of ZON notation, which could lead to complexity and inconsistency across configuration files. The user provides examples showing how ZON-only notation can become less readable compared to established declarative systems. The maintainer suggests using tuples where the meaning is clear but warns against overusing them in places where implicit structures might confuse users. Both parties agree that explicitness and consistency are important, and they discuss the need for documentation and context-aware snippets to aid users in understanding configuration files.

## Related Questions
- What are the potential drawbacks of using nested declarative languages within ZON notation?
- How does the maintainer suggest improving the readability of configuration files without introducing new DSLs?
- Can you provide examples of how ZON-only notation can become less readable compared to established declarative systems?
- What is the maintainer's stance on using tuples in configuration files, and why?
- How does the discussion highlight the importance of explicitness and consistency in configuration file design?
- What solutions are proposed to help users understand complex configuration files?

*Source: unknown | chunk_id: github_issue_1912_discussion*
