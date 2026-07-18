# [issues/issue_1364.md] - Issue #1364 discussion

**Type:** review
**Keywords:** snow layers, rotation mode, collision mechanics, melting effects, frost layer, ore pile system, shader
**Concepts:** collision detection, visual representation, shaders

## Summary
Discussion on implementing snow layers in the game, including considerations for rotation modes, collision mechanics, melting effects, and visual representation.

## Explanation
The discussion revolves around the implementation of snow layers in Cubyz. The basic implementation includes a rotation mode that allows varying heights of snow, enabling it to cover objects like leaves. Future mechanics involve adding collision detection (with varying levels of slowdown based on height) and melting effects from heat sources. There is also a debate between implementing snow as a frost layer or as distinct snow piles. Maintainers suggest using shaders for visual effects and consider integrating snow into an ore pile system. The user emphasizes the distinction between snow and frost, advocating for separate implementations to allow for fluffy snow piling on leaves.

## Related Questions
- What are the proposed collision mechanics for snow layers?
- How will melting effects be implemented in the snow layers?
- Are there any plans to differentiate between snow and frost visually?
- What is the suggested approach for integrating snow into the game's ore system?
- Can you explain the role of shaders in enhancing the visual appearance of snow layers?
- How does the rotation mode affect the height variation of snow layers?

*Source: unknown | chunk_id: github_issue_1364_discussion*
