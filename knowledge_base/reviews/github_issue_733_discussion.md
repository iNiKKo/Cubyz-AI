# [issues/issue_733.md] - Issue #733 discussion

**Type:** review
**Keywords:** data format, JSON, ZON, syntax errors, editors, GitHub, PRs, asset files, code changes
**Symbols:** Cubyz, modded json, Zig Object Notation (ZON), zig extension
**Concepts:** syntax highlighting, editor compatibility, source code alignment

## Summary
Discussion about switching from modded JSON to Zig Object Notation (ZON) for Cubyz assets due to editor compatibility issues with hex colors and trailing commas. Maintainers suggest waiting until all PRs are completed before making such a significant change, as it would only affect asset files rather than code changes.

## Explanation
The issue discusses the current awkwardness of using modded JSON in Cubyz, which leads to syntax errors in many editors and GitHub due to unsupported hex color codes (e.g., `0xff222222`) and trailing commas. The proposal suggests switching to ZON, a format that aligns with source code and provides syntax highlighting if the Zig extension is used. However, it is noted that ZON is not widely supported in editors out of the box. The maintainer comments suggest waiting until all PRs are completed before making such a significant change, as it would only affect asset files rather than code changes. Specific examples include JSON issues like highlighted errors and unsupported syntax, while ZON offers better alignment with source code and potential benefits for future development.

## Related Questions
- What are the specific syntax issues in modded JSON that cause problems?
- How do hex color codes and trailing commas improve usability?
- Why is syntax highlighting important when using Zig extensions?
- What are the exact advantages of ZON over modded JSON for Cubyz assets?

*Source: unknown | chunk_id: github_issue_733_discussion*
