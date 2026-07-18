# [issues/issue_379.md] - Issue #379 discussion

**Type:** review
**Keywords:** 9-slice, button textures, bold outlines, pixel cut-off, base texture, overlay, customization
**Concepts:** 9-slice textures, button appearance, pixel cut-off

## Summary
Discussion about implementing 9-slice button textures to improve button appearance and prevent pixel cut-off issues.

## Explanation
The discussion revolves around the implementation of 9-slice button textures in Cubyz. The user proposes using this technique to create buttons with bold outlines, aiming to avoid abrupt pixel cuts. The maintainer initially questions the concept but later suggests overlaying a nine-slice texture for the outline on top of a base texture like wood or chalk. Additionally, the maintainer has unhardcoded the button selection and pressed states, allowing for more customization.

## Related Questions
- What is the purpose of implementing 9-slice button textures in Cubyz?
- How does the 9-slice technique address pixel cut-off issues on buttons?
- What customization options are available for button states after unhardcoding them?
- Can you explain how the nine-slice texture will be overlaid onto a base texture?
- What are the potential benefits of using 9-slice textures for button design in Cubyz?
- How does the maintainer's suggestion for a chalk texture pattern on buttons align with the user's request?

*Source: unknown | chunk_id: github_issue_379_discussion*
