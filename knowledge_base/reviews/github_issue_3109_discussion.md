# [issues/issue_3109.md] - Issue #3109 discussion

**Type:** review
**Keywords:** argsparse, struct, parse function, default behavior, recursive parsing, error messages, discord chat, explicit flag, generic type
**Symbols:** argsparse, Coordinates, Axis, enableRecursiveParsing, Recursive
**Concepts:** default behavior, recursive parsing, error handling, struct iteration

## Summary
The issue proposes adding default parsing behavior for structs without a parse function and discusses the need for controlling recursive parsing.

## Explanation
The discussion revolves around enhancing the `argsparse` module to handle structs that lack a custom parse function by providing a default behavior that iterates over all fields. The maintainer highlights potential issues with obscure error messages arising from deep struct recursion, suggesting two solutions: requiring an explicit flag (`enableRecursiveParsing`) to toggle automatic iteration of members or introducing a generic type (`Recursive`) that implements this behavior. This approach aims to prevent silent failures and improve error reporting.

## Related Questions
- What is the purpose of the `enableRecursiveParsing` flag?
- How does the proposed `Recursive` generic type work in the context of struct parsing?
- What are the potential benefits and drawbacks of requiring an explicit flag for recursive parsing?
- Can you explain how the default behavior iterates over struct fields without a custom parse function?
- What kind of error messages can arise from deep struct recursion, and how does this proposal address them?
- How might the introduction of `Recursive` impact existing code that relies on automatic struct parsing?

*Source: unknown | chunk_id: github_issue_3109_discussion*
