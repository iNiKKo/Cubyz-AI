# [issues/issue_1945.md] - Issue #1945 discussion

**Type:** review
**Keywords:** build failure, Zig upgrade, std.compress.flate, missing members, run_linux.sh, Wayland
**Symbols:** compress.flate, deflate, decompressor, compressor
**Concepts:** backwards compatibility, versioning

## Summary
Build failure due to missing members in `std.compress.flate` struct after Zig upgrade.

## Explanation
The build failed on Linux because the `std.compress.flate` struct no longer contains the members 'deflate', 'decompressor', and 'compressor' after upgrading from Zig 0.15.0 to 0.15.1. The maintainer suggests using provided scripts (`run_linux.sh`) to ensure compatibility with the required version of Zig and dependencies. The user confirms that using the script resolved the build issue but encountered another problem related to Wayland.

## Related Questions
- What is the correct version of Zig required for Cubyz development?
- How can I resolve build issues related to missing members in `std.compress.flate`?
- Why was there a breaking change in `std.compress.flate` between Zig 0.15.0 and 0.15.1?
- What are the steps to use the provided scripts for Cubyz development on Linux?
- How can I address compatibility issues with Wayland when running Cubyz?
- Are there any additional dependencies required for Cubyz development besides Zig?

*Source: unknown | chunk_id: github_issue_1945_discussion*
