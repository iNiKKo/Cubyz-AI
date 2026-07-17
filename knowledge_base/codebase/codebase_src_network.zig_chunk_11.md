# [hard/codebase_src_network.zig] - Chunk 11

**Type:** implementation
**Keywords:** mbedtls_ssl_handshake, mbedTlsSend, mbedTlsReceive, receiveThroughTls, sendThroughTls, WANT_READ, verification data, ChannelId, ConnectionState, HandShakeState, secure channel, TLS read loop, mutex lock, checkResult, insertMessageSecure
**Symbols:** mbedTlsSend, mbedTlsReceive, receiveThroughTls, sendThroughTls, ChannelId, ConnectionState, HandShakeState, ConfirmationData, manager, user, remoteAddress, bruteforcingPort, lossyChannel, secureChannel, slowChannel, restartChannelCounter, restartCounter
**Concepts:** TLS handshake, mbedTLS callbacks, verification data collection, encrypted I/O, WANT_READ handling, mutex locking, error checking, channel types, handshake states, secure channel extension

## Summary
Implements secure TLS channel logic with mbedTLS callbacks and handshake state management for encrypted network communication.

## Explanation
This chunk defines the SecureChannel struct extending Channel with mbedTLS integration. It provides C-callable send/receive callbacks (mbedTlsSend, mbedTlsReceive) that handle verification data collection during client signature phases. The receiveThroughTls and sendThroughTls methods implement TLS read/write loops using mbedtls_ssl_read/ssl_write, handling WANT_READ via mutex-protected sleep, closed connections, and error checking through checkResult. Public wrapper methods delegate to super.receiveBuffer.receiveSecure and super.sendBuffer.insertMessageSecure for encrypted I/O. The chunk declares ChannelId enum with secure=1 variant, ConnectionState enum (awaitingClientConnection, awaitingServerResponse, etc.), and HandShakeState enum enumerating handshake phases from start through complete. Fields include manager pointer, user reference, remoteAddress, bruteforcingPort flag, lossyChannel, secureChannel, slowChannel, restartChannelCounter array, and restartCounter.

## Related Questions
- What happens when mbedTlsSend is called during the client signature phase?
- How does receiveThroughTls handle a WANT_READ return from mbedtls_ssl_read?
- What error is returned if mbedtls_ssl_read returns 0 in receiveThroughTls?
- Which enum value corresponds to the secure channel type in ChannelId?
- What fields are added by SecureChannel that are not present in base Channel?
- How does sendThroughTls manage partial writes and remaining data?
- What state transitions occur through HandShakeState during a TLS handshake?
- Is there any public method for sending encrypted messages directly on SecureChannel?
- Does the chunk declare any confirmation data structures for secure channels?
- Are there any restart-related fields exposed in this chunk?
- How does the chunk ensure thread safety when calling mbedTLS functions?
- What happens if checkResult encounters an error during TLS operations?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_11*
