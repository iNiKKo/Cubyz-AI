# [issues/issue_2800.md] - Issue #2800 discussion

**Type:** review
**Keywords:** multithreading, ECS, mutex, component pointers, get/set functions, lock-free, performance, cache invalidation, left-right data structure
**Symbols:** EntityManager, HealthComponent, mutex, get(id), set(id,.attribute,newvalue)
**Concepts:** multithreading, thread safety, Entity Component System (ECS), lock-free system

## Summary
The discussion revolves around handling multithreading in the Entity Component System (ECS) of Cubyz, focusing on whether component pointers should be given out and how to ensure thread safety.

## Explanation
The issue explores two main approaches for managing multithreading in ECS: giving out component pointers only when a mutex is locked or using get/set functions that internally assert locks. The maintainer suggests treating components as values, similar to ECS libraries like Flecs, and emphasizes the goal of achieving a lock-free system where expensive entity updates are done in parallel while cheaper operations are handled sequentially. The discussion also touches on performance considerations, such as minimizing cache invalidation and using left-right data structures for synchronization.

## Related Questions
- What are the benefits and downsides of giving out component pointers only when a mutex is locked?
- How does using get/set functions internally assert locks improve thread safety?
- What is the maintainer's goal for handling multithreading in ECS?
- How can expensive entity updates be done in parallel while cheaper operations are handled sequentially?
- Why should components be treated as values in ECS?
- What technical reasons support treating components as values in ECS?
- How does minimizing cache invalidation contribute to performance in multithreaded ECS?
- What is the purpose of using a left-right data structure for synchronization in ECS?

*Source: unknown | chunk_id: github_issue_2800_discussion*
