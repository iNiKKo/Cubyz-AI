# [hard/codebase_src_network.zig] - Chunk 2

**Type:** networking
**Keywords:** network initialization, deinitialization, IP address formatting, condition variable, network request
**Symbols:** init, deinit, Address, Address.ip, Address.port, Address.isSymmetricNAT, Address.localHost, Address.format, Request, Request.address, Request.data, Request.requestNotifier
**Concepts:** networking, address formatting, request handling

## Summary
Handles network initialization and deinitialization, defines address formatting, and structures for network requests.

## Explanation
This chunk manages the lifecycle of the networking system by initializing various components like sockets, protocols, and authentication during setup. It also provides a method to format IP addresses into human-readable strings. The `Request` struct encapsulates details about a network request, including the target address, data payload, and a condition variable for notification purposes.

The `init` function initializes the networking system by starting up sockets, initializing protocols and authentication, and checking the result of `psa_crypto_init`. The `deinit` function frees the cryptographic resources using `mbedtls_psa_crypto_free`.

The `Address` struct contains fields for IP address (`ip`), port (`port`), and a boolean indicating if it is symmetric NAT (`isSymmetricNAT`). It also has a constant `localHost` representing the loopback address. The `format` method formats the IP address into a human-readable string, optionally including the port number.

The `Request` struct contains fields for the target address (`address`), data payload (`data`), and a condition variable (`requestNotifier`) used for notification purposes.

## Code Example
```zig
pub fn init() !void {
	Socket.startup();
	protocols.init();
	authentication.init();
	try Connection.SecureChannel.checkResult(c.psa_crypto_init(), "psa_crypto_init");
}
```

## Related Questions
- How does the network initialization process start?
- What components are initialized during network setup?
- How is an IP address formatted in this code?
- What fields does a Request struct contain?
- What is the purpose of the requestNotifier field in the Request struct?
- How is the networking system deinitialized?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_2*
