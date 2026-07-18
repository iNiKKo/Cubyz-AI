# [issues/issue_288.md] - Issue #288 discussion

**Type:** review
**Keywords:** lighting, bounce, algorithm, fog, realism, brightness, source
**Concepts:** lighting algorithm, floodfill lighting, light propagation, realism

## Summary
The proposal suggests adding a second bounce of light to the existing lighting algorithm, which currently simulates a single direct bounce.

## Explanation
The current lighting algorithm in Cubyz uses floodfill lighting, which is a cheap and simple method that only considers the brightest light source at each block. It does not simulate multiple bounces of light but rather distributes light uniformly as if the room were filled with fog. The proposal aims to enhance realism by adding a second bounce of light, where light reflected off surfaces propagates further. However, the maintainer points out that this would not significantly change the lighting behavior because the existing algorithm already treats incoming light as the brightest source, making additional bounces less noticeable.

## Related Questions
- How does the current floodfill lighting algorithm handle multiple light sources?
- What is the impact of adding a second bounce of light on performance?
- Can the existing algorithm be modified to simulate more than one bounce of light?
- How would the addition of secondary light bounces affect ambient occlusion?
- Is there a way to optimize the lighting calculations for better performance?
- What are the potential visual artifacts introduced by simulating multiple light bounces?

*Source: unknown | chunk_id: github_issue_288_discussion*
