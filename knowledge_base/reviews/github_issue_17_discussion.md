# [issues/issue_17.md] - Issue #17 discussion

**Type:** review
**Keywords:** VSync, GPU, high frame rate, performance, commit, settings, maintenance
**Concepts:** VSync, GPU usage, frame rate

## Summary
The game's high GPU usage was caused by VSync being disabled, which led to the game running at an extremely high frame rate (5000 fps). The maintainers have enabled VSync by default in a recent commit (cbbcf507a67c0512b2fdc06fdf68b335f1ffe1b0) and instructed users to enable it manually in the settings.

## Explanation
The issue was identified as high GPU usage due to VSync being disabled, which caused the game to run at an unreasonably high frame rate (5000 fps), leading to inefficient GPU utilization. The maintainers addressed this by enabling VSync by default in a recent commit. This change aims to prevent excessive GPU load and improve performance by capping the frame rate to match the display's refresh rate. However, users are still required to manually enable VSync through the game settings under `Opções/Gráficos/Vertical Synchronization`.

## Related Questions
- What was the previous state of VSync before commit cbbcf507a67c0512b2fdc06fdf68b335f1ffe1b0?
- How does enabling VSync by default impact the game's performance?
- Why did the maintainers choose to enable VSync by default instead of fixing the high frame rate issue programmatically?
- What are the potential side effects of manually enabling VSync through the settings?
- Is there a way to automatically detect and adjust VSync based on hardware capabilities?
- How can users verify if VSync is enabled in their game settings?

*Source: unknown | chunk_id: github_issue_17_discussion*
