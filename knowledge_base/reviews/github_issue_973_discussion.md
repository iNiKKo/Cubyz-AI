# [issues/issue_973.md] - Issue #973 discussion

**Type:** review
**Keywords:** language support, translation files, hierarchical approach, cascading translations, Weblate, Crowdin, modular design, maintenance overhead, explicit translation, localization strategy
**Symbols:** baobab_log.zig.zon, english.zig.zon, polish.zig, lang.translatedGame, lang.translatedTag, lang.translatedProperty, lang.translatedItem
**Concepts:** Localization, Translation Management, Hierarchical Data Structures, Cascading Translations

## Summary
Discussion about adding language support in Cubyz, focusing on design decisions and implementation strategies.

## Explanation
The discussion revolves around the addition of full names for blocks in different languages, with maintainers expressing concerns about the maintenance overhead. The proposal includes using explicit translation files, hierarchical approaches, and cascading translations to handle multiple languages efficiently. There is also a suggestion to integrate translation services like Weblate or Crowdin to streamline the process.

## Related Questions
- How does the hierarchical approach resolve language-specific naming conflicts?
- What are the potential benefits and drawbacks of using explicit translation files?
- How can cascading translations be implemented to handle incomplete translations?
- What is the impact of integrating translation services like Weblate on the development workflow?
- How would the proposed language module (`lang`) interact with existing Cubyz systems?
- What are the considerations for maintaining backward compatibility when adding language support?
- How can the design be optimized to minimize review cycles and maintainability overhead?
- What strategies can be employed to handle homograph issues in translations?
- How does the proposed system accommodate different naming conventions across languages?
- What are the potential performance implications of implementing a translation lookup table?

*Source: unknown | chunk_id: github_issue_973_discussion*
