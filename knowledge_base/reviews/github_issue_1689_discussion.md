# [issues/issue_1689.md] - Issue #1689 discussion

**Type:** review
**Keywords:** jump height, lag, sneak-jump, Terraria, fps dependent, lerp, exact integration, movement, delta time
**Concepts:** frame rate, linear interpolation (lerp), fixed frame rate, exact integration

## Summary
Discussion about the impact of frame rate on jump height and movement in Cubyz. Maintainers suggest using fixed frame rates for critical functions like movement.

## Explanation
The discussion revolves around the issue where jump height is affected by lag, making it difficult to perform actions like sneak-jumping onto blocks. The maintainers explore potential solutions such as running the computing side at a fixed 60 fps while rendering separately, similar to Terraria's approach. They also consider whether the problem stems from linear interpolation (lerp) being frame rate dependent. A maintainer comment specifically states that 'Cubyz uses exact integration for the position update, including gravity, no lerping there.' Users point out that any function not accounting for frame rate is inherently frame rate dependent and suggest either enforcing a fixed frame rate for important functions or modifying them to account for delta time.

## Related Questions
- How does changing the frame rate affect jump height in Cubyz?
- What is the impact of using linear interpolation on movement in games with variable frame rates?
- Can enforcing a fixed frame rate for critical functions like movement resolve issues related to lag?
- How does exact integration differ from using lerp for position updates in game physics?
- What are the benefits and drawbacks of separating computation and rendering in terms of performance and gameplay consistency?
- How can developers modify functions to account for delta time to ensure frame rate independence?

*Source: unknown | chunk_id: github_issue_1689_discussion*
