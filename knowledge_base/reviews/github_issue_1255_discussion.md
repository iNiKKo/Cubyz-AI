# [issues/issue_1255.md] - Issue #1255 discussion

**Type:** review
**Keywords:** model_pile, texture_pile, states, directions, bits, pile, mushrooms
**Symbols:** model_pile, texture_pile
**Concepts:** state management, feature design

## Summary
Discussion on adding a `model_pile` feature equivalent to `texture_pile`, exploring different state configurations for models.

## Explanation
Discussion on adding a `model_pile` feature equivalent to `texture_pile`, exploring different state configurations for models. The proposal includes several specific options:

1. Allow all 6 directions with 3 states each (and 1 empty state) using `6x2 bits`
2. Allow 5 directions (without placing on the bottom of a different block) with 7 states (and 1 empty state) using `5x3 bits`
3. Allow placing in only one direction at once with up to 16 states in that direction using `4+6 bits`
4. Allow placing either +X-X+Y-Y or +Z-Z with up to 8 states, using `4x3+1 bits` (horizontal), `2x3+1 bits` (vertical)

The maintainer suggests merging the concept into a single `pile` feature and provides an example use case involving ile mushrooms.

## Related Questions
- What are the different state configurations proposed for `model_pile`?
- How many bits are used in each configuration option?
- Why was the concept of merging into a single `pile` feature suggested?
- Can you provide an example use case for the `model_pile` feature?

*Source: unknown | chunk_id: github_issue_1255_discussion*
