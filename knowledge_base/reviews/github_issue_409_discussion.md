# [issues/issue_409.md] - Issue #409 discussion

**Type:** review
**Keywords:** ReleaseSafe, ReleaseFast, undefined behavior, performance impact, fast math, profiling, DebugAllocator, SmpAllocator, bug detection, compile flags
**Symbols:** run, ReleaseSafe, ReleaseFast, @setRuntimeSafety(false), @setFloatMode, FloatMode, -ffast-math, time, GPA, DebugAllocator, SmpAllocator
**Concepts:** performance optimization, debugging, memory safety, allocator choice

## Summary
The discussion revolves around whether to compile Cubyz scripts in ReleaseSafe instead of ReleaseFast, considering the trade-offs between better debug information and potential performance degradation.

## Explanation
The maintainers initially considered disabling safety checks in critical functions with `@setRuntimeSafety(false)` but found that the performance impact could be significant. Specifically, loading a render distance 12 world went from 33.5 seconds to 40 seconds with ReleaseSafe mode, representing a 20% increase in runtime. The user suggested using fast math options (`@setFloatMode(comptime mode: FloatMode) void`), which is equivalent to `-ffast-math` in GCC. However, the maintainers ultimately decided against switching to ReleaseSafe due to longer compile and run times, although they acknowledged its benefits for bug detection.

With Zig 14.0 introducing new allocators like DebugAllocator and SmpAllocator, there is a renewed interest in using DebugAllocator for debug scripts and considering options for release scripts, including safety features or performance optimizations (`@setRuntimeSafety(false)`). The maintainers noted that the types of bugs caught by DebugAllocator (use-after-free, leaks, double frees) are easily detected during development but acknowledged the need for stack traces for segfaults.

The exact performance impact of using DebugAllocator in Cubyz is not explicitly stated. To profile Cubyz more accurately without including menu times, one could use a timer that excludes menu time or consider other profiling tools. Logging profiling results for further analysis can be achieved by redirecting the output to a log file or using a dedicated logging library.

The potential benefits of switching to ReleaseSafe mode include better debug information and earlier detection of undefined behavior, while the drawbacks include potentially more crashes and lower performance. Implementing compile flags to allow users to choose between different allocators could provide flexibility but requires careful consideration of the trade-offs involved.

## Related Questions
- What is the exact performance impact of using DebugAllocator in Cubyz?
- How can we profile Cubyz more accurately without including menu times?
- Is there a way to log profiling results for further analysis?
- What are the potential benefits and drawbacks of switching to ReleaseSafe mode?
- Can we implement compile flags to allow users to choose between different allocators?
- How does enabling fast math affect floating-point operations in Cubyz?

*Source: unknown | chunk_id: github_issue_409_discussion*
