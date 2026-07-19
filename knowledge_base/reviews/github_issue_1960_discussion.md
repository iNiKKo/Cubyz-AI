# [issues/issue_1960.md] - Issue #1960 discussion

**Type:** review
**Keywords:** IP banning, per-session, client-wide, timeouts, VPN, router restarts, manual whitelists, proof-of-work, fingerprinting, malicious actors, innocent users, server management
**Concepts:** IP banning, per-session bans, client-wide storage, timeouts, proof-of-work systems, device fingerprinting

## Summary
Discussion about implementing IP banning for malicious users, focusing on the scope and effectiveness of such a feature.

## Explanation
The discussion revolves around whether to implement permanent or per-session IP banning. The maintainers suggest starting with per-session bans and storing them client-wide, ensuring they apply across different worlds hosted by the same server but not when downloading a world. Users raise concerns about the ineffectiveness of IP banning due to the ease of changing IPs through VPNs or router restarts, as well as the potential for innocent users being banned if they share an IP with malicious actors. The maintainers propose adding timeouts (e.g., a timeout period after which a ban is automatically lifted) and consider proof-of-work systems (such as requiring users to solve computational puzzles each time they create an account) or device fingerprinting (collecting data about the user's device to make them more identifiable) as alternative approaches, but these are deemed too intrusive or impractical. Ultimately, there's a consensus that manual whitelists might be more effective for smaller servers, while larger servers can implement their own automated solutions.

## Related Questions
- What are the potential drawbacks of implementing per-session IP bans?
- How can timeouts be effectively implemented to mitigate the impact on innocent users?
- What are the advantages and disadvantages of using proof-of-work systems for IP banning?
- Why is device fingerprinting considered a less desirable approach in this context?
- How can manual whitelists be efficiently managed for smaller servers?
- What are the potential challenges in implementing automated solutions for larger servers?

*Source: unknown | chunk_id: github_issue_1960_discussion*
