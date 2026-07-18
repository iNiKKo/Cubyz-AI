# [issues/issue_2666.md] - Issue #2666 discussion

**Type:** review
**Keywords:** avatar, permissions, admin rights, world specific file, permission system, avatar system, manual permission checks, default permissions, command logic, entity models
**Symbols:** /avatar, cubyz:snale, cubyz:cubert, cubyz:missing, #1425, #2641, #2652, #2540, source.hasPermission
**Concepts:** Permissions, Command System, Entity Models, World Configuration, Default Permissions

## Summary
Discussion on implementing permissions for the /avatar command, considering both user-defined and admin-only entity models.

## Explanation
The discussion revolves around adding permissions to the /avatar command in Cubyz. The proposal involves two types of entity models: one accessible by everyone and another restricted to users with admin rights. A world-specific file would define which models are allowed for everyone. The implementation is contingent on the completion of the permission system (#1425) and the avatar system (#2641 / #2652). Users suggest an alternative approach if the permission system cannot be waited for, involving manual permission checks within the command logic. There's also a mention of the need for default permissions or a default permission group (#2540) to handle cases where no specific permissions are defined.

## Related Questions
- What is the proposed alternative approach for implementing avatar permissions if the permission system cannot be completed?
- How does the world-specific file define which entity models are accessible to everyone?
- What is the role of the default permission group in handling cases where no specific permissions are defined?
- Can you explain how the manual permission checks within the command logic work?
- What are the dependencies for implementing the avatar permissions feature?
- How does the current implementation handle user-defined and admin-only entity models?
- What is the impact of the permission system on the /avatar command?
- How can the default permission group be integrated into the existing permission framework?
- What are the potential security implications of allowing users to pick certain avatar models based on permissions?
- How does the world-specific file interact with the permission system to enforce access control?

*Source: unknown | chunk_id: github_issue_2666_discussion*
