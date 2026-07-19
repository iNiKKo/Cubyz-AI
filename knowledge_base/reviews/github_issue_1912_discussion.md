# [issues/issue_1912.md] - Issue #1912 discussion

**Type:** review
**Keywords:** stripes, ground structure, zon notation, DSL, readability, consistency, syntax highlighting, documentation, context-aware snippets, Cubyz Dev Kit
**Symbols:** .stripes, cubyz:chalk/pink, cubyz:cloth/brown, cubyz:air, zon notation
**Concepts:** readability, consistency, declarative languages, DSL (Domain Specific Language), ZON notation

## Summary
The discussion revolves around improving the readability and verbosity of Cubyz's configuration files by proposing changes to the stripes and ground structure definitions. The maintainer argues against introducing nested declarative languages within ZON notation, citing issues with readability and consistency.

## Explanation
The discussion revolves around improving the readability and verbosity of Cubyz's configuration files by proposing changes to the stripes and ground structure definitions. The maintainer argues against introducing nested declarative languages within ZON notation, citing issues with readability and consistency.

Specifically, the user proposes a more concise way to define stripes using arrays of blocks instead of individual structures:
```zig
.stripes = .{
    .direction = .{0, 0, 1},
    .blocks = .{
        "1 cubyz:chalk/pink",
        "1 cubyz:chalk/magenta",
        "1 cubyz:chalk/violet",
        "1 cubyz:chalk/purple",
        "1 cubyz:chalk/violet",
        "1 cubyz:chalk/magenta",
    },
},
```
The maintainer rejects this idea, emphasizing that embedding structured data within a blob of characters without syntax highlighting reduces readability. The maintainer also expresses concern about the potential for creating multiple DSLs on top of ZON notation, which could lead to complexity and inconsistency across configuration files.

The user provides examples showing how ZON-only notation can become less readable compared to established declarative systems:
```zig
ground_structure = .{
    "1 cubyz:cloth/brown:0b111111",
    "5 cubyz:air",
}
```
With zon only:
```zig
.ground_structure = .{
    .{.count = 1, .mod = "cubyz", .item = "cloth/brown", .data = "0b111111"},
    .{.count = 5, .mod = "cubyz", .item = "air"},
}
```
The maintainer suggests using tuples where the meaning is clear but warns against overusing them in places where implicit structures might confuse users:
```zig
.ground_structure = .{
    .{3, "cubyz:xyz"},
    .{5, "cubyz:xyz"},
}
```
The maintainer also discusses the need for documentation and context-aware snippets to aid users in understanding configuration files. Both parties agree that explicitness and consistency are important.

## Related Questions
-  What is the proposed alternative way to define stripes using arrays of blocks instead of individual structures?
-  How does embedding structured data within a blob of characters without syntax highlighting affect readability according to the maintainer?
-  Can you provide examples showing how ZON-only notation can become less readable compared to established declarative systems?
-  What is the maintainer's stance on using tuples in configuration files, and why?

*Source: unknown | chunk_id: github_issue_1912_discussion*
