# [issues/issue_288.md] - Issue #288 discussion

**Type:** review
**Keywords:** lighting, bounce, algorithm, fog, realism, brightness, source
**Concepts:** lighting algorithm, floodfill lighting, light propagation, realism

## Summary
The proposal suggests adding a second bounce of light to the existing lighting algorithm, which currently simulates a single direct bounce.

## Explanation
The proposal suggests adding a second bounce of light to the existing lighting algorithm in Cubyz, which currently uses floodfill lighting. Floodfill lighting is a cheap and simple method that only considers the brightest light source at each block and does not simulate multiple bounces of light. Instead, it distributes light uniformly as if the room were filled with fog, making it direction-independent. The maintainer points out that adding secondary light bounces would not significantly change the lighting behavior because the existing algorithm already treats incoming light as the brightest source, making additional bounces less noticeable and potentially redundant. Adding a light source at each block would not make a difference because the algorithm only accounts for the brightest light source and the incoming light is brighter than the proposed secondary light source.

## Related Questions
- How does the current floodfill lighting algorithm handle multiple light sources?
- What is the impact of adding a second bounce of light on performance?
- Can the existing algorithm be modified to simulate more than one bounce of light?
- How would the addition of secondary light bounces affect ambient occlusion?
- Is there a way to optimize the lighting calculations for better performance?

*Source: unknown | chunk_id: github_issue_288_discussion*
