# [issues/issue_3109.md] - Issue #3109 discussion

**Type:** review
**Keywords:** argsparse, struct, parse function, default behavior, recursive parsing, error messages, discord chat, explicit flag, generic type
**Symbols:** argsparse, Coordinates, Axis, enableRecursiveParsing, Recursive
**Concepts:** default behavior, recursive parsing, error handling, struct iteration

## Summary
The issue proposes adding default parsing behavior for structs without a parse function and discusses the need for controlling recursive parsing.

## Explanation
The discussion revolves around enhancing the `argsparse` module to handle structs that lack a custom parse function by providing a default behavior that iterates over all fields. The maintainer highlights potential issues with obscure error messages arising from deep struct recursion, suggesting two solutions: requiring an explicit flag (`enableRecursiveParsing`) to toggle automatic iteration of members or introducing a generic type (`Recursive`). This approach aims to prevent silent failures and improve error reporting.

The `enableRecursiveParsing` flag is a boolean value that, when set to `true`, enables the automatic iteration over struct fields. The proposed `Recursive` generic type would implement this behavior explicitly, ensuring that recursive parsing is controlled and intentional. Both solutions aim to address the problem of obscure error messages by making it clear whether recursive parsing should occur.

The maintainer suggests that requiring an explicit flag (`enableRecursiveParsing`) helps prevent silent failures and improves error reporting by making it clear whether recursive parsing should occur. The `Recursive` generic type, on the other hand, provides a more explicit way to implement this behavior, ensuring that recursive parsing is controlled and intentional.

The potential benefits of requiring an explicit flag include improved error handling and clarity in code intent. However, there may be drawbacks such as increased complexity in managing multiple flags or types. The introduction of `Recursive` could impact existing code that relies on automatic struct parsing, but it provides a more controlled approach to recursive parsing.

## Related Questions
- What is the purpose of the `enableRecursiveParsing` flag?
- How does the proposed `Recursive` generic type work in the context of struct parsing?
- What are the potential benefits and drawbacks of requiring an explicit flag for recursive parsing?
- Can you explain how the default behavior iterates over struct fields without a custom parse function?
- What kind of error messages can arise from deep struct recursion, and how does this proposal address them?
- How might the introduction of `Recursive` impact existing code that relies on automatic struct parsing?

*Source: unknown | chunk_id: github_issue_3109_discussion*
