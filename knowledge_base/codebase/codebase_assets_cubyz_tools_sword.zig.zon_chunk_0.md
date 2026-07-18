# [easy/codebase_assets_cubyz_tools_sword.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** config data, sword tool, effect parameters, matrix coefficients, factor, method
**Symbols:** swordToolEffects
**Concepts:** configuration, tool effects, damage modification, swing speed adjustment

## Summary
Configuration data for sword tool effects

## Explanation
This chunk defines configuration data for sword tool effects, including parameters that modify the damage and swing speed of a sword based on its mass, hardness, durability, and swing speed. The data is structured as an array of effect configurations, each specifying a source attribute, destination attribute, matrix coefficients, factor, and method.

- **Effect Configuration 1:**
  - Source: `massDamage`
  - Destination: `damage`
  - Matrix Coefficients:
    ```
    3.0, 2.5, 2.0, 0x0, 0x0,
    2.5, 0.5, 1.0, 1.5, 0.1,
    2.0, 1.0, 0.1, 0.1, 0.1,
    0x0, 1.5, 0.1, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `0.4`
  - Method: `.sum`
- **Effect Configuration 2:**
  - Source: `massDamage`
  - Destination: `damage`
  - Matrix Coefficients:
    ```
    3.0, 2.5, 2.5, 0x0, 0x0,
    2.5, 0.5, 1.0, 2.0, 0.1,
    2.5, 1.0, 0.1, 0.1, 0.1,
    0x0, 2.0, 0.1, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `0.6`
  - Method: `.average`
- **Effect Configuration 3:**
  - Source: `hardnessDamage`
  - Destination: `damage`
  - Matrix Coefficients:
    ```
    3.0, 2.5, 2.0, 0x0, 0x0,
    2.5, 0.5, 1.0, 1.5, 0.1,
    2.0, 1.0, 0.1, 0.1, 0.1,
    0x0, 1.5, 0.1, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `1.0`
  - Method: `.average`
- **Effect Configuration 4:**
  - Source: `durability`
  - Destination: `maxDurability`
  - Matrix Coefficients:
    ```
    0.5, 1.0, 1.0, 0x0, 0x0,
    1.0, 2.5, 1.0, 1.0, 0.1,
    1.0, 1.0, 1.5, 0.5, 0.1,
    0x0, 1.0, 0.5, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `0.2`
  - Method: `.sum`
- **Effect Configuration 5:**
  - Source: `durability`
  - Destination: `maxDurability`
  - Matrix Coefficients:
    ```
    0.5, 1.0, 1.0, 0x0, 0x0,
    1.0, 2.5, 1.0, 1.0, 0.1,
    1.0, 1.0, 1.5, 0.5, 0.1,
    0x0, 1.0, 0.5, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `0.8`
  - Method: `.average`
- **Effect Configuration 6:**
  - Source: `swingSpeed`
  - Destination: `swingSpeed`
  - Matrix Coefficients:
    ```
    3.0, 2.5, 2.5, 0x0, 0x0,
    2.5, 0.5, 1.0, 2.0, 0.1,
    2.5, 1.0, 0.2, 0.5, 0.1,
    0x0, 2.0, 0.5, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `-0.5`
  - Method: `.sum`
- **Effect Configuration 7:**
  - Source: `swingSpeed`
  - Destination: `swingSpeed`
  - Matrix Coefficients:
    ```
    3.0, 2.5, 2.5, 0x0, 0x0,
    2.5, 0.5, 1.0, 2.0, 0.1,
    2.5, 1.0, 0.2, 0.5, 0.1,
    0x0, 2.0, 0.5, 0.1, 0x0,
    0x0, 0.1, 0.1, 0x0, 0.1
    ```
  - Factor: `0.6`
  - Method: `.average`

## Related Questions
- What are the source and destination attributes for each effect configuration?
- How many different methods are used to calculate the factor values?
- What is the maximum number of matrix coefficients in any effect configuration?
- Which attribute is modified by the first effect configuration?
- What is the factor value for the second effect configuration?
- How many effect configurations are there in total?
- What is the destination attribute for the third effect configuration?
- Which method is used to calculate the factor values for the fourth effect configuration?
- What is the maximum number of matrix coefficients in the fifth effect configuration?
- Which source attribute is modified by the sixth effect configuration?
- What is the factor value for the seventh effect configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_sword.zig.zon_chunk_0*
