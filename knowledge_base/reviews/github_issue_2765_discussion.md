# [issues/issue_2765.md] - Issue #2765 discussion

**Type:** review
**Keywords:** ctrl+select, ctrl+delete, underscore, word separation, resource IDs, intuitive behavior
**Concepts:** text selection, keyboard shortcuts, word boundaries

## Summary
Discussion on handling underscore '_' as a word separator in text selection features like ctrl+select and ctrl+delete.

## Explanation
### Issue #2765 Discussion

The issue revolves around the behavior of text selection when using keyboard shortcuts like ctrl+shift+left arrow or ctrl+delete. The primary concern is whether underscores should be treated as part of words or as spaces.

#### Steps to Reproduce and Observed Behavior

1. Type a word then a number, separated by a space (e.g., 'word 123').
2. Hold `ctrl+shift` and press the left arrow key to select the previous 'word'.

This applies to `ctrl+delete` too.

#### Discussion

**Maintainer Comment:** Many other things are also unintuitive here, e.g., I think it should select words combined with `_` characters since we use them often enough in file names.

**User Comment:** Personally, I think it makes sense to count `_` as a space, since it's being used to separate words. Also, most implementations of this treat `_` as a space so it's what most people are used to.

**Maintainer Comment:** Since `_` will mostly appear in resource IDs, I think treating it as part of the word makes more sense and allows you to e.g., modify commands more quickly. Also, most implementations of this treat `_` as part of the word, browsers like Firefox and Chrome do so too.

**Maintainer Comment:** I'd say it's split pretty evenly, and not just code editors treat `_` as a part of the word; browsers like Firefox and Chrome do so too. Also, I'd say most people (apart from programmers) are probably not even aware of this nuance since this situation rarely comes up outside of code.

The current implementation treats underscores as part of words, especially in resource IDs, allowing for quicker modifications. Users argue that treating underscores as spaces aligns with common practices in code editors and browsers, making it more intuitive for non-programmers.

## Related Questions
- What is the current implementation of underscore handling in text selection features?
- How does treating underscores as spaces affect user experience for non-programmers?
- Are there any performance implications of changing underscore handling in text editors?
- What are the potential regressions if underscores are treated as part of words?
- How do other popular code editors and browsers handle underscore separation in text selection?

*Source: unknown | chunk_id: github_issue_2765_discussion*
