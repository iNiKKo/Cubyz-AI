# [issues/issue_1704.md] - Issue #1704 discussion

**Type:** review
**Keywords:** bouncy mushrooms, coyote time, bounce threshold, micro-bounces, crouching, onGround, jumping
**Symbols:** bouncing, coyote time, threshold, crouching
**Concepts:** gameplay mechanics, player movement

## Summary
The discussion revolves around implementing bouncy mushrooms in Cubyz, with maintainers providing feedback on activating coyote time, setting bounce thresholds, and handling crouching mechanics.

## Explanation
The primary focus of the discussion is to ensure that the bouncing behavior of mushrooms in Cubyz meets specific gameplay requirements. The maintainers emphasize the importance of activating coyote time during bounces to prevent micro-bouncing and ensure smooth player movement. Additionally, they suggest implementing a threshold for bounces to avoid rapid, small jumps. The user addresses these points by adjusting the bounce threshold and ensuring that crouching affects bouncing behavior. However, there are ongoing issues with coyote time not being activated correctly during bounces.

## Related Questions
- What is the current implementation of coyote time during bounces?
- How does the bounce threshold affect player movement?
- Is there a specific condition that prevents coyote time from activating during bounces?
- How should crouching be handled to modify bouncing behavior?
- Are there any known issues with the current bounce mechanics in Cubyz?
- What is the intended effect of setting `onGround` to true during bouncing?

*Source: unknown | chunk_id: github_issue_1704_discussion*
