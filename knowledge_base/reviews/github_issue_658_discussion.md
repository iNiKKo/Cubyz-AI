# [issues/issue_658.md] - Issue #658 discussion

**Type:** review
**Keywords:** nixos, build scripts, reproducible, launcher, shell.nix, devenv, non-FHS-compliant, prebuilt binaries
**Symbols:** shell.nix, devenv.sh, debug_linux.sh
**Concepts:** reproducibility, build process, NixOS compatibility

## Summary
Discussion about improving Cubyz's build process for Linux/NixOS by adding Nix-specific files to enhance reproducibility and robustness.

## Explanation
The discussion revolves around the challenges of building Cubyz on NixOS, which differs from other Linux distributions due to its non-FHS-compliant library storage and difficulty in using prebuilt binaries. The user proposes adding a `shell.nix` or devenv file to create a project-local shell environment with all necessary libraries and environment variables set. This approach aims to make the build process more reproducible and robust, aligning with NixOS's principles. The maintainer questions how this would integrate with the launcher, which is intended to replace the current build scripts.

## Related Questions
- What specific changes are proposed to the build process for NixOS?
- How will the addition of `shell.nix` or devenv files affect the current build scripts?
- What are the potential benefits and drawbacks of using Nix-specific files in the Cubyz repository?
- How can the launcher be integrated with the new NixOS build process?
- Are there any known issues with using prebuilt binaries on NixOS, and how will they be addressed?
- What steps should be taken to ensure compatibility between the NixOS build environment and other Linux distributions?

*Source: unknown | chunk_id: github_issue_658_discussion*
