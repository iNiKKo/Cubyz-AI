# [issues/issue_1969.md] - Issue #1969 discussion

**Type:** review
**Keywords:** in-air controls, unintended falls, coyote time, air friction, air mobility, charged jumps, b-hopping, landing mechanics, walking speed, prototype
**Symbols:** air friction, air mobility, coyote time, charged jumps, walking speed
**Concepts:** player control, physics simulation, gameplay balance

## Summary
The discussion revolves around improving in-air controls to prevent unintended falls and enhance player experience. Proposals include increasing air control with coyote time, charged jumps, and adjusting landing mechanics.

## Explanation
The discussion revolves around improving in-air controls to prevent unintended falls and enhance player experience. Proposals include increasing air control with coyote time, charged jumps, and adjusting landing mechanics. The two main ways to increase air control mentioned are: increasing air friction (which makes you fall slower) and increasing air mobility (which directly leads to b-hopping). 'Coyote time' aims to improve player control by giving a short period after leaving the ground to adjust jump/fall direction, similar to how it works in Dark Souls. There is a concern about increasing air mobility leading to b-hopping because it might make this movement optimal for travel. An alternative solution proposed for adjusting landing mechanics involves slowing down walking speed upon landing instead of character speed. The charged jump mechanism works by making the jump height depend on how long the spacebar is held, inspired by Ori and the Blind Forest. Potential drawbacks of implementing charged jumps include frequent jumping in the game feeling unnatural and potentially making animations less 'snappy'. A prototype was made to adjust landing mechanics but found ineffective at low speeds due to glider physics limitations. The maintainers emphasize testing these possibilities to ensure they improve gameplay without introducing new issues like b-hopping or overly snappy animations.

## Related Questions
- What are the two main ways to increase air control mentioned in the discussion?
- How does the 'coyote time' proposal aim to improve player control?
- Why is there a concern about increasing air mobility leading to b-hopping?
- What alternative solution is proposed for adjusting landing mechanics?
- How does the charged jump mechanism work, and what game does it draw inspiration from?
- What are the potential drawbacks of implementing charged jumps in the game?

*Source: unknown | chunk_id: github_issue_1969_discussion*
