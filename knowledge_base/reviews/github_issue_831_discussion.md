# [issues/issue_831.md] - Issue #831 discussion

**Type:** review
**Keywords:** fog, banding, stone, dithering, post-processing, shader
**Concepts:** color banding, dithering, post-processing

## Summary
Discussion about adding dithering in a post-processing shader to fix color banding issues.

## Explanation
Discussion about adding dithering in a post-processing shader to fix color banding issues. The issue report highlights that fog and other surfaces like stone exhibit color banding. The maintainer suggests implementing dithering as a solution but emphasizes that it may not be necessary immediately due to the low visibility of the banding effect. Specifically, the maintainer states: 'The banding is completely unrelated to the fog by the way, you can also see it on the stone for example.' This clarifies that while fog and stone both exhibit color banding, the issue is more general and not specific to any particular surface.

## Related Questions
- What are the potential benefits of implementing dithering in the post-processing shader?
- How does dithering help mitigate color banding issues?
- Are there any performance considerations when adding dithering to the shader?
- Can you provide examples of other surfaces that exhibit color banding besides fog and stone?
- What is the current visibility level of color banding in Cubyz, according to the maintainer?
- Is there a plan to implement dithering soon, or will it be addressed later?

*Source: unknown | chunk_id: github_issue_831_discussion*
