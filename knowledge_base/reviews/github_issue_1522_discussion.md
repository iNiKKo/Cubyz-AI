# [issues/issue_1522.md] - Issue #1522 discussion

**Type:** review
**Keywords:** event scheduling, command design pattern, leaf decay, torch particles, block entities, server ticks, client-side, server-side
**Concepts:** Command Design Pattern, Event Scheduling, Block Entities

## Summary
The discussion revolves around proposing an event scheduling system using the Command Design Pattern for server-side actions like fast leaf decay and client-side effects like torch particles. The maintainers suggest using block entities or a similar system to manage these events, noting that existing systems might already cover some requirements.

## Explanation
The discussion revolves around proposing an event scheduling system using the Command Design Pattern for server-side actions like fast leaf decay and client-side effects like torch particles. The proposal introduces an event scheduling mechanism where functions with arguments are scheduled to run after a specified number of server ticks. This system aims to handle tasks like leaf decay and particle spawning more efficiently by distributing the workload over multiple ticks and allowing for batching updates. For example, when a log block is broken, an event is scheduled to check its direct neighbors (logs or leaves) and decide whether to destroy or keep them accordingly. If necessary, a subsequent event with a higher radius can be scheduled. The maintainers suggest using block entities or a similar system to manage these events, noting that existing systems might already cover some requirements. They propose instantiating the underlying block entity when starting an event and removing it upon deactivation. This approach would allow for efficient management of server-side actions without converting all basic blocks into entities. The proposal includes mechanisms for saving scheduled events across server restarts by ensuring the server saves which actions are supposed to run when it closes and loads them back next time it starts. For leaf decay, the event checks direct neighbors of the log block to determine if they are leaves or logs, deciding whether to destroy or keep them accordingly, possibly scheduling a subsequent event with a higher radius. The maintainers also note that while this system could be used for spawning torch particles every X ticks, these would require different systems since leaf decay is server-side and particles are client-side. They suggest using the existing block entity system set up in #1446, where empty signs or empty chests wouldn't have a block entity instance associated with them.

## Related Questions
- How does the proposed event scheduling system handle server restarts?
- What are the potential performance implications of distributing leaf decay over multiple ticks?
- How can the block entity system be adapted to manage events without converting all basic blocks?
- Can the existing random tick system be modified to meet the reliability requirements for specific actions?

*Source: unknown | chunk_id: github_issue_1522_discussion*
