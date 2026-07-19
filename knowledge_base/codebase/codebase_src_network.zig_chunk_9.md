# [hard/codebase_src_network.zig] - Chunk 9

**Type:** networking
**Keywords:** mbedTLS, SSL, TCP, encryption, buffer, packet, timestamp, congestion control
**Symbols:** ReceiveBuffer, SendBuffer, ChannelId, SequenceIndex, Channel, Channel.receiveBuffer, Channel.sendBuffer, Channel.allowedDelay, Channel.channelId, Channel.init, Channel.deinit, Channel.connect, Channel.receive, Channel.send, Channel.receiveConfirmationAndGetTimestamp, Channel.checkForLosses, Channel.sendNextPacketAndGetSize, Channel.getStatistics, SecureChannel, SecureChannel.super, SecureChannel.sslContext, SecureChannel.sslConfig, SecureChannel.serverCertificate, SecureChannel.serverKey, SecureChannel.dataToReceive, SecureChannel.mutex, SecureChannel.side, SecureChannel.finishedCollectingClientVerificationData, SecureChannel.verificationDataForClientSignature, SecureChannel.init
**Concepts:** networking, SSL/TLS encryption, buffer management, packet transmission, congestion control

## Summary
Defines network channel and secure channel structures with methods for initialization, deinitialization, sending, receiving, and managing data.

## Explanation
The chunk defines two main structures: `Channel` and `SecureChannel`. The `Channel` structure manages the sending and receiving of data over a network connection, including handling buffers, timestamps, and congestion control. It provides methods for initialization (`init`), deinitialization (`deinit`), connecting to a remote start index (`connect`), receiving data (`receive`), sending data (`send`), receiving confirmation and getting timestamp (`receiveConfirmationAndGetTimestamp`), checking for packet losses (`checkForLosses`), sending the next packet and getting its size (`sendNextPacketAndGetSize`), and retrieving statistics about unconfirmed and queued packets (`getStatistics`). The `SecureChannel` structure extends `Channel` to add SSL/TLS encryption using the mbedTLS library. It includes methods for initialization (`init`) that set up SSL configurations, generate self-signed certificates (for server-side use), and manage secure data transmission.

The `init` method in `SecureChannel` initializes the SSL context and configuration, sets the authentication mode to none, and configures debugging output. For server-side use, it generates a self-signed RSA key pair with 2048 bits and sets up the certificate details. The `sendNextPacketAndGetSize` method in `Channel` constructs a packet by writing the channel ID, sequence index, and data to a binary writer, then sends the packet over the network connection.

Specifically, the `init` method for `SecureChannel` performs the following steps:
1. Initializes the SSL context and configuration using `mbedtls_ssl_init` and `mbedtls_ssl_config_init`.
2. Sets default SSL configurations with `mbedtls_ssl_config_defaults`, specifying whether it is a client or server.
3. Disables server certificate verification with `mbedtls_ssl_conf_authmode`.
4. Configures debugging output with `mbedtls_ssl_conf_dbg`.
5. For server-side use, generates a self-signed RSA key pair with 2048 bits using `psa_generate_key` and wraps it with `mbedtls_pk_wrap_psa`.
6. Sets up the certificate details such as subject name, issuer name, issuer key, and subject key using `mbedtls_x509write_crt_set_subject_name`, `mbedtls_x509write_crt_set_issuer_name`, `mbedtls_x509write_crt_set_issuer_key`, and `mbedtls_x509write_crt_set_subject_key`.

The `sendNextPacketAndGetSize` method constructs a packet by:
1. Writing the channel ID to the binary writer using `writer.writeEnum`.
2. Getting the next packet to send from the `SendBuffer` with `self.sendBuffer.getNextPacketToSend`, which includes writing the sequence index and data to the buffer.
3. Sending the constructed packet over the network connection using `conn.manager.send`.

## Code Example
```zig
pub fn receive(self: *Channel, conn: *Connection, start: SequenceIndex, data: []const u8) !ReceiveBuffer.ReceiveStatus {
			return self.receiveBuffer.receive(conn, start, data);
		}
```

## Related Questions
- What is the purpose of the `Channel` structure in this code?
- How does the `SecureChannel` extend the functionality of `Channel`?
- What methods are available for initializing and deinitializing a `Channel`?
- How does the `sendNextPacketAndGetSize` method work in the `Channel` structure?
- What is the role of the `sslContext` and `sslConfig` fields in the `SecureChannel` structure?
- How is packet loss detected and handled in the `Channel` structure?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_9*
