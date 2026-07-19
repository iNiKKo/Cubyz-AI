# [issues/issue_1649.md] - Issue #1649 discussion

**Type:** review
**Keywords:** Blockbench, Cubyz, entity models, hitboxes, animation, modular design, community contributions, open-source integration
**Symbols:** Blockbench, Cubyz, hitbox, model, entity
**Concepts:** modularity, community-driven development, open-source integration

## Summary
Discussion about adding Blockbench model support for entities in Cubyz, including hitbox definitions and potential integration with existing plugins.

## Explanation
The discussion revolves around adding support for Blockbench model (.bbmodel) files to Cubyz for creating entity models and animations. Key points include defining hitboxes within a group named 'hitbox' which uses any cubes within that group as the hitbox, with the pivot point of the group acting as the eye height of the entity. A prefix like 'h_' or 'head_' can be used to define the model's head. Blockbench's scriptable keyframes allow for defining parts of an animation that trigger events such as particles or damage during specific animations (e.g., attack animations). Users suggest separating hitboxes from models to facilitate easier remodeling and maintaining modularity in entity design. Specific group names like 'hitbox' and 'model' are proposed to enable replacing model parts without affecting others, enhancing flexibility in entity creation. The maintainer notes that while Cubyz is open to community contributions for Blockbench integrations, there are currently no active contributors interested in working on such features.

## Related Questions
- How can hitboxes be defined within a group named 'hitbox' and what role does the pivot point play?
- What are the benefits of using specific prefixes like 'h_' or 'head_' for defining the model's head?
- Can you provide an example of how scriptable keyframes in Blockbench can trigger events such as particles or damage during animations?
- How might separating hitboxes from models enhance flexibility and modularity in entity design?

*Source: unknown | chunk_id: github_issue_1649_discussion*
