# [issues/issue_1522.md] - Issue #1522 discussion

**Type:** review
**Keywords:** event scheduling, command design pattern, leaf decay, torch particles, block entities, server ticks, client-side, server-side
**Concepts:** Command Design Pattern, Event Scheduling, Block Entities

## Summary
The discussion revolves around proposing an event scheduling system using the Command Design Pattern for server-side actions like fast leaf decay and client-side effects like torch particles. The maintainers suggest using block entities or a similar system to manage these events, noting that existing systems might already cover some requirements.

## Explanation
The proposal introduces an event scheduling mechanism where functions with arguments are scheduled to run after a specified number of server ticks. This system aims to handle tasks like leaf decay and particle spawning more efficiently by distributing the workload over multiple ticks and allowing for batching updates. The maintainers raise concerns about the separation between server-side and client-side actions, suggesting that block entities could be leveraged to manage these events without converting all basic blocks into entities. They also mention existing work on block entities in another pull request, indicating a potential path forward for implementing such features.

## Related Questions
- How does the proposed event scheduling system handle server restarts?
- What are the potential performance implications of distributing leaf decay over multiple ticks?
- How can the block entity system be adapted to manage events without converting all basic blocks?
- Can the existing random tick system be modified to meet the reliability requirements for specific actions?
- What considerations should be made for ensuring thread safety in the event scheduling mechanism?
- How does the proposed system compare to existing mechanisms for handling scheduled tasks in Cubyz?

*Source: unknown | chunk_id: github_issue_1522_discussion*
