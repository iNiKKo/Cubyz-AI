# [issues/issue_2083.md] - Issue #2083 discussion

**Type:** review
**Keywords:** Observer, event system, callbacks, cross-world, server-client, metadata, priority, security critical, octree, entity component system, polling
**Symbols:** Observer, Event system, CircularBufferQueue, ListUnmanaged, event loop thread
**Concepts:** Observer pattern, asynchronous communication, thread safety, performance optimization, moddability

## Summary
The discussion revolves around implementing a global event/message system using the Observer pattern to facilitate communication between different systems in Cubyz, including modding interfaces and UI interactions.

## Explanation
The proposal suggests creating a globally accessible event API where any code can attach callbacks to specific events identified by ID and trigger these events. The maintainer outlines a potential implementation involving separate client and server-side event systems, using circular buffers for event queues and lists for callbacks, with an event loop thread handling the execution of callbacks. However, there are concerns about performance due to the need to register, unregister, and call thousands of event handlers, as well as the complexity of managing cross-world/UI and server/client barriers. The maintainer also highlights that event handling is unordered and delayed, making it unsuitable for security-critical tasks. Additionally, there are discussions about the inefficiency of using the event system for interactions involving entities or the world, suggesting that proper polling through entity component systems would be more appropriate.

## Related Questions
- How does the event system handle synchronization between threads?
- What are the potential performance implications of having thousands of event handlers?
- How is metadata used to manage events distributed across server and client?
- What strategies are proposed for efficiently handling entity interactions with the event system?
- How does the event system ensure that critical events are executed in a timely manner?
- What are the considerations for implementing cross-world/UI barriers in the event system?

*Source: unknown | chunk_id: github_issue_2083_discussion*
