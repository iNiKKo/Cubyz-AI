# [issues/issue_1915.md] - Issue #1915 discussion

**Type:** review
**Keywords:** player data corruption, extreme position values, lag spike, crash, recent changes
**Symbols:** update, start, entryFn
**Concepts:** thread safety, data corruption, lag handling

## Summary
The player data corruption issue was reported with extreme position values and a lag spike. The maintainer noted that the issue is no longer reproducible with recent changes.

## Explanation
The player data corruption issue was reported with extremely high position values and a lag spike, leading to a crash. The maintainer reviewed the provided log and noted that while there were significant lag spikes (server lagging behind by 162.6 ms), the extreme position values suggest a deeper issue:

```
{
	.entity = {
		.position = {
			-1.3335808012825433e26,
			-1.4280661955554763e26,
			7.940002435588171e26
		},
	}
}
```

The maintainer concluded that recent changes have made the issue non-reproducible for now, but the extreme position values indicate a potential thread safety or data corruption problem. Despite this, no specific part of the code was identified as causing the lag spike.

Recent changes include improvements to thread safety and better handling of large numerical values in player data. The maintainer noted that while these changes have made the issue non-reproducible for now, further investigation is needed if similar issues arise again.

## Related Questions
- What were the exact numerical values of the player's position when the crash occurred?
- How did recent changes address the issue of extreme position values in player data?

*Source: unknown | chunk_id: github_issue_1915_discussion*
