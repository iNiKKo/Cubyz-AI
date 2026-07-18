# [issues/issue_2177.md] - Issue #2177 discussion

**Type:** review
**Keywords:** structure generation, multiple structure maps, power of two, chunk size, cave maps, storage requirements, computational cost
**Symbols:** structure map, biome, stalagmite, crater
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue proposes creating multiple structure maps based on structure sizes instead of a single fixed-size map.

## Explanation
The current system generates structures within chunks and adjacent chunks, which becomes computationally expensive for larger structures. The proposed change involves creating multiple structure maps of varying sizes to accommodate different structure dimensions. However, this approach introduces challenges such as increased storage requirements for cave maps and higher computational costs for generating these maps.

## Related Questions
- What is the current time complexity of generating structures in chunks?
- How does the proposed system handle structures larger than 32x32x32?
- What are the storage requirements for cave maps in the proposed system?
- How does the proposed system impact memory usage?
- What alternative solutions have been considered to address the computational cost issue?
- How does the current structure generation system determine where structures need to generate?

*Source: unknown | chunk_id: github_issue_2177_discussion*
