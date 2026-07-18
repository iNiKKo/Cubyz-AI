# [issues/issue_3192.md] - Issue #3192 discussion

**Type:** review
**Keywords:** seed phrase, account system, user confusion, single-player, multiplayer, UI improvements, storage options, security concerns, local account, email login, steam login, password manager
**Symbols:** seed phrase, Account Code, local account, multiplayer server, singleplayer worlds, Account code storage options, email login, steam login, password manager, UI improvements
**Concepts:** User Experience (UX), Security, Friction Reduction, Account Management, Multiplayer Gaming

## Summary
The discussion revolves around improving the seed phrase system to reduce user confusion and annoyance, particularly for single-player users. The maintainers propose various solutions such as adding a local account option, improving UI prompts, and offering multiple storage options for the account code.

## Explanation
The discussion revolves around improving the seed phrase system to reduce user confusion and annoyance, particularly for single-player users. Users find the current implementation confusing and annoying, especially when they want to play without setting up an account or understanding its purpose. The maintainers propose various solutions including adding a local account option for single-player users, improving the UI to guide users through the account creation process more smoothly, and providing multiple options for storing the account code (e.g., saving it as a file, using a password manager). They also address concerns about security and user friction, aiming to balance these factors while making the system more user-friendly. The maintainers propose changes in PRs #3229 and #3252 to implement these improvements. Specifically, they suggest adding an 'Account' button in the menus with a pop-up when joining a multiplayer server that you must create an account first. They also discuss potential issues such as losing access to single-player worlds if the local player is not logged in properly. The maintainers propose offering checkboxes for different storage options (e.g., save as file, send email, use default password manager) and implementing a timer during account creation to ensure users read important information before proceeding.

## Related Questions
- What are the proposed solutions to reduce user confusion with the seed phrase system?
- How does the maintainers' proposal address security concerns while improving UX?
- What changes were made in PRs #3229 and #3252 to improve the account system?
- How does the local account option impact single-player gameplay?
- What are the potential issues with automatically saving the account code on disk?
- What are the benefits of offering multiple storage options for the account code?
- How does the maintainers' proposal address the issue of users forgetting their account codes?

*Source: unknown | chunk_id: github_issue_3192_discussion*
