# [src/server/command/tickspeed.zig] - Chunk 2511376938

**Type:** review
**Keywords:** tickspeed, description, tickrate, blocks, chunk, tick, frame, server, documentation, random, update
**Symbols:** tickspeed, description
**Concepts:** documentation accuracy, server tick vs frame distinction, random tickrate, blocks per chunk, architectural clarity

## Summary
The reviewer corrected the documentation for the tickspeed command to accurately describe its unit as 'blocks per chunk per tick' instead of 'ticks per chunk per frame', clarifying that a tick represents the server's equivalent of a frame.

## Explanation
The original description stated the command measured 'random tickrate, measured in ticks per chunk per frame'. This phrasing was architecturally misleading because it conflated two distinct concepts: the server's internal time unit (a tick) and the client-side rendering unit (a frame). In Cubyz, a tick is explicitly defined as the server-equivalent of a frame. The command actually controls how many blocks are randomly ticked per chunk within one server tick. By changing 'ticks per chunk per frame' to 'blocks per chunk per tick', the documentation now correctly reflects that the rate is measured in terms of block updates (the effect) occurring per chunk, driven by the server's tick cycle. This edit prevents confusion for users who might expect a direct mapping between client frames and server ticks, ensuring they understand that the command governs block-level randomness within each server tick.

## Related Questions
- What is the exact definition of a tick in Cubyz?
- How does the tickspeed command affect block updates?
- Why was 'ticks per chunk per frame' considered incorrect documentation?
- Does changing this description impact runtime behavior or only docs?
- Is there any code that relies on the old unit interpretation?
- What other commands use similar tickrate terminology?
- How is random tickrate implemented in the server core?
- Are there tests validating the tickspeed command's output?
- Could users be confused by mixing 'tick' and 'frame' terms?
- Is this change part of a larger documentation cleanup effort?

*Source: unknown | chunk_id: github_pr_2226_comment_2511376938*
