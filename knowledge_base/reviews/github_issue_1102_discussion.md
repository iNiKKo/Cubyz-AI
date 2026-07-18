# [issues/issue_1102.md] - Issue #1102 discussion

**Type:** review
**Keywords:** crash, rendering, SIGABRT, glFenceSync, graphics driver, Haswell, Mesa, software rendering, driver update, system logs
**Symbols:** glFenceSync, SIGABRT, std.debug.print()
**Concepts:** Graphics Rendering, Driver Compatibility, Hardware Limitations

## Summary
The game crashes during rendering due to a `SIGABRT` error on the `glFenceSync` call, suspected to be caused by outdated or incompatible graphics drivers.

## Explanation
The issue is characterized by the game getting stuck on a blank screen with just the HUD before crashing. The root cause is identified as a `SIGABRT` error occurring at the `glFenceSync` function call in the rendering pipeline. The maintainer suggests that this could be due to driver issues, specifically noting that upstream Mesa may no longer support Haswell graphics processors. The user reports that forcing software rendering resolves the issue but significantly reduces performance. The discussion highlights the complexity of dealing with outdated hardware and drivers, emphasizing that while the game developers cannot fix driver issues directly, they can provide guidance and workarounds.

## Related Questions
- What is the impact of using software rendering on game performance?
- How can one check for driver compatibility with the Haswell graphics processor?
- Are there any known workarounds for `SIGABRT` errors in OpenGL applications?
- What steps should be taken to update graphics drivers on Void Linux?
- Can forcing software rendering be a long-term solution for this issue?
- How does the game handle different types of hardware configurations?
- Is there a way to obtain more detailed error logs from the system?
- What are the potential risks of using outdated graphics drivers with modern applications?
- How can one determine if the issue is related to the graphics driver or the application code?
- Are there any plans to support older hardware in future game updates?

*Source: unknown | chunk_id: github_issue_1102_discussion*
