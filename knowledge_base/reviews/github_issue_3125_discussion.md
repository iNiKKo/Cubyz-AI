# [issues/issue_3125.md] - Issue #3125 discussion

**Type:** documentation
**Keywords:** ambiguous arguments, greedy parsing, union(enum), autocomplete, error messages, namespace, comptime struct building, preferred_alias, hash map
**Symbols:** /tp, /perm, /cubyz worldedit undo
**Concepts:** command parsing, subcommands, aliasing, client-server interaction, mod compatibility

## Summary
Discussion about improving command parsing and aliasing in a game engine.

## Explanation
The discussion revolves around enhancing the way commands are parsed and managed within a game engine. The current system is criticized for being ambiguous and complex, leading to errors and poor user experience. The proposal suggests adopting a more structured approach using subcommands, which would make parsing paths clearer and reduce ambiguity. This involves treating each command as a black box with customizable arguments through structs. Additionally, the idea of aliasing commands to simplify user input is discussed, with potential implementation on the client side to handle aliases dynamically without server intervention. The conversation also touches on how to manage conflicts between aliases from different mods and whether to automatically generate aliases for existing commands.

## Code Example
```zig
const Args = union(enum) {
	biome: struct { biome: command.BiomeId },
	position: struct {
		x: command.Coordinate,
		y: command.Coordinate,
		z: command.Coordinate,
	},
	player: struct { playerIndex: command.PlayerIndex },
}
```

## Related Questions
- How can we implement subcommands in a game engine to improve command parsing?
- What are the benefits of using aliasing for commands in a game environment?
- How should conflicts between aliases from different mods be handled?
- Can you explain how automatic alias generation could work within a game engine?
- What are the potential drawbacks of implementing client-side alias resolution in a game command system?
- How can we ensure that subcommands and aliases do not interfere with mod compatibility?

*Source: unknown | chunk_id: github_issue_3125_discussion*
