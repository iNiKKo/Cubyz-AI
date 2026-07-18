# [issues/issue_329.md] - Issue #329 discussion

**Type:** review
**Keywords:** segmentation fault, getValue, utils.zig, lighting.zig, chunk_meshing.zig, memory handling, null pointer dereference, thread safety
**Symbols:** getValue, utils.zig, getValueHoldingTheLock, lighting.zig, getValues, chunk_meshing.zig, getLightAt, getCornerLight, getLight, finish, finishData, run, Thread.zig
**Concepts:** memory safety, segmentation fault, thread safety

## Summary
The game crashes due to a segmentation fault in the `getValue` function within the `utils.zig` file.

## Explanation
The crash occurs when accessing memory at address 0x7fed1d7d5cc0, specifically within the `getValue` function. The issue is likely related to improper memory handling or dereferencing a null pointer. The stack trace indicates that this function is called multiple times through various layers of the rendering and chunk meshing processes. The maintainer suggests creating a new issue with more detailed information if a different bug is identified.

## Related Questions
- What is the value of `ptr` at line 1173 in `utils.zig`?
- Is there any check for null before accessing `ptr.*` in `getValue`?
- How does the `palette` array in `lighting.zig` get initialized?
- Are there any known issues with memory allocation in `chunk_meshing.zig`?
- What is the purpose of `getValueHoldingTheLock` and how is it used?
- Is there a possibility of race conditions in the rendering process?
- How does the `run` function in `Thread.zig` handle task execution?
- Are there any logs or error messages before the segmentation fault occurs?
- What is the state of `self.data` when `getValue` is called?
- Is there a way to add more robust error handling around memory access?

*Source: unknown | chunk_id: github_issue_329_discussion*
