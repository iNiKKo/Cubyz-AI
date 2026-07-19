# [hard/codebase_src_network_protocols.zig] - Chunk 0

**Type:** networking
**Keywords:** protocol registration, message dispatch, handshake validation, binary data transmission, connection type differentiation
**Symbols:** clientReceiveList, serverReceiveList, bytesReceived, bytesSent, init, onReceive, reload, reload.id, reload.informClientOfRestart, reload.informServerOfRestart
**Concepts:** networking protocol, message handling, handshake management, data serialization

## Summary
Handles network protocol initialization and message reception.

## Explanation
This chunk manages the initialization of network protocols and processes incoming messages. It maintains lists of receive functions for both clients and servers, indexed by protocol ID (`clientReceiveList` and `serverReceiveList`). The `init` function registers protocols with their respective receive handlers. The `onReceive` function checks handshake completion and dispatches incoming data to the appropriate handler based on connection type (client or server). The `reload` struct defines a protocol for informing clients and servers about restarts. It includes methods `informClientOfRestart` and `informServerOfRestart`, which write necessary data using `BinaryWriter` and send it over three different network channels: `.secure`, `.lossy`, and `.slow`. Each method writes the connection's restart counter and, in the case of `informClientOfRestart`, also writes the user's state. Specifically, `informClientOfRestart` writes the restart counter and the user's state using `BinaryWriter`, then sends this data over three channels: `.secure`, `.lossy`, and `.slow`. Similarly, `informServerOfRestart` writes only the restart counter and sends it over the same three channels. If there is a duplicate protocol ID during initialization, an error message is logged. The `bytesReceived` and `bytesSent` arrays track the number of bytes received and sent for each protocol index.

## Code Example
```zig
pub fn init() void { // MARK: init()
	inline for (@typeInfo(@This()).@"struct".decls) |decl| {
		const Protocol = @field(@This(), decl.name);
		if (@TypeOf(Protocol) == type and @hasDecl(Protocol, "id")) {
			const id = Protocol.id;
			if (clientReceiveList[id] == null and serverReceiveList[id] == null) {
				if (@hasDecl(Protocol, "clientReceive")) {
					clientReceiveList[id] = Protocol.clientReceive;
				}
				if (@hasDecl(Protocol, "serverReceive")) {
					serverReceiveList[id] = Protocol.serverReceive;
				}
			} else {
				std.log.err("Duplicate list id {}.", .{id});
			}
		}
	}
}
```

## Related Questions
- What is the purpose of the `init` function?
- How are protocols registered in this chunk?
- What does the `onReceive` function check before processing a message?
- How is data serialized and sent in the `reload` struct methods?
- What happens if there is a duplicate protocol ID during initialization?
- How many different network channels are used to send restart information?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_0*
