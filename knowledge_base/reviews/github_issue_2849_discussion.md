# [issues/issue_2849.md] - Issue #2849 discussion

**Type:** review
**Keywords:** crop mechanics, growth stages, soil effects, withering, chance-based, dry soil, player engagement
**Concepts:** gameplay, player engagement, simplification

## Summary
Discussion on crop growth and withering mechanics in Cubyz, focusing on simplicity versus complexity.

## Explanation
Discussion on crop mechanics in Cubyz, including detailed aspects of growth stages, soil effects, withering, and player engagement. The maintainer proposes simplifying the system to make it more engaging by removing chance-based withering and ensuring crops do nothing on dry soil. This approach aims to encourage players to actively tend to their farms without adding unnecessary complexity. Specific details include: 

- **Growth:** Crops have multiple stages of growth, growing every minute based on soil type (soil-dependent chance). They also suck moisture from the soil every minute (crop-dependent chance), only grow during daylight hours and under glass.
- **Soil Types:** Mud (most efficient, transforms into Soil), Soil (medium efficiency, transforms into Dirt), Dirt (low efficiency, allows withering), Clay (medium efficiency, faster withering), Aerosoil (low efficiency, no sunlight required but allows withering), Permafrost (very low efficiency, allows withering).
- **Withering Mechanics:** Mature crops on soil that allow withering will begin to visibly wilt in stages. Only the final few stages prevent successful harvest.
- **Harvesting:** Crops can be harvested slowly by hand or efficiently using a sickle; mature crops yield 2-3 crops and 0-2 seeds.

## Related Questions
- What are the specific soil types that affect crop growth?
- How does moisture absorption work for different crops?
- What happens to crops when planted on dry soil?
- What is the exact yield of mature crops during harvesting?

*Source: unknown | chunk_id: github_issue_2849_discussion*
