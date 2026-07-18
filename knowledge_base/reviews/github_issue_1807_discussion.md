# [issues/issue_1807.md] - Issue #1807 discussion

**Type:** review
**Keywords:** game version, network compatibility, major version, minor version, patch version, -dev suffix, server acceptance, player notification
**Concepts:** version checking, multiplayer compatibility, development builds

## Summary
The issue proposes adding version checking functionality to allow clients to join servers based on compatible versions, with special handling for development builds.

## Explanation
This change aims to enhance the compatibility and stability of multiplayer sessions by ensuring that players connect to servers running compatible game versions. The proposal specifies that clients should be allowed to join if they have the same major and minor version, ignoring patch differences unless there are breaking network changes. Development builds, indicated by a `-dev` suffix, are restricted from joining normal version servers unless the server itself is also a development build. This ensures that stable releases do not inadvertently connect with potentially unstable development versions. Additionally, players should receive notifications if they attempt to join a server with an incompatible version. The discussion notes that while it might be useful for the server to send additional messages when kicking players due to version incompatibility, this feature is deemed unnecessary at the moment.

## Related Questions
- What is the proposed behavior for clients with different patch versions?
- How are development builds handled in terms of server connections?
- Is there a mechanism to notify players about version incompatibility?
- Why might additional messages when kicking players be useful?
- Are there any plans to implement the feature for sending additional messages?
- What is the rationale behind ignoring patch versions unless necessary?

*Source: unknown | chunk_id: github_issue_1807_discussion*
