# [issues/issue_3349.md] - Issue #3349 discussion

**Type:** review
**Keywords:** command piping, Unix-style, spawn, tp, coordinates, clickable, clipboard, copy-paste, chat functionality, command semantics
**Concepts:** command piping, Unix shell, human-friendly output, game state alteration

## Summary
Discussion on implementing command piping in Cubyz, with suggestions for alternative approaches like direct spawning or copying coordinates.

## Explanation
The discussion revolves around the idea of adding Unix-style command piping to Cubyz. The maintainer points out that current command outputs are human-friendly and not designed for capturing or processing as input. They also note that commands in Cubyz are intended to alter game state rather than output data or take extended input. Users suggest alternatives such as direct spawning with coordinates, making coordinates clickable, or copying them to the clipboard. The maintainer considers allowing chat copy-paste functionality as a potential solution.

## Related Questions
- How can command outputs be modified to support piping in Cubyz?
- What are the potential use cases for Unix-style command piping in a game environment?
- How could direct spawning with coordinates address the issue of teleporting players?
- What technical challenges would arise from implementing command piping in Cubyz?
- Can chat copy-paste functionality be used to achieve similar results as command piping?
- How might the architecture of Cubyz commands need to change to support piping?

*Source: unknown | chunk_id: github_issue_3349_discussion*
