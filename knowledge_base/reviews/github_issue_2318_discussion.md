# [issues/issue_2318.md] - Issue #2318 discussion

**Type:** review
**Keywords:** command handling, argument parsing, reflection, standardization, error messages, custom types, usage generation
**Symbols:** CommandCaller, Arguments, execute, @typeInfo, Coordinate, parse
**Concepts:** Reflection, Standardization, Error Handling, Custom Types

## Summary
Proposes unifying command handling by creating a shared `CommandCaller` that parses arguments using reflection.

## Explanation
The current implementation of commands in Cubyz results in duplicated parsing logic and inconsistent behavior. The proposed solution involves creating a `CommandCaller` that handles argument parsing, error message generation, and execution. This would standardize command handling, simplify the addition of new commands, and prevent inconsistencies. The `CommandCaller` uses reflection (`@typeInfo`) to parse arguments based on their declared types, allowing for automatic error messages and support for custom types with a `parse` function. Additionally, it could generate usage messages and descriptions automatically.

## Related Questions
- How does the `CommandCaller` handle custom argument types?
- What is the role of the `parse` function in custom types?
- How does the `CommandCaller` generate error messages for invalid arguments?
- Can you explain how reflection (`@typeInfo`) is used to parse command arguments?
- What are the benefits of using a shared `CommandCaller` for command handling?
- How would adding a new command differ with this unified approach?
- Is there any potential performance impact from using reflection in argument parsing?
- Can you provide an example of how the `printUsage` function might be implemented?
- What are the architectural implications of standardizing command execution in Cubyz?
- How does this change affect backwards compatibility with existing commands?

*Source: unknown | chunk_id: github_issue_2318_discussion*
