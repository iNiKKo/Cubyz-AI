# [hard/codebase_src_network_protocols.zig] - Chunk 1

**Type:** networking
**Keywords:** network protocols, handshake states, TLS handshake, ZonElement, version compatibility
**Symbols:** serverReceive, sendServerPlayerData, serverSide, clientSide
**Concepts:** networking, handshake protocol, data exchange, player authentication

## Summary
Handles server-side network protocols for Cubyz, including handshake states and data exchange.

## Explanation
This chunk implements the server-side logic for handling network connections in the Cubyz engine. It includes functions for receiving client data (`serverReceive`), sending player data to the server (`sendServerPlayerData`), initializing the server side of a connection (`serverSide`), and setting up the client side of a connection (`clientSide`). The `serverReceive` function processes different handshake states such as userData, signatureResponse, reload, and more. It ensures that the received data is valid, verifies player names, checks version compatibility, and handles asset loading. The `sendServerPlayerData` function constructs a ZonElement object containing various game state information and sends it to the client. The `serverSide` function initializes the handshake state for a new connection. The `clientSide` function prepares the initial handshake data and starts the TLS handshake process.

## Code Example
```zig
pub fn serverSide(conn: *Connection) void {
	conn.handShakeState.store(.start, .monotonic);
}
```

## Related Questions
- What is the initial handshake state set in the `serverSide` function?
- How does the `serverReceive` function handle userData packages?
- What data is sent to the client in the `sendServerPlayerData` function?
- What steps are taken to start a TLS handshake on the client side?
- How is player name validation performed in the `serverReceive` function?
- What happens if an unexpected state package is received by the server?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_1*
