# [issues/issue_571.md] - Issue #571 discussion

**Type:** review
**Keywords:** music quality, degrades over time, Windows, audio resampling, spectrogram, perceivable difference, better audio library
**Concepts:** audio quality, resampling, spectrogram

## Summary
The maintainer investigates an issue where music quality degrades over time in Cubyz, but cannot reproduce the problem themselves.

## Explanation
The maintainer investigates an issue where music quality degrades over time in Cubyz. They ask for clarification on the timeframe and whether it's specific to Windows. After examining audio files and comparing them side by side using Audacity, they find no perceivable difference in sound quality, attributing any visual differences in spectrograms to expected resampling artifacts. The maintainer suggests that improving audio resampling might require a better audio library but believes the current implementation is acceptable given their inability to hear a difference.

## Related Questions
- What is the reported timeframe for the music quality degradation issue?
- Does the maintainer believe the issue is specific to Windows?
- How did the maintainer compare the audio files to check for differences?
- What visual differences were observed in the spectrograms, and why are they expected?
- Why does the maintainer suggest using a better audio library for improvement?
- Is there any plan to address the issue further based on the current findings?

*Source: unknown | chunk_id: github_issue_571_discussion*
