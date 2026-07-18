# [issues/issue_2227.md] - Issue #2227 discussion

**Type:** review
**Keywords:** test, CI, launch, close, error logs, curated world, LOD regeneration, controlled shutdown, communication protocol, stdin/stdout, Python script
**Symbols:** Cubyz, CI, LOD regeneration, curated world, launchConfig, controlled shutdown, communication protocol, stdin/stdout, Python script
**Concepts:** testing, continuous integration, server control, protocol design, external communication

## Summary
Discussion on adding a test in the CI to launch and close the standalone server, checking for error logs. The team decides to create a curated world with specific actions to trigger certain behaviors and implement a controlled shutdown mechanism using a communication protocol.

## Explanation
The discussion revolves around implementing a CI test that launches and closes the standalone Cubyz server while checking for error logs. The team considers two types of tests: one using an existing world from the last release and another using a new world created from the commit triggering the CI. They decide to create a curated world with specific actions, such as LOD regeneration, to deliberately trigger certain behaviors and catch both migration-type errors and general launch errors. For controlled shutdown, they propose a communication protocol that allows the server to communicate its execution stage to an external controller, which can then terminate it gracefully. The team also decides to use stdin/stdout for initial implementation and suggests using a Python script as the controller due to its ease of creation and extension.

## Related Questions
- What are the steps to create a curated world for testing?
- How does the communication protocol work between the server and the controller?
- What specific actions trigger LOD regeneration in the curated world?
- How is the controlled shutdown implemented using stdin/stdout?
- What is the role of the Python script as the controller?
- How are error logs checked during the CI test?
- What are the benefits of using a communication protocol for server control?
- How does the team plan to handle compatibility with older worlds in the curated world?
- What are the potential challenges in implementing the controlled shutdown mechanism?
- How will the team ensure that the controller can communicate effectively with the server?

*Source: unknown | chunk_id: github_issue_2227_discussion*
