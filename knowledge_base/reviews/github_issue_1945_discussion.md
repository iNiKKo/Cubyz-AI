# [issues/issue_1945.md] - Issue #1945 discussion

**Type:** review
**Keywords:** build failure, Zig upgrade, std.compress.flate, missing members, run_linux.sh, Wayland
**Symbols:** compress.flate, deflate, decompressor, compressor
**Concepts:** backwards compatibility, versioning

## Summary
Build failure due to missing members in `std.compress.flate` struct after Zig upgrade.

## Explanation
Build failure due to missing members in `std.compress.flate` struct after upgrading from Zig 0.15.0 to 0.15.1 on Linux. The error messages indicate that the root source file struct 'compress.flate' has no member named 'deflate', 'decompressor', and 'compressor'. This issue arises because installing Zig with a package manager is not recommended, as it may use an outdated version of the compiler. To resolve this, the maintainer advises using provided scripts (`run_linux.sh`) to download the required version of Zig and dependencies for Cubyz development. The user confirmed that using the script resolved the build issue but encountered another problem related to Wayland.

## Related Questions
- What is the correct version of Zig required for Cubyz development?
- How can I resolve build issues related to missing members in `std.compress.flate`?
- Why was there a breaking change in `std.compress.flate` between Zig 0.15.0 and 0.15.1?
- What are the steps to use the provided scripts for Cubyz development on Linux?

*Source: unknown | chunk_id: github_issue_1945_discussion*
