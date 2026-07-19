# [issues/issue_2688.md] - Issue #2688 discussion

**Type:** review
**Keywords:** terminal velocity, altitude, falling damage, flaming effect, heat-proof accessory, specialized equipment, Desmos model, physics calculations, game.zig update function
**Symbols:** terminalVelocity, physics.baseGravity, Player.super.pos, Player.volumeProperties, Player.outerBoundingBox
**Concepts:** Physics simulation, Gameplay balance, Realism in games

## Summary
Discussion on adjusting terminal velocity based on altitude to prevent players from falling too far, with considerations for gameplay balance and realism.

## Explanation
Discussion on adjusting terminal velocity based on altitude to prevent players from falling too far, with considerations for gameplay balance and realism. The maintainer and users debate the impact on fast-travel methods and propose solutions like heat-proof accessories or specialized equipment for high-altitude environments. A user provides a Desmos model and a code snippet demonstrating how terminal velocity could be adjusted based on altitude using realistic physics calculations. The formula provided is:

```zig
const terminalVelocity = @sqrt((2.0 * 37.3 * physics.baseGravity) / (0.390625 * 1.0 * std.math.exp(@min(-Player.super.pos[2], 0) / 4150.0) * 0.7));
```

This formula calculates the terminal velocity based on player mass, cross-sectional area, air density, atmospheric scale height, and drag coefficient. The user's model shows that at height 0, Snale has a terminal velocity of approximately 90 m/s, increasing to about 300 m/s at height 10000.

## Related Questions
- How does the proposed terminal velocity formula affect player movement at different altitudes?
- What are the potential impacts on gameplay balance if terminal velocity is increased at higher altitudes?
- Can the Desmos model be used to predict the effects of changing atmospheric scale height or mass on terminal velocity?
- How would implementing heat-proof accessories or specialized equipment for high-altitude environments affect player progression in Cubyz?
- What are the implications of adjusting terminal velocity for player safety and realism in the game world?
- How could the code snippet be modified to account for different player masses or cross-sectional areas?

*Source: unknown | chunk_id: github_issue_2688_discussion*
