# [issues/issue_2461.md] - Issue #2461 discussion

**Type:** review
**Keywords:** block replacements, randomized substitutions, probabilities, palette, tagged unions, alias table, zig.zon, world generation, efficiency, flexibility
**Symbols:** Sbb, block replacements, palette, tagged unions, alias table, substitute, zig.zon
**Concepts:** randomization, world generation, efficiency, flexibility

## Summary
The issue proposes extending block replacement functionality to allow randomized substitutions with specified probabilities, enhancing flexibility and efficiency in world generation.

## Explanation
The current method for block replacements is described as tedious and inefficient. The proposed solution involves using a palette filled with tagged unions at runtime, where each entry can either be a single block or an alias table with associated probabilities. This approach aims to simplify the process by reducing the need for multiple branches during execution. The maintainer notes that this request extends issue #1412, which currently supports fixed replacements but lacks the ability to handle randomized substitutions. The proposed syntax in the `zig.zon` file demonstrates how block substitutions could be defined with probabilities, and the engine would store these as a list of tagged unions for efficient sampling.

## Related Questions
- How does the current block replacement mechanism work in Cubyz?
- What is the proposed change to support randomized substitutions?
- Can you explain how the tagged unions and alias tables will be used at runtime?
- How does this proposal extend the functionality of issue #1412?
- What are the potential performance implications of using tagged unions for block replacements?
- How will the new substitution palette be stored in the engine?
- Can you provide an example of how to define randomized substitutions in the `zig.zon` file?
- What is the maintainer's understanding of the relationship between this issue and #1412?
- How does the proposed change affect world generation in Cubyz?
- Are there any backward compatibility concerns with this new feature?

*Source: unknown | chunk_id: github_issue_2461_discussion*
