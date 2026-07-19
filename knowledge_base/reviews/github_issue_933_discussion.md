# [issues/issue_933.md] - Issue #933 discussion

**Type:** review
**Keywords:** oxygen meter, suffocation, drowning, max health, modular design, environmental effects, breathing difficulties, toxic gases, submerged, health reduction
**Symbols:** oxygen meter, suffocation, drowning, max health
**Concepts:** modular design, player health management, environmental effects

## Summary
The discussion revolves around implementing an oxygen meter system that affects player health when submerged in water or exposed to toxic gases. The proposed system includes effects like suffocation and drowning, with potential for modding.

## Explanation
The discussion revolves around implementing an oxygen meter system to simulate breathing difficulties underwater or in toxic environments. The maintainers propose a modular design where different effects can be applied based on the player's oxygen level, such as suffocation and drowning. When submerged in water, the player loses max health over time at a constant rate due to drowning. If the player enters an unbreathable area like water or toxic gas, their oxygen meter starts depleting; when fully depleted, the unbreathable block applies its effects (drowning for water, poisoning for toxic gases). The suffocation effect is applied regardless of whether it's from water or toxic gas and causes a constant rate loss of max health. When out of the water, the player's maximum health remains reduced until the drowning bar is completely drained; once drained, max health regenerates alongside the oxygen bar. If the player goes underwater again while the drowning bar isn't drained, the effect continues. The system also allows for modders to create additional effects like smoker's lung and COPD: smoker's lung reduces max oxygen gradually based on how much smoke is inhaled (permanent until death), and COPD increases coughing chances every second with a random chance of being given when smoking.

The oxygen meter's depletion rate depends on the environment. For example, water depletes oxygen faster than toxic gases. There are no plans for a visual indicator for the oxygen meter in the game interface at this time. The performance implications of implementing this system have not been discussed or addressed.

## Related Questions
- What are the proposed effects of suffocation and drowning in the oxygen meter system?
- How does the modular design allow for additional effects to be created by modders?
- What is the impact on player health when submerged in water or exposed to toxic gases?
- How does the oxygen meter interact with different environmental conditions?
- Can players recover their maximum health after being affected by drowning?
- What are the potential long-term effects of inhaling smoke or having COPD according to the proposed system?
- How is the oxygen meter's depletion rate determined in different environments?
- Are there any plans for a visual indicator for the oxygen meter in the game interface?
- How does the system handle players who return to water after their oxygen bar has been drained?
- What are the performance implications of implementing this oxygen meter system?

*Source: unknown | chunk_id: github_issue_933_discussion*
