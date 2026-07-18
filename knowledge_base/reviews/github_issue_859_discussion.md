# [issues/issue_859.md] - Issue #859 discussion

**Type:** review
**Keywords:** IPv6, NAT, support, maintenance, socket, IPV6_V6ONLY, error handling
**Concepts:** IPv6, carrier-grade NAT, networking, socket programming

## Summary
The discussion revolves around the feasibility of switching to IPv6 for Cubyz, addressing issues with carrier-grade NATs and potential improvements in error handling for IPv6 addresses.

## Explanation
The issue discusses the challenges of using IPv6 due to poor support from ISPs and devices. The maintainer is concerned about the complexity and maintenance overhead of supporting both IPv4 and IPv6. However, a user argues that most modern devices support IPv6 and suggests using a single socket on the server that can handle both IPv4 and IPv6 connections. The user also proposes setting the `IPV6_V6ONLY` option to allow an IPv6 socket to accept IPv4 connections as well.

## Related Questions
- What are the potential benefits and drawbacks of switching to IPv6 in Cubyz?
- How can Cubyz detect carrier-grade NATs without using IPv6?
- What is the impact of IPv6 headers on bandwidth usage in Cubyz?
- How can Cubyz improve error handling for IPv6 addresses?
- Can an IPv6 socket be configured to accept both IPv4 and IPv6 connections?
- What are the implications of maintaining separate sockets for IPv4 and IPv6 in Cubyz?

*Source: unknown | chunk_id: github_issue_859_discussion*
