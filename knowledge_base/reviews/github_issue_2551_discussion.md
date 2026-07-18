# [issues/issue_2551.md] - Issue #2551 discussion

**Type:** review
**Keywords:** TPM, encrypt, player Account Code, UEFI update, corrupted settings, login prompt, checksums
**Concepts:** TPM, encryption, security, checksums

## Summary
Discussion on using TPM for encrypting player Account Code locally, addressing potential issues like UEFI updates or corrupted settings.

## Explanation
The discussion revolves around enhancing security by encrypting the player's Account Code using TPM (Trusted Platform Module) when stored locally. The maintainer addresses concerns about what happens if the UEFI version is updated (which might wipe the TPM) or if the settings get corrupted. The intended behavior is that the game will prompt the user to log in again, and checksums will be used to prevent corruption. Additionally, the maintainer notes that similar issues occur when switching PCs and taking over settings.

## Related Questions
- What is the impact of updating UEFI on TPM-encrypted data?
- How does the game handle corrupted encrypted settings?
- What measures are in place to prevent corruption of encrypted settings?
- What happens if a player switches PCs and takes over their settings?
- How does the game ensure that the encrypted Account Code remains secure?
- What is the role of checksums in protecting encrypted data?
- How does the game prompt users for login after encryption issues?
- Are there any potential security risks associated with using TPM for encryption?
- How does the game handle situations where TPM might be wiped?
- What are the steps taken to ensure that the encrypted Account Code is not compromised?

*Source: unknown | chunk_id: github_issue_2551_discussion*
