# [issues/issue_694.md] - Issue #694 discussion

**Type:** review
**Keywords:** OpenGL, GLFW, WGL, Nvidia, Intel, UHD Graphics, Zig, Cubyz, Windows 10, Graphics drivers, GPU settings, Executable compilation
**Symbols:** run_windows.bat, GLFW Error(65543), WGL: Driver does not support OpenGL version 4.6, Nvidia GeForce GTX 1050, Intel UHD Graphics 630, zig-out\bin\Cubyzig.exe
**Concepts:** OpenGL version support, GPU settings, Executable compilation

## Summary
The user reports an issue with Cubyz not running on their PC due to a missing OpenGL version support error. The maintainer clarifies that the game executable is compiled on first launch and suggests changing the GPU settings to high performance, which resolves the issue.

## Explanation
The user encounters an error related to missing OpenGL version support when trying to run Cubyz on their Windows 10 system with a GTX 1050 GPU. The maintainer provides information that the game executable is compiled during the first launch and stored in `zig-out\bin\Cubyzig.exe`. The user then successfully resolves the issue by changing the GPU settings to high performance, indicating that the default low-performance UHD card was causing the problem.

## Related Questions
- Where is the game executable stored after first launch?
- How can I check if my GPU supports OpenGL 4.6?
- What are the steps to change GPU settings to high performance on Windows 10?
- Why does Cubyz compile the executable during the first launch?
- Is there a way to manually specify the GPU for Cubyz?
- How do I ensure that the latest graphics drivers are installed for my GPU?

*Source: unknown | chunk_id: github_issue_694_discussion*
