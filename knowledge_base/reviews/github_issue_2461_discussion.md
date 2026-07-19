# [issues/issue_2461.md] - Issue #2461 discussion

**Type:** review
**Keywords:** block replacements, randomized substitutions, probabilities, palette, tagged unions, alias table, zig.zon, world generation, efficiency, flexibility
**Symbols:** Sbb, block replacements, palette, tagged unions, alias table, substitute, zig.zon
**Concepts:** randomization, world generation, efficiency, flexibility

## Summary
The issue proposes extending block replacement functionality to allow randomized substitutions with specified probabilities, enhancing flexibility and efficiency in world generation.

## Explanation
The current method for block replacements is described as tedious and inefficient. The proposed solution involves using a palette filled with tagged unions at runtime, where each entry can either be a single block or an alias table with associated probabilities. This approach aims to simplify the process by reducing the need for multiple branches during execution. The maintainer notes that this request extends issue #1412, which currently supports fixed replacements but lacks the ability to handle randomized substitutions. The proposed syntax in the `zig.zon` file demonstrates how block substitutions could be defined with probabilities as follows:

```zig.zon
.substitute = .{
	.{.old = "cubyz:stone", .new = .{
		.{.id = "cubyz:stone", .chance = 0.99},
		.{.id = "cubyz:coal_ire", .chance = 0.01},
	}},
}
```
The engine would store these substitutions as a list of tagged unions for efficient sampling, allowing for more flexible and efficient world generation.

In the current implementation (issue #1412), fixed replacements are defined like this:

```zig.zon
.substitute = .{
	.{.old = "cubyz:birch_log", .new = "cubyz:oak_log"},
}
```
The proposed change extends this by introducing probabilities for randomized substitutions.

## Related Questions
- Can you provide an example of how to define randomized substitutions in the `zig.zon` file?

*Source: unknown | chunk_id: github_issue_2461_discussion*
