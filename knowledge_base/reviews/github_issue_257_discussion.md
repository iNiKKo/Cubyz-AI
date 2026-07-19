# [issues/issue_257.md] - Issue #257 discussion

**Type:** review
**Keywords:** stamina, muscle groups, oxygen, energy, sleep quality, grinding, biome design, nutrition
**Concepts:** stamina mechanics, muscle tracking, respiration types, player communication, skilling/levelling system

## Summary
The discussion revolves around the complexity of implementing stamina mechanics in Cubyz, including muscle-specific tracking and nutritional effects. The maintainer suggests keeping it simple with a single stamina bar for ease of communication.

## Explanation
Stamina in Cubyz is replenished naturally and consumes hunger. Not all actions consume stamina; for example, sprinting does not consume stamina but requires a certain level of stamina to perform. When using tools or weapons, stamina decreases depending on their weight. This can add depth to combat and crafting, such as a low-range dagger consuming less stamina than a long-range spear. As players conserve stamina in combat styles or against certain bosses, the choice between different weapons might vary.

The discussion also explores more complex implementations of stamina mechanics, including muscle-specific tracking and nutritional effects. For instance, each muscle could have its own temporary store of oxygen/energy, which could be tracked independently. There are several categories of muscle fibers that use different types of respiration (aerobic or anaerobic), which could affect stamina consumption differently. Anaerobic respiration might deplete hunger more quickly due to being less efficient.

The maintainer suggests keeping it simple with a single stamina bar for ease of communication and does not think adding another bar to the UI is justified. They also consider that similar mechanical depth could be achieved with the energy bar concept.

## Related Questions
- How does using tools or weapons affect stamina consumption?
- What is the impact of sprinting on stamina?

*Source: unknown | chunk_id: github_issue_257_discussion*
