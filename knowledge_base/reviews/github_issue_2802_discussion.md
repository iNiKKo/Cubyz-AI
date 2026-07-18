# [issues/issue_2802.md] - Issue #2802 discussion

**Type:** review
**Keywords:** allowCheats, permission group, server owner, cheats, flexible permissions
**Symbols:** allowCheats, default permission group
**Concepts:** permission management, server owner permissions

## Summary
The issue discusses replacing the `allowCheats` option with a default permission group to enhance server owner permissions and align with a more robust permission system.

## Explanation
The discussion revolves around improving the permission management in Cubyz by replacing the binary `allowCheats` flag with a more flexible default permission group. This change aims to provide greater control over player permissions, allowing the server owner to elevate their privileges beyond what is currently possible with the `allowCheats` option. The reviewers consider either implementing two default permission groups or maintaining a single group that strictly enforces no cheats if enabled. The primary motivation for this change is to align with a more comprehensive and customizable permission system.

## Related Questions
- What are the potential benefits of replacing `allowCheats` with a default permission group?
- How does this change impact backward compatibility with existing Cubyz servers?
- Can you provide examples of how the new permission system will be implemented?
- What are the security implications of allowing more granular control over server permissions?
- How will this change affect the user experience for server administrators?
- Are there any potential performance impacts associated with implementing a more complex permission system?

*Source: unknown | chunk_id: github_issue_2802_discussion*
