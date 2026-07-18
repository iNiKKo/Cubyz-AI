# [issues/issue_733.md] - Issue #733 discussion

**Type:** review
**Keywords:** data format, JSON, ZON, syntax errors, editors, GitHub, PRs, asset files, code changes
**Symbols:** Cubyz, modded json, Zig Object Notation (ZON), zig extension
**Concepts:** syntax highlighting, editor compatibility, source code alignment

## Summary
Discussion about switching from modded JSON to a different data format like Zig Object Notation (ZON) for Cubyz assets.

## Explanation
The issue discusses the current awkwardness of using modded JSON in Cubyz, which leads to syntax errors in many editors and GitHub. The proposal suggests switching to ZON, which aligns with the source code and provides syntax highlighting if the Zig extension is used. However, it is noted that ZON is not widely supported in editors out of the box. The maintainer comments suggest waiting until all PRs are completed before making such a significant change, as it would only affect asset files rather than code changes.

## Related Questions
- What are the potential benefits of switching to ZON for Cubyz assets?
- Why is syntax highlighting important in this context?
- How does the maintainer's comment impact the timeline of this change?
- What are the disadvantages of using a custom format for Cubyz assets?
- How might the lack of editor support for ZON affect user experience?
- Can you explain the advantages and disadvantages of using trailing commas in JSON?
- Why is alignment with source code considered an advantage for data formats?
- How does the maintainer's comment address the impact on open PRs?
- What are the potential risks associated with making such a significant change to Cubyz?
- How might the choice of data format affect future development and maintenance?

*Source: unknown | chunk_id: github_issue_733_discussion*
