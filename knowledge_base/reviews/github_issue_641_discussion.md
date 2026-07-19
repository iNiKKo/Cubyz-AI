# [issues/issue_641.md] - Issue #641 discussion

**Type:** review
**Keywords:** volume slider, dB, % amplitude, perceived volume, logarithmic nature, linear scale, usability issues
**Concepts:** logarithmic scale, amplitude, decibels, user interface design

## Summary
The issue discusses an inaccurate volume slider that does not correctly represent decibels, with a maintainer defending the current logarithmic scale used for amplitude.

## Explanation
The issue discusses an inaccurate volume slider that does not correctly represent decibels, with a maintainer defending the current logarithmic scale used for amplitude. The maintainer explains that the slider shows % amplitude and that 20 dB corresponds to a factor of 10 in amplitude. This means that the formula used is dB = 10 * log10(amplitude / max_amplitude). The reporter suggests using dB = 10log_2(slider %) for better perceived volume accuracy, especially towards the higher end of the slider range. However, the maintainer counters this by stating that a linear scale in amplitude would create usability issues because small changes at low amplitudes (e.g., from 2% to 3%) are more noticeable than larger changes at high amplitudes (e.g., from 99% to 100%). The logarithmic scale is preferred as it aligns with industry standards and highlights the logarithmic nature of sound perception.

## Related Questions
- What is the current formula used to calculate decibels in the volume slider?
- Why does the maintainer believe the logarithmic scale is correct for amplitude representation?
- How does the reporter suggest changing the formula for better accuracy?
- What are the potential issues with using a linear scale for amplitude in audio applications?

*Source: unknown | chunk_id: github_issue_641_discussion*
