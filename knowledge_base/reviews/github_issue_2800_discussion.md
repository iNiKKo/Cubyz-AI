# [issues/issue_2800.md] - Issue #2800 discussion

**Type:** review
**Keywords:** multithreading, ECS, mutex, component pointers, get/set functions, lock-free, performance, cache invalidation, left-right data structure
**Symbols:** EntityManager, HealthComponent, mutex, get(id), set(id,.attribute,newvalue)
**Concepts:** multithreading, thread safety, Entity Component System (ECS), lock-free system

## Summary
The discussion revolves around handling multithreading in the Entity Component System (ECS) of Cubyz, focusing on whether component pointers should be given out and how to ensure thread safety.

## Explanation
The issue explores handling multithreading in Cubyz's Entity Component System (ECS) by discussing whether component pointers should be given out and how to ensure thread safety. Two main approaches are considered: giving out component pointers only when a mutex is locked, or using get/set functions that internally assert locks.

**Idea 1:**
- **Benefits:** Doesn't confuse your IDE.
- **Downsides:** Someone might accidentally use entityPointers after unlocking the entityManager (not foolproof).
Example:
```zig
healthComponent.mutex.lock();
const component:*HealthComponent = healthComponent.get(id); //assert lock
component.health = 15;
healthComponent.mutex.unlock();
//Illegal / not fool proof when:
component.health=17;
```
**Idea 2:**
- **Benefits:** More foolproof (though 100% foolproof is unreasonably possible).
- **Downsides:** Confuses Intellisense.
Example:
```zig
healthComponent.mutex.lock();
healthComponent.set(id,.health,15); //assert lock
healthComponent.mutex.unlock();
healthComponent.set(id,.health,17); //assert lock, fails successfully! more fool proof.
```
The maintainer suggests treating components as values similar to ECS libraries like Flecs and emphasizes the goal of achieving a lock-free system where expensive entity updates are done in parallel based on their position while cheaper operations (like checking health or ticking down effect timers) are handled sequentially. This approach minimizes cache invalidation by caching changes and applying them in batches after full iterations, using left-right data structures for synchronization.

**Technical Considerations:**
- Components should be small enough to fit within a single cache line (e.g., four u64).
- Components shouldn't contain hash maps or lists; they can have pointers into system-held data structures.
- Changes to entity state should be cached and applied as batches after full iterations, ensuring consistent iteration order.
- Left-right data structure: Two exact copies of the same thing are used, reading from one copy while writing to another. After syncing (copying contents), they swap roles for unobstructed reading with no cache invalidation.

## Related Questions
-  What are the benefits and downsides of giving out component pointers only when a mutex is locked?
-  How does using get/set functions internally assert locks improve thread safety?
-  What is the maintainer's goal for handling multithreading in ECS?
-  How can expensive entity updates be done in parallel while cheaper operations are handled sequentially?
-  Why should components be treated as values in ECS?
-  What technical reasons support treating components as values in ECS?
-  How does minimizing cache invalidation contribute to performance in multithreaded ECS?
-  What is the purpose of using a left-right data structure for synchronization in ECS?

*Source: unknown | chunk_id: github_issue_2800_discussion*
