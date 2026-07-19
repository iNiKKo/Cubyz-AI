# [issues/issue_763.md] - Issue #763 discussion

**Type:** review
**Keywords:** music handling, global cache, download links, addon creators, link rot, bandwidth usage, Cubyz updater, pre-installation, assets repository
**Concepts:** asset management, caching, bandwidth optimization, link rot, hosting

## Summary
The issue discusses improving how large assets like music are handled in Cubyz by storing them in a global cache instead of bundling them with the game. This change aims to reduce download times and bandwidth usage but introduces challenges such as link rot and hosting responsibilities for addon creators.

## Explanation
The issue discusses improving how large assets like music are handled in Cubyz by storing them in a global cache instead of bundling them with the game. The current system redownloads music every time the game is updated, causing delays for first-time players and unnecessary server bandwidth usage. Specifically, right now they are redownloaded every time the game is updated using [the easy way](https://github.com/PixelGuys/Cubyz?tab=readme-ov-file#the-easy-way-no-tools-needed). Either way, they are downloaded before launching the game (→ more waiting for first-time player). For server side assets, they are downloaded from the server (→ unnecessary bandwidth usage on join) and redownloaded every time (→ not that important, since there are other fixes).

The proposed solution involves storing music download links in the assets and using a global cache to check before downloading. This could reduce compilation times but requires addon creators to host music files externally. The exact disadvantages of this approach include: addon creators need to host the music somewhere instead of just bundling them in with the other assets, and music of these addons would be prone to link rot and are likely to break at some point in the future.

Maintainers suggest exploring alternatives like using a Cubyz updater that updates Cubyz to the latest version without redownloading game assets repeatedly or pre-installing addons for servers. The decision is postponed pending further development and the creation of a new assets repository at https://github.com/PixelGuys/Cubyz-Assets.

Additionally, it was mentioned that Zig's compile-time caching system was chosen over other methods because the maintainer wasn't sure if they should download these individually at runtime and couldn't get the http client to work.

## Related Questions
-  What specific problems does the current system have with handling music assets?
-  How exactly would storing music in a global cache improve asset management?
-  What are the exact disadvantages of using a global cache for music files?
-  What alternatives were suggested to reduce download times and bandwidth usage, and how do they work?
-  Why was Zig's compile-time caching system chosen over other methods?

*Source: unknown | chunk_id: github_issue_763_discussion*
