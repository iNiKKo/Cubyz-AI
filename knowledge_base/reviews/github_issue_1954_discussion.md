# [issues/issue_1954.md] - Issue #1954 discussion

**Type:** review
**Keywords:** tabs, spaces, Zig style, code formatter, editor extensions, asset loading time, byte saving
**Concepts:** code formatting, indentation, performance, disk space

## Summary
The discussion revolves around the use of tabs versus spaces for indentation in the Cubyz project, with maintainers defending the current formatting choices and users advocating for adherence to Zig's style guidelines.

## Explanation
The discussion revolves around whether the Cubyz project should adopt a code formatter that aligns with established Zig style guidelines or continue using its bespoke formatting rules. The maintainers argue for tabs over spaces, citing easier navigation with arrow keys and saving bytes in the source code. They also mention concerns about asset loading time being affected by spaces but this is disputed as an assumption rather than empirical evidence. Users advocate for adherence to Zig's style guidelines for consistency and ease of use across different tech stacks. Editor extensions like Visual Studio Code extension (https://github.com/PixelGuys/Cubyz-dev-kit-vscode) are suggested to help contributors adapt to the project’s formatting rules more easily. The maintainers emphasize that the purpose of formatting is to ensure code style consistency, which will speed up code navigation once adapted to and reduce the burden of commenting on PRs.

## Related Questions
- What specific formatting choices does the Cubyz project enforce?
- How do tabs versus spaces impact performance and disk space usage according to maintainers' claims?
- Which editor extensions support the Cubyz code formatting style?
- Why is commenting out blocks of code problematic when using tabs?

*Source: unknown | chunk_id: github_issue_1954_discussion*
