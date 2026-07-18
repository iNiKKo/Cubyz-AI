# [issues/issue_460.md] - Issue #460 discussion

**Type:** review
**Keywords:** Zig build, rpath issues, distribution, macOS, Linux, XQuartz, libx11, root_module.addRPathSpecial, exe.addObjectFile, unused rpaths
**Symbols:** cubyz_deps, Library, XQuartz, libx11, rpath, root_module.addRPathSpecial, exe.addObjectFile
**Concepts:** linking, build system, rpaths, static libraries

## Summary
The review discusses issues with Cubyz's rpaths during distribution on macOS and Linux, focusing on removing duplicate paths, correcting library paths, and ensuring proper linking.

## Explanation
The issue highlights that Cubyz has multiple problems with its rpaths, including duplicates, incorrect build-time evaluation of paths, and unnecessary links to specific libraries like XQuartz. The reviewer suggests ideal rpath configurations but notes Zig's limitations in handling such cases. The maintainer proposes using `root_module.addRPathSpecial` to add necessary rpaths and mentions the discovery of `exe.addObjectFile` for managing static libraries. The user confirms these solutions and removes unnecessary X11 linking.

## Related Questions
- How can I remove duplicate rpaths in Cubyz's build process?
- What is the correct way to link against XQuartz X11 in Zig?
- Can `root_module.addRPathSpecial` be used to add custom rpaths during build?
- Is there a way to prevent unnecessary library paths from being included in rpaths?
- How does Zig handle static libraries like cubyz_deps during linking?
- What are the implications of using `exe.addObjectFile` for managing static libraries?
- How can I ensure that Cubyz's rpaths are correctly set for distribution on macOS and Linux?
- Are there any best practices for configuring rpaths in Zig projects to avoid build-time path issues?
- Can Zig's commandline linker be used to manually manage rpath settings?
- What steps should be taken to prevent username leakage from build paths in Cubyz?

*Source: unknown | chunk_id: github_issue_460_discussion*
