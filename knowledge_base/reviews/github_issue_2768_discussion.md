# [issues/issue_2768.md] - Issue #2768 discussion

**Type:** review
**Keywords:** callback refactor, decoupling, flexibility, polymorphic vtable, modular design, event handling, input decoupling
**Symbols:** Callback.init, .zon files, onTouch, onInteract, clientRun, serverRun, touchRun
**Concepts:** polymorphism, modularity, event-driven architecture

## Summary
Proposes refactoring callbacks to allow more flexibility, enabling multiple callbacks per event and decoupling event types from specific functions.

## Explanation
The current implementation of callbacks in Cubyz is rigid, with each callback having fixed inputs and limited functionality. The proposal aims to decouple events like `onTouch` from specific callback functions by introducing a more generic approach where any callback can be used for any event. This would involve changing the initialization of callbacks (`Callback.init`) and the event names in the `.zon` files to include the function to run. A polymorphic solution, such as using a vtable, is suggested to allow mods to provide their own implementations of functions. The goal is to make block callbacks more versatile, allowing for complex behaviors like those described in user examples (e.g., a thorny bush that hurts and breaks on touch). This change would open up possibilities for base addons and improve modularity.

## Related Questions
- What is the current implementation of callbacks in Cubyz?
- How does the proposed refactoring aim to improve callback functionality?
- What are the potential benefits of using a polymorphic vtable for callbacks?
- Can you provide examples of how the new callback system would be used in practice?
- How might this change impact existing mods and their compatibility with Cubyz?
- What are the architectural implications of decoupling events from specific functions?
- How could this refactoring affect performance, especially with a large number of callbacks?
- Is there any risk of introducing bugs or regressions with this significant change to the callback system?
- How would this proposal address the limitations mentioned in issues #2083 and #2144?
- What are the potential challenges in implementing this refactoring, particularly regarding backward compatibility?

*Source: unknown | chunk_id: github_issue_2768_discussion*
