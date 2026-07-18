# [issues/issue_2363.md] - Issue #2363 discussion

**Type:** review
**Keywords:** torch light, darkness, nighttime, brightness, gamma correction, lighting tiers, screen brightness
**Concepts:** lighting, graphics engine, accessibility

## Summary
Discussion about the darkness of torch light at night in Cubyz, with suggestions for improving lighting tiers and potential bugs in the graphics engine.

## Explanation
The issue revolves around the perceived darkness of torches during nighttime gameplay, affecting accessibility. The maintainer notes that the current implementation intentionally rounds down colors to zero at night to maintain true blackness. However, users argue that this makes it difficult to see even with high screen brightness. Suggestions include adjusting lighting tiers based on distance rather than brightness and implementing a gamma correction slider for more control over lighting. The maintainer acknowledges addressing night brightness in issue #2444 but notes that the primary concern remains the brightness of torches.

## Related Questions
- What is the current implementation of night lighting in Cubyz?
- How does the graphics engine handle color rounding at night?
- What are the potential benefits and drawbacks of adjusting lighting tiers based on distance?
- Why was gamma correction not initially considered for lighting adjustments?
- How can users disable the daylight cycle to see all the time?
- What changes were made in issue #2444 regarding night brightness?

*Source: unknown | chunk_id: github_issue_2363_discussion*
