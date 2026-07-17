# [src/network.zig] - PR #1309 review diff

**Type:** review
**Keywords:** protocol handler, explosion, packet processing, block entity, onInteract, server validation, client trust
**Symbols:** explode, id, asynchronous, receive, doExplode, Connection, utils.BinaryReader, Vec3i
**Concepts:** network protocol handling, block entities, server-client interaction, thread safety, performance optimization

## Summary
A new protocol handler for explosions is added to the network module.

## Explanation
The code introduces a new protocol handler named 'explode' within the Protocols struct in the network.zig file. This handler processes incoming packets that trigger explosions, reading the position from the packet and checking if the server allows explosives. If valid, it calls the `doExplode` function to handle the explosion logic. The reviewer suggests redesigning this functionality to use block entities, aligning with how other interactions are handled (e.g., onInteract). This would involve moving the code closer to or within the onInteract mechanism and potentially trusting client-side data more unless server-side validation is reintroduced.

## Related Questions
- What is the purpose of the 'explode' protocol handler?
- How does the 'receive' function validate incoming packets for explosions?
- Why does the reviewer suggest redesigning the explosion handling to use block entities?
- What are the implications of trusting client-side data more in this context?
- How could server-side validation be reintroduced to ensure security?
- What other interactions might benefit from being handled as block entities?

*Source: unknown | chunk_id: github_pr_1309_comment_2132492844*
