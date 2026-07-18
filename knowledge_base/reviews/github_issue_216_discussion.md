# [issues/issue_216.md] - Issue #216 discussion

**Type:** review
**Keywords:** networking safety, congestion, packet loss, multiplayer, recovery time, urgent fix
**Concepts:** networking, congestion control, packet loss, multiplayer

## Summary
The issue discusses the need for making networking safe during congestion, highlighting severe packet loss and prolonged recovery times.

## Explanation
The maintainer notes that network congestion is more severe than initially anticipated, causing multiplayer sessions to halt with packet losses exceeding 95%. This situation can persist for minutes, necessitating an urgent fix to ensure stable and reliable networking under congested conditions.

## Related Questions
- What are the current strategies for handling network congestion in Cubyz?
- How can we measure and monitor packet loss during gameplay to identify congestion issues?
- Are there any existing solutions or libraries that could be integrated to improve networking resilience under high congestion?
- What specific changes need to be made to ensure stable multiplayer sessions even with high packet loss?
- How will the proposed fixes impact the overall performance of Cubyz's network handling?
- Can we simulate different levels of network congestion to test the effectiveness of the proposed solutions?

*Source: unknown | chunk_id: github_issue_216_discussion*
