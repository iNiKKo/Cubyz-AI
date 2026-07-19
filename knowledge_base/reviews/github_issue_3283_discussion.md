# [issues/issue_3283.md] - Issue #3283 discussion

**Type:** review
**Keywords:** ECS restructuring, naming conventions, code consolidation, directory structure, legacy code removal, entity management, component handling, system handling, file organization, modular design
**Symbols:** Entity.zig, entity_manager.zig, entityComponent, _list.zig, _template.zig, bag.zig, model.zig, player.zig, entityModel.zig, entitySystem, modelRenderer.zig
**Concepts:** Entity-Component-System (ECS), Directory Structure, Naming Conventions, Code Consolidation

## Summary
The issue discusses the need for restructuring and renaming components of the ECS system in Cubyz, focusing on reducing redundancy and improving clarity.

## Explanation
The issue discusses the need for restructuring and renaming components of the ECS system in Cubyz to reduce redundancy and improve clarity. The review highlights that the current directory structure and naming conventions are inconsistent and redundant. Specifically, it is suggested to merge duplicate files like Entity.zig (see #3241) and consolidate entity managers (tracked in #3249). Additionally, there's a proposal to move components to a mods directory and rename entitySystem to just system as it doesn't have any functions specific to entities. The reviewer also suggests introducing an assets folder for handling entity models. The main goal is to improve the ECS architecture by centralizing similar functionalities and removing legacy code. Requirements include dedicated client-side ECS global state and API, components directory logic that handles runtime component management, systems directory logic that handles runtime system management, and removal of legacy items.

## Related Questions
- How can we merge Entity.zig files without losing functionality?
- What is the proposed solution for consolidating entity managers?
- Why should entityComponent be moved to mods, and how will this affect naming conventions?
- What changes are needed in the linter to enforce better file naming conventions?
- How will renaming entitySystem to system impact existing codebase?
- What steps are being taken to introduce an assets folder for entity models?

*Source: unknown | chunk_id: github_issue_3283_discussion*
