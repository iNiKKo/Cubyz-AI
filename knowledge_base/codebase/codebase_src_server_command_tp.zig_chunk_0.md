# [easy/codebase_src_server_command_tp.zig] - Chunk 0

**Type:** api
**Keywords:** union enum, ArgParser parse, ClimateMap fragment, genericUpdate sendTPCoordinates, spiral radius, biome height hills mountains roughness, Target fromPlayerIndex, defer deinit
**Symbols:** Args, ArgParser, execute
**Concepts:** command parsing, spiral search, biome lookup, coordinate resolution, network protocol message sending

## Summary
Implements the /tp server command for teleporting a user to a specified biome via spiral search or direct coordinates.

## Explanation
The chunk defines an Args union with three cases: biome lookup, coordinate parsing, and player-index target. It uses ArgParser.parse to validate input into a result union. For the biome case it computes a spiral radius (16384) and iterates over ClimateMap fragments in a spiral pattern, sampling each fragment's map for matching biome; when found it calculates z from height/hills/mountains/roughness and sends TP coordinates via genericUpdate.sendTPCoordinates. If no match is found after the spiral it reports an error. For the coordinate case it delegates to command.resolveCoordinates. For the player-index case it calls command.Target.fromPlayerIndex, defers deinit, then breaks with target.user.player().pos. Finally it always sends the resolved position via genericUpdate.sendTPCoordinates.

## Related Questions
- What are the three possible argument forms for the /tp command and their corresponding data structures?
- How does the chunk compute the spiral search radius and iterate over ClimateMap fragments?
- In the biome case, how is the target Z coordinate derived from sample fields?
- What happens when ArgParser.parse fails and what message is sent to the user?
- How does the chunk handle teleporting to another player via their index?
- Where are TP coordinates transmitted after a successful resolution?

*Source: unknown | chunk_id: codebase_src_server_command_tp.zig_chunk_0*
