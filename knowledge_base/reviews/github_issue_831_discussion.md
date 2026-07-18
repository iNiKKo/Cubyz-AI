# [issues/issue_831.md] - Issue #831 discussion

**Type:** review
**Keywords:** fog, banding, stone, dithering, post-processing, shader
**Concepts:** color banding, dithering, post-processing

## Summary
Discussion about adding dithering in a post-processing shader to fix color banding issues.

## Explanation
The issue report highlights that fog and other surfaces like stone exhibit color banding. The maintainer suggests implementing dithering as a solution in the post-processing shader, but emphasizes that it may not be necessary immediately due to the low visibility of the banding effect. The maintainer also clarifies that the banding is not specifically related to fog.

## Related Questions
- What are the potential benefits of implementing dithering in the post-processing shader?
- How does dithering help mitigate color banding issues?
- Are there any performance considerations when adding dithering to the shader?
- Can you provide examples of other surfaces that exhibit color banding besides fog and stone?
- What is the current visibility level of color banding in Cubyz, according to the maintainer?
- Is there a plan to implement dithering soon, or will it be addressed later?
- How does the maintainer suggest handling the unrelated nature of banding with different surfaces?
- Are there any alternative solutions proposed for fixing color banding issues?
- What are the potential trade-offs of adding dithering in terms of visual quality and performance?
- Can you explain how dithering works in a post-processing shader context?

*Source: unknown | chunk_id: github_issue_831_discussion*
