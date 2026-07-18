# [issues/issue_2984.md] - Issue #2984 discussion

**Type:** review
**Keywords:** static linking, glibc, musl, NixOS, hardware acceleration, proprietary drivers, AppImage, OpenGL4.6
**Symbols:** glibc, musl, NixOS
**Concepts:** static linking, dynamic linking, compatibility

## Summary
Discussion about statically linking release artifacts against musl instead of glibc to ensure compatibility with systems like NixOS.

## Explanation
The issue revolves around the current build process that statically links against glibc, making binaries incompatible with systems like NixOS. The user proposes switching to musl for full static linking, which could resolve this issue but raises concerns about losing dynamic library capabilities such as hardware acceleration and proprietary drivers. The maintainer initially questions the logic behind the issue but later shares a failed attempt at linking musl. The discussion highlights trade-offs between compatibility and functionality.

## Related Questions
- What are the potential benefits and drawbacks of statically linking against musl?
- Why did the maintainer's attempt to link musl fail?
- How does dynamic linking impact hardware acceleration and proprietary drivers?
- What is the current build process for Cubyz release artifacts?
- How can compatibility with NixOS be improved without losing dynamic library capabilities?
- What are the implications of using AppImage on systems like NixOS?

*Source: unknown | chunk_id: github_issue_2984_discussion*
