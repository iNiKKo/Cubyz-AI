# [easy/codebase_src_server_command_worldedit_toggledecay.zig] - Chunk 0

**Type:** api
**Keywords:** command processing, argument parsing, enum usage, struct definition, error handling, blueprint capture, block data modification
**Symbols:** description, usage, Target, State, Args, Args.parse, execute, toggledecay
**Concepts:** world editor, command parsing, blueprint manipulation, block modification

## Summary
This chunk implements the /toggledecay command for enabling or disabling decay on selected blocks in a world editor context.

## Explanation
This chunk implements the `/toggledecay` command for enabling or disabling decay on selected blocks in a world editor context. The command allows users to toggle decay on either their current selection or clipboard. It includes parsing logic for command arguments, capturing and modifying blueprints based on the target (selection or clipboard), and applying changes to blocks.

The `Target` enum has two values: `selection` and `clipboard`. The `State` enum also has two values: `on` and `off`. The `Args.parse` function parses two required arguments: `<target>` which can be either 'selection' or 'clipboard', and `<decayState>` which can be either 'on' or 'off'. If an argument is missing, it sends a specific error message indicating the missing argument. For example, if the target argument is missing, it sends `#ff0000Missing required <selection/clipboard> argument.`. Similarly, if the decay state argument is missing, it sends `#ff0000Missing required <on/off> argument.`. If there are too many arguments provided for `/toggledecay`, it also sends an error message stating that only two arguments are expected: `#ff0000Too many arguments for command /toggledecay. Expected two.`.

The `execute` function handles capturing and modifying blueprints based on the target (selection or clipboard) and applies changes to blocks using the `toggledecay` function. The `toggledecay` function specifically handles the modification of block data for branches (`cubyz:branch`) and decayable blocks (`cubyz:decayable`). For branches, it sets a flag indicating whether they were placed by a human or not based on the decay state. For decayable blocks, it simply toggles the decay state using a boolean value.

User feedback is provided for successful or failed commands. For example, if the selection is modified successfully, it sends `#00ff00Selection modified. History entry created.`. If the clipboard is modified successfully, it sends `#00ff00Clipboard modified.`. If there is an error while capturing a block, it sends `#ff0000Error while capturing block {}: {s}. Nothing was modified.` and logs the error.

The Blueprint struct plays a crucial role in this chunk by allowing the capture and modification of selections or clipboards. Selections and clipboards are managed within the command by using the `getCurrentSelection` function to get the current selection, and by checking if the clipboard is empty before attempting to modify it.

## Code Example
```zig
const Target = enum { selection, clipboard }
```

## Related Questions
- What is the purpose of the /toggledecay command?
- How are arguments parsed in the /toggledecay command?
- What happens if there are too many arguments provided for /toggledecay?
- How does the chunk handle errors during argument parsing?
- What data structures are used to store and modify blueprints?
- How is block decay toggled in the world editor?
- Which specific types of blocks can be modified by the /toggledecay command?
- How is user feedback provided for successful or failed commands?
- What role does the Blueprint struct play in this chunk?
- How are selections and clipboards managed within the command?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_toggledecay.zig_chunk_0*
