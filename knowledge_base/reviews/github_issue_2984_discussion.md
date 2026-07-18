# [issues/issue_2984.md] - Issue #2984 discussion

**Type:** review
**Keywords:** static linking, glibc, musl, NixOS, hardware acceleration, proprietary drivers, AppImage, OpenGL4.6
**Symbols:** glibc, musl, NixOS
**Concepts:** static linking, dynamic linking, compatibility

## Summary
Discussion about statically linking release artifacts against musl instead of glibc to ensure compatibility with systems like NixOS.

## Explanation
Discussion about statically linking release artifacts against musl instead of glibc to ensure compatibility with systems like NixOS. The current builds are statically linked against glibc, making them incompatible with NixOS and other systems that do not support dynamically-linked binaries. The user proposes switching to musl for full static linking, which would resolve the incompatibility issue but raises concerns about losing dynamic library capabilities such as hardware acceleration (via dlopen) and proprietary drivers like NVIDIA's. The maintainer initially questions this logic but later shares a failed attempt at linking musl with commit fe5afde6d36acd37637d56746536cf3387b9eeed. Additionally, the user suggests using an AppImage built for Alpine Linux and NixOS, which works as long as the GPU supports OpenGL 4.6. However, running this AppImage on NixOS requires disabling `appimage-run` due to SquashFS expectations.

## Related Questions
- What are the potential benefits and drawbacks of statically linking against musl?
- Why did the maintainer's attempt to link musl fail?
- How does dynamic linking impact hardware acceleration and proprietary drivers?
- What is the current build process for Cubyz release artifacts?
- How can compatibility with NixOS be improved without losing dynamic library capabilities?
- What are the implications of using AppImage on systems like NixOS?

*Source: unknown | chunk_id: github_issue_2984_discussion*
