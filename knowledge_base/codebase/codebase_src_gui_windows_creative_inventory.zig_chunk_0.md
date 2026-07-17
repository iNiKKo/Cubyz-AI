# [medium/codebase_src_gui_windows_creative_inventory.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, HorizontalList, TextInput, ItemSlot, search filter, tag matching, cursor preservation, content initialization, deinitialization
**Symbols:** Item, ClientInventory, Player, Vec2f, GuiComponent, GuiWindow, TextInput, Label, HorizontalList, VerticalList, ItemSlot, window, padding, slotsPerRow, items, inventory, searchInput, searchString, lessThan, onOpen, onClose, hasMatchingTag, initContent, deinitContent, update, filter
**Concepts:** creative inventory GUI, search filtering, item slot rendering, tag-based search, cursor preservation, vertical list layout, horizontal row grouping, content initialization, deinitialization cleanup

## Summary
Implements the Creative Inventory GUI window with a vertical list of item slots and an integrated search filter that updates content on user input.

## Explanation
This chunk defines a GuiWindow for the creative inventory, declaring padding (8), slotsPerRow (10), and global variables items (ListManaged(Item)), inventory (ClientInventory), searchInput (*TextInput), and searchString ([]const u8). It exposes onOpen() which clears searchString and calls initContent(), and onClose() which deinitContent() and frees searchString. The core logic is in initContent(): it builds a root VerticalList, then adds a secondary list containing a HorizontalList with a Label ('Search:') and the TextInput (searchInput) configured with an onNewline callback to filter(). It initializes items via main.items.iterator(), applying filtering: if searchString starts with '.' it treats the remainder as a tag name and uses hasMatchingTag() against item.tags() or block tags; otherwise it filters by substring match using std.mem.containsAtLeast. After filtering, it sorts items with lessThan() which orders baseItem folders then id case-insensitively. It computes slotCount (rounding up to slotsPerRow), creates a ClientInventory of type .creative/.other, populates inventory.super._items with amount 1 for each filtered item, and builds HorizontalList rows of ItemSlot entries—using .default/.takeOnly for items that exist and .immutable/.immutable for empty slots. It finishes the lists, assigns root to window.rootComponent, adjusts window.contentSize based on component positions plus padding, and calls gui.updateWindowPositions(). deinitContent() cleans up the component tree, items.deinit(), and inventory.deinit(). update() checks if searchInput.currentString differs from searchString; if so it calls filter(). filter() saves selectionStart/cursor, frees old searchString, duplicates currentString into searchString, re-runs initContent(), then restores cursor/selection. hasMatchingTag iterates tags and uses std.mem.containsAtLeast to detect substring presence.

## Related Questions
- What is the default padding value used for the creative inventory window layout?
- How does initContent() handle a search string that starts with a dot character?
- Which function is called when the user presses Enter in the search input field?
- What happens to the cursor and selection range after filtering updates the content?
- How are empty item slots represented in the inventory UI structure?
- Does update() perform any action if the current search string matches searchString?
- Which global allocator is used for freeing the search string on close?

*Source: unknown | chunk_id: codebase_src_gui_windows_creative_inventory.zig_chunk_0*
