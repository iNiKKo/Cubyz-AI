# [medium/docs_CONTRIBUTING.md] - Chunk 0

**Type:** documentation
**Keywords:** AI/LLMs, Zig, formatter, pull requests, issues tab, Discord server, error handling, allocators, defer, errdefer
**Symbols:** zig, Cubyz-formatter, main.globalAllocator, main.stackAllocator, std.log.err, std.debug.assert, main.List, utils.NeverFailingAllocator, MemoryPool, allocator.create-destroyArena()
**Concepts:** contributing guidelines, programming in Zig, code quality, error handling, resource management, performance optimizations, style guide

## Summary
This document provides guidelines for contributing to Cubyz, covering topics such as using AI for pull requests, learning Zig, disabling Zig's formatter, selecting what to work on, writing code quality, error handling, resource management, performance optimizations, and following the style guide.

## Explanation
The document begins by advising against using AI/LLMs to create pull requests due to their inability to follow project conventions and learn from mistakes. It recommends learning Zig, a programming language used in Cubyz, and provides resources for doing so. The importance of disabling Zig's automatic formatter is emphasized to maintain the project's formatting standards.

The document outlines steps for selecting what to work on, suggesting starting with issues labeled as 'Contributor friendly' or seeking ideas from the Discord server. It advises splitting large pull requests into smaller ones to reduce review cycles and improve success rates.

Key aspects of writing code are covered, including explicit error handling, using appropriate allocators based on lifetime, freeing all allocated resources, keeping code simple, and following performance optimization philosophies. The style guide includes naming conventions, line limits, comments, imports, file organization, declaration order, magic constants, const correctness, unused variables, and operator precedence.

Finally, the document stresses the importance of not putting multiple changes into a single pull request, recommending that each PR be no more than 200 lines to minimize delays and conflicts.

## Related Questions
- What is the recommended approach for contributing to Cubyz?
- Why should AI/LLMs not be used to create pull requests in Cubyz?
- How do you disable Zig's automatic formatter in Cubyz?
- What are the main allocators available in Cubyz and when should they be used?
- How should error handling be implemented in Cubyz code?
- What is the importance of keeping code simple in Cubyz development?
- What are some key points to follow regarding performance optimizations in Cubyz?
- What are the naming conventions for variables, constants, and functions in Cubyz?
- What is the recommended line limit for code in Cubyz?
- How should comments be used in Cubyz code?

*Source: unknown | chunk_id: docs_CONTRIBUTING.md_chunk_0*
