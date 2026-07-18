# [issues/issue_3283.md] - Issue #3283 discussion

**Type:** review
**Keywords:** ECS restructuring, naming conventions, code consolidation, directory structure, legacy code removal, entity management, component handling, system handling, file organization, modular design
**Symbols:** Entity.zig, entity_manager.zig, entityComponent, _list.zig, _template.zig, bag.zig, model.zig, player.zig, entityModel.zig, entitySystem, modelRenderer.zig
**Concepts:** Entity-Component-System (ECS), Directory Structure, Naming Conventions, Code Consolidation

## Summary
The issue discusses the need for restructuring and renaming components of the ECS system in Cubyz, focusing on reducing redundancy and improving clarity.

## Explanation
The review highlights that the current directory structure and naming conventions for ECS-related files are inconsistent and redundant. The reviewer suggests merging duplicate files like Entity.zig and consolidating entity managers. There's a proposal to move components to a mods directory and rename entitySystem to just system, as it doesn't have entity-specific functions. Additionally, there's a suggestion to introduce an assets folder for entity models. The main goal is to improve the ECS architecture by centralizing similar functionalities and removing legacy code.

## Related Questions
- How can we merge Entity.zig files without losing functionality?
- What is the proposed solution for consolidating entity managers?
- Why should entityComponent be moved to mods, and how will this affect naming conventions?
- What changes are needed in the linter to enforce better file naming conventions?
- How will renaming entitySystem to system impact existing codebase?
- What steps are being taken to introduce an assets folder for entity models?

*Source: unknown | chunk_id: github_issue_3283_discussion*
