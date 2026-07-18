# [issues/issue_1403.md] - Issue #1403 discussion

**Type:** review
**Keywords:** SBB, blueprint, zon file, inlined declarations, ambiguity, strict contract, autocompletion, VS Code extension
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The discussion revolves around allowing inlined SBB (Structure Blueprint) declarations without needing separate zon files when SBBs have no children. The maintainer argues for explicit blueprint fields to avoid ambiguity and maintain strict contracts, while others suggest connecting IDs or creating VS Code extensions for better autocompletion.

## Explanation
The discussion revolves around allowing inlined SBB (Structure Blueprint) declarations without needing separate zon files when SBBs have no children. The maintainer argues for explicit blueprint fields to avoid ambiguity and maintain strict contracts, while others suggest alternative approaches like connecting IDs or creating VS Code extensions for better autocompletion.

Specifically, the syntax could be:
```zig
.{
    .blueprint = "cubyz:tree/oak/1/branch_3",
    .children = .{
        .crimson = .{
            .{.structure = "cubyz:tree/oak/1/leaf_1"},
            .{.structure = "cubyz:tree/oak/1/leaf_2"},
            .{.structure = "cubyz:tree/oak/1/leaf_3"},
        },
    },
}
```
Where `cubyz:tree/oak/1/leaf_1` must map to an existing blueprint asset.

The maintainer emphasizes the importance of explicit blueprint fields to prevent ambiguity and ensure clear error messages, advocating for a strict contract approach. They also discuss the independence of blueprints from SBBs and the potential for different use cases, such as segment-based maze generation. Other maintainers suggest alternative approaches like connecting IDs or creating VS Code extensions to improve autocompletion and readability.

The maintainer's suggestion for substitution maps at higher levels addresses the issue of shared blueprints across different SBBs by allowing substitutions to be defined only once at the root level.

## Related Questions
- What are the potential benefits and drawbacks of allowing inlined SBB declarations without separate zon files?
- How does the maintainer's approach to explicit blueprint fields address ambiguity in SBB definitions?
- What are the implications of keeping blueprints independent from SBBs for different use cases?
- How could a VS Code extension improve autocompletion for Cubyz IDs?
- What are the potential issues with connecting IDs in SBB definitions?
- How does the maintainer's suggestion for substitution maps at higher levels address the issue of shared blueprints across different SBBs?

*Source: unknown | chunk_id: github_issue_1403_discussion*
