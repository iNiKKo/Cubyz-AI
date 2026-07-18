# [issues/issue_767.md] - Issue #767 discussion

**Type:** review
**Keywords:** zon, recipe files, clunky, result = ingredients, damage, chisel, minecraft, domainless files, duplicate entries, future-proofing
**Symbols:** cubyz:oak_planks, cubyz:workbench, cubyz:birch_planks, cubyz:torch, cubyz:stone_bricks, cubyz:stone, chisel
**Concepts:** file format conversion, recipe syntax, tool attributes, flexibility

## Summary
The discussion revolves around converting recipe files to a new format (zon) and exploring various syntax options. The maintainers consider different approaches, including a 'result = ingredients' style and handling tools with additional attributes like damage. Ultimately, they decide to stick with the clunky version due to its flexibility and ease of adding future features.

## Explanation
The discussion revolves around converting recipe files to a new format (zon) and exploring various syntax options. The maintainers consider different approaches, including a 'result = ingredients' style and handling tools with additional attributes like damage. They explore several syntax options such as:

```zig
.{
    ."cubyz:workbench" = .{"4 cubyz:oak_planks"},
    ."cubyz:torch" = .{"cubyz:oak_planks", "cubyz:coal"},
}
```
and
```zig
.{
    ."cubyz:stone_bricks" = .{"cubyz:stone", .{
        .type = .chisel,
        .requiredPower = 5,
        .damage = 1,
    }},
}
```
The maintainers encounter issues such as not allowing duplicate entries on the left-hand side, which complicates handling multiple recipes with similar inputs. They also consider adding attributes for tools like damage but decide that this would require a separate type and might introduce complexity. After evaluating various options, including Minecraft's approach, they conclude that the clunky version is acceptable due to its flexibility and ease of future expansion.

Specific examples include:
- A recipe format where each entry maps an output item to an array of ingredients (e.g., `cubyz:workbench` -> `4 cubyz:oak_planks`).
- Another example with a chisel tool requiring specific power and damage attributes for crafting stone bricks.

The maintainers ultimately decide on the clunky version due to its flexibility in handling various types of recipes, including those involving tools.

## Related Questions
- How does the clunky version handle recipes with similar inputs?
- What are the potential issues with allowing duplicate entries on the left-hand side?
- How does the proposed format accommodate tool attributes like damage?
- Why was Minecraft's approach not chosen as a reference?
- What specific improvements were considered for the custom recipe format?
- How does the clunky version provide flexibility for future features?

*Source: unknown | chunk_id: github_issue_767_discussion*
