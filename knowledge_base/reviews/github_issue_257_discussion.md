# [issues/issue_257.md] - Issue #257 discussion

**Type:** review
**Keywords:** stamina, muscle groups, oxygen, energy, sleep quality, grinding, biome design, nutrition
**Concepts:** stamina mechanics, muscle tracking, respiration types, player communication, skilling/levelling system

## Summary
The discussion revolves around the complexity of implementing stamina mechanics in Cubyz, including muscle-specific tracking and nutritional effects. The maintainer suggests keeping it simple with a single stamina bar for ease of communication.

## Explanation
The discussion revolves around the complexity of implementing stamina mechanics in Cubyz, including individual muscle group tracking and nutritional effects. The user proposes a detailed model where each muscle has its own temporary store of oxygen/energy, leading to different types of respiration (aerobic vs anaerobic) affecting stamina differently. For example, anaerobic respiration depletes hunger more quickly due to being less efficient, which could mean that running and sprinting have slightly different stamina trackers. The maintainer suggests keeping it simple with a single stamina bar for ease of communication, arguing against the complexity introduced by muscle-specific tracking and nutritional effects. They also mention that while sleep quality could boost stamina recovery (though this is a separate topic), simulating muscle growth would introduce a skilling/levelling system which might lead to more grinding and complicate biome design.

## Related Questions
- What are the potential benefits of tracking each muscle group's stamina independently?
- How does anaerobic respiration affect hunger depletion compared to aerobic respiration?
- Why does the maintainer suggest keeping the stamina mechanics simple with a single bar?
- What is the proposed relationship between sleep quality and stamina recovery in Cubyz?
- How could simulating muscle growth impact the game's balance and player progression?
- What are the potential challenges of ensuring all nutrients are accessible in most surface biomes?

*Source: unknown | chunk_id: github_issue_257_discussion*
