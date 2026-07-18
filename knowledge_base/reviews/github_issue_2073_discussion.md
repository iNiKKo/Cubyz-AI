# [issues/issue_2073.md] - Issue #2073 discussion

**Type:** review
**Keywords:** server side, plugins, GUI, zon, compile-time, latency
**Concepts:** server-client architecture, plugin development, GUI rendering

## Summary
Discussion about extending server-side capabilities in Cubyz to allow for more complex interactions like GUIs.

## Explanation
The issue discusses the limitation of current server-side plugin capabilities in Cubyz, where plugins can only perform limited actions without requiring client-side mods. The user proposes allowing GUI definitions to be sent from the server to the client, but acknowledges that this would be complex due to the current compile-time nature of the GUI system. The maintainer notes that any server-side GUI operations would likely introduce significant latency.

## Related Questions
- How can the current GUI system be modified to support server-side rendering?
- What are the potential performance impacts of implementing server-side GUIs in Cubyz?
- Are there any existing solutions or libraries that could facilitate server-side GUI rendering in Cubyz?
- How would the proposed changes affect backwards compatibility with existing plugins?
- What security considerations should be taken into account when allowing server-side GUI operations?
- Can you provide examples of other games or applications that successfully implement server-side GUIs?

*Source: unknown | chunk_id: github_issue_2073_discussion*
