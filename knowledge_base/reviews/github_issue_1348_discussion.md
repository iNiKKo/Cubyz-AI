# [issues/issue_1348.md] - Issue #1348 discussion

**Type:** review
**Keywords:** recipes, tags, mapping, UI, boilerplate reduction, named symbols, addon support
**Symbols:** .wood, cubyz:coal, cubyz:torch, cubyz:planks
**Concepts:** recipe definitions, tags, input/output mapping, UI display

## Summary
Discussion on implementing tags in recipe definitions to reduce boilerplate and improve flexibility.

## Explanation
Discussion on implementing tags in recipe definitions to reduce boilerplate and improve flexibility.

The discussion revolves around allowing tags in recipes to specify inputs and outputs, reducing the need for duplicating recipes for different item types like wood. The main concerns include how to map input types to correct output types and how to display these recipes in the UI. The maintainer suggests using a mapping option within recipe definitions to explicitly specify the relationship between input and output types.

The proposal involves using tags to specify input and output of recipes, avoiding the need to duplicate all recipes for different wood types. For example, instead of having separate recipes for converting each type of log to planks, there would be one recipe that can take any log type and produce the corresponding plank type. This approach aims to reduce the length of the crafting list and lessen boilerplate in recipe definitions.

One of the challenges is mapping log types to correct plank types. The maintainer suggests manually mapping these relationships after implementing tags. Another alternative is to automatically generate all recipes based on tags, which could be more efficient as the number of recipes using planks as inputs grows quadratically with the number of total items.

The UI display of recipes that use tags for inputs and outputs can either cycle through textures or list each variant separately. The maintainer proposes adding a filter to the UI that takes only mismatched planks from things inserted into the filter, though this implementation may not be smooth. Alternatively, highlighting items in the inventory when hovering over the recipe could also be considered.

Named symbols are proposed for recipe inputs and outputs to maintain consistency with the current system. For example, a recipe definition might look like this:

```zig
.{
    .{
        .inputs = .{ "cubyz:planks/{typ}", "cubyz:coal" },
        .outputs = .{ .typ = "cubyz:torch/{typ}", .count = 8 },
    },
}
```

This syntax allows for automatic creation of recipes for plank types, including those from addons. The goal is to maintain consistency with the current system while improving flexibility and reducing boilerplate.

The maintainer also proposes using a `.mapping` option within recipe definitions to explicitly specify the relationship between input and output types. For example, a recipe definition might look like this:

```zig
.{
    .{
        .inputs = .wood,
        .outputs = .{ .typ = ".planks", .count = 4 },
        .mapping = .{ .startswith = ".recipe_subtype:" },
    },
}
```

This approach allows for more complex patterns or rules to be defined, and can be extended to support more advanced mapping options in the future.

## Related Questions
-  How does the proposed mapping option work in recipe definitions?
-  What are the potential issues with allowing mismatching items in recipes?
-  How will the UI display recipes that use tags for inputs and outputs?
-  What is the impact of using named symbols on recipe consistency?
-  How can addon support be integrated into the tag-based recipe system?
-  What are the advantages and disadvantages of generating all recipes eagerly versus using tags?
-  How does the proposed solution address the issue of mixing different wood types in recipes?
-  What are the potential technical challenges in implementing dedicated crafting stations with single input slots?
-  How can the mapping option be extended to support more complex patterns or rules?
-  What is the relationship between this tag-based recipe system and the concept of dedicated crafting stations?

*Source: unknown | chunk_id: github_issue_1348_discussion*
