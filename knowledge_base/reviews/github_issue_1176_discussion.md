# [issues/issue_1176.md] - Issue #1176 discussion

**Type:** review
**Keywords:** branch placement, solid blocks, extra faces, boolean values, auto-generated models
**Concepts:** block data, auto-generated models

## Summary
The issue discusses improving branch placement by allowing branches to connect to other branches or solid blocks.

## Explanation
The current implementation of branch placement is limited, only allowing branches to be placed on themselves or solid blocks. The maintainer suggests that to allow branches to connect to other branches without extra faces on full connections, at least six additional boolean values would be needed for block data. This change would require generating 4096 auto-generated models to support the new placement rules.

## Related Questions
- What is the current limitation of branch placement in Cubyz?
- How many additional boolean values are suggested to allow branches to connect to other branches?
- How many auto-generated models would be required with the new placement rules?
- What is the main concern regarding extra faces on full connections?
- Is there any plan to implement this change in the near future?
- What potential performance impacts could arise from generating 4096 auto-generated models?

*Source: unknown | chunk_id: github_issue_1176_discussion*
