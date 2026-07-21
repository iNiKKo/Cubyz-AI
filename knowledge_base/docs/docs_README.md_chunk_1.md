# [easy/docs_README.md] - Chunk 1

**Type:** documentation
**Keywords:** run_linux.sh, run_windows.bat, zig build run, git pull, zig-cache, compile hangs, troubleshooting, contributing, CONTRIBUTING.md, GAME_DESIGN_PRINCIPLES.md, CONTENT_SUGGESTIONS.md
**Symbols:** run_linux.sh, run_windows.bat, zig build run, zig-cache

## Summary
How to run/compile Cubyz from source (the Easy Way and the Better Way), what to do if compiling hangs or errors, and where the three contributing-guideline docs live.

## Explanation
**The Easy Way (no tools needed):** download the source zip, extract it, and double-click `run_linux.sh` or `run_windows.bat` depending on OS -- this compiles Cubyz automatically.

**If it doesn't work:** if compiling keeps running for more than 10 minutes without doing anything, it can help to kill and restart the process (a known but uninvestigated issue affecting some users) -- it might also help to delete the `zig-cache` folder. If you see an error message in the terminal, report it on the Issues tab or the Discord server. Otherwise, ask for help on Discord; if you can't get it compiling, someone may compile a release for you.

**The Better Way:** install Git, clone the repository (`git clone https://github.com/pixelguys/Cubyz`), then run `run_linux.sh`/`run_windows.bat`, or `zig build run` directly if a compatible Zig is already installed. To update your local copy, use `git pull` -- this keeps everything in one place instead of re-downloading the compiler on every update.

**Contributing:** code contributions follow CONTRIBUTING.md, gameplay-mechanic additions follow GAME_DESIGN_PRINCIPLES.md, and content (blocks/items/etc.) additions follow CONTENT_SUGGESTIONS.md.

## Related Questions
- What should you do if compiling Cubyz keeps running for more than 10 minutes without doing anything?
- What might help if Cubyz fails to compile or hangs during compilation?
- What is the difference between the "Easy Way" and the "Better Way" to run Cubyz from source?
- How do you update your local Cubyz source checkout?
- Where should code vs. gameplay vs. content contributions be documented, per the README?

*Source: unknown | chunk_id: docs_README.md_chunk_1*
