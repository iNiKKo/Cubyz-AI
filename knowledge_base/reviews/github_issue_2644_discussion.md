# [issues/issue_2644.md] - Issue #2644 discussion

**Type:** review
**Keywords:** music volume slider, decibels, linear perception, non-linear behavior, perceived loudness, actual loudness
**Concepts:** perceived loudness, actual loudness

## Summary
The music volume slider does not feel linear due to its use of decibels.

## Explanation
The issue arises because the music volume control uses decibels (dB) for adjusting volume, which do not correspond linearly with perceived loudness. This results in a non-linear perception where small changes at higher dB levels have a larger impact on perceived volume compared to lower levels. The maintainer argues that this is intentional as dBs represent actual loudness rather than perceived loudness.

## Related Questions
- What is the relationship between decibels and perceived loudness?
- Why does the music volume slider use decibels instead of a linear scale?
- How can the slider be adjusted to provide a more linear perception of volume?
- Are there any plans to change the volume control mechanism in future updates?
- What are the advantages and disadvantages of using decibels for volume control?
- How does the current implementation affect user experience with music playback?

*Source: unknown | chunk_id: github_issue_2644_discussion*
