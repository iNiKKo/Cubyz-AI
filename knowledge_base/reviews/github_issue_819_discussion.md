# [issues/issue_819.md] - Issue #819 discussion

**Type:** review
**Keywords:** MTU, Path MTU Discovery, RFC 8899, probe messages, padding data, client hello, server hello, network capacity, endpoint processing, slow protocol
**Concepts:** Path MTU Discovery, RFC 8899, MTU reduction detection

## Summary
The discussion revolves around implementing Path MTU discovery in Cubyz, considering both temporary fixes and more robust solutions like RFC 8899. The main points include setting a minimum MTU, using padding for probe messages, and ensuring proper handling of MTU reductions.

## Explanation
The discussion revolves around implementing Path MTU discovery in Cubyz to handle varying network conditions without significantly impacting performance. The user proposes a temporary fix where the client dictates the MTU size through progressively smaller packets until a successful connection is established, starting with an initial MTU of 576 bytes (minus headers). This approach builds a foundation for variable MTUs, which is essential for constant MTU discovery. The maintainer considers this if implementing RFC 8899 takes too long.

The user suggests that the client should send client hellos from very large to very low sizes. If no server hello is returned after sending a client hello of a certain size, the client should make the client hello smaller and repeat the process until a successful connection is established. The server retrieves the MTU size from the size of the client hello and adds that information to a connection, assembling packets with that MTU in mind. This ensures that the connection has a fixed MTU that works.

The discussion also explores different probe message variants from RFC 8899:
- Probing using padding data: A probe packet that contains only control information together with any padding, which is needed to inflate to the size of the probe packet. Since these probe packets do not carry an application-supplied data block, they do not typically require retransmission, although they do still consume network capacity and incur endpoint processing.
- Probing using application data and padding data: A probe packet that contains a data block supplied by an application that is combined with padding to inflate the length of the datagram to the size of the probe packet.
- Probing using only application data: A probe packet that contains a data block supplied by an application that matches the size of the probe packet. This method requests the application to issue a data block of the desired probe size.

These methods involve sending packets of varying sizes to detect the actual MTU size on the network path. The main concern is detecting and reacting to MTU reductions, which could occur due to network changes.

To address this, the server retrieves the MTU size from the size of the client hello and adjusts packet sizes accordingly. Additionally, the `mtuEstimate` variable is used in the network implementation for debugging purposes. The maintainer notes that one of the main issues was how to detect and react to MTU reductions (which could theoretically happen if your traffic is rerouted for some reason). The obvious answer is the slow protocol, as the data inside is supposed to assume that it's fine to arrive late.

Overall, which method we choose probably doesn't matter, as long as the math is right and the cost of the probe packet is always significantly less than the expected gains. In the end, it's probably just a question of which is easier to implement.

## Related Questions
- How does the client determine the MTU size in the proposed temporary fix?
- What are the potential drawbacks of using padding data for probe messages?
- How does the server adjust packet sizes based on the detected MTU?
- What is the role of the `mtuEstimate` variable in the network implementation?
- How can we ensure that the cost of probe packets is less than the expected gains?
- What are the implications of using the slow protocol for sending probe messages?

*Source: unknown | chunk_id: github_issue_819_discussion*
