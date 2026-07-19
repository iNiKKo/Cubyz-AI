# [issues/issue_859.md] - Issue #859 discussion

**Type:** review
**Keywords:** IPv6, NAT, support, maintenance, socket, IPV6_V6ONLY, error handling
**Concepts:** IPv6, carrier-grade NAT, networking, socket programming

## Summary
The discussion revolves around the feasibility of switching to IPv6 for Cubyz, addressing issues with carrier-grade NATs and potential improvements in error handling for IPv6 addresses.

## Explanation
The discussion revolves around the feasibility of switching to IPv6 for Cubyz due to issues with carrier-grade NATs (CGNAT) and potential improvements in error handling for IPv6 addresses. The maintainer is concerned about poor support from ISPs, such as the maintainer's internet provider not supporting IPv6 natively but only via 6to4 tunneling. Additionally, there are still many devices that do not fully support IPv6, leading to concerns about user interface complexity and maintenance overhead when supporting both IPv4 and IPv6.

A user argues that most modern devices manufactured in the last 20 years and operating systems updated within this period can handle IPv6 connections effectively. The maintainer's concern is based on a pessimistic statistic showing less than 50% of devices actively preferring IPv6 over IPv4, but the user suggests that actual device support is much higher.

To address CGNAT detection issues, the user proposes using two STUN servers to check for symmetric NATs. The maintainer notes that this method was already implemented but did not resolve the issue with a specific CGNAT in the UK. Another suggestion involves defaulting to IPv6 and switching to IPv4 if necessary or vice versa.

The user also suggests configuring an IPv6 socket to handle both IPv4 and IPv6 connections by setting the `IPV6_V6ONLY` option to 0, allowing the server to accept IPv4 connections on an IPv6 socket. This can be achieved with the following code snippet:
```c++
int no = 0;
setsockopt(handle, IPPROTO_IPV6, IPV6_V6ONLY, (const char*)&no, sizeof(no));
```
The user tested this configuration and confirmed that an IPv4 client could connect to an IPv6 server using `netcat`.

## Related Questions
- What are the potential benefits and drawbacks of switching to IPv6 in Cubyz?
- How can Cubyz detect carrier-grade NATs without using IPv6?
- What is the impact of IPv6 headers on bandwidth usage in Cubyz?
- How can Cubyz improve error handling for IPv6 addresses?
- Can an IPv6 socket be configured to accept both IPv4 and IPv6 connections?
- What are the implications of maintaining separate sockets for IPv4 and IPv6 in Cubyz?

*Source: unknown | chunk_id: github_issue_859_discussion*
