# [issues/issue_2782.md] - Issue #2782 discussion

**Type:** review
**Keywords:** Zig Compiler, Linux Installation, run_linux.sh, debug_linux.sh, Build Error, Version Mismatch, Local Binary, Terminal Output, Cubyz Game, Script Execution Failure
**Symbols:** zig, run_linux.sh, debug_linux.sh, Build.Step.Run, std.Build
**Concepts:** Version Management, Script Execution, Local Binary Installation

## Summary
The issue involved installation failures on Linux due to a mismatch between Zig versions. The solution involved running specific scripts (`run_linux.sh`) that manage the correct Zig version and build process.

## Explanation
The user encountered an error when trying to run Cubyz using `zig build run`, which indicated a compatibility issue with the Zig compiler version. The discussion revealed that Cubyz uses a specific pre-release version of Zig, and running `run_linux.sh` ensures the correct version is used. Initially, the script did not execute properly, leading to confusion. After deleting the `compiler` directory and re-running `run_linux.sh`, the correct Zig binary was downloaded and installed locally, allowing the game to build and run successfully.

## Related Questions
- What is the purpose of `run_linux.sh` in Cubyz?
- Why did running `debug_linux.sh` cause a terminal crash?
- How does Cubyz manage its Zig compiler version?
- What steps should be taken if `run_linux.sh` fails to execute correctly?
- Where is the built project located after successful execution of `run_linux.sh`?
- How can one verify that the correct Zig version is being used for building Cubyz?

*Source: unknown | chunk_id: github_issue_2782_discussion*
