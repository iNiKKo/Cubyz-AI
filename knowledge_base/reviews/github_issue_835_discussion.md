# [issues/issue_835.md] - Issue #835 discussion

**Type:** review
**Keywords:** raytracing, low-end hardware, integrated GPUs, rendering backends, open-source, third-party implementation
**Concepts:** performance, compatibility, maintenance

## Summary
The maintainer discusses the feasibility of adding raytracing to Cubyz, citing performance concerns on low-end hardware and the desire to avoid maintaining multiple rendering backends.

## Explanation
The maintainer explains that while raytracing is a desirable feature for enhancing visual effects in Cubyz, it poses significant challenges. The primary concern is the performance impact on low-end hardware and integrated GPUs, which are critical for broad compatibility. Additionally, maintaining two separate rendering backends (one for traditional methods and another for raytracing) would complicate the codebase and increase maintenance overhead. However, the maintainer acknowledges that the open-source nature of Cubyz allows for third-party developers to create their own implementations of raytracing effects.

## Related Questions
- What are the primary performance concerns with implementing raytracing in Cubyz?
- Why does the maintainer want to avoid maintaining multiple rendering backends?
- How could third-party developers contribute raytracing effects to Cubyz?
- What is the current status of raytracing support in Cubyz?
- Are there any plans for future updates regarding raytracing in Cubyz?
- How does the maintainer balance performance and visual quality in Cubyz?

*Source: unknown | chunk_id: github_issue_835_discussion*
