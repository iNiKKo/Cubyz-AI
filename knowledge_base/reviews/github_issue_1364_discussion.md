# [issues/issue_1364.md] - Issue #1364 discussion

**Type:** review
**Keywords:** snow layers, rotation mode, collision mechanics, melting effects, frost layer, ore pile system, shader
**Concepts:** collision detection, visual representation, shaders

## Summary
Discussion on implementing snow layers in Cubyz, including a rotation mode for varying heights, no collision detection (but slows movement), melting by heat sources, debate between snow piles and frost layer, and potential shader integration.

## Explanation
The discussion centers around the implementation of snow layers in Cubyz. The basic implementation includes a rotation mode that allows for varying heights of snow, enabling it to cover objects like leaves without any collision detection (though walking through it slows you down). The higher the snow pile is, the more it will slow movement; the first layer has no effect on movement. Snow melts when exposed to heat sources. There is debate between implementing snow as distinct piles or a frost layer applied to blocks. Maintainers suggest using shaders for visual effects and consider integrating snow into an ore pile system. The user emphasizes the distinction between snow and frost, advocating for separate implementations to allow for fluffy snow piling on leaves.

## Related Questions
- What are the proposed collision mechanics for snow layers?
- How will melting effects be implemented in the snow layers?
- Are there any plans to differentiate between snow and frost visually?
- What is the suggested approach for integrating snow into the game's ore system?
- Can you explain the role of shaders in enhancing the visual appearance of snow layers?

*Source: unknown | chunk_id: github_issue_1364_discussion*
