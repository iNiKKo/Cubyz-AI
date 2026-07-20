# [hard/codebase_src_sync.zig] - Chunk 14

**Type:** serialization
**Keywords:** binary serialization, action execution, permission checks, state updates, user interactions
**Symbols:** UpdateBlock, UpdateBlock.serialize, UpdateBlock.deserialize, AddHealth, AddHealth.target, AddHealth.health, AddHealth.cause, AddHealth.run, AddHealth.serialize, AddHealth.deserialize, ChatCommand, ChatCommand.message, ChatCommand.finalize, ChatCommand.run, ChatCommand.serialize, ChatCommand.deserialize
**Concepts:** serialization, deserialization, game actions, server-side logic

## Summary
This chunk defines serialization and deserialization functions for various game actions such as block updates, health changes, and chat commands.

## Explanation
This chunk defines serialization and deserialization functions for various game actions such as block updates, health changes, and chat commands. Each struct has methods for serializing its data to a BinaryWriter and deserializing it from a BinaryReader. The serialize methods write the fields of each struct in a specific order, while the deserialize methods read these fields back into new instances of the respective structs. Additionally, the AddHealth and ChatCommand structs have 'run' methods that implement the logic for executing the action on the server side, including checking permissions and updating game state.

The 'AddHealth' struct includes permission checks to ensure that only users in creative mode can receive health changes. The 'ChatCommand' struct handles deserialization of its message field by reading a variable-length integer followed by the actual message bytes.

### Serialization Methods
- **UpdateBlock.serialize**: Writes the source, position, drop location normal direction, min and max values, old block, and new block to the BinaryWriter.
- **AddHealth.serialize**: Writes the target entity, health value, and cause of damage to the BinaryWriter.
- **ChatCommand.serialize**: Writes the length of the message followed by the message bytes to the BinaryWriter.

### Deserialization Methods
- **UpdateBlock.deserialize**: Reads the source, position, drop location normal direction, min and max values, old block, and new block from the BinaryReader and returns a new instance of UpdateBlock.
- **AddHealth.deserialize**: Reads the target entity, health value, and cause of damage from the BinaryReader and returns a new instance of AddHealth. It also checks if the user executing the command is valid.
- **ChatCommand.deserialize**: Reads the length of the message followed by the message bytes from the BinaryReader and returns a new instance of ChatCommand.

### Run Methods
- **AddHealth.run**: Executes the health change action, checking permissions and updating the game state. It also handles the case where the target user is not found.
- **ChatCommand.run**: Executes the chat command, logging the command if cheats are allowed and sending a message otherwise.

## Code Example
```zig
fn serialize(self: UpdateBlock, writer: *BinaryWriter) void {
	self.source.write(writer);
	writer.writeVec(Vec3i, self.pos);
	writer.writeVec(Vec3f, self.dropLocation.normalDir);
	writer.writeVec(Vec3f, self.dropLocation.min);
	writer.writeVec(Vec3f, self.dropLocation.max);
	writer.writeInt(u32, @as(u32, @bitCast(self.oldBlock)));
	writer.writeInt(u32, @as(u32, @bitCast(self.newBlock)));
}
```

## Related Questions
- What specific fields does the UpdateBlock struct serialize?
- How does the AddHealth struct ensure that only users in creative mode can receive health changes?
- What is the format of the message field in the ChatCommand struct during deserialization?
- What checks are performed before executing a chat command on the server?
- How is the health value serialized and deserialized in the AddHealth struct?
- What happens if the target user is not found during the execution of an AddHealth action?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_14*
