# [issues/issue_2624.md] - Issue #2624 discussion

**Type:** review
**Keywords:** Modifier revamp, Tag-based system, GLFW limitations, custom toggles, efficient lookup, enum Tags, global hashmap
**Symbols:** Key, Modifiers, Tag, tag.zig, .tag, .requiredModifiers, .modById, GLFW
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Proposes revamping the Modifier system in the Key struct to use a Tag-based approach for better flexibility and easier addition of new modifier categories.

## Explanation
Proposes revamping the Modifier system in the Key struct to use a Tag-based approach for better flexibility and easier addition of new modifier categories.

The current Modifier code in the Key struct is described as rigid, with manually added boolean flags for possible modifier keys. The proposed change involves removing these booleans and replacing the Modifiers struct with Tags. This allows for easy addition of new modifier keybinds by simply adding a new statically declared Tag in tag.zig.

The system would use `.tag` to declare which modifier a keybind is, and `.requiredModifiers` array of Tags to specify required modifiers for other keybinds. Instead of checking GLFW's mods via the Key's pressed modifiers, the system will check `.modById(<tag>).?.pressed`. The discussion highlights limitations imposed by GLFW and suggests ignoring GLFW's mods and implementing custom toggles for tagged modifiers.

Specific keys that are themselves a modifier include Left Shift, Left Control, Caps Lock. These keybinds have tag defined in constructor in KeyBoard. Keys that consume modifiers check `main.KeyBoard.getModByTag(<tag>).isPressed` to determine the pressed status of these tags.

The system also addresses the need for efficient lookup of tags without constant looping over keybinds, proposing an array-based approach where Tags are enums, and a global accessible hashmap to store the pressed status of each tag. This ensures that when toggled, the boolean is set to true, allowing actions dependent on modifiers to use this globally accessible hashmap.

The global hashmap for tag lookup is initialized at start by looping over all keybinds and building a tag -> bool hashmap stored somewhere accessible to all keys. When keybinds are changed, the hashmap is updated accordingly. The system ensures thread safety when accessing the global hashmap of pressed statuses by using synchronization mechanisms such as mutexes.

The proposed system addresses the need for custom rebindable modifier keys by allowing players to change the default bindings without making it just a single modifier that's rebindable. This revamp is expected to improve code readability and maintainability by providing a more flexible and modular approach to handling modifiers.

## Related Questions
- How does the proposed Tag-based system handle the addition of new modifier categories?
- What is the impact on performance when using an array for tag lookup instead of a dictionary?
- How does the system ensure thread safety when accessing the global hashmap of pressed statuses?
- What are the potential backwards compatibility issues with this revamp?
- How does the system handle cases where a keybind needs multiple modifiers?
- What is the role of GLFW in the current Modifier system, and how will it be affected by this change?
- How does the proposed system address the need for custom rebindable modifier keys?
- What are the steps involved in implementing the global hashmap for tag lookup?
- How does the system handle the initialization and update of the global hashmap when keybinds are changed?
- What is the expected impact on code readability and maintainability with this revamp?

*Source: unknown | chunk_id: github_issue_2624_discussion*
