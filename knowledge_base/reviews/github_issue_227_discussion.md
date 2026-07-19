# [issues/issue_227.md] - Issue #227 discussion

**Type:** review
**Keywords:** launcher, version selection, GitHub, compilation, binary size, error logs, scripts, user-friendly
**Symbols:** Cubyz-Launcher, zig
**Concepts:** dependency management, portability, error logging, user experience

## Summary
Discussion about creating a launcher for Cubyz that allows selecting versions from GitHub, with considerations around dependency management and compilation.

## Explanation
The discussion revolves around creating a user-friendly launcher for Cubyz that allows selecting versions from GitHub. The maintainer emphasizes reducing dependencies to minimize binary size (aiming for below 1 MB in ReleaseSmall) and improve portability. There are concerns about hiding error logs during compilation, which could complicate troubleshooting. The maintainer points out that existing alternatives like scripts already address many of the proposed launcher's features and suggests focusing on other areas instead. The PixelGuys/Cubyz-Launcher repository is incomplete and unmaintained. Alternative solutions include handling updating without losing saves within the game (#1485), capturing messages not handled through the logger (e.g., stack traces) (#1486), and making the general installation process easier for average users (#388). The main disadvantages of a launcher are maintaining it, taking time away from development on the actual game, adding more points of failure such as linkrot, and introducing another step for entering a world.

## Related Questions
- What is the exact size requirement for the binary in ReleaseSmall?
- Why is the PixelGuys/Cubyz-Launcher repository incomplete and unmaintained?
- How does the maintainer propose handling updating without losing saves within the game?

*Source: unknown | chunk_id: github_issue_227_discussion*
