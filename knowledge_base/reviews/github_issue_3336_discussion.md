# [issues/issue_3336.md] - Issue #3336 discussion

**Type:** review
**Keywords:** permissions, command arguments, argparser, boilerplate code, God class, fine-grained control, explicit checks, automated permission checks, command parser responsibilities, separation of concerns
**Concepts:** permissions, command arguments, argparser, boilerplate code, God class

## Summary
Discussion about implementing permissions based on command arguments, with concerns over complexity and potential for boilerplate code.

## Explanation
Discussion about implementing permissions based on command arguments, with concerns over complexity and potential for boilerplate code. The maintainer is hesitant due to the potential for unnecessary complexity and boilerplate code, preferring explicit manual permission checks. Specific examples include the `/spawn` command where users should be able to set their own spawnpoint but not others'. Proposed permission paths are `/command/spawn/playerIndex=null` (whitelist) and `/command/spawn/playerIndex=null/x` (blacklist). The maintainer suggests using unique field names for subcommands in the union, allowing the parser to skip any subcommand that is not present in the permission path. This would reduce error sets to only commands users have permission to use. However, concerns are raised about overloading the ArgParser with too many responsibilities and turning it into a 'God class'. There are also considerations for handling permissions at a higher level, possibly by separating command dispatch and permission handling.

## Related Questions
-  How can the ArgParser be modified to handle permissions without becoming a God class?
-  What are the potential benefits and drawbacks of automating permission checks through the command parser?
-  How can we design a flexible permission system that scales well with complex commands like `/sbb` and `/blueprint`?
-  What is the best approach for determining default asset sources based on user privileges?
-  How can we ensure that users cannot access or modify assets they do not have permission to?
-  What are the implications of using a hierarchical subcommand approach for permissions?
-  How can we balance the need for fine-grained control with the risk of creating overly complex systems?
-  What are the potential security risks associated with allowing users to specify asset sources in commands?

*Source: unknown | chunk_id: github_issue_3336_discussion*
