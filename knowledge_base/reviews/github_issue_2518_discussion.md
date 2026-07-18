# [issues/issue_2518.md] - Issue #2518 discussion

**Type:** review
**Keywords:** zig fmt, struct initialization, nested constructs, formatting consistency, Zig ecosystem
**Concepts:** code formatting, consistency, developer experience

## Summary
Discussion on aligning Cubyz's formatting style with Zig's preferred format, particularly around struct initialization. Maintainer prefers consistency over personal preference.

## Explanation
Discussion on aligning Cubyz's formatting style with Zig's preferred format, particularly around struct initialization. The maintainer expresses dissatisfaction with how the Zig formatter handles nested constructs, specifically in struct initializations like:

```zig
.{ .attachments = &.{.{ // zig fmt
	.srcColorBlendFactor = .one,
	.dstColorBlendFactor = .one,
	.colorBlendOp = .add,
	.srcAlphaBlendFactor = .one,
	.dstAlphaBlendFactor = .one,
	.alphaBlendOp = .add,
}} },
```

Despite this, progress has been made towards adopting more Zig-like formatting conventions to enhance compatibility and accessibility for developers familiar with the Zig ecosystem. The maintainer prefers consistency over personal preference but will keep the struct initialization as it was due to dissatisfaction with the weirdness of the zig formatter.

## Related Questions
-  What specific issues are raised with the Zig formatter's handling of nested struct initializations?
-  How does the maintainer plan to balance personal formatting preferences with maintaining consistency in Cubyz?
-  What progress has been made towards making Cubyz more compatible with the Zig ecosystem?
-  Are there any plans to update the formatter further based on feedback from this discussion?
-  How might the decision to maintain the current struct initialization style impact future updates to Cubyz?

*Source: unknown | chunk_id: github_issue_2518_discussion*
