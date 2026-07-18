# [issues/issue_2782.md] - Issue #2782 discussion

**Type:** review
**Keywords:** Zig Compiler, Linux Installation, run_linux.sh, debug_linux.sh, Build Error, Version Mismatch, Local Binary, Terminal Output, Cubyz Game, Script Execution Failure
**Symbols:** zig, run_linux.sh, debug_linux.sh, Build.Step.Run, std.Build
**Concepts:** Version Management, Script Execution, Local Binary Installation

## Summary
The issue involved installation failures on Linux due to a mismatch between Zig versions. The solution involved running specific scripts (`run_linux.sh`) that manage the correct Zig version and build process.

## Explanation
The user encountered an installation failure on Linux when trying to run Cubyz using `zig build run`, which resulted in a compatibility error due to an outdated Zig compiler version. The discussion revealed that Cubyz uses a specific pre-release version of Zig, and running the script `run_linux.sh` ensures the correct version is used. Initially, the user faced issues with both `run_linux.sh` and `debug_linux.sh`. Running `run_linux.sh` outputted instructions to press enter or set an environment variable to skip the prompt. However, executing `debug_linux.sh` caused a terminal crash due to missing files in the `compiler/` directory. After deleting the `compiler` directory and re-running `run_linux.sh`, the correct Zig binary was downloaded and installed locally at `Cubyz-0.1.1/compiler/zig`. This allowed the game to build successfully, as indicated by the terminal output confirming that the Zig compiler is valid and building Cubyz from source. The exact error message encountered during initial execution was:
```
/home/ibadullah/.cache/zig/p/zig-0.0.0-Fp4XJAXmXQ1r23tqehV14LpPFILnnXSyg7bPitqs8mrf/test/standalone/empty_env/build.zig:34:9: error: no field named 'color' in struct 'Build.Step.Run'
    run.color = .manual;
        ^~~~~
/snap/zig/15308/lib/std/Build/Step/Run.zig:1:1: note: struct declared here
const std = @import("std");
^~~~~
referenced by:
    runBuild__anon_78184: /snap/zig/15308/lib/std/Build.zig:2214:33
    dependencyInner__anon_105895: /snap/zig/15308/lib/std/Build.zig:2195:29
    17 reference(s) hidden; use '-freference-trace=19' to see all references
```
This issue was resolved by ensuring the correct Zig version is used via `run_linux.sh`, which downloads and installs the appropriate binary in the `compiler/` directory.

## Related Questions
- What specific error message did the user encounter when running `zig build run`?
- How does Cubyz manage its Zig compiler version locally within the project folder?
- Why did executing `debug_linux.sh` cause a terminal crash and what was the exact output?
- What steps should be taken if `run_linux.sh` fails to execute correctly due to missing files in the `compiler/` directory?

*Source: unknown | chunk_id: github_issue_2782_discussion*
