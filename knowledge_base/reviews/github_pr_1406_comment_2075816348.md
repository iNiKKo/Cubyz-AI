# [src/ecs/components/Model.zig] - PR #1406 review diff

**Type:** review
**Keywords:** server-side ECS, client data requirements, performance optimization, architectural decision, entity-component system
**Symbols:** Model, main.graphics.Texture, Image, ZonElement
**Concepts:** Entity-Component System (ECS), Server-client Architecture, Performance Optimization

## Summary
The review discusses the architectural decision to implement a server-side only ECS, considering the client's limited data requirements and reduced update needs.

## Explanation
The reviewer suggests starting with a server-side only ECS because the client does not need most of the data and requires fewer updates. This approach is intended to optimize performance by avoiding unnecessary ECS overhead on the client side. The review highlights the importance of aligning system architecture with actual usage patterns to prevent potential performance issues.

## Related Questions
- What are the primary reasons for choosing a server-side only ECS?
- How does the client's limited data impact the need for an ECS?
- What potential performance issues could arise from using an ECS on the client side?
- How might the current implementation of Model.zig be affected by this architectural decision?
- What are the benefits of optimizing ECS usage based on actual data needs?
- How does this review align with broader system design goals for Cubyz?

*Source: unknown | chunk_id: github_pr_1406_comment_2075816348*
