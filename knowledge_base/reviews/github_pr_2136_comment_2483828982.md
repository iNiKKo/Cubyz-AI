# [src/gui/windows/save_creation.zig] - PR #2136 review diff

**Type:** review
**Keywords:** world seed, random integer, time-based seed, seed generation code, architectural review, security concerns, predictable seeds
**Symbols:** getWorldSeed, testingModeCallback
**Concepts:** seed generation, randomness, security, predictability

## Summary
A new function `getWorldSeed` is introduced to generate a world seed using a random integer if the input string is empty. The reviewer suggests using existing code for seed generation instead, citing concerns about the current method's reliance on time, which limits the search space for reconstructing a seed.

## Explanation
The introduction of `getWorldSeed` aims to handle cases where no seed is provided by generating a random one. However, the reviewer points out that the existing code for seed generation should be reused instead. The current method's reliance on time makes it easier to predict and reconstruct seeds, which could pose security risks or make world generation less random. The reviewer emphasizes the importance of using a more secure and unpredictable method for seed generation.

## Related Questions
- What is the purpose of the `getWorldSeed` function?
- Why does the reviewer suggest using existing seed generation code?
- How does the current method of seed generation rely on time?
- What are the potential security implications of predictable seeds?
- How can the seed generation be made more secure and unpredictable?
- What is the impact of using a random integer for seed generation when no input is provided?

*Source: unknown | chunk_id: github_pr_2136_comment_2483828982*
