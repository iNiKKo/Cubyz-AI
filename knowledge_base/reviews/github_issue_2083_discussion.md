# [issues/issue_2083.md] - Issue #2083 discussion

**Type:** review
**Keywords:** Observer, event system, callbacks, cross-world, server-client, metadata, priority, security critical, octree, entity component system, polling
**Symbols:** Observer, Event system, CircularBufferQueue, ListUnmanaged, event loop thread
**Concepts:** Observer pattern, asynchronous communication, thread safety, performance optimization, moddability

## Summary
The discussion revolves around implementing a global event/message system using the Observer pattern to facilitate communication between different systems in Cubyz, including modding interfaces and UI interactions.

## Explanation
The discussion revolves around implementing a global event/message system using the Observer pattern to facilitate communication between different systems in Cubyz. The proposal suggests creating a globally accessible event API where any code can attach callbacks to specific events identified by ID and trigger these events. The maintainer outlines a potential implementation involving separate client and server-side event systems, with each event type having its own `CircularBufferQueue` for storing events and a `ListUnmanaged` for storing callbacks. There is a constantly running 'event loop' thread that processes events in the queues by calling all associated callbacks. Events can be marked with metadata to determine if they should cross server-client barriers or world/UI barriers, ensuring efficient filtering of unnecessary event propagation.

However, there are significant concerns about performance due to the need to register, unregister, and call thousands of event handlers, which introduces a substantial overhead. The maintainer also highlights that event handling is inherently unordered and delayed, making it unsuitable for security-critical tasks where immediate execution is required. Additionally, discussions reveal inefficiencies in using the event system for interactions involving entities or the world, such as turrets reacting to entity positions. Proper polling through an optimized entity component system is proposed instead of relying on global event propagation.

The maintainer emphasizes that while the event system can be used for modding interfaces and UI interactions (e.g., player movement informing windows to close/open), it should not cross world/UI barriers except for active events like placing or clicking blocks. This ensures that only relevant and necessary events are processed, reducing unnecessary overhead.

## Related Questions
- How does the event system handle synchronization between threads?
- What are the potential performance implications of having thousands of event handlers?
- How is metadata used to manage events distributed across server and client?
- What strategies are proposed for efficiently handling entity interactions with the event system?
- How does the event system ensure that critical events are executed in a timely manner?
- What are the considerations for implementing cross-world/UI barriers in the event system?

*Source: unknown | chunk_id: github_issue_2083_discussion*
