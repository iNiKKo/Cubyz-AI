# [hard/codebase_src_network.zig] - Chunk 1

**Type:** networking
**Keywords:** UDP, socket operations, OS-specific handling, error management, timeout handling
**Symbols:** Socket, Socket.posix, Socket.socketID, Socket.windowsError, Socket.startup, Socket.init, Socket.deinit, Socket.send, Socket.receive, Socket.resolveIP, Socket.getPort
**Concepts:** networking

## Summary
The chunk defines a `Socket` struct for UDP networking, handling OS-specific socket operations and errors.

## Explanation
This chunk implements a `Socket` struct that encapsulates the creation, initialization, sending, receiving, and cleanup of UDP sockets. It handles both Windows and POSIX-compliant systems by checking the operating system tag at compile time. The `Socket` struct includes methods for error handling specific to Windows (`windowsError`), initializing the socket (`init`), deinitializing it (`deinit`), sending data (`send`), receiving data with a timeout (`receive`), resolving IP addresses from hostnames (`resolveIP`), and retrieving the local port of the socket (`getPort`). The code manages OS-specific differences in socket operations, such as using `WSAStartup` on Windows and handling different error codes. It also includes logging for warnings and errors encountered during socket operations.

On Windows, the socket type is `c.SOCKET`, while on POSIX systems, it is `posix.socket_t`. The `windowsError` function maps specific Windows error codes to Zig error types as follows:
- `WSASYSNOTREADY` to `error.NetworkDown`
- `WSAVERNOTSUPPORTED` to `error.VersionUnsupported`
- `WSAEINPROGRESS` to `error.BlockingOperationInProgress`
- `WSAEPROCLIM` to `error.ProcessFdQuotaExceeded`
- `WSAEADDRINUSE` to `error.AddressInUse`
- `WSAEADDRNOTAVAIL` to `error.AddressNotAvailable`
- `WSAENOBUFS` to `error.SystemResources`
- `WSAENOTSOCK` to `error.FileDescriptorNotASocket`
- Any other error code to `error.UNKNOWN`

The `Socket.init` method creates a UDP socket using `c.socket` on Windows and `std.c.socket` on POSIX systems. It specifies the address family as `AF_INET`, the socket type as `SOCK_DGRAM`, and the protocol as `0`. If the socket creation fails, it logs an error and panics.

The `resolveIP` method uses `std.Io.net.HostName.lookup` to resolve hostnames to IP addresses. It handles both IPv4 and IPv6 addresses but only returns IPv4 addresses as a 32-bit integer. The method initializes a buffer for the hostname lookup result, sets up a queue for results, and performs the lookup with the specified parameters. If no data is received within the timeout period in the `receive` method, it uses `WSAPoll` on Windows and `posix.poll` on POSIX systems to handle timeouts and returns an `error.Timeout`.

The `getPort` method retrieves the local port of the socket using `c.getsockname` on Windows and `std.c.getsockname` on POSIX systems. It specifies the address family as `AF_INET` and retrieves the port number from the socket address structure.

## Code Example
```zig
fn windowsError(err: c_int) !void {
		if (err == 0) return;
		switch (err) {
			c.WSASYSNOTREADY => return error.NetworkDown,
			c.WSAVERNOTSUPPORTED => return error.VersionUnsupported,
			c.WSAEINPROGRESS => return error.BlockingOperationInProgress,
			c.WSAEPROCLIM => return error.ProcessFdQuotaExceeded,
			c.WSAEFAULT => unreachable,
			c.WSANOTINITIALISED => unreachable,
			c.WSAENETDOWN => return error.NetworkDown,
			c.WSAEACCES => return error.AccessDenied,
			c.WSAEADDRINUSE => return error.AddressInUse,
			c.WSAEADDRNOTAVAIL => return error.AddressNotAvailable,
			c.WSAEINVAL => unreachable,
			c.WSAENOBUFS => return error.SystemResources,
			c.WSAENOTSOCK => return error.FileDescriptorNotASocket,
			else => return error.UNKNOWN,
		}
	}
```

## Related Questions
-  What is the purpose of the `windowsError` function in the Socket struct?
-  How does the `Socket.init` method handle socket creation on Windows and POSIX systems?
-  What steps are taken to resolve an IP address from a hostname using the `resolveIP` method?
-  Describe the error handling mechanism for sending data through the `send` method.
-  How is the local port of a socket retrieved in the `getPort` method?
-  What is the role of the `startup` function in the Socket struct, and when is it called?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_1*
