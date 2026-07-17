# [src/game.zig] - Chunk 1755254993

**Type:** review
**Keywords:** update, Player, bobVel, bobTime, bobMag, onGround, viewBobStrength, mutex, lerp, framerate
**Symbols:** update, Player.selectedSlot, main.Window.scrollOffset, fac, targetBobVel, horizontalMovementSpeed, vec.length, vec.xy, Player.getVelBlocking, Player.bobVel, std.math.exp, std.math.pow, Player.onGround, Player.bobTime, Player.bobMag, @min, @sqrt, settings.viewBobStrength
**Concepts:** thread safety, mutex locking, framerate independence, exponential damping, lerping, view bobbing, ground check, magnitude clamping, settings exposure

## Summary
The change introduces a framerate-independent view bobbing system that lerps velocity toward a target based on horizontal movement speed, updates bob time only when the player is on ground, and caps bob magnitude by strength settings.

## Explanation
The original code had no view bobbing; this diff adds it. The reviewer flagged that all writes to Player fields (bobVel, bobTime, bobMag) must be protected by a mutex because they touch the Player struct concurrently with other threads. Architecturally, the implementation uses exponential damping (fac = 1 - exp(-15*delta)) to make velocity updates independent of frame rate, then derives targetBobVel from horizontal speed via sqrt(pow(speed/4,0.5)). The bobTime increment is scaled by pow(bobVel,0.9) and only applied when onGround, preventing air-bobbing. BobMag clamps the square root of bobVel against a maximum (1.2) multiplied by settings.viewBobStrength to keep visual jitter bounded. This refactor improves realism without breaking existing movement logic.

## Related Questions
- What is the purpose of the 'fac' variable in this diff?
- How does the code ensure view bobbing only occurs when the player is on ground?
- Which Player struct fields are modified by this new block and why must they be mutex-locked?
- Explain how horizontalMovementSpeed is computed from Player.getVelBlocking().
- What formula is used to derive targetBobVel and why is a square root applied?
- How does the code prevent view bobbing in the air?
- What role does settings.viewBobStrength play in determining final bob magnitude?
- Why use std.math.exp with -15 * deltaTime instead of a simple linear decay?
- Is there any existing usage of Player.bobVel before this diff that might conflict with the new lerping logic?
- How would increasing viewBobStrength affect gameplay feel according to this implementation?

*Source: unknown | chunk_id: github_pr_665_comment_1755254993*
