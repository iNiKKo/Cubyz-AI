# [easy/codebase_assets_cubyz_tools_axe.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** configurations, tool settings, damage modifiers, durability adjustments, swing speed changes
**Symbols:** disabled, optional, parameters
**Concepts:** configuration data, tool properties

## Summary
Configuration data for the axe tool in Cubyz

## Explanation
This chunk defines configuration settings for the axe tool in Cubyz. It includes detailed disabled and optional states, along with parameters that modify its damage, durability, and swing speed based on various sources. Specifically, it covers the following configurations:

- **Disabled States:**
  ```
  .{
    0, 0, 1, 1, 1,
    0, 0, 0, 1, 1,
    0, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 0
  }
  ```
- **Optional States:**
  ```
  .{
    1, 1, 0, 0, 0,
    1, 1, 1, 0, 0,
    0, 1, 1, 1, 0,
    0, 0, 1, 1, 0,
    0, 0, 0, 0, 0
  }
  ```
- **Damage Parameters:**
  - Mass Damage to Damage:
    ```
    .{
      source = .massDamage,
      destination = .damage,
      matrix = .{
        1.5, 2.0, 0x0, 0x0, 0x0,
        2.0, 2.0, 1.5, 0x0, 0x0,
        2.0, 1.5, 1.0, 0.5, 0x0,
        0x0, 1.0, 0.5, 0.1, 0x0,
        0x0, 0x0, 0x0, 0x0, 0.1
      },
      factor = 0.08,
      method = .sum
    }
    ```
    - Average Mass Damage to Damage:
      ```
      .{
        source = .massDamage,
        destination = .damage,
        matrix = .{
          1.5, 2.0, 0x0, 0x0, 0x0,
          2.0, 2.0, 1.5, 0x0, 0x0,
          2.0, 1.5, 1.0, 0.5, 0x0,
          0x0, 1.0, 0.5, 0.1, 0x0,
          0x0, 0x0, 0x0, 0x0, 0.1
        },
        factor = 0.32,
        method = .average
      }
      ```
    - Hardness Damage to Damage:
      ```
      .{
        source = .hardnessDamage,
        destination = .damage,
        matrix = .{
          0.0, 0.0, 0x0, 0x0, 0x0,
          0.1, 0.0, 0.0, 0x0, 0x0,
          1.0, 0.1, 0.0, 0.0, 0x0,
          0x0, 1.0, 0.1, 0.0, 0x0,
          0x0, 0x0, 0x0, 0x0, 0.0
        },
        factor = 0.3,
        method = .average
      }
      ```
- **Durability Parameters:**
  - Durability to Max Durability:
    ```
    .{
      source = .durability,
      destination = .maxDurability,
      matrix = .{
        0.1, 0.5, 0x0, 0x0, 0x0,
        1.0, 1.5, 0.5, 0x0, 0x0,
        2.0, 2.0, 2.5, 0.5, 0x0,
        0x0, 2.0, 1.5, 1.0, 0x0,
        0x0, 0x0, 0x0, 0x0, 1.0
      },
      factor = 0.05,
      method = .sum
    }
    ```
    - Average Durability to Max Durability:
      ```
      .{
        source = .durability,
        destination = .maxDurability,
        matrix = .{
          0.1, 0.5, 0x0, 0x0, 0x0,
          1.0, 1.5, 0.5, 0x0, 0x0,
          2.0, 2.0, 2.5, 0.5, 0x0,
          0x0, 2.0, 1.5, 1.0, 0x0,
          0x0, 0x0, 0x0, 0x0, 1.0
        },
        factor = 0.2,
        method = .average
      }
      ```
- **Swing Speed Parameters:**
  - Swing Speed to Swing Speed:
    ```
    .{
      source = .swingSpeed,
      destination = .swingSpeed,
      matrix = .{
        0.1, 0.5, 0x0, 0x0, 0x0,
        0.5, 1.0, 0.5, 0x0, 0x0,
        2.0, 2.5, 1.5, 0.5, 0x0,
        0x0, 2.0, 0.5, 0.5, 0x0,
        0x0, 0x0, 0x0, 0x0, 0.5
      },
      factor = -0.2,
      method = .sum
    }
    ```
    - Average Swing Speed to Swing Speed:
      ```
      .{
        source = .swingSpeed,
        destination = .swingSpeed,
        matrix = .{
          0.1, 0.5, 0x0, 0x0, 0x0,
          0.5, 1.0, 0.5, 0x0, 0x0,
          2.0, 2.5, 1.5, 0.5, 0x0,
          0x0, 2.0, 0.5, 0.5, 0x0,
          0x0, 0x0, 0x0, 0x0, 0.5
        },
        factor = 1.2,
        method = .average
      }
      ```

## Related Questions
- What are the disabled states of the axe tool?
- How many optional states does the axe tool have?
- What parameters modify the damage of the axe tool based on mass and hardness?
- What is the factor used to calculate average damage from mass and hardness?
- Which method is used to calculate average damage from mass and hardness?
- What are the source and destination properties for the durability parameter?
- What is the factor used to calculate sum of durability changes?
- What is the method used to calculate sum of durability changes?
- What are the source and destination properties for the swing speed parameter?
- What is the factor used to calculate average swing speed changes?
- Which method is used to calculate average swing speed changes?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_axe.zig.zon_chunk_0*
