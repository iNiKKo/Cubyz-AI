# [issues/issue_3336.md] - Issue #3336 discussion

**Type:** review
**Keywords:** permissions, command arguments, argparser, boilerplate code, God class, fine-grained control, explicit checks, automated permission checks, command parser responsibilities, separation of concerns
**Concepts:** permissions, command arguments, argparser, boilerplate code, God class

## Summary
Discussion about implementing permissions based on command arguments, with concerns over complexity and potential for boilerplate code.

## Explanation
The discussion revolves around the idea of allowing fine-grained control over command permissions using argument parsing. The maintainer is hesitant due to the potential for unnecessary complexity and boilerplate code, preferring explicit manual permission checks. There are also considerations about the flexibility and scalability of the permission system, especially in commands like `/sbb` and `/blueprint`, which require detailed access controls. The user suggests automating permission checks through the command parser, but the maintainer worries about overloading the ArgParser with too many responsibilities, potentially turning it into a 'God class'. There is also a suggestion to handle permissions at a higher level, possibly by separating command dispatch and permission handling.

## Related Questions
- How can the ArgParser be modified to handle permissions without becoming a God class?
- What are the potential benefits and drawbacks of automating permission checks through the command parser?
- How can we design a flexible permission system that scales well with complex commands like `/sbb` and `/blueprint`?
- What is the best approach for determining default asset sources based on user privileges?
- How can we ensure that users cannot access or modify assets they do not have permission to?
- What are the implications of using a hierarchical subcommand approach for permissions?
- How can we balance the need for fine-grained control with the risk of creating overly complex systems?
- What are the potential security risks associated with allowing users to specify asset sources in commands?
- How can we ensure that the permission system is backward compatible with existing command structures?
- What are the best practices for designing a robust and scalable permission management system?

*Source: unknown | chunk_id: github_issue_3336_discussion*
