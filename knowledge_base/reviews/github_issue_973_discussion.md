# [issues/issue_973.md] - Issue #973 discussion

**Type:** review
**Keywords:** language support, translation files, hierarchical approach, cascading translations, Weblate, Crowdin, modular design, maintenance overhead, explicit translation, localization strategy
**Symbols:** baobab_log.zig.zon, english.zig.zon, polish.zig, lang.translatedGame, lang.translatedTag, lang.translatedProperty, lang.translatedItem
**Concepts:** Localization, Translation Management, Hierarchical Data Structures, Cascading Translations

## Summary
Discussion about adding language support in Cubyz, focusing on design decisions and implementation strategies.

## Explanation
Discussion about adding language support in Cubyz, focusing on design decisions and implementation strategies. The maintainers express concerns about maintenance overhead due to the complexity of supporting multiple languages. Proposals include using explicit translation files with hierarchical approaches and cascading translations to handle incomplete translations efficiently. Specific examples are provided for how this could work:

- **Explicit Translation Files**: Translatable strings go through an additional lookup step by indexing into a huge table, e.g.,
  ```zig
  .{
      .name = "Baobab log",
      .description = "Can be placed",
      ...
  }
  ```
  and the corresponding translation file,
  ```zig
  polish.zig
  .{
      ."Baobab log" = "Kłoda baobabu",
      ."Can be placed" = "Można umieścić",
      ...
  }
  ```
- **Hierarchical Approach**: Each addon could get a file, and each folder could get an additional layer of nesting in the file. For example,
  ```zig
  .{
      .@"cubyz:log/baobab" = .{
          .itemName = "Baobab",
          .itemDescription = "can be placed",
      },
  }
  ```
- **Cascading Translations**: Language files should allow cascading to extend incomplete translations.

The maintainers also discuss the use of translation services like Weblate or Crowdin to streamline the process and handle homograph issues by using an arbitrary ID to X translation. The proposal includes detecting the lack of a `:` in item names and auto-prepending a `modname:` for better integration.

## Related Questions
-  How does the hierarchical approach resolve language-specific naming conflicts?
-  What are the potential benefits and drawbacks of using explicit translation files?
-  How can cascading translations be implemented to handle incomplete translations?
-  What is the impact of integrating translation services like Weblate on the development workflow?
-  How would the proposed language module (`lang`) interact with existing Cubyz systems?
-  What are the considerations for maintaining backward compatibility when adding language support?
-  How can the design be optimized to minimize review cycles and maintainability overhead?
-  What strategies can be employed to handle homograph issues in translations?
-  How does the proposed system accommodate different naming conventions across languages?

*Source: unknown | chunk_id: github_issue_973_discussion*
