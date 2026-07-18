# [issues/issue_1016.md] - Issue #1016 discussion

**Type:** review
**Keywords:** mushrooms, rotation mode, model configuration, base model, side model, wall placement, object orientation
**Symbols:** .rotation, .torch, .model, .base, .side, cubyz:ground_mushroom, cubyz:shelf_mushroom
**Concepts:** Model Configuration, Rotation Mode, Object Orientation

## Summary
Discussion on allowing overwriting the side models of the torch rotation mode for mushrooms.

## Explanation
The issue revolves around enabling the use of different models for mushrooms based on their placement (ground or wall). The maintainer suggests using an existing rotation mode with a custom model configuration instead of creating a new one. This approach allows specifying both base and side models, with the side model needing to be oriented towards the negative x wall.

## Related Questions
- How is the shelf_mushroom.obj oriented in relation to the wall?
- What are the requirements for attaching models to walls in Cubyz?
- Can different base models be used with this configuration?
- Is there a limit to the number of models that can be specified in the .model field?
- How does this change affect existing mushroom models?
- Are there any performance implications for using multiple models per object?

*Source: unknown | chunk_id: github_issue_1016_discussion*
