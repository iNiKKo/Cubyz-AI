# [issues/issue_1833.md] - Issue #1833 discussion

**Type:** review
**Keywords:** massDamage, swingSpeed, durability, 20% sum, 80% average, wood hook, tool properties, balance, realistic representation
**Symbols:** toolValue, sum, average, weight, partialWeight, partialSum
**Concepts:** averaging, summing, realism, usability

## Summary
The discussion revolves around modifying the calculation for tool properties like massDamage, swingSpeed, and durability to include a mix of summing and averaging, with a focus on achieving a balance between realism and usability.

## Explanation
The discussion revolves around modifying the calculation for tool properties like massDamage, swingSpeed, and durability to include a mix of summing and averaging, with a focus on achieving a balance between realism and usability. The initial proposal was to calculate tool values using 20% summing and 80% averaging, represented by the formula `toolValue = (sum * 0.2) + (average * 0.8)`. However, the first implementation resulted in an interpretation that seemed too strong for certain tools like wood hooks. The user then adjusted the approach by averaging 80% of the weight instead of adding 20% of the sum on top of it. This change was intended to provide a more balanced and realistic representation of tool properties without making partially filled tools unviable. In the adjusted formula, `partialWeight` is calculated as `weight * 0.8`, and `partialSum` is calculated as `sum * 0.2`. The new approach uses `sum /= partialWeight` to achieve a more nuanced and realistic representation of tool properties. Images provided in the discussion include an old wood hook and a new wood hook, illustrating the changes made. The user also shared calculations and adjustments based on these images to refine the tool property formulas.

## Related Questions
- What is the initial formula proposed for calculating tool values?
- Why was the first implementation of the formula considered too strong?
- How did the user adjust the approach to achieve a better balance?
- What are the key differences between the initial and adjusted formulas?
- How does the new approach impact the usability of partially filled tools?
- Can you explain the role of 'partialWeight' and 'partialSum' in the adjusted formula?

*Source: unknown | chunk_id: github_issue_1833_discussion*
