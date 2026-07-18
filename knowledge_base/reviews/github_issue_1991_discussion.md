# [issues/issue_1991.md] - Issue #1991 discussion

**Type:** review
**Keywords:** framerate drop, chat history, culling, vertical list, rendering optimization
**Symbols:** history.items, GuiWindow, VerticalList.zig
**Concepts:** performance optimization, rendering culling, UI performance

## Summary
The user is working on fixing a performance issue where the game's framerate drops significantly when the UI is open, specifically due to rendering all chat history.

## Explanation
The maintainer identified that the issue stems from rendering all text in the chat history, even if it's outside the viewable range. The user initially considered changing the message order from FILO (First In Last Out) to FIFO (First In First Out), but was advised against limiting the history. Instead, the focus shifted to implementing culling, where only visible pieces of text are rendered. The user explored modifying the `VerticalList`'s render function to skip rendering items below a certain threshold, aiming to improve performance by not processing non-visible messages. However, this approach did not resolve the issue as expected.

## Related Questions
- What is the current implementation of chat history rendering in Cubyz?
- How does the `VerticalList`'s render function handle large lists of items?
- Can changing the message order from FILO to FIFO improve performance in this scenario?
- What are the potential side effects of limiting the number of messages displayed in the chat window?
- How can we ensure that only visible text is rendered without affecting the scroll bar functionality?
- Are there any existing optimizations or techniques for rendering large amounts of text efficiently in Cubyz?

*Source: unknown | chunk_id: github_issue_1991_discussion*
