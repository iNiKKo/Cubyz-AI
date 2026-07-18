# [issues/issue_3284.md] - Issue #3284 discussion

**Type:** review
**Keywords:** command line argument, help dialog, simplification, user experience, maintenance
**Concepts:** command line interface, user experience

## Summary
The maintainer suggests that any command line argument should trigger the display of a help dialog.

## Explanation
The discussion revolves around handling command line arguments in the Cubyz application. The maintainer proposes that instead of processing each argument, the application should consistently print a help dialog whenever any command line argument is provided. This approach aims to simplify usage and ensure users are always informed about available options.

## Related Questions
- What is the current behavior of Cubyz when a command line argument is provided?
- How does the proposed change impact the user's ability to interact with Cubyz via the command line?
- Are there any potential performance implications from always displaying the help dialog?
- What are the maintainability benefits of this approach?
- Could this change introduce any regressions in how arguments are processed?
- How would this affect backward compatibility with existing scripts or automation tools?

*Source: unknown | chunk_id: github_issue_3284_discussion*
