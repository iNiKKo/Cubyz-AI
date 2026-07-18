# [issues/issue_641.md] - Issue #641 discussion

**Type:** review
**Keywords:** volume slider, dB, % amplitude, perceived volume, logarithmic nature, linear scale, usability issues
**Concepts:** logarithmic scale, amplitude, decibels, user interface design

## Summary
The issue discusses an inaccurate volume slider that does not correctly represent decibels, with a maintainer defending the current logarithmic scale used for amplitude.

## Explanation
The discussion revolves around the discrepancy between the perceived volume change and the slider's percentage representation. The maintainer argues that the current logarithmic scale is correct as it aligns with industry standards and highlights the logarithmic nature of the slider. However, the reporter suggests a different formula (dB = 10log_2(slider %)) to better reflect human perception, especially towards the higher end of the slider range. The maintainer counters that this linear approach in amplitude could lead to usability issues, as small changes at low amplitudes would be more noticeable than at high amplitudes.

## Related Questions
- What is the current formula used to calculate decibels in the volume slider?
- Why does the maintainer believe the logarithmic scale is correct for amplitude representation?
- How does the reporter suggest changing the formula for better accuracy?
- What are the potential issues with using a linear scale for amplitude in audio applications?
- Can you explain why small changes at low amplitudes are more noticeable than at high amplitudes?
- How does the logarithmic scale help in showing the nature of the slider?

*Source: unknown | chunk_id: github_issue_641_discussion*
