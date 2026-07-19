# [issues/issue_1431.md] - Issue #1431 discussion

**Type:** review
**Keywords:** Moffalo, behavior, breeding, life cycle, fur re-growing, eating system, saturation, model parameters, Rimworld, moth life cycle
**Symbols:** Moffalo, EntityType, fur re-growing system, eating system, saturation component
**Concepts:** entity behavior, breeding mechanics, life cycle simulation

## Summary
The discussion revolves around the behavior, breeding mechanics, and potential life cycle changes for the Moffalo entity in Cubyz.

## Explanation
**Explanation**
The review comments discuss the current behavior of Moffalo, including their social structure, aggression, and night-time activities. The maintainer highlights the need for a fur re-growing system, an eating system, and multiple model parameters to represent different states (e.g., hungry, starved). There is also a suggestion to change the name from 'Moffalo' to 'Mothalo' to avoid confusion with a creature in Rimworld. The breeding mechanics are detailed, specifying conditions under which Moffalo will breed: it requires a full moon, night time, non-hungry status, an adult moffalo in its herd, and fewer than 10 moffalo in the herd. A user proposes a more complex life cycle inspired by moth biology, including egg-laying, hatching into moffa-worms, and cocooning before becoming baby Moffalo.

**Specific Behaviors and States:**
- **Social Structure:** Moffalo spawn in groups of 3 to 6, with the oldest being the leader. Younger Moffalo copy the leader's behavior. If the leader dies, a new leader is elected based on age.
- **Aggression:** If approached aggressively (sprinting/making noise), nearby Moffalo will run away and sometimes split into multiple groups. If attacked or sheared, they become aggressive and try to stampede over the player.
- **Night-Time Activities:** During night, Moffalo sleep together, allowing the player to shear them without making noise or provoking them.
- **Idle Behavior:** Includes self-grooming, sitting, stomping, playing, and frolicking.

**Hunger System:**
- **Grazing:** Moffalo eat grass vegetation. If they cannot get enough food, they enter a 'hungry' state, then 'starved,' and eventually die.

**Breeding Mechanics:**
- **Conditions for Breeding:** A full moon, night time, non-hungry status, an adult moffalo in the herd, and fewer than 10 moffalo in the herd. When these conditions are met, a new child is born to the herd.

**Proposed Life Cycle Changes:**
- **Adult Moffalo:** Lay eggs.
- **Egg Hatching:** Into moffa-worms.
- **Moffa-Worm Development:** After eating, they cocoon.
- **Cocoon Hatching:** Into baby Moffalo.

## Related Questions
- What are the conditions for Moffalo breeding?
- How does the current eating and hunger system work for Moffalo?
- Is there a plan to implement different textures or models for Moffalo based on their state?
- Why was the name 'Moffalo' chosen, and is there any consideration for changing it?
- What are the potential impacts of implementing a moth-inspired life cycle for Moffalo?
- How will the new breeding mechanics be integrated with the existing social structure of Moffalo herds?

*Source: unknown | chunk_id: github_issue_1431_discussion*
