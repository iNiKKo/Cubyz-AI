# [src/entity.zig] - PR #2675 review diff

**Type:** review
**Keywords:** EntityComponentVTable, serverLoad, clientLoad, serverUnload, clientUnload, initComponents, deinitComponents, loadComponent, componentList, BinaryReader
**Symbols:** EntityComponentLoadError, EntityComponentVTable, serverLoad, clientLoad, serverUnload, clientUnload, componentList, initComponents, deinitComponents, load
**Concepts:** Memory Management, Initialization and Cleanup, Component System Design

## Summary
The code introduces new functions for loading and unloading components on both server and client sides. It also renames the `initComponent` function to `initComponents` and adds a corresponding `deinitComponents` function.

## Explanation
The changes involve expanding the `EntityComponentVTable` struct to include `serverUnload` and `clientUnload` functions, which are responsible for unloading components. The `initComponents` function now initializes these unload functions along with the load functions. Additionally, a new `deinitComponents` function is added to properly deinitialize the component list. The reviewer suggests renaming the `load` function to `loadComponent` to avoid confusion.

The `EntityComponentLoadError` enum includes an additional error type: `unknownComponentID`. This error is thrown when an unknown component ID is encountered during loading.

The `initComponents` function initializes a temporary list (`tmpComponentList`) and ensures that each component ID has a unique entry in the `componentList`. If a duplicate component ID is found, an error message is logged.

The `deinitComponents` function sets the `componentList` to undefined, effectively deinitializing it.

The `load` function takes five parameters: `side`, `componentID`, `entityID`, `componentData`, and `componentVersion`. It loads component data based on the provided parameters. The reviewer suggests renaming this function to `loadComponent` to avoid confusion with other potential functions named `load`.

## Related Questions
- What is the purpose of the `serverUnload` and `clientUnload` functions in the `EntityComponentVTable` struct?
- How does the `initComponents` function ensure that each component ID has a unique entry in the `componentList`?
- Why was the `load` function renamed to `loadComponent` according to the reviewer's suggestion?
- What is the role of the `deinitComponents` function in the component system?
- How does the code handle duplicate component IDs during initialization?
- Can you explain the purpose of the `main.worldArena` in the context of appending items to the list?

*Source: unknown | chunk_id: github_pr_2675_comment_3067822326*
