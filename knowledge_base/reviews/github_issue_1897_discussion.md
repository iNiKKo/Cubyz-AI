# [issues/issue_1897.md] - Issue #1897 discussion

**Type:** review
**Keywords:** world edit, missing chunks, generate unsaved chunks, manipulate saved chunks, chunk sizes, consistent chunk sizes, block index calculation, compressed chunks, decompression, server configuration, interaction range
**Symbols:** World Edit, chunks, unsaved chunks, saved chunks
**Concepts:** world editing, chunk management, data compression

## Summary
Discussion on handling missing chunks during world edit operations, focusing on generating unsaved chunks on demand and manipulating saved chunks without fully loading them.

## Explanation
The issue revolves around improving the World Edit (WE) functionality to handle scenarios where chunks are not loaded. The main points of discussion include generating unsaved chunks on demand for reading, changing, and saving during modifying operations, as well as manipulating saved chunks by directly accessing their data without fully loading them. The maintainer notes that chunks are compressed for storage, requiring proper decompression and loading to access their data. There is also a suggestion to limit the interaction range based on server configuration rather than relying on the number of loaded chunks.

## Related Questions
- How can unsaved chunks be generated on demand during world edit operations?
- What is the process for manipulating saved chunks without fully loading them?
- How does chunk compression affect the ability to directly access chunk data?
- What are the potential performance implications of generating and manipulating chunks on demand?
- How can the interaction range for world editing be limited by server configuration?
- Are there any memory considerations when handling unsaved and saved chunks during world edit?

*Source: unknown | chunk_id: github_issue_1897_discussion*
