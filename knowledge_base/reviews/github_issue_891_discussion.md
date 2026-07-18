# [issues/issue_891.md] - Issue #891 discussion

**Type:** review
**Keywords:** block drops, visual artifacts, shader, item_drop.fs, raymarching, gl_FragDepth, depth calculations
**Symbols:** gl_FragDepth, gl_FragCoord.z, depth, gl_DepthRange.diff, gl_DepthRange.near, gl_DepthRange.far
**Concepts:** Shader programming, Fragment depth calculation, Visual rendering artifacts

## Summary
The maintainer attempted to resolve block drop visual artifacts by removing specific lines from the item drop shader, but the issue persisted.

## Explanation
The maintainer initially suspected that the issue might be related to raymarching code used in item drops. They suggested removing lines 89 and 176 from the `item_drop.fs` shader file, which handle fragment depth calculations. However, after testing these changes, the user reported no noticeable difference. The maintainer then identified a potential problem but did not provide further details on what was found or how it might resolve the issue.

## Related Questions
- What is the purpose of lines 89 and 176 in `item_drop.fs`?
- How does removing these lines affect the rendering of block drops?
- Is there a known issue with raymarching code causing visual artifacts?
- What other parts of the shader might be responsible for the artifact?
- Can the maintainer provide more details on the identified problem?
- Are there any logs or additional information that could help diagnose the issue?

*Source: unknown | chunk_id: github_issue_891_discussion*
