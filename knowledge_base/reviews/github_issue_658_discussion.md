# [issues/issue_658.md] - Issue #658 discussion

**Type:** review
**Keywords:** nixos, build scripts, reproducible, launcher, shell.nix, devenv, non-FHS-compliant, prebuilt binaries
**Symbols:** shell.nix, devenv.sh, debug_linux.sh
**Concepts:** reproducibility, build process, NixOS compatibility

## Summary
Discussion about improving Cubyz's build process for Linux/NixOS by adding Nix-specific files to enhance reproducibility and robustness.

## Explanation
The discussion centers around improving Cubyz's build process for NixOS by addressing challenges such as non-FHS-compliant library storage and difficulties in using prebuilt binaries. The user proposes adding a `shell.nix` or devenv file to create a project-local shell environment with all necessary libraries and environment variables set, aiming to enhance reproducibility and robustness. Specific files needed include `shell.nix`, which can be used to build the project locally without triggering precompiled zig compiler downloads (`debug_linux.sh`). The maintainer questions how this would integrate with the launcher, intended to replace current build scripts. Potential benefits include total reproducibility and compatibility across different environments.

## Related Questions
- What specific changes are proposed to the build process for NixOS?
- How will the addition of `shell.nix` or devenv files affect the current build scripts?
- What are the potential benefits and drawbacks of using Nix-specific files in the Cubyz repository?
- How can the launcher be integrated with the new NixOS build process?

*Source: unknown | chunk_id: github_issue_658_discussion*
