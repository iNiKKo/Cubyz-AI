# [hard/codebase_src_network.zig] - Chunk 2

**Type:** networking
**Keywords:** STUN, NAT, ipServerList, MAGIC_COOKIE, requestAddress, format, isSymmetricNAT, localHost, ConnectionManager, socket resolution
**Symbols:** Address, localHost, format, Request, stun, ipServerList, MAPPED_ADDRESS, XOR_MAPPED_ADDRESS, MAGIC_COOKIE, requestAddress
**Concepts:** STUN protocol, NAT traversal, symmetric NAT detection, server list configuration, message construction, magic cookie handling, transaction ID generation, address resolution

## Summary
Implements STUN protocol logic for NAT traversal including server list configuration, message construction with magic cookies and transaction IDs, address resolution handling, and symmetric NAT detection.

## Explanation
This chunk defines the Address struct with fields ip (u32), port (u16), and isSymmetricNAT (bool default false). It exposes a public const localHost set to 0x0100007f. The format method conditionally prints IPv4 dotted-decimal notation, inserting an extra octet when isSymmetricNAT is true to represent the symmetric NAT address format. A Request struct holds an Address, data ([]const u8), and a notifier Condition from main.utils. The stun struct contains a const ipServerList array of 70+ STUN server strings with ports (mostly 3478, some exceptions like Google's 19302 and sipgate.net's 10000). It defines constants MAPPED_ADDRESS (0x0001) and XOR_MAPPED_ADDRESS (0x0020), and MAGIC_COOKIE as [_]u8{0x21, 0x12, 0xA4, 0x42}. The requestAddress function takes a ConnectionManager pointer, seeds std.Random.DefaultCsprng using main.timestamp().toMilliseconds() written into the first 16 bytes of a seed array via std.mem.writeInt with builtin.cpu.arch.endian(), then initializes the RNG. It iterates 16 times to pick random servers from ipServerList using random.random().intRangeAtMost(usize, 0, ipServerList.len - 1). For each server it builds a STUN message: bytes 0-1 set to 0x00, 0x01 (message type), bytes 2-3 zeroed as length placeholder, magic cookie at indices 4-7, and zeros for transaction ID. It fills data[8..] with random bytes via random.fill. The server string is split on ':' using std.mem.splitScalar(u8, ...). The ip field of Address is set by Socket.resolveIP(ip) which returns an error if resolution fails; the catch block logs a warning with @errorName(err) and continues to the next iteration. If resolveIP fails, port defaults to 3478 via std.fmt.parseUnsigned fallback.

## Related Questions
- What is the default value of Address.isSymmetricNAT?
- Which constant represents the local host IP in this network module?
- How does the format method handle symmetric NAT addresses differently from regular ones?
- Where are STUN server addresses stored and how many servers are listed by default?
- What magic cookie bytes are used for STUN messages in this implementation?
- How is the random seed initialized inside requestAddress before picking a server?
- What happens if Socket.resolveIP fails when constructing a STUN message?
- Which function exposes the public API for formatting an Address value?
- Does the stun struct define any constants for STUN message types or flags?
- How is the transaction ID portion of the STUN message populated with randomness?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_2*
