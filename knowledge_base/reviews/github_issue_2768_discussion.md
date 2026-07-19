# [issues/issue_2768.md] - Issue #2768 discussion

**Type:** review
**Keywords:** callback refactor, decoupling, flexibility, polymorphic vtable, modular design, event handling, input decoupling
**Symbols:** Callback.init, .zon files, onTouch, onInteract, clientRun, serverRun, touchRun
**Concepts:** polymorphism, modularity, event-driven architecture

## Summary
Proposes refactoring callbacks to allow more flexibility, enabling multiple callbacks per event and decoupling event types from specific functions.

## Explanation
The current implementation of callbacks in Cubyz is rigid, with each callback having fixed inputs and limited functionality. The proposal aims to decouple events like `onTouch` from specific callback functions by introducing a more generic approach where any callback can be used for any event. This would involve changing the initialization of callbacks (`Callback.init`) and the event names in the `.zon` files to include the function to run. A polymorphic solution, such as using a vtable, is suggested to allow mods to provide their own implementations of functions. The goal is to make block callbacks more versatile, allowing for complex behaviors like those described in user examples (e.g., a thorny bush that hurts and breaks on touch). This change would open up possibilities for base addons and improve modularity by providing all necessary data such as server, client, and ontouch inputs so the callback can independently decide which of the functions it wants to run. Each event type (`onTouch`, `onTick`, etc.) will have separate `run` functions like `clientRun`, `serverRun`, and `touchRun`. The proposal addresses limitations mentioned in issues #2083 and #2144, aiming to enhance flexibility and modularity.

## Related Questions
- What specific data is provided to each callback when an event occurs?
- How does the new system allow callbacks to decide which 'run' function to use?
- Can you provide detailed examples of current limitations in the callback system?

*Source: unknown | chunk_id: github_issue_2768_discussion*
