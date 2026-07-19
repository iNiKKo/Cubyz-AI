# [issues/issue_266.md] - Issue #266 discussion

**Type:** review
**Keywords:** mesh networking, Cubyz, small-scale multiplayer game, conflicting game states, decentralized system, additional work, storage requirements, authentication server, holepunching
**Concepts:** mesh networking, peer-to-peer, centralized server, game state consistency

## Summary
Discussion on implementing mesh networking for Cubyz, with maintainer concerns about scalability and consistency.

## Explanation
Discussion on implementing mesh networking for Cubyz, where each node acts as both a server and client. The maintainer argues against this approach due to potential issues with conflicting game states without a centralized server. They also highlight the additional work and storage requirements associated with a decentralized system. Specifically mentioned tools and protocols include Hyprspace, n2n, nebula, qaul, Hypercore Protocol, pinecone, libp2p, devp2p, WebRTC, bittorrent, Gemini, Earthstar, Pigeon, and geneva Protocol. The maintainer notes that while Cubyz has some peer-to-peer elements (no authentication server and support for game servers behind firewalls via holepunching), these do not justify the complexity of full mesh networking.

## Related Questions
- What are the potential benefits of implementing mesh networking in Cubyz?
- How does the maintainer justify the need for a centralized server in Cubyz?
- What specific issues could arise from conflicting game states without a centralized server?
- Why does the maintainer believe additional work and storage are required for a decentralized system?
- Can you explain how holepunching contributes to Cubyz's current peer-to-peer capabilities?
- What other factors should be considered when deciding on networking architecture for Cubyz?
- Which specific mesh networking tools and protocols were mentioned in the discussion?

*Source: unknown | chunk_id: github_issue_266_discussion*
