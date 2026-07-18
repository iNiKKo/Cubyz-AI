# [issues/issue_2446.md] - Issue #2446 discussion

**Type:** review
**Keywords:** execute command, server owners, moderators, impersonation, private messages, security through obscurity, administrators, limited command permissions
**Concepts:** security, moderator abuse, permissions

## Summary
Discussion about adding an execute command feature for server owners and moderators.

## Explanation
The issue revolves around the potential addition of an `/execute` command that allows server owners or moderators to run commands as a specific player. The maintainers argue against this feature due to security concerns, specifically the risk of moderator abuse through impersonation via private messages. They suggest instead using separate commands with distinct permissions for such actions. The discussion also touches on the distinction between administrators who can modify server code and moderators who cannot, emphasizing that security measures should not rely solely on obscurity.

## Related Questions
- What are the potential security risks associated with allowing moderators to execute commands as other players?
- How can separate commands with distinct permissions address the concerns raised about moderator abuse?
- Why is it important not to rely on security through obscurity in an open-source project?
- What measures should be taken to ensure that only administrators, and not moderators, have access to sensitive server code?
- How can the execute command feature be useful in a debugging context for controlling all players from one game window?
- What are the implications of allowing moderators to edit server code on their own?

*Source: unknown | chunk_id: github_issue_2446_discussion*
