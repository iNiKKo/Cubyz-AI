# [issues/issue_2343.md] - Issue #2343 discussion

**Type:** review
**Keywords:** GUI, hidden, show inventory, screenshot, accidental key presses, natural option
**Symbols:** F1, ESC
**Concepts:** user interface, keyboard shortcuts, game mechanics

## Summary
The issue discusses a scenario where pressing ESC after hiding the GUI with F1 does not show the inventory as expected.

## Explanation
The issue discusses a scenario where pressing ESC after hiding the GUI with F1 does not show the inventory as expected. Instead, when the GUI is hidden and ESC is pressed, the user sees only their mouse cursor. This behavior is intended to allow users to take screenshots without any additional elements obscuring the view. The maintainers acknowledge that while some users rely on this feature for taking screenshots, others find it confusing because pressing ESC does not restore the previous state (e.g., showing the inventory). There is a suggestion to introduce a dedicated screenshot button as an alternative solution. Additionally, there is a consideration to revert the effects of F1/F2 when ESC is pressed to prevent accidental key presses and improve user experience.

## Related Questions
- What is the current behavior of pressing ESC after hiding the GUI with F1?
- Why do some users rely on this feature for taking screenshots?
- How can the game be modified to revert the effects of F1/F2 when ESC is pressed?
- Is there a plan to introduce a dedicated screenshot button in future updates?
- What are the potential implications of changing the behavior of ESC after hiding the GUI?
- How can user confusion regarding keyboard shortcuts be mitigated?

*Source: unknown | chunk_id: github_issue_2343_discussion*
