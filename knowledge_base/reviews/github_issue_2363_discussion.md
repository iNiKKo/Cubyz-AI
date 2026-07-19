# [issues/issue_2363.md] - Issue #2363 discussion

**Type:** review
**Keywords:** torch light, darkness, nighttime, brightness, gamma correction, lighting tiers, screen brightness
**Concepts:** lighting, graphics engine, accessibility

## Summary
Discussion about the darkness of torch light at night in Cubyz, with suggestions for improving lighting tiers and potential bugs in the graphics engine.

## Explanation
The discussion centers around the perceived darkness of torches during nighttime gameplay, affecting accessibility. Users report difficulty seeing even with high screen brightness and suggest adjusting lighting tiers based on distance rather than brightness and implementing a gamma correction slider for more control over lighting. The maintainer notes that rounding down colors to zero at night is intentional to maintain true blackness but acknowledges this makes it difficult to see during nighttime gameplay. The maintainer also mentions addressing night brightness in issue #2444, but the primary concern remains the brightness of torches. Users suggest disabling the daylight cycle as an alternative solution.

## Related Questions
- What is the current implementation of night lighting in Cubyz?
- How does the graphics engine handle color rounding at night?
- Why was gamma correction not initially considered for lighting adjustments?
- What are the potential benefits and drawbacks of adjusting lighting tiers based on distance?
- How can users disable the daylight cycle to see all the time?
- What changes were made in issue #2444 regarding night brightness?

*Source: unknown | chunk_id: github_issue_2363_discussion*
