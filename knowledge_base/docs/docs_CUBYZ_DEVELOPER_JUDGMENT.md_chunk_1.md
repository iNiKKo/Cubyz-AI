# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 1

**Type:** documentation
**Keywords:** accurate naming, unit specification, name collisions, casing conventions, inclusive/exclusive boundaries, input validation, integer overflow, secure random value generation, single concern, explicit return, out-of-scope suggestions, backward compatibility, documentation, attributed ported algorithms, log message severity
**Symbols:** loadWorldData, loadWorldConfig, getProperty, setProperty, TimeDelta, ZLS, snake_case, PascalCase, Air, argparse
**Concepts:** naming conventions, correctness, defensive programming, pull request management, backward compatibility, documentation, code review processes

## Summary
The document outlines coding standards and best practices for the Cubyz voxel engine development, focusing on naming conventions, correctness, defensive programming, pull request management, backward compatibility, documentation, and code review processes.

## Explanation
This section provides detailed guidelines for developers working on the Cubyz project. It emphasizes the importance of accurate naming that reflects current functionality, clear unit specification for numeric values, avoiding name collisions with existing types, and adhering to specific casing conventions (snake_case for values, PascalCase for types). The document also stresses the need for consistent inclusive/exclusive boundary handling, input validation, integer overflow prevention, and secure random value generation. It outlines the importance of keeping pull requests focused on a single concern, ensuring every code path has an explicit return, and deferring out-of-scope suggestions to follow-up issues. Backward compatibility with existing saved data formats is crucial, as is providing documentation for new public API surfaces and attributing ported algorithms. Log message severity and wording must accurately reflect the situation. The document concludes with a set of questions reviewers should ask when reviewing or writing Cubyz code. Review response categorization: a debugging-style response applies when a change addresses a genuine bug or "why doesn't this work" problem -- broken/incorrect runtime behavior; a design-review response applies when the discussion is about a design, style, or architectural choice with no broken behavior involved (e.g. issue #3279's excessive Zig cache disk usage was explicitly treated as "not a bug per se," just something to optionally mitigate; PR #2682's SparseSet-vs-VirtualList revert was an architectural/pointer-stability tradeoff discussion, not a bug fix). Misreading a design preference as a bug report (or vice versa) leads to fixing something that was never broken, or dismissing a real defect as "just style."

## Related Questions
- What is the recommended naming convention for functions in Cubyz?
- How should numeric values be handled to avoid ambiguity about their units?
- Why is it important to avoid name collisions with existing types in Cubyz?
- What are the specific casing conventions used in Cubyz development?
- How should inclusive/exclusive boundaries be consistently applied in Cubyz code?
- What measures should be taken to prevent integer overflow in timestamp arithmetic?
- Why is it crucial to keep pull requests focused on a single concern?
- How should changes to serialized/save formats be handled to maintain backward compatibility?
- In a Cubyz code review, what's the difference between when a change should get a debugging-style response vs a design-review response?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_1*
