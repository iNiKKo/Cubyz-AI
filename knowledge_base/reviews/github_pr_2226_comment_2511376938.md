# [src/server/command/tickspeed.zig] - PR #2226 review diff

**Type:** review
**Keywords:** tickrate, ticks per chunk per frame, blocks per chunk per tick, server-equivalent of a frame, terminology, user understanding
**Symbols:** tickspeed, description
**Concepts:** terminology consistency, user understanding

## Summary
The review suggests changing the description of the 'tickspeed' command to clarify that the tickrate is measured in blocks per chunk per tick instead of ticks per chunk per frame.

## Explanation
The reviewer points out an inconsistency in terminology within the code. The original description states that the tickrate is measured in 'ticks per chunk per frame,' but since a tick is defined as the server-equivalent of a frame, this description could be misleading. The suggested change corrects this by specifying that the tickrate should be measured in 'blocks per chunk per tick.' This clarification helps ensure that users understand the actual units being used for the tickrate setting.

## Related Questions
- What is the purpose of the 'tickspeed' command in Cubyz?
- Why was there a need to change the description of the 'tickspeed' command?
- How does the corrected description improve user understanding?
- Are there any other commands in Cubyz that might have similar terminology issues?
- How does this change affect the server's performance or behavior?
- Is there a specific section of the code where the tickrate is calculated or adjusted?

*Source: unknown | chunk_id: github_pr_2226_comment_2511376938*
