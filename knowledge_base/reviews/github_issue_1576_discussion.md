# [issues/issue_1576.md] - Issue #1576 discussion

**Type:** review
**Keywords:** block item appearance, inventoryData property, rotation modes, item models, texture differences, automatic resolution lowering, detail loss, log spiral pattern, complex task, automatic generation
**Concepts:** inventoryData, rotation modes, item models, texture mapping

## Summary
Discussion on allowing separate item models for blocks, focusing on visual consistency and feasibility.

## Explanation
Discussion on allowing separate item models for blocks to ensure visual consistency between full blocks and their corresponding items. The issue highlights that logs should use `line` texture on the sides, `top` texture on top and bottom in inventory, while full blocks do not get item textures. A user proposes an 'inventoryData' property for rotation modes as a solution but is met with skepticism about automatic resolution lowering due to potential detail loss like spiral patterns on logs. The maintainer expresses interest in having such item models in the game despite initial doubts. The user acknowledges the complexity of creating these models and suggests generating some automatically while manually crafting others.

## Related Questions
- What is the proposed solution for making block items visually consistent with their full blocks?
- Why does the maintainer question the feasibility of automatically lowering resolution to match item models?
- How does the user suggest addressing the complexity of creating item models for all blocks?
- Can automatic generation of some block models be combined with manual creation for others?

*Source: unknown | chunk_id: github_issue_1576_discussion*
