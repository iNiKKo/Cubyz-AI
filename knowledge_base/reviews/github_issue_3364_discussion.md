# [issues/issue_3364.md] - Issue #3364 discussion

**Type:** review
**Keywords:** sound audio assets, sound definition assets, volume, attenuation, spatial audio, sound mixing, looping sounds, UI sounds, data-driven sfx, sound handle structures, random sound picking, simd mixing, doppler effect, ambient triggers, dynamic sound filters
**Concepts:** sound effect system, audio assets, data-driven design, thread safety, memory management

## Summary
The issue outlines a checklist for implementing various features in the sound effect system of Cubyz, ranging from basic functionalities like volume and attenuation to more complex features such as SIMD mixing and dynamic sound filters.

## Explanation
This issue outlines a detailed checklist for implementing various features in Cubyz's sound effect system. The tasks are categorized into easy, medium, hard, and phantasmal difficulty levels. Here is the breakdown of each category:

**Easy: **
- Sound audio assets
- Sound definition assets (reusing existing sounds with effects)
- Volume control
- Attenuation settings
- Spatial and non-spatial audio
- Sound mixing
- Looping sounds
- UI sounds

**Medium: **
- Data-driven sfx for addon creators and modders, such as defining block sounds like breaking or placing
- Sound handle structures that allow controlling sound effects through logic (e.g., position)
- Random sound picking from a user-defined list in the sound definition file and sound sequences

**Hard: **
- SIMD mixing
- Doppler effect
- Ambient triggers (birds, scary sounds, wind)

**Phantasmal Difficulty: **
- Dynamic sound filters (downsampling, phaser, pitch-shifting, etc.)
- Reverb
- Custom sound/music fading triggers
- Ambient overrides (e.g., adding echo underground or something else)

The discussion section addresses user comments about controlling sounds attached to moving entities, which is part of the 'medium' difficulty tasks.

## Related Questions
- What are the essential features for a basic sound effect system in Cubyz?
- How does the checklist categorize tasks based on difficulty?
- What advanced feature is mentioned under 'phantasmal difficulty'?
- Can you explain how sounds can be controlled through logic, like position and other settings?
- What is the purpose of data-driven sfx for addon creators and modders?
- How does random sound picking work in Cubyz's sound definition file?

*Source: unknown | chunk_id: github_issue_3364_discussion*
