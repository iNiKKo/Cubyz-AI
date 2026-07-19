# [issues/issue_2551.md] - Issue #2551 discussion

**Type:** review
**Keywords:** TPM, encrypt, player Account Code, UEFI update, corrupted settings, login prompt, checksums
**Concepts:** TPM, encryption, security, checksums

## Summary
Discussion on using TPM for encrypting player Account Code locally, addressing potential issues like UEFI updates or corrupted settings.

## Explanation
Discussion on using TPM for encrypting player Account Code locally when stored. The maintainer addresses concerns about UEFI updates (which might wipe TPM) and potential corruption of settings. If the TPM is wiped due to an update or if settings get corrupted, the game will prompt the user to log in again. Checksums are used to prevent data corruption, ensuring that even if switching PCs, similar issues occur but with safeguards in place.

## Related Questions
- What happens when a player updates their UEFI version?
- How does the game handle corrupted settings after an update or switch of PC?
- What is the role of checksums in preventing data corruption?

*Source: unknown | chunk_id: github_issue_2551_discussion*
