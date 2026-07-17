# [easy/codebase_src_server_command_entity_avatar.zig] - Chunk 0

**Type:** api
**Keywords:** union enum, argparse parser, stack allocator, defer cleanup, entity model index, get put server, message list
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command parsing, argument union dispatch, server-side state mutation, user messaging

## Summary
Implements the /avatar command handler for server-side avatar lookup and modification.

## Explanation
The chunk defines a public description and usage string for the /avatar command, then declares an Args union with two cases: one for bare /avatar (struct {}) and one for /avatar <entityModel> carrying an entityModel field of type command.EntityModel. It instantiates ArgParser using main.argparse.Parser(Args, .{.commandName = "/avatar"}). The execute function takes a raw argument slice and a source User pointer; it allocates a List(u8) errorMessage on the stack allocator with defer cleanup. Parsing is performed via ArgParser.parse(main.stackAllocator, args, &errorMessage), catching any parse failure: on error the message list is sent to the user as red text and execution returns early. On success, result is switched over: for the parameterized case it calls model.server.put(source.id, .{.entityModel = params.entityModel.index}) to store the new entity model index under the user's ID, then sends a green confirmation message containing the resolved entityModelId via rc.get().entityModelId. For the bare /avatar case it attempts to retrieve the existing record with model.server.get(source.id); if found (rc is non-null) it sends a green message showing the current entityModelId, otherwise it sends a magenta "You are invisible." message.

## Related Questions
- What does the Args union contain and how are its cases distinguished?
- How is ArgParser instantiated for this command?
- What happens when parsing fails in execute?
- Which function is called to store a new avatar under a user ID?
- How is the current avatar retrieved before displaying it?
- What text color is used for an invisible user message?

*Source: unknown | chunk_id: codebase_src_server_command_entity_avatar.zig_chunk_0*
