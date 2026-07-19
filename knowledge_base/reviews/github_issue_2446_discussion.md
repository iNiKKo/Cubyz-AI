# [issues/issue_2446.md] - Issue #2446 discussion

**Type:** review
**Keywords:** execute command, server owners, moderators, impersonation, private messages, security through obscurity, administrators, limited command permissions
**Concepts:** security, moderator abuse, permissions

## Summary
Discussion about adding an execute command feature for server owners and moderators.

## Explanation
Discussion about adding an `/execute` command feature for server owners and moderators, which would allow them to run commands as a specific player. The maintainers argue against this due to security concerns, specifically the risk of moderator abuse through impersonation via private messages. They suggest using separate commands with distinct permissions instead. Administrators can modify server code directly but moderators cannot; thus, relying on obscurity for security is not effective in an open-source project. The `/execute` command could be useful in debugging contexts to control all players from one game window without needing direct access to the server code.

## Related Questions
- What are the potential security risks associated with allowing moderators to execute commands as other players?
- How can separate commands with distinct permissions address the concerns raised about moderator abuse?
- Why is it important not to rely on security through obscurity in an open-source project?
- What measures should be taken to ensure that only administrators, and not moderators, have access to sensitive server code?
- How can the execute command feature be useful in a debugging context for controlling all players from one game window?

*Source: unknown | chunk_id: github_issue_2446_discussion*
