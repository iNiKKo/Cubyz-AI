# [issues/issue_2507.md] - Issue #2507 discussion

**Type:** review
**Keywords:** Zig, GLFW, Wayland, segmentation fault, build from source, vendored libraries, system package manager, distribution maintainers, musl libc, void-linux
**Symbols:** Cubyz, GLFW, Wayland, zig-out/bin/Cubyz, run_linux.sh
**Concepts:** packaging, distribution support, library vendoring, compatibility, precompiled binaries

## Summary
The issue discusses difficulties in packaging Cubyz for Linux/BSD distributions due to reliance on specific Zig versions, vendored libraries without Wayland support, and precompiled binaries that may not work across different systems.

## Explanation
The issue discusses difficulties in packaging Cubyz for Linux/BSD distributions due to reliance on specific Zig versions, vendored libraries without Wayland support, and precompiled binaries that may not work across different systems. The user reports a segmentation fault with the latest binary (version 0.1.1) on void-linux with musl libc:

```
zsh: segmentation fault ./Cubyz
``` 
When using the build script (`run_linux.sh`), it fails due to missing Wayland support in the vendored version of GLFW, resulting in an initialization error:

```
Starting game with version 0.1.0-dev
GLFW Error(65550): X11: The DISPLAY environment variable is missing
thread 30303 panic: Failed to initialize GLFW
/home/cubyz/Cubyz-0.1.1/src/graphics/Window.zig:714:3: 0x12d1e8c in init (Cubyz)
  @panic("Failed to initialize GLFW");
  ^
/home/cubyz/Cubyz-0.1.1/compiler/zig/lib/std/start.zig:705:22: 0x12c4e3b in callMain (Cubyz)
            root.main();
                     ^
src/env/__libc_start_main.c:95:2: 0x7fe6efa16dca in libc_start_main_stage2 (src/env/__libc_start_main.c)
Unwind error at address `/lib/ld-musl-x86_64.so.1:0x7fe6efa16dca` (unwind info unavailable), remaining frames may be incorrect
zsh: abort      zig-out/bin/Cubyz
```
The maintainer acknowledges these issues but notes that enabling Wayland support in GLFW was previously rejected due to compatibility concerns, and prebuilt binaries must use self-built libraries for maximum compatibility. The user suggests that building from source with system libraries would resolve the Wayland issue.

The main suggestions include:
1. Using a released version of Zig for each Cubyz release to allow distribution maintainers to use an already packaged version of Zig if available on the system.
2. Allowing building using system libraries, as dependencies like GLFW and freetype are often packaged by the distribution maintainer with patches and configurations specific to that system.
3. Ensuring it is easy to build everything from source, even if some libraries are vendored, to minimize binary blobs in packages.

## Related Questions
- What is the impact of using unreleased Zig versions on distribution packaging?
- How can Cubyz be modified to support Wayland in GLFW without breaking compatibility with other systems?
- Why are prebuilt binaries necessary for maximum compatibility, and what challenges do they present?
- What steps can be taken to ensure that vendored libraries like GLFW work correctly across different distributions?
- How can the build process be improved to allow building from source using system libraries?
- What is the root cause of the segmentation fault reported with the latest Cubyz binary on void-linux with musl libc?

*Source: unknown | chunk_id: github_issue_2507_discussion*
