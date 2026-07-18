# [issues/issue_44.md] - Issue #44 discussion

**Type:** review
**Keywords:** BUILD FAILURE, mvn exec:java, readme outdated, plugin parameters, goal execution
**Symbols:** org.codehaus.mojo:exec-maven-plugin, executable
**Concepts:** build process, documentation accuracy

## Summary
Updated build instructions for Maven execution.

## Explanation
The issue report indicated a build failure due to missing or invalid parameters for the 'executable' goal in the org.codehaus.mojo:exec-maven-plugin. The maintainer comment clarified that the readme documentation was outdated and provided the correct command `mvn exec:java` instead of the previously mentioned `mvn exec:exec`. This change ensures that users can correctly execute the project using Maven, addressing the build failure issue.

## Related Questions
- What is the correct Maven command to execute the project?
- Why was the original 'mvn exec:exec' command incorrect?
- How does updating the readme prevent future build failures?
- Are there any other outdated commands in the documentation?
- What steps should be taken if a similar build failure occurs again?
- Is there a way to automate checking for outdated Maven plugin commands?

*Source: unknown | chunk_id: github_issue_44_discussion*
