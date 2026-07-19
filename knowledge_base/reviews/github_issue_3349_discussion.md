# [issues/issue_3349.md] - Issue #3349 discussion

**Type:** review
**Keywords:** command piping, Unix-style, spawn, tp, coordinates, clickable, clipboard, copy-paste, chat functionality, command semantics
**Concepts:** command piping, Unix shell, human-friendly output, game state alteration

## Summary
Discussion on implementing command piping in Cubyz, with suggestions for alternative approaches like direct spawning or copying coordinates.

## Explanation
Discussion on implementing command piping in Cubyz, with suggestions for alternative approaches like direct spawning or copying coordinates. The maintainer points out that current command outputs are designed to be human-friendly and not intended for capturing or processing as input. They also note that commands in Cubyz are intended to alter game state rather than output data or take extended input, indicating there is no compelling use case within the scope of Cubyz's design philosophy. Users suggest alternatives such as direct spawning with coordinates (e.g., `/summon entityName ~ ~ ~`), making coordinates clickable, copying them to the clipboard, and allowing chat copy-paste functionality as potential solutions.

The maintainer explains that in Unix shell, piping connects stdout of one command to stdin of another without changing the argument list. They also mention that Cubyz commands are not designed for dynamic input or extended processing. Users propose `/tp spawn` as a better solution, detecting coordinates and making them clickable, or using `/spawn copy` to copy coordinates to the clipboard. The maintainer suggests that chat copy-paste functionality could be used to achieve similar results.

The discussion highlights the technical challenges of implementing command piping in Cubyz, such as capturing reliable output from commands and changing their behavior based on input. The maintainers also note that there are no compelling use cases within Cubyz's design philosophy that would require such a feature.

## Related Questions
- How can command outputs be modified to support piping in Cubyz?
- What are the potential use cases for Unix-style command piping in a game environment?
- How could direct spawning with coordinates address the issue of teleporting players?
- What technical challenges would arise from implementing command piping in Cubyz?
- Can chat copy-paste functionality be used to achieve similar results as command piping?
- How might the architecture of Cubyz commands need to change to support piping?

*Source: unknown | chunk_id: github_issue_3349_discussion*
