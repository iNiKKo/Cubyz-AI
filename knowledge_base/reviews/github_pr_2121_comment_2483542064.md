# [src/game.zig] - Chunk 2483542064

**Type:** review
**Keywords:** EyeData, Player, eyePos, eyeVel, coyote, step, box, desiredPos, Vec3d, refactorings, PR size
**Symbols:** EyeData, Player, Vec3d, collision.Box
**Concepts:** refactoring, code consolidation, PR size guidelines, struct composition

## Summary
Refactors Player.eyePos/eyeVel/eyeCoyote/eyeStep fields into a single EyeData struct to consolidate player eye state.

## Explanation
The change introduces an EyeData struct containing pos, vel, coyote, step, box, and desiredPos. This consolidates previously scattered eye-related fields (eyePos, eyeVel, eyeCoyote, eyeStep) into one cohesive definition, improving readability and maintainability. The reviewer explicitly requested that such refactorings be split into a separate PR to adhere to contributing guidelines on PR size, indicating concern about diff magnitude rather than correctness of the logic itself.

## Related Questions
- What fields are included in the newly introduced EyeData struct?
- Which previous Player fields were replaced by eyeData?
- Why does the reviewer suggest moving this refactor into a separate PR?
- Does the diff modify any other files besides game.zig?
- Is there an initialization of eyeData shown in the snippet?
- What is the type of the box field inside EyeData?
- How many lines were added versus removed in this change?
- Are there any comments explaining the motivation for consolidating eye fields?
- Does the change affect any public API surface beyond Player definition?
- Is the desiredPos field part of the original codebase or new?

*Source: unknown | chunk_id: github_pr_2121_comment_2483542064*
