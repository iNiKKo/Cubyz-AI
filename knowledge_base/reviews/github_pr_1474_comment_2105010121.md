# [src/blocks.zig] - PR #1474 review diff

**Type:** review
**Keywords:** Entity, blocks.zig, main.server.Entity, ecs/components/cubyz/entity.zig, architectural review, touch functions, import, ModelIndex, RotationMode, Degrees
**Symbols:** Entity, ModelIndex, RotationMode, Degrees
**Concepts:** architectural review, integration, touch functions

## Summary
The `Entity` type in `blocks.zig` has been updated from a direct import from `main.server.Entity` to an import from `ecs/components/cubyz/entity.zig`. This change is part of a critical architectural review aimed at integrating touch functions into the current design.

## Explanation
The update involves changing the source of the `Entity` type, which was previously imported directly from `main.server.Entity` to now be imported from `ecs/components/cubyz/entity.zig`. This modification is significant as it aligns with a broader architectural review focused on how touch functions should be integrated into the existing design. The reviewer emphasizes the importance of considering the implications of this change, particularly in terms of ensuring that the new import does not disrupt the functionality of touch events or introduce any unforeseen issues.

## Related Questions
- What are the potential impacts of changing the Entity import on touch function behavior?
- How does this change align with the broader architectural goals for integrating touch functions?
- Are there any backward compatibility concerns with this update?
- What is the purpose of the critical architectural review mentioned in the comment?
- Does the new Entity import from ecs/components/cubyz/entity.zig provide additional functionality or just a different source?
- How should the on touch functions be integrated into the current design after this change?

*Source: unknown | chunk_id: github_pr_1474_comment_2105010121*
