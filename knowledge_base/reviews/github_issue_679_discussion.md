# [issues/issue_679.md] - Issue #679 discussion

**Type:** review
**Keywords:** Vetch invisible, model name fix, cross to cubyz:cross, issue resolution, namespace correction
**Symbols:** vetch.json
**Concepts:** model names, namespace

## Summary
The issue 'Vetch is invisible' was resolved by correcting the model name in vetch.json from 'cross' to 'cubyz:cross'.

## Explanation
The problem arose because the model name for Vetch was not updated after a previous fix involving model names. The reviewer identified that Vetch may have been added after these changes, leading to its invisibility due to an incorrect reference. The solution involved modifying vetch.json to use the correct namespace prefix 'cubyz:', ensuring that the model is correctly recognized and displayed.

## Related Questions
- What was the previous model name for Vetch?
- Why did the namespace prefix 'cubyz:' need to be added?
- How many other models might have similar issues due to missing namespace prefixes?
- Is there a script or tool that can automatically check and fix model names with missing namespaces?
- What are the potential consequences of not fixing model name issues like this one?
- Can you provide more context on when Vetch was added and why it wasn't included in previous model name fixes?

*Source: unknown | chunk_id: github_issue_679_discussion*
