# [issues/issue_763.md] - Issue #763 discussion

**Type:** review
**Keywords:** music handling, global cache, download links, addon creators, link rot, bandwidth usage, Cubyz updater, pre-installation, assets repository
**Concepts:** asset management, caching, bandwidth optimization, link rot, hosting

## Summary
The issue discusses improving how large assets like music are handled in Cubyz by storing them in a global cache instead of bundling them with the game. This change aims to reduce download times and bandwidth usage but introduces challenges such as link rot and hosting responsibilities for addon creators.

## Explanation
The current system redownloads music every time the game is updated, causing delays for first-time players and unnecessary server bandwidth usage. The proposed solution involves storing music in a global cache checked before downloading, which could reduce compilation times but requires addon creators to host music files externally. This approach may lead to link rot issues if not managed properly. Maintainers suggest exploring alternatives like using a Cubyz updater or pre-installing addons for servers. The decision is postponed pending further development and the creation of a new assets repository.

## Related Questions
- What is the current system for handling music assets in Cubyz?
- How does the proposed solution aim to improve asset management?
- What are the potential drawbacks of storing music in a global cache?
- What alternatives have been suggested to reduce download times and bandwidth usage?
- Why was the decision to use Zig's compile-time caching system made?
- When is the plan to address this issue expected to be completed?

*Source: unknown | chunk_id: github_issue_763_discussion*
