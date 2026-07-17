# [src/server/command/entity/avatar.zig] - Chunk 3330250347

**Type:** review
**Keywords:** avatar, entityModelId, splitScalar, main.entityModel.getById, model.server.put, BinaryWriter, .playerNearby, connectionManager, EntityComponentUpdate.load
**Symbols:** avatar.zig, main.server.User, User, description, usage, model, execute, args, source, split, entityModelId, main.entityModel.getById, entityModel, model.server.put, main.utils.BinaryWriter, binaryWriter, rc.save, .playerNearby, main.server.connectionManager.connections.items, conn, main.network.protocols.EntityComponentUpdate.load
**Concepts:** command parsing, argument validation, entity model registry lookup, server-side state mutation, nearby client broadcasting, stack allocator usage, defer cleanup pattern, connection manager iteration, EntityComponentUpdate protocol, timing of new user registration vs. broadcast

## Summary
The avatar command implementation was added to allow users to change their entity model ID via a /avatar <entityTypeID> syntax, with proper argument parsing and error messaging.

## Explanation
This chunk introduces the /avatar command in src/server/command/entity/avatar.zig. It first checks if the user already has an avatar; if so, it reports the current entityModelId. If no avatar exists, it splits the remaining arguments to extract exactly one entity model ID string. The code validates that only one argument is provided (rejecting extra args with a red message). It then looks up the requested entity model via main.entityModel.getById and stores the new model for the user using model.server.put. Upon success, it sends a green confirmation message. Crucially, after updating the server-side state, it prepares to transmit the change to nearby clients: it initializes a BinaryWriter on the stack allocator, defers cleanup, saves the player’s component data with .playerNearby, and iterates over main.server.connectionManager.connections.items to push an EntityComponentUpdate for each connection. The reviewer notes that this transmission happens before the new user is appended to the users list, meaning the newly connected client would not receive the update; instead, their own initial avatar data will be sent later via zonObject.put("player", ...) after palettes load.

## Related Questions
- What happens if a user runs /avatar with no arguments?
- How does the code prevent sending too many arguments to /avatar?
- Where is the entity model ID stored after a successful change?
- Why is BinaryWriter initialized on main.stackAllocator and deferred?
- Which connections receive the EntityComponentUpdate after an avatar change?
- What message is sent if the requested entityModelId does not exist?
- How does the reviewer suggest handling new clients that connect during /avatar execution?
- Is there any race condition between model.server.put and the broadcast loop?
- What would happen if main.entityModel.getById returns null for a valid ID?
- Does the code handle the case where the user already has an avatar set?

*Source: unknown | chunk_id: github_pr_2865_comment_3330250347*
