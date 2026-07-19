# [issues/issue_1897.md] - Issue #1897 discussion

**Type:** review
**Keywords:** world edit, missing chunks, generate unsaved chunks, manipulate saved chunks, chunk sizes, consistent chunk sizes, block index calculation, compressed chunks, decompression, server configuration, interaction range
**Symbols:** World Edit, chunks, unsaved chunks, saved chunks
**Concepts:** world editing, chunk management, data compression

## Summary
Discussion on handling missing chunks during world edit operations, focusing on generating unsaved chunks on demand and manipulating saved chunks without fully loading them.

## Explanation
Discussion on handling missing chunks during world edit operations, focusing on generating unsaved chunks on demand for reading, changing, and saving during modifying operations. The maintainer notes that chunks are compressed for storage, requiring proper decompression and loading to access their data before manipulation can occur. There is also a suggestion to limit the interaction range based on server configuration instead of relying on the number of loaded chunks. Additionally, it is mentioned that if chunk sizes in file are consistent (e.g., we can determine the position of a block with simple multiplication), this should be doable by just calculating the desired index and manipulating it.

## Related Questions
- How does chunk compression affect the ability to directly access chunk data?
- What are the potential performance implications of generating and manipulating chunks on demand?

*Source: unknown | chunk_id: github_issue_1897_discussion*
