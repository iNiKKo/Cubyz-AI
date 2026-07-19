# [src/network.zig] - PR #1309 review diff

**Type:** review
**Keywords:** explosion, protocol handler, network.zig, receive function, doExplode function, block entities, onInteract, server-client trust
**Symbols:** explode, id, asynchronous, receive, doExplode, Connection, utils.BinaryReader, Vec3i
**Concepts:** network protocol handling, block entities, client-server trust model, architectural redesign

## Summary
A new protocol handler for explosions is added to the network module.

## Explanation
A new protocol handler for explosions is added to the network module within the Protocols struct in the network.zig file. This handler has an ID of 14 and is synchronous. The 'receive' function processes incoming packets related to explosions by reading the position from the packet using Vec3i, checking if the user is valid and if explosives are allowed in the server world, and then calls the doExplode function to handle the explosion logic. The reviewer suggests that this functionality should be integrated with block entities and possibly moved to a more centralized interaction handling mechanism like onInteract, due to architectural concerns about trust in client-side data and potential redesign implications.

## Related Questions
- What is the purpose of the 'explode' protocol handler in network.zig?
- How does the 'receive' function handle incoming explosion packets?
- Why does the reviewer suggest moving this functionality to block entities?
- What are the implications of trusting client-side data for explosions?
- How might integrating with onInteract affect the server-client interaction model?
- Can you explain the role of Vec3i in the 'explode' protocol handler?

*Source: unknown | chunk_id: github_pr_1309_comment_2132492844*
