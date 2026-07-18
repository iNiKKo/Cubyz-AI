# [build.zig] - PR #2064 review diff

**Type:** review
**Keywords:** build.zig, new step, compiler checks, output files, simplicity, refactor, code correctness
**Symbols:** build, zig_fmt_step, checkStep, modules
**Concepts:** build system, compiler checks, simplicity

## Summary
A new build step 'check' is added to run compiler checks without producing output files.

## Explanation
The reviewer suggests adding a new build step named 'check' that runs compiler checks without generating any output files. The reviewer emphasizes the importance of simplicity and warns against over-engineering, noting that future refactors might require reinventing similar code. This change aims to provide a straightforward way to verify code correctness during the build process.

## Related Questions
- What is the purpose of the 'check' build step?
- How does the 'check' step differ from other build steps?
- Why did the reviewer emphasize simplicity in this change?
- Could future refactors lead to changes in how compiler checks are handled?
- What potential benefits might come from adding a 'check' step to the build process?
- Is there any risk of over-engineering with this new build step addition?

*Source: unknown | chunk_id: github_pr_2064_comment_2475397660*
