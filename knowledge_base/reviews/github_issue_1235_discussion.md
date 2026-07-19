# [issues/issue_1235.md] - Issue #1235 discussion

**Type:** review
**Keywords:** OKLCH, HSL, RGB, mix colors, quantization, #225
**Concepts:** color model, lighting, quantization

## Summary
Discussion about implementing a new color model, OKLCH, for lighting in Cubyz. The maintainer seeks clarification on where and how this model should be applied, specifically regarding fading values by 8 or rounding them during quantization processes. There is mention of a previous issue (#225) that tracks an unspecified problem occurring after quantization.

## Explanation
The discussion revolves around the potential implementation of the OKLCH color model for lighting effects in Cubyz. The maintainer seeks clarification on where and how this model should be applied, specifically regarding fading values by 8 or rounding them during quantization processes. There is mention of a previous issue (#225) that tracks an unspecified problem occurring after quantization. The maintainer also asks about mixing colors using these models instead of RGB. Each value would fade by 8 like usual or be rounded rather, but the exact implementation details are unclear. For further reading on OKLCH, see [OKLCH](https://oklch.com/), [Oklab](https://bottosson.github.io/posts/oklab/), and [Shadertoy Example](https://www.shadertoy.com/view/wfsXzN).

## Related Questions
- What are the specific requirements for implementing OKLCH in Cubyz?
- How does the current color mixing process work in Cubyz?
- What is the impact of quantization on lighting effects in Cubyz?
- How can the issues tracked by #225 be resolved?
- Are there any performance considerations when switching to OKLCH?
- What are the benefits of using OKLCH over RGB for lighting in Cubyz?

*Source: unknown | chunk_id: github_issue_1235_discussion*
