# [issues/issue_1371.md] - Issue #1371 discussion

**Type:** review
**Keywords:** performance warning, API_ID_REDUNDANT_FBO, glBindFramebuffer, driver verbosity, silencing warnings, underlying issue
**Concepts:** OpenGL API performance, redundant state change, glBindFramebuffer

## Summary
The user reports receiving numerous performance warnings related to redundant state changes in glBindFramebuffer API calls. The maintainer suggests that these warnings are not bugs but driver verbosity and advises finding a way to silence them or fixing the underlying issue.

## Explanation
The user is encountering a large number of performance warnings indicating redundant state changes when calling glBindFramebuffer with FBO 0, which is already bound. The maintainer acknowledges that this is not a bug per se but rather an overly verbose driver warning. They suggest two potential solutions: silencing the warnings or addressing the underlying issue if desired.

## Related Questions
- How can the driver be configured to reduce verbosity?
- Is there a way to programmatically silence these specific warnings in OpenGL?
- What are the potential performance impacts of redundant glBindFramebuffer calls?
- Are there any known issues with FBO 0 being bound multiple times?
- Can the underlying issue causing these warnings be identified and fixed?
- How does the driver determine if a state change is redundant?
- Is there a way to log only critical warnings instead of all performance warnings?
- What are the best practices for handling OpenGL performance warnings in applications?
- Are there any tools or libraries that can help manage OpenGL warning output?
- How might these warnings affect application performance and stability?

*Source: unknown | chunk_id: github_issue_1371_discussion*
