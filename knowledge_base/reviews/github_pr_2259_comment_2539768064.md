# [src/network.zig] - PR #2259 review diff

**Type:** review
**Keywords:** IpAddress, parse, resolve, parseOrResolve, stack allocator, testing, network code
**Symbols:** IpAddress, localHost, format, fromString, parse, resolve, AddressParseMode
**Concepts:** networking, IP address parsing, resolution, unit testing

## Summary
Refactored `Address` struct into `IpAddress` with additional parsing and resolution capabilities.

## Explanation
The change introduces a new `IpAddress` struct to replace the old `Address` struct, adding functionality for IP address parsing and resolution. The `IpAddress` struct includes an `address` field of type `u32`, and a constant `localHost` initialized with the value `0x0100007f`. The `format` method formats the IP address as a string in the form "{}.{}.{}.{}". The `fromString` function parses or resolves an IP address based on the specified mode (`parse`, `resolve`, or `parseOrResolve`). The `resolve` function uses `std.net.getAddressList` to resolve the address, and it requires a `NeverFailingAllocator`. The reviewer points out that testing network code in Zig might be challenging due to the unavailability of the stack allocator during tests, which could affect the reliability of network-related unit tests.

## Related Questions
- How does the `fromString` function handle different address parsing modes?
- What is the purpose of the `localHost` constant in the `IpAddress` struct?
- Why was the stack allocator mentioned as a concern for testing network code?
- How does the `resolve` function interact with the `std.net.getAddressList` method?
- Can you explain the difference between `parse`, `resolve`, and `parseOrResolve` modes in `AddressParseMode`?
- What potential issues might arise from using a `NeverFailingAllocator` in network operations?

*Source: unknown | chunk_id: github_pr_2259_comment_2539768064*
