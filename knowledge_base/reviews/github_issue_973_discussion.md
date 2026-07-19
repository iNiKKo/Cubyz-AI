# [issues/issue_973.md] - Issue #973 discussion

**Type:** review
**Keywords:** language support, translation files, hierarchical approach, cascading translations, Weblate, Crowdin, modular design, maintenance overhead, explicit translation, localization strategy
**Symbols:** baobab_log.zig.zon, english.zig.zon, polish.zig, lang.translatedGame, lang.translatedTag, lang.translatedProperty, lang.translatedItem
**Concepts:** Localization, Translation Management, Hierarchical Data Structures, Cascading Translations

## Summary
Discussion about adding language support in Cubyz, focusing on design decisions and implementation strategies. The maintainers express concerns about maintenance overhead due to supporting multiple languages. They propose using explicit translation files with hierarchical approaches and cascading translations to handle incomplete translations efficiently. Specific examples are provided for how this could work.

## Explanation
The maintainers express concerns about the maintenance overhead due to supporting multiple languages. They propose using explicit translation files with hierarchical approaches and cascading translations to handle incomplete translations efficiently. Specific examples are provided for how this could work:

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

Additionally, there is a discussion on allowing aliases for use in commands, such as `cubyz:ocean/temperate/base` being able to also be written as `cubyz:temperate_ocean` or `cubyz:ocean/temperate`. The maintainers suggest that the text should always be the same but that autocomplete could react to language-specific names.

The maintainers also mention that using colons in zon fields is possible with the syntax `.@"cubyz:log/baobab"` and that there are two options for organizing assets: a hierarchical approach or an ID-based approach. They propose splitting the hierarchy at the top into two parts, game and assets, to allow for better organization and fallbacks.

Finally, there is a discussion on maintaining backward compatibility when adding language support and optimizing the design to minimize review cycles and maintainability overhead.

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

*Source: unknown | chunk_id: github_issue_973_discussion*
