# [issues/issue_2485.md] - Issue #2485 discussion

**Type:** review
**Keywords:** crash, torches, integer overflow, getLight, chunk_meshing.zig, lighting, bounds checking, thread safety
**Symbols:** getLight, finish, finishData, finishNeighbors, generateMesh, generateLightingData, run, callFn__anon_63101, entryFn
**Concepts:** thread safety, integer overflow, lighting calculation, bug fixing

## Summary
A crash occurs when joining a world with torches due to an integer overflow in the lighting calculation.

## Explanation
The issue stems from an integer overflow in the `getLight` function within `chunk_meshing.zig`. The overflow happens during the accumulation of light values, likely due to incorrect handling of large numbers or insufficient bounds checking. This bug affects unaligned models like torches, causing the application to panic and crash. The maintainer notes that something broke for these specific models, indicating a potential issue with how lighting is calculated or applied to certain block types.

## Related Questions
- What is the cause of the integer overflow in the `getLight` function?
- How does the lighting calculation affect unaligned models like torches?
- Is there any bounds checking implemented for light values in the current codebase?
- What changes were made to address this issue in commit df0a0592adda985d865669f1e96ffa2e5b293887?
- How can we prevent similar integer overflow issues in the future?
- Are there any other models that might be affected by this lighting bug?
- What is the impact of this crash on user experience and game stability?
- How does the current implementation handle threading in the rendering process?
- Is there a need for additional testing to ensure the fix works across different scenarios?
- Can we optimize the lighting calculation to avoid potential overflow issues?

*Source: unknown | chunk_id: github_issue_2485_discussion*
