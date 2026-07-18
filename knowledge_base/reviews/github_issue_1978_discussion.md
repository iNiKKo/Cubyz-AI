# [issues/issue_1978.md] - Issue #1978 discussion

**Type:** review
**Keywords:** delay, input response, control key, sprint, random delay, accumulation, Minecraft Java
**Concepts:** input handling, frame rate, user experience

## Summary
The user reports a delay in input response when holding down the control key to sprint, which varies from 200ms to 2000ms and accumulates over time.

## Explanation
The user reports a delay in input response when holding down the control key to sprint, which varies from 200ms to 2000ms and accumulates over time. The maintainer initially suspects it might be related to frame rate or user-specific settings but is unable to reproduce the problem. The user provides additional context about similar issues in Minecraft Java, suggesting a potential broader problem with input processing. However, the maintainer concludes that they cannot fix this issue as it appears to be an issue on the user's side.

## Related Questions
- What is the current frame rate at which the user experiences the input delay?
- Are there any known issues with input processing in Cubyz that could cause this delay?
- How does the input handling system in Cubyz differ from Minecraft Java, and are there any similarities in their implementation?
- Can the maintainer reproduce the issue by simulating different frame rates or user settings?
- What steps can be taken to debug and quantify the input delay in Cubyz?
- Are there any existing patches or fixes for similar input issues in other games that could be applied to Cubyz?

*Source: unknown | chunk_id: github_issue_1978_discussion*
