# [issues/issue_1928.md] - Issue #1928 discussion

**Type:** review
**Keywords:** policy, fixing things that aren't broken, PR focus, user benefit, bug report, measurable improvement, compatibility proof, security improvement, performance benefit, maintenance reduction, evidence checklist, problem statement, supported platforms, proof, risk analysis
**Symbols:** PR, bugfix, compatibility, security, performance, maintenance
**Concepts:** user-visible value, churn reduction, regression prevention, evidence-based decision-making

## Summary
Proposes a policy for fixing things that aren't broken, focusing on PRs with clear user benefits or bug fixes.

## Explanation
Proposes a policy for fixing things that aren't broken, focusing on pull requests (PRs) with clear user benefits or bug fixes. The policy aims to ensure PRs contribute meaningful value by either fixing confirmed bugs or providing measurable improvements such as compatibility, security, performance, or maintainability. It outlines acceptance criteria for non-broken areas and requires PR descriptions to include detailed evidence and risk analysis. Specifically, a PR that adjusts a non-broken area must satisfy at least one of the following criteria:

1. **Compatibility Proof:** Expands support (e.g., works on more distros/OSes) with evidence (commands, versions, CI matrix, or user reports).
2. **Security Improvement:** Fixes or mitigates a known vulnerability (CVE, advisory, threat model, etc.).
3. **Performance Benefit:** Shows measurable wins (benchmarks, before/after numbers) with no regressions.
4. **Maintenance Reduction:** Simplifies codepath, removes dead code, reduces dependencies, or aligns with a widely adopted, documented standard.

If none apply → prefer Issue discussion first; PR may be closed as *Low Value / No Evidence*.

The policy defines 'broken' as a feature failing on any supported platform/config or contradicting documented behavior. 'Unbroken' means the feature works as documented on all supported targets. The review process involves labeling (e.g., `needs-evidence`, `compat-improvement`, `perf-claim`, `maintenance`), a decision tree, and specific approval requirements based on the nature of the changes. Exceptions are made for critical security fixes, CI/build breakages, and documentation/comment-only changes.

## Related Questions
- What are the acceptance criteria for a PR that adjusts a non-broken area?
- How does the policy define 'broken' and 'unbroken' features?
- What evidence is required in a PR description according to the policy?
- What are the labels used in the review process, and how are they applied?
- How many reviewers are needed for different types of PRs according to the decision tree?
- What exceptions are made to the policy, and why?

*Source: unknown | chunk_id: github_issue_1928_discussion*
