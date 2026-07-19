# [issues/issue_1738.md] - Issue #1738 discussion

**Type:** review
**Keywords:** disconnection behavior, attackable ghost, fading ghost, geiger counter, logout timer, combat logging prevention, base security, server-side mod, multiplayer experience
**Concepts:** combat logging, base haunting, ghost player, logout timer, geiger counter

## Summary
Discussion on player disconnection behavior, focusing on implications of leaving bodies and potential solutions like temporary ghost states or logout timers.

## Explanation
The issue revolves around modifying player disconnection mechanics to prevent combat logging and base haunting. The discussion explores various solutions such as making disconnected players attackable for up to a minute after they log off, displaying a ghost player that fades over time, using geiger counters to detect player presence, and implementing logout timers. Maintainers express concerns about the permanence of ghost entities and their potential misuse for griefing. For example, if a player logs out in someone's base, their body will be visible and attackable for up to a minute before fading away. Additionally, maintainers suggest using a geiger counter-like item that can detect players but does not reveal their exact position or name. The final decision leans towards server-side mods rather than core game features due to concerns about disrupting cooperative multiplayer experiences. Specifically, the logout timer solution involves starting a logout timer when a player initiates logging out, allowing them to remain in control of the situation until they move, at which point the logout stops and they have to wait again next time. This solution was considered less suitable for the core game experience because it disrupts the intended cooperative multiplayer experience.

## Related Questions
- What are the potential implications of making disconnected players attackable for up to a minute after they log off?
- How could fading ghosts over time address combat logging and base haunting issues?
- What is the purpose of implementing a geiger counter in this context?
- Why was the logout timer solution considered less suitable for the core game experience?
- Can you explain the concerns regarding the permanence of ghost entities?
- How might server-side mods be used to implement these disconnection behaviors?

*Source: unknown | chunk_id: github_issue_1738_discussion*
