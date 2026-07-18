# [hard/codebase_src_sync.zig] - Chunk 14

**Type:** serialization
**Keywords:** binary serialization, action execution, permission checks, state updates, user interactions
**Symbols:** UpdateBlock, UpdateBlock.serialize, UpdateBlock.deserialize, AddHealth, AddHealth.target, AddHealth.health, AddHealth.cause, AddHealth.run, AddHealth.serialize, AddHealth.deserialize, ChatCommand, ChatCommand.message, ChatCommand.finalize, ChatCommand.run, ChatCommand.serialize, ChatCommand.deserialize
**Concepts:** serialization, deserialization, game actions, server-side logic

## Summary
This chunk defines serialization and deserialization functions for various game actions such as block updates, health changes, and chat commands.

## Explanation
The chunk contains three main structs: UpdateBlock, AddHealth, and ChatCommand. Each struct has methods for serializing its data to a BinaryWriter and deserializing it from a BinaryReader. The serialize methods write the fields of each struct in a specific order, while the deserialize methods read these fields back into new instances of the respective structs. Additionally, the AddHealth and ChatCommand structs have a 'run' method that implements the logic for executing the action on the server side, including checking permissions and updating game state.

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
- How does the UpdateBlock struct serialize its data?
- What is the purpose of the 'run' method in the AddHealth struct?
- How does the ChatCommand struct handle deserialization of its message field?
- What checks are performed before executing a chat command on the server?
- How is the health value serialized and deserialized in the AddHealth struct?
- What happens if the target user is not found during the execution of an AddHealth action?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_14*
