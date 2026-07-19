# [issues/issue_460.md] - Issue #460 discussion

**Type:** review
**Keywords:** Zig build, rpath issues, distribution, macOS, Linux, XQuartz, libx11, root_module.addRPathSpecial, exe.addObjectFile, unused rpaths
**Symbols:** cubyz_deps, Library, XQuartz, libx11, rpath, root_module.addRPathSpecial, exe.addObjectFile
**Concepts:** linking, build system, rpaths, static libraries

## Summary
The review discusses issues with Cubyz's rpaths during distribution on macOS and Linux, focusing on removing duplicate paths, correcting library paths, and ensuring proper linking.

## Explanation
The review discusses issues with Cubyz's rpaths during distribution on macOS and Linux. The current rpaths include:

```text
path /Users/USER/.cache/zig/p/12204ba799cc74baeec8284b8a22cd0b597b58d5fa32c6eac999635fdc1834c950fc/lib (offset 12)
path /usr/local/GL/lib (offset 12)
path /Users/USER/Cubyz/Library (offset 12)
path /opt/homebrew/Cellar/libx11/1.8.9/lib (offset 12)
path /Users/USER/.cache/zig/p/12204ba799cc74baeec8284b8a22cd0b597b58d5fa32c6eac999635fdc1834c950fc/lib (offset 12)
```

There are several problems:
- `cubyz_deps` is listed twice and should be removed since it's a static library.
- The Library path `/Users/USER/Cubyz/Library` is evaluated at build-time instead of runtime, making it nonsensical for distribution.
- Cubyz should link against XQuartz X11 rather than homebrew's `libx11`, and X11 doesn't need an RPATH.

Ideally, the rpaths should be:
```text
path @executable_path/../Library (if app bundle)
path /usr/local/GL/lib (if local build)
```

The maintainer suggests using `root_module.addRPathSpecial` to add necessary rpaths and mentions that `exe.addObjectFile` can manage static libraries like `cubyz_deps`. The user confirms these solutions and removes unnecessary X11 linking.

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
