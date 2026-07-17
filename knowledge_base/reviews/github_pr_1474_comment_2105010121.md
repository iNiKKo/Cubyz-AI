# [src/blocks.zig] - PR #1474 review diff

**Type:** review
**Keywords:** Entity, rotation.zig, ecs/components/cubyz/entity.zig, main.server.Entity, touch functions, architectural review, design integration
**Symbols:** Entity, ModelIndex, RotationMode, Degrees
**Concepts:** architectural review, integration, design considerations

## Summary
Updated the import statement for the `Entity` type from `main.server.Entity` to `@import("ecs/components/cubyz/entity.zig").Data`. This change is part of a critical architectural review aimed at integrating touch functions into the current design.

## Explanation
The update involves changing the source of the `Entity` type, which was previously imported from `main.server.Entity` to now be imported directly from `ecs/components/cubyz/entity.zig`. This modification is significant as it aligns with a broader architectural review focused on integrating touch functions into the existing design. The reviewer emphasizes the importance of considering how these touch functions will fit within the current system architecture, suggesting potential changes or refactoring may be necessary to ensure seamless integration.

## Related Questions
- What is the purpose of the architectural review mentioned in the comment?
- How does changing the `Entity` import affect other parts of the codebase?
- What are the potential implications of integrating touch functions into the current design?
- Can you explain the significance of the `ecs/components/cubyz/entity.zig` file in this context?
- How might the updated import statement impact performance or correctness?
- Are there any other files that need to be reviewed as part of this architectural change?

*Source: unknown | chunk_id: github_pr_1474_comment_2105010121*
