# [issues/issue_2030.md] - Issue #2030 discussion

**Type:** review
**Keywords:** ore rotation, dense ore blocks, multiple resources, storage limitation, issue #1821
**Concepts:** resource management, block storage

## Summary
The issue discusses implementing a pile rotation mode for ores to allow denser ore blocks that can be mined multiple times. The current storage in blocks is insufficient, blocking the implementation.

## Explanation
The issue proposes implementing a pile rotation mode for ores to allow denser ore blocks that can be mined multiple times. These ore blocks would contain multiple layers of different resources and would need to be mined one step at a time to harvest all contained resources. The current block storage system is insufficient, blocking the implementation due to limitations mentioned in issue #1821. The maintainer expresses enthusiasm for the idea but acknowledges that it is blocked by the existing storage limitation. The proposal includes an example texture of a copper ore block with multiple layers, indicating how such denser ore blocks could be visually represented. Players would mine these ore blocks one step at a time to harvest all resources contained within them. The discussion also touches on potential performance implications and the impact on resource gathering balance in Cubyz.

## Related Questions
- What is the current block storage capacity in Cubyz?
- How does the proposed ore rotation mode differ from the existing mining system?
- Are there any plans to address the storage limitation mentioned in issue #1821?
- Can you provide more details on how the denser ore blocks will be implemented?
- What are the potential performance implications of adding ore rotation mode?
- How will this feature impact the balance of resource gathering in Cubyz?

*Source: unknown | chunk_id: github_issue_2030_discussion*
