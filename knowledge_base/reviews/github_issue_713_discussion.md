# [issues/issue_713.md] - Issue #713 discussion

**Type:** review
**Keywords:** chat, keybind, /, pause menu, textbox, europeans, shift+7, remappable
**Concepts:** keybind, internationalization, remappability

## Summary
Discussion on implementing a keybind to open chat and insert '/' in the chat, with consideration for international keyboard layouts.

## Explanation
The discussion revolves around the implementation of a keybind that opens the chat and inserts a '/' character. The initial suggestion was to use the '/' key, but this raised concerns about its availability on European keyboards where it might be mapped differently (e.g., using 'shift+7'). The maintainer emphasizes the importance of remappability to accommodate various keyboard layouts.

## Related Questions
- What is the current implementation of chat keybindings in Cubyz?
- How can we ensure that the new keybind is remappable for different keyboard layouts?
- Are there any existing issues with chat functionality that this change might address or exacerbate?
- What are the potential performance implications of adding a new keybind feature?
- How does this change affect backwards compatibility with older versions of Cubyz?
- Is there a plan to document the remapping process for users in different regions?

*Source: unknown | chunk_id: github_issue_713_discussion*
