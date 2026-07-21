# Cubyz Addon Creator Knowledge Base

## [easy/addon_creator_items.html] - Chunk 0

**Type:** documentation

**Summary:** The provided HTML code snippet is a form for creating and editing an item in a game development project. It includes fields for the item's name, description, durability, swing speed, texture roughness, mass damage, hardness damage, material color, and various modifiers such as durability, fragility, heaviness, lightness, power, and weakness. The form also allows users to select an item sprite texture from a dropdown list or upload their own custom PNG file. Additionally, there's a button to save the item details to the project.

**Explanation:**
This HTML code snippet is designed for creating and editing items in a game development project. It includes several input fields for various properties of an item such as its name, description, durability, swing speed, texture roughness, mass damage, hardness damage, material color, and modifiers like durability, fragility, heaviness, lightness, power, and weakness. The form also provides options to select or upload a custom PNG file for the item's sprite texture. Additionally, there is a button that allows users to save the item details to the project.

**Symbols:** <div>, </div>, <h3>, </h3>, <label>, </label>, <input>, </input>, <button>, </button>, <img>, </img>

**Concepts:** HTML, Form Elements, Input Fields, Dropdown Lists, File Upload, JavaScript Functions, Game Development Project

**Keywords:** item creation form, game development project, input fields, dropdown lists, file upload, javascript functions, game development

**Related Questions:**
- What are the input fields in this form?
- How can I add a custom PNG file for the item's sprite texture?
- What is the purpose of the 'Save Item to Project' button?
- Can you explain how the dropdown lists work in this form?
- What are the different modifiers available in this form?
- How does the file upload feature work in this form?

*Contributed by: babab*


---
## [easy/addon_creator_entities.html] - Chunk 0

**Type:** ui

**Summary:** UI component for creating and configuring entity blueprints in the Cubyz Addon Creator workspace.

**Explanation:**
This UI component is responsible for allowing users to create and configure entity blueprints in the Cubyz Addon Creator. It includes fields for specifying the entity's ID, height, coordinate system, model, texture, and tags. The component also provides dropdowns for selecting models and textures, as well as buttons for adding custom GLB and PNG files. Additionally, it includes a save button to upload the entity blueprint to the project.

**Symbols:** panel, form-group, col, label, input, hidden, text, number, span, dropdown-options, dropdown-option, file-input-label, recipe-dropdown, filter-dropdown, handleCustomEntityModel, handleCustomEntityTexture, addDynamicTagPill

**Concepts:** data-binding, form validation, live preview

**Keywords:** entity creator, blueprint creation, model selection, texture upload, tag management

**Code Example:**
```zig
<input type="text" id="entityId" placeholder="snale" autocomplete="off" oninput="this.value = this.value.toLowerCase().replace(/[^a-z0-9_]/g, '')">
```

**Related Questions:**
- What is the purpose of the 'Entity ID' field?
- How does the 'Height' input control work?
- Can you explain how the coordinate system dropdown works?
- What are the options available in the model dropdown?
- How can I add a custom GLB file for the entity?
- What is the purpose of the texture upload feature?
- How do I add a custom PNG file for the entity?
- Can you explain how the tag management section works?
- What are some quick tags available to add?
- How does the save button work in this UI component?
- What is the role of the hint text and field explanation elements?
- How can I customize the appearance or behavior of the entity creator UI?

*Contributed by: babab*


---
## [hard/addon_creator_app-studio.js] - Chunk 1

**Type:** ui

**Summary:** This chunk defines the core panel-loading logic for the Cubyz Addon Studio, handling navigation between blocks/items/recipes/etc., fetching HTML templates, rebuilding dropdowns, and initializing dynamic tag systems.

**Explanation:**
UI Controls: nav-btn buttons (active state), customConfirmModal dialog with OK/Cancel, dynamicWorkspace container for injected HTML. Event Handlers: loadStudioPanel triggers fetch of panelName.html, rebuildDropdowns on blocks/items/entities/particles panels, markFormAsDirty on any input/change except ID fields, initDynamicTagSystem calls for blockTagsContainer/itemTagsContainer/entityTagsContainer. Validation: showCustomConfirm returns Promise resolving true/false; handleSimpleInteractChange/handleSimpleEnvChange map user-select values to raw inputs and toggle visibility of advanced sub-forms (advInteractWindowWrapper/simpleDecaySettings). Defaults: decayReplacement defaults to 'cubyz:air' when updateType is 'decay'; decayPrevention defaults to '.log, .branch'. Templates: dynamicWorkspace.innerHTML replaced by fetched HTML; dropdowns regenerated via rebuildDropdowns. Bindings: Object.assign sets hasUnsavedChanges=false, currentPanelName=panelName, editingId=targetIdToEdit; funcMap maps panelName to populate*FormValues functions. Engine Mappings: none explicit here—pure DOM manipulation and fetch. Configuration Generation: none in this chunk.

**Symbols:** loadStudioPanel, showCustomConfirm, handleSimpleInteractChange, handleSimpleEnvChange, addDynamicTagPill, removeDynamicTagPill, updateTagSuggestionVisibility, initDynamicTagSystem

**Concepts:** panel navigation, template loading, dynamic tag pills, form dirty tracking, modal confirmation, dropdown rebuilding, event delegation on inputs

**Keywords:** studio panel, nav buttons, fetch template, tag pill system, dirty flag, custom confirm modal, dropdown rebuild, input change handler, decay settings toggle, populate form values

**Related Questions:**
- What happens when a user clicks a nav-btn for the 'blocks' panel while unsaved changes exist?
- How does loadStudioPanel prevent duplicate dropdown generation after fetching a new panel template?
- Which DOM elements are excluded from triggering markFormAsDirty on input/change events, and why?
- In handleSimpleEnvChange, what rawUpdate value is assigned when the user selects 'support' for decay type?
- How does addDynamicTagPill ensure that duplicate tag pills are not added to a container?
- What is the purpose of updateTagSuggestionVisibility after removing or adding a dynamic tag pill?
- When loadStudioPanel receives a targetIdToEdit, how are existing form values populated into the newly loaded template?
- Which panels trigger rebuildDropdowns automatically after their HTML is injected into dynamicWorkspace?
- What default replacement string is set for decayReplacement when updateType equals 'decay'?
- How does showCustomConfirm handle the case where its modal element (#customConfirmModal) is missing from the DOM?

*Contributed by: Caleb*


---
## [hard/addon_creator_app-studio.js] - Chunk 3

**Type:** ui

**Summary:** This module contains utility functions to populate form inputs with data from project definitions (biomes, entities, particles) and load preset configurations for blocks, items, and recipes.

**Explanation:**
The chunk defines several window-scoped functions: populateBiomeFormValues populates a biome configuration form by finding the matching biome in projectData.biomes and setting various input fields including ID, chance, interpolation, radius limits, height limits, roughness, hills, mountains, soil creep, terrain preservation, surface/sub/stone blocks, caves, crystals, music, fog density, beach smoothing, cave spawning, sky/fog colors, climate/humidity/zone/growth/elevation radio buttons, and dynamically rendering structures. populateEntityFormValues fills entity form fields (ID, height, coordinate system, model search, texture search) and initializes the dynamic tag system for entity tags. populateParticleFormValues loads particle data into corresponding inputs (ID, texture, emission flag with warning visibility, speed/size/life/density ranges, rotation velocity, drag, spawn shape, direction mode, directional components, random rotate, collision), toggles shape-specific fields (radius vs size) and direction-specific fields based on the loaded values. toggleParticleShapeFields dynamically builds and shows/hides a wrapper containing either a sphere radius input or cube bounds vector input depending on the particle shape. loadBlockPreset loads predefined block configurations (log, leaves, ore, stone, dirt) into form inputs for health, resistance, rotation, collision, transparency, texture searches for top/front/left/right/up/bottom faces, item icon search, handles rotation change, initializes dynamic tag system for block tags, toggles drop input, marks form as dirty, and schedules a preview update. loadItemPreset loads predefined item configurations (amber, ruby, iron) into inputs for ID, stack size, texture search, material properties (durability, swing speed, roughness, mass damage, hardness damage), modifier strength, base color, modifier type dropdown/search, and initializes dynamic tag system for item tags. loadRecipePreset handles recipe preset loading by setting filename, input/output searches and counts based on the key ('planks' or 'workbench').

**Symbols:** populateBiomeFormValues, populateEntityFormValues, populateParticleFormValues, toggleParticleShapeFields, loadBlockPreset, loadItemPreset, loadRecipePreset

**Concepts:** data-binding, form-population, preset-loading, dynamic-tag-system, conditional-field-toggling, UI-state-management

**Keywords:** biome-form, entity-form, particle-form, block-preset, item-preset, recipe-preset, dynamic-tags, form-population, preset-loading, conditional-fields

**Related Questions:**
- What happens when populateBiomeFormValues is called with a biome ID that does not exist in projectData.biomes?
- How are the climate and humidity radio buttons populated in the biome form?
- Which fields are conditionally shown or hidden based on particle shape in toggleParticleShapeFields?
- What preset keys are supported by loadBlockPreset and what data do they contain?
- How does loadItemPreset handle modifier types, and where is that information displayed to the user?
- In populateEntityFormValues, how is the coordinate system input initialized if not provided in the entity definition?
- What triggers window.markFormAsDirty when loading a block preset?
- Does populateParticleFormValues initialize any default values for missing particle properties?
- How does loadRecipePreset differentiate between 'planks' and 'workbench' presets in terms of input/output configuration?
- Are there any event handlers attached to the inputs populated by these functions, or are they purely static assignments?

*Contributed by: Caleb*


---
## [hard/addon_creator_app-studio.js] - Chunk 4

**Type:** ui

**Summary:** This module defines the core UI event handlers for the Addon Studio blueprint editor, including functions to populate form fields from preset data (item presets, recipe presets, biome presets), update texture previews based on user input, and handle custom entity/block textures uploaded via file inputs.

**Explanation:**
The chunk exports several window-level functions that bind UI controls to data models. loadRecipePreset populates the crafting recipe form fields with predefined values for 'planks' or 'workbench', clearing other input slots. loadBiomePreset clears the biome structures container and sets biome ID, height ranges, surface/sub/stone blocks, and adds structure rows based on the key ('mountain' or 'cave'). updateBlockFacePreviews reads text inputs (topSearch, frontSearch, etc.), maps them to texture data URLs from window.serverTextures or fallbacks, and updates preview images accordingly; it also handles thumbnail generation for various texture search fields. handleCustomEntityModel processes a file upload for custom entity models: it extracts the addon name and filename, constructs an identifier like 'my_addon:name', stores the file in window.customEntityModels, and sets the corresponding search input value. handleCustomEntityTexture performs similar logic for textures: it reads the uploaded file as a data URL, prepends a texture object to window.serverTextures with metadata (isCustom:true, isEntityType:true), updates the search input, and triggers updateBlockFacePreviews. handleCustomBlockTexture begins analogous handling for block textures.

**Symbols:** loadRecipePreset, loadBiomePreset, updateBlockFacePreviews, handleCustomEntityModel, handleCustomEntityTexture, handleCustomBlockTexture

**Concepts:** preset loading, texture preview generation, custom asset upload handling, form state management, data binding to UI inputs, addon identifier construction

**Keywords:** recipe preset, biome preset, texture preview, custom entity model, custom texture upload, form dirty flag, serverTextures registry, file input handler, addon identifier, thumbnail generation

**Related Questions:**
- What happens when loadRecipePreset is called with the key 'planks'?
- How does updateBlockFacePreviews determine which texture to display for a given face?
- Where are custom entity model files stored after upload via handleCustomEntityModel?
- Does loadBiomePreset clear existing biome structures before adding new ones?
- What metadata is attached to textures added by handleCustomEntityTexture?
- How does the code construct an addon identifier from a filename and addon name?
- Which UI elements are affected when updateBlockFacePreviews runs?
- Is there any validation on texture filenames before they are registered?
- What fallback is used if no matching texture is found in serverTextures?
- How does the form get marked as dirty after preset loading or custom uploads?

*Contributed by: Caleb*


---
## [hard/addon_creator_app-studio.js] - Chunk 6

**Type:** ui

**Summary:** This module handles the dynamic generation of UI forms for various Cubyz addon types (e.g., vegetation, boulders) and provides reusable dropdown logic with filtering and clear-button management.

**Explanation:**
UI Controls: createInputHTML / createNormalInputHTML generate form fields bound to data properties; showRecipeDropdown populates a select from projectData.blocks/items or serverTextures; filterDropdown filters options by text. Event Handlers: input listeners call markFormAsDirty (guarded by isInitializingPanel); mouseup triggers updateBlockFacePreviews and initDropdownClearButtons; mousedown outside texture-select-wrapper hides open dropdowns. Validation/Defaults: defaults are passed as third arguments to create*HTML functions (e.g., '6' for height). Templates: none explicitly defined here, but HTML strings are injected via innerHTML. Bindings: data?.log → field-log with default 'cubyz:oak_log'; data?.block → field-block; etc. Engine Mappings: Cubyz block IDs (cubyz:oak_log, cubyz:fern) map to UI inputs. Configuration Generation: showRecipeDropdown builds a pool of selectable items and renders them as clickable divs inside the dropdown container.

**Symbols:** createInputHTML, createNormalInputHTML, showRecipeDropdown, filterDropdown, initDropdownClearButtons, updateClearButtonVisibility, markFormAsDirty, updateBlockFacePreviews

**Concepts:** dynamic form generation, dropdown filtering, clear-button visibility toggle, data binding to Cubyz block IDs, event-driven UI updates

**Keywords:** dropdown, filtering, form-generation, Cubyz-blocks, texture-select, clear-button, mark-dirty, project-data, server-textures, input-handling

**Related Questions:**
- What happens when a user types into a texture-select input field?
- How are custom project blocks added to the dropdown options?
- Which Cubyz block IDs are used as defaults for vegetation addons?
- Why is markFormAsDirty guarded by window.isInitializingPanel?
- What triggers updateBlockFacePreviews and when does it run?
- How does filterDropdown handle case-insensitive search queries?
- Where are the clear-input-btn elements inserted in the DOM?
- Can a user select a vanilla texture from serverTextures via this dropdown?
- What prevents multiple dropdowns from staying open simultaneously?
- Are any validation rules enforced on numeric inputs like height or width?

*Contributed by: Caleb*


---
## [hard/addon_creator_app-studio.js] - Chunk 5

**Type:** ui

**Summary:** This chunk defines the core UI logic for adding and configuring biome structure rows, including dynamic sub-field toggling based on selected feature type.

**Explanation:**
The code implements window.addStructureRow to create a new row in #biomeStructuresContainer with a hidden value input, a searchable dropdown (triggered on focus), spawn chance number field, and a remove button. It populates displayLabels for types like cubyz:simple_tree, cubyz:simple_vegetation, etc., and renders them as clickable options inside an absolute-positioned dropdown div. When a user selects an option via mousedown, it updates the hidden value input, the search text input, calls window.toggleStructSubFields with the rowId and selected type, and hides the dropdown. The toggleStructSubFields function clears any existing sub-fields in .struct-subfields-wrapper and conditionally injects HTML for each supported type: simple_tree adds Log Block (dropdown), Leaves Block (dropdown), Base Trunk Height, Height Variance, Crown Size; simple_vegetation adds Foliage Sprite Block (dropdown) and Sprite Max Height; flower_patch adds Foliage/Flower Block (dropdown), Patch Width Scale, Patch Variance, Patch Density; boulder adds Stone Block Variant (dropdown), Base Radius Size, Size Variance Step; ground_patch adds Replacement Block (dropdown), Patch Width, Patch Depth layers, Edge Smoothness; fallen_tree adds Log Block Type (dropdown), Log Length size, Length Variance; sbb adds SBB Asset path ID and Place Mode flag. Each dropdown input has onfocus="window.showRecipeDropdown(...)" to open a recipe list and oninput="window.filterDropdown(...)" to filter as the user types. Normal inputs have placeholder text and are bound via createNormalInputHTML. After injecting HTML, it attaches an 'input' event listener to all newly created inputs that calls window.markFormAsDirty() unless window.isInitializingPanel is true. The chunk also includes partial implementation of initDropdownClearButtons which iterates over .texture-select-wrapper elements, finds the text input, and if not readonly creates a clear button wrapper (code truncated).

**Symbols:** window.addStructureRow, window.toggleStructSubFields, window.initDropdownClearButtons, displayLabels, createInputHTML, createNormalInputHTML

**Concepts:** dynamic form generation, type-specific sub-fields, searchable dropdowns with focus trigger, live filtering on input, form dirty state tracking, hidden value binding to visible search, UI event delegation via inline handlers

**Keywords:** structure row, feature type selector, spawn chance, dropdown focus trigger, sub-field injection, filter on input, mark form dirty, readonly search field, hidden value binding, clear button wrapper

**Related Questions:**
- What happens when a user focuses the structure type search input?
- How does toggleStructSubFields determine which inputs to render for a given feature type?
- Which event listeners are attached to newly created sub-field inputs and why?
- Is there any validation on spawn chance values before they are stored?
- What is the purpose of window.markFormAsDirty in this context?
- How does the code handle saving existing data when adding a row with savedData parameter?
- Are dropdown options generated dynamically or hardcoded, and how are they populated?
- What role does initDropdownClearButtons play for texture-select-wrapper elements?
- Does the UI support undoing changes to structure rows before finalizing the addon?
- How are placeholder values chosen when a row is created without savedData?

*Contributed by: Caleb*


---
## [hard/addon_creator_app-save.js] - Chunk 0

**Type:** ui

**Summary:** This module defines the core save logic for both blocks and items within the Cubyz Addon Creator. It gathers values from various form inputs, validates them (e.g., requiring a block ID or texture), constructs detailed data objects with properties like rotation mode, health, callbacks, and material stats, then updates the global `window.projectData` state and triggers UI refresh functions.

**Explanation:**
UI Controls: Multiple text inputs (blockId, topSearch, itemTextureSearch, itemId, matColorBase), checkboxes (dropAuto, hasItemIcon, blockCollide, etc.), select dropdowns (rotationMode, touchType, decayReplacement), and numeric inputs (friction, bounciness). Event Handlers: Functions `saveBlockToProject` and `saveItemToProject` are bound to window-level events; they read DOM values via `document.getElementById`. Validation: Block save requires non-empty blockId and topSearch; ore rotation requires itemIconSearch. Item save requires itemId and texture; base color parsing includes HSL conversion logic. Defaults: Missing numeric fields default to 0 or specific constants (e.g., friction 20, emittedLightColor '#000000'). Templates: None explicitly defined here; data is assembled into objects using spread operators for optional properties like `blockEntity`. Bindings: All inputs are bound directly via DOM queries. Engine Mappings: Data structures align with Cubyz block/item schema (e.g., sides, callbacks, material). Configuration Generation: Produces `window.projectData.blocks` and `window.projectData.items` arrays.

**Symbols:** function showDropdown, function saveBlockToProject, function saveItemToProject, window.dropdownsGenerated, window.rebuildDropdowns, window.filterDropdown, window.projectData.blocks, window.projectData.items, window.editingId, window.hasUnsavedChanges, window.updateSearchableItems, window.updateSidebarProjectTree

**Concepts:** data-binding, form-validation, state-management, object-construction, color-space-conversion

**Keywords:** block-save, item-save, validation, dropdowns, callbacks, material-stats, HSL-conversion, project-data, checkboxes, text-inputs

**Related Questions:**
- What happens if a user saves a block without specifying a Block ID?
- How does the system handle missing textures for procedural world ores?
- Which DOM elements are queried to populate the `sidesData` object in saveBlockToProject?
- What is the default value assigned to `friction` when the input field is empty?
- How does the item save function convert the base color hex string into HSL values?
- Are there any optional properties added conditionally during block or item saving, and what triggers them?
- Which global state flags are reset after a successful save operation?
- What UI refresh functions are called immediately after updating `window.projectData`?
- How does the code ensure that duplicate IDs (e.g., editingId) do not persist in the project data arrays?
- Is there any validation for numeric inputs like `blockHealth` or `matDurability`, and what defaults apply if they are missing?

*Contributed by: Caleb*


---
## [medium/addon_creator_app-core.js] - Chunk 2

**Type:** ui

**Summary:** This module defines the core UI logic for managing project assets (blocks, items, recipes, etc.) in the sidebar tree view and provides dropdown filtering/searching functionality.

**Explanation:**
UI Controls: The code exposes several global functions that manipulate the DOM. window.updateSidebarProjectTree() dynamically renders lists of saved assets into specific sidebar containers identified by IDs like 'sidebarBlocksTree', 'sidebarItemsTree', etc., handling both empty states and populated lists with delete buttons. It also conditionally appends an unsaved changes indicator if the current panel matches the asset type.

Event Handlers: The updateSidebarProjectTree function attaches onclick handlers to individual list items that call window.loadStudioPanel() to load a specific asset into the editor, and calls window.deleteItemFromProject() for removal. Delete buttons also have onmouseover/onmouseout events to toggle their color state.

Validation/Defaults: The delete operation uses window.showCustomConfirm() (an external dependency) to validate user intent before modifying window.projectData arrays or objects. It tracks deleted IDs in window.deletedAddonElements and clears the editingId if a deletion occurs while an item is being edited, setting hasUnsavedChanges to false.

Templates: No explicit HTML templates are defined; instead, innerHTML is used with string interpolation for dynamic content generation (e.g., adding subfolder indicators).

Engine Mappings: The code maps asset categories ('blocks', 'items', 'recipes', etc.) to specific DOM containers and data structures in window.projectData.

Configuration Generation: This chunk does not generate configuration files; it manipulates the runtime state of the application.

**Symbols:** window.deletedAddonElements, window.updateSidebarProjectTree, window.deleteItemFromProject, window.showRecipeDropdown, window.filterDropdown

**Concepts:** sidebar tree rendering, asset deletion with confirmation, dropdown filtering and search, unsaved changes indicator, dynamic DOM manipulation

**Keywords:** projectData, deleteItemFromProject, updateSidebarProjectTree, filterDropdown, showRecipeDropdown, loadStudioPanel, unsavedChanges, sidebarTree, dropdown-options, asset management

**Related Questions:**
- What happens to the editingId when an asset is deleted while it is currently being edited?
- How does the updateSidebarProjectTree function handle empty project data lists versus populated ones?
- Which DOM element IDs are targeted by the updateSidebarProjectTree function for rendering different asset categories?
- Does the deleteItemFromProject function modify window.projectData directly, and how does it track deleted items?
- What is the purpose of the showCustomConfirm call within the deleteItemFromProject function?
- How does the filterDropdown function determine which dropdown options to display based on user input?
- In what way does the code handle unsaved changes when an asset is deleted from the project data?
- Are there any specific event handlers attached to the delete buttons in the sidebar tree rows, and how do they behave on hover?
- What logic is used to construct the validationItems array inside showRecipeDropdown for different filter types like blocks or textures?
- How does the code ensure that deleting an asset stops propagation of events when clicking a delete button?

*Contributed by: Caleb*


---
## [medium/addon_creator_biomes.html] - Chunk 0

**Type:** ui

**Summary:** The Biome Creator panel provides a UI for defining biome generation parameters, including preset loading, terrain size/shape constraints, climate/humidity/environment settings via segmented controls, and ground layer block selection with live recipe dropdowns.

**Explanation:**
UI Controls: Text inputs (biomeId, biomeChance, bioInterpolationSearch, bioSurfaceBlock, bioSubBlock, bioStoneBlock, bioMinRadius, bioMaxRadius, bioMinHeight, bioMaxHeight, bioMinHeightLimit, bioMaxHeightLimit) with validation via oninput handlers; Dropdowns (biomePresetDropdown, bioInterpolationDropdown) triggered by focus/mousedown events; Segmented radio controls for Climate (.hot/.temperate/.cold), Humidity (.wet/.neither/.dry), Environment (.inland/.land/.ocean), Flora (.barren/.balanced/.overgrown), Elevation Type (.lowTerrain/.balanced/.mountain/.antiMtn); Checkbox (bioSmoothBeaches). Event Handlers: onfocus on preset selector opens dropdown and sets value; onmousedown on dropdown options updates the readonly search input, calls window.loadBiomePreset('type'), and hides dropdown; oninput on block inputs filters a recipe dropdown via window.filterDropdown and shows it via window.showRecipeDropdown when focused. Defaults: biomeId placeholder 'ruby_valleys' (auto-lowercased, alphanumeric+underscore only); bioInterpolation default '.square'; Climate temperate, Humidity neitherWetNorDry, Environment inland, Flora balanced, Elevation Type balanced; Smooth Beaches checked. Templates: none explicitly defined in this chunk. Engine Mappings: window.loadBiomePreset maps preset name to biome type string; window.filterDropdown filters block recipes by input value; window.showRecipeDropdown renders a dropdown list of matching blocks. Configuration Generation: The UI constructs a biome config object (not shown here) from the collected values, likely using the IDs as property names and the segmented control names as grouped fields.

**Symbols:** biomePresetSelectorSearch, biomePresetDropdown, biomeId, biomeChance, bioInterpolationSearch, bioInterpolationDropdown, bioInterpolation, bioSurfaceBlock, bioSurfaceDropdown, bioSubBlock, bioSubDropdown, bioStoneBlock, bioStoneDropdown, bioMinRadius, bioMaxRadius, bioMinHeight, bioMaxHeight, bioSmoothBeaches, bioMinHeightLimit, bioMaxHeightLimit

**Concepts:** data-binding, form-validation, live-preview, dropdown-selection, segmented-controls, preset-loading, block-recipe-filtering

**Keywords:** biome, presets, terrain, climate, humidity, environment, flora, elevation, blocks, dropdowns, validation, defaults

**Related Questions:**
- What happens when a user clicks on a preset option in the dropdown?
- How does the UI enforce alphanumeric-only input for biomeId?
- Which segmented control is used to set the default climate value?
- What triggers the display of the block recipe dropdowns for surface/subsurface layers?
- Are there any hidden inputs that store the actual biome configuration values?
- How does the UI handle the checkbox for Smooth Beaches in terms of defaults and user interaction?

*Contributed by: Caleb*


---
## [medium/addon_creator_app-io.js] - Chunk 1

**Type:** ui

**Summary:** This module parses .zig.zon addon files and populates the projectData object with items, entities, particles, recipes, and biomes by extracting values from file contents.

**Explanation:**
The code handles multiple file paths: blocks (absorbedLightColor, dropAuto, etc.), items (stackSize, foodValue, blockPlacement, tags, texture, colors, baseColor, material), entityModels/models (height, coordinateSystem, model, defaultTexture, tags), particles (speedRange, lifeRange, densityRange, rotRange, dragRange, directionVectorMatch, hasEmission, shape, mode), recipes (inputsParsed, output), and biomes (parsedStructures). It uses extractVal helper for simple key-value extraction, extractMinMax for range values, regex matches for complex structures like tags or inputs, and manual brace counting for nested JSON-like blocks. Each parsed section pushes an object into the corresponding window.projectData array or property.

**Symbols:** window.projectData.items, window.projectData.entities, window.projectData.particles, window.projectData.recipes, extractVal, extractMinMax, getSideTex, parseIntegerToHexColor

**Concepts:** file parsing, regex extraction, nested JSON handling, project data population, addon blueprint processing

**Keywords:** .zig.zon, items, entities, particles, recipes, biomes, extractVal, regex match, brace counting, projectData

**Related Questions:**
- How does the code extract tags from a .zig.zon file?
- What happens if a block file lacks an absorbedLight value?
- How are particle speed ranges parsed from content?
- Where is the entity model ID constructed in the code?
- Does the recipe parser handle quoted input strings?
- How does the biome parser locate structures within nested braces?
- What default values are used when extractVal fails to find a key?
- Is there any validation for texture file existence before pushing items?
- How is the coordinateSystem determined for an entity model?
- Can the particle shape be changed dynamically by editing the .zig.zon?

*Contributed by: Caleb*


---
## [medium/addon_creator_app-io.js] - Chunk 3

**Type:** ui

**Summary:** This module defines the `importExistingAddon` function, which parses an imported addon ZIP payload to extract terrain configuration values (min/max heights, roughness, hills, mountains, soil creep, cave settings, crystals, music, fog density) and structural data (structures, climate, humidity, zone, growth, elevation type), then triggers UI refresh functions (`updateSearchableItems`, `updateSidebarProjectTree`) and alerts the user of success or failure.

**Explanation:**
UI Controls: None directly rendered; this is a backend parsing function. Event Handlers: Calls `window.updateSearchableItems()` if defined, calls `window.updateSidebarProjectTree()` if defined, triggers an alert on success/failure. Validation: Uses `extractVal` helper to pull string values from the parsed content object with fallback defaults (e.g., minHeightLimit default '7', maxHeightLimit default '50'). Also checks for specific strings like '.isCave = true' and '.validPlayerSpawn = false' using includes, negating them where appropriate. Defaults: All terrain parameters have explicit fallbacks if not found in content; stoneBlock defaults to 'cubyz:slate/base'; music defaults to 'cubyz:sunrise'. Templates: None present here—this is pure data extraction logic. Bindings: Returns an object containing all extracted fields, which are then passed to the UI layer (presumably via a template or state update mechanism not shown in this chunk). Engine Mappings: Uses Cubyz namespace prefixes for blocks ('cubyz:slate/base') and music ('cubyz:sunrise'). Configuration Generation: The returned object is effectively the configuration payload that will be used to reconstruct or preview the addon's terrain and structure settings. No direct user interaction UI components are defined in this chunk; it serves as a data ingestion step for the editor.

**Symbols:** importExistingAddon, extractVal, window.updateSearchableItems, window.updateSidebarProjectTree

**Concepts:** data-binding, form-validation, default-values, configuration-parsing, UI-refresh-hooks

**Keywords:** import, parse, terrain-config, cave-settings, crystals, music, fog-density, stone-block, valid-player-spawn, update-searchable-items, update-sidebar-project-tree

**Related Questions:**
- What default value is assigned to minHeightLimit if not found in the addon content?
- How does the code determine whether caves are enabled from the imported file?
- Which Cubyz namespace prefix is used for the stone block when importing an existing addon?
- Under what conditions will the alert message say 'Successfully imported' instead of 'Failed parsing addon zip payload'?
- What happens if window.updateSearchableItems is not defined when this function runs?
- How does the code handle the isValidPlayerSpawn flag based on string presence in content?
- Is there any validation performed on the numeric values extracted via extractVal before they are returned?
- Which UI components are triggered after a successful import, and how are they invoked?
- What is the fallback value for music if no music setting is found in the addon file?
- Does this function modify the DOM directly or does it rely on external state updates?

*Contributed by: Caleb*


---
## [medium/addon_creator_blocks.html] - Chunk 0

**Type:** ui

**Summary:** The Block Creator panel provides UI controls for defining block properties including preset loading, ID naming, health/resistance values, render modes, collision/visibility flags, light emission, tags, engine physics parameters (replaceable, degradability, view-through, backfaces, ore allowance), and touch interaction presets.

**Explanation:**
UI Controls: Text inputs for blockId (with sanitization on input), blockHealth (number), blockResistance (number with step 0.1), emittedLightColor/absorbedLightColor (color pickers), checkboxes for blockCollide, blockTransparent, blockReplaceable, blockDegradable, blockViewThrough, blockAlwaysViewThrough, blockHasBackFace, blockAllowOres, and dropdowns for render modes (blockRotation) and touch presets (simpleTouchPreset). Event Handlers: oninput sanitizes blockId to lowercase alphanumeric; onfocus triggers dropdown visibility; onmousedown on dropdown options sets hidden input values and calls window.loadBlockPreset or window.handleRotationChange or window.handleSimpleTouchChange. Validation: blockId uses placeholder 'ruby_ore' and regex replacement /[^a-z0-9_]/g to strip invalid chars; health/resistance have default values (1/0); render mode dropdowns include descriptive labels like '3D Block (cubyz:stairs)'. Defaults: emittedLightColor defaults #000000, absorbedLightColor #ffffff; blockCollide checked by default. Templates: Dropdown options are inline HTML with padding/cursor-pointer styling; tag container supports dynamic pill addition via window.addDynamicTagPill. Engine Mappings: hidden inputs store engine-specific identifiers (e.g., 'cubyz:stairs', 'cubyz:ore') while visible text shows user-friendly names. Configuration Generation: The UI likely feeds a JSON-like config object built from these fields, passed to the Cubyz addon generation pipeline.

**Symbols:** blockPresetSelectorSearch, blockPresetDropdown, loadBlockPreset, blockId, blockHealth, blockResistance, blockRotation, blockRotationSearch, blockRotationDropdown, handleRotationChange, blockCollide, blockTransparent, emittedLightColor, absorbedLightColor, blockTagsContainer, tagTextInput, addDynamicTagPill, blockReplaceable, blockDegradable, blockViewThrough, blockAlwaysViewThrough, blockHasBackFace, blockAllowOres, blockFriction, blockBounciness, blockDensity, blockTerminalVelocity, blockMobility, simpleTouchPreset, simpleTouchPresetSearch, simpleTouchDropdown, handleSimpleTouchChange

**Concepts:** data-binding, form-validation, live-preview, preset-loading, dropdown-selection, tag-management, engine-mapping, physics-configuration, touch-interaction

**Keywords:** block-id, render-mode, collision, light-emission, tags, replaceable, degradable, view-through, backfaces, ore-veins, friction, bounciness, density, terminal-velocity, mobility

**Related Questions:**
- What happens when a user clicks on one of the preset dropdown options for block rotation?
- How is the blockId input sanitized and what characters are allowed?
- Which hidden input stores the engine-specific render mode identifier after selection?
- What default values are assigned to emittedLightColor and absorbedLightColor fields?
- Describe the purpose of the addDynamicTagPill function in relation to blockTagsContainer.
- How does the UI handle user interaction with the simpleTouchPreset dropdown?
- Which checkbox controls whether ores can be spawned inside this block type?
- What is the step attribute for blockResistance and why might it be set that way?
- Explain how the blockRotation hidden input value relates to the visible search text.
- Are any of the physics parameters (friction, bounciness) constrained by min/max attributes?
- How does the UI indicate which engine preset is currently loaded for a given block type?
- What event triggers the display of the blockPresetDropdown element?

*Contributed by: Caleb*


---
## [medium/addon_creator_blocks.html] - Chunk 3

**Type:** ui

**Summary:** This HTML chunk defines the texture input controls for slots 14 and 15, including dropdowns and file upload buttons, followed by a visual layout map of the six cube faces with image placeholders.

**Explanation:**
The UI contains two form groups (Texture Slot 14 and Texture Slot 15). Each group has: <label> text, an <input type="text"> bound to id 'tex14'/'tex15', a hidden dropdown div ('tex14Dropdown'/'tex15Dropdown'), and a file-input-label wrapping a hidden <input type="file" accept=".png"> that triggers window.handleCustomTexture(this, 'tex14') on change. The inputs have onfocus='showDropdown(...)' and oninput='filterDropdown(...)'. Below the slots is a styled div titled 'Texture Layout Map' containing a CSS grid (block-layout-cross-grid) with 3 columns x 4 rows; only specific cells contain layout-face-box elements, each holding an <img> (id view_up, view_left, etc.) and a .face-lbl span. The face images are hidden by default via CSS.

**Symbols:** tex14, tex15, tex14Dropdown, tex15Dropdown, view_up, view_left, view_front, view_right, view_bottom, view_back, window.handleCustomTexture, showDropdown, filterDropdown

**Concepts:** texture-slot-inputs, dropdown-filtering, file-upload-binding, face-layout-map, grid-positioning

**Keywords:** texture, slot, upload, png, dropdown, filter, layout, map, cube, face, grid, view

**Related Questions:**
- What happens when a user focuses the text input for Texture Slot 14?
- How is the custom texture file handler invoked for slot 15?
- Which CSS class controls the visibility of the face images in the layout map?
- Are all six cube faces represented in the layout map, or only some?
- What placeholder text is used for the texture input fields?
- Does the dropdown appear immediately on focus, or after typing?
- Is there any validation logic attached to these inputs besides filtering?
- How are the face labels (e.g., 'Top', 'Left') rendered in the layout map?
- Can a user add multiple PNG files for a single texture slot via this UI?
- What is the purpose of the block-layout-cross-grid CSS rule?

*Contributed by: Caleb*


---
## [easy/addon_creator_recipes.html] - Chunk 0

**Type:** ui

**Summary:** The Recipe Creator panel provides a UI for defining crafting recipes by allowing users to load preset templates, specify up to four input ingredients with quantity and search-based item selection, define an output item result with quantity, and save the configuration to the project.

**Explanation:**
UI Controls: The component includes a 'Load Preset' dropdown (recipePresetSelectorSearch) that triggers window.loadRecipePreset on selection; four input rows for ingredients each containing a quantity field (recipeInputCount1-4), a search text input (recipeInputSearch1-4) with placeholder guidance, and hidden dropdown containers (recipeInputDropdown1-4) populated via showRecipeDropdown/filterDropdown functions; an output section with a quantity field (recipeOutputCount) and a search input (recipeOutputSearch) for the result item, also using showRecipeDropdown/filterDropdown. Event Handlers: Inline handlers onfocus open the respective dropdowns; oninput calls filterDropdown to limit results; onmousedown on preset options sets the search value and invokes loadRecipePreset then hides the dropdown. Validation/Defaults: Quantity inputs have min='1' and default value '1'; recipeFilename input sanitizes user entry via oninput (lowercase, alphanumeric + underscore only); placeholders guide optional entries. Templates: Dropdowns are rendered as absolute-positioned divs with class 'dropdown-options', hidden by default; content is injected dynamically (not shown in this chunk). Bindings: No explicit data-binding attributes appear here; interaction relies on DOM events and inline scripts. Engine Mappings: Preset IDs ('planks', 'workbench') map to window.loadRecipePreset calls, implying an internal recipe registry keyed by string identifiers. Configuration Generation: The save button (saveRecipeToProject) likely serializes the collected ingredient/output objects into a JSON-like structure stored under a project key.

**Symbols:** recipePresetSelectorSearch, recipePresetDropdown, loadRecipePreset, recipeFilename, recipeInputCount1-4, recipeInputSearch1-4, recipeInputDropdown1-4, showRecipeDropdown, filterDropdown, recipeOutputCount, recipeOutputSearch, recipeOutputDropdown, saveRecipeToProject

**Concepts:** data-entry form, searchable dropdowns, preset loading, ingredient quantity control, output result definition, project configuration save

**Keywords:** recipe, crafting, ingredients, output, presets, search, dropdowns, quantity, save, project, UI form

**Related Questions:**
- What happens when a user selects 'Oak Planks' from the Load Preset dropdown?
- How are ingredient search results filtered as the user types in recipeInputSearch1-4?
- Which function is called to populate each hidden dropdown (recipeInputDropdown1-4)?
- What sanitization is applied to the Recipe ID input before it is stored?
- Can a recipe be saved without defining any input ingredients, and what default values are used?
- How does the output section differ from the ingredient sections in terms of quantity handling?
- Is there any validation that ensures total input quantities do not exceed a limit?
- What data structure is likely generated by saveRecipeToProject for the project configuration?
- Are preset IDs like 'planks' and 'workbench' stored globally or per-session?
- How does the UI handle cases where an ingredient search returns no results?
- Is there a way to clear all inputs before saving, and which element would trigger that?
- What CSS classes are used for the dropdown containers and how is their visibility toggled?

*Contributed by: Caleb*


---
## [easy/addon_creator_index.html] - Chunk 0

**Type:** ui

**Summary:** The Cubyz Addon Creator index page provides the main navigation hub, displaying a toolbar with addon name input and import/export buttons, alongside a project explorer sidebar listing blocks, items, recipes, biomes, entities, and particles.

**Explanation:**
UI Controls: The page includes an editable text input for 'addonName' that auto-sanitizes to lowercase alphanumeric characters via oninput event. Two toolbar buttons are present: an import button wrapping a hidden file input (id='importAddonFile') triggered by onchange, and an export button invoking exportFullAddon(). A metrics panel with id='folderStatus' is clickable via onclick handler window.toggleMetricsPanel() showing a status pill labeled 'Connecting...'. The sidebar contains six collapsible tree sections: sidebarBlocksTree, sidebarItemsTree, sidebarRecipesTree, sidebarBiomesTree, sidebarEntitiesTree, and sidebarParticlesTree, each initially displaying placeholder text. Navigation buttons in the nav-bar (loadStudioPanel) switch between categories.

**Symbols:** addonName, importAddonFile, exportFullAddon(), toggleMetricsPanel(), folderStatus, sidebarBlocksTree, sidebarItemsTree, sidebarRecipesTree, sidebarBiomesTree, sidebarEntitiesTree, sidebarParticlesTree, loadStudioPanel()

**Concepts:** data-binding, form-validation, live-preview, tree-navigation, addon-import-export

**Keywords:** toolbar, sidebar, import, export, navigation, panels, blocks, items, recipes, biomes, entities, particles

**Related Questions:**
- What happens when the user types into the addonName field?
- How does the import button trigger file selection without a visible input element?
- Which function is called when the metrics panel is clicked?
- Are there any validation rules applied to the addon name besides lowercasing?
- How are unsaved changes communicated to the user before switching panels?
- What placeholder text appears in each sidebar tree section initially?
- Is there a way to programmatically load a specific studio panel from this index page?
- Does the export button perform any pre-export validation or confirmation?
- How does the nav-bar buttons interact with the dynamicWorkspace div?
- Are any external scripts loaded that handle addon creation logic?

*Contributed by: Caleb*


---
## [hard/addon_creator_app-studio.js] - Chunk 0

**Type:** ui

**Summary:** The chunk defines various event handlers and utility functions for managing UI components in the Cubyz Addon Creator, including handling changes to block types, toggling input fields, initializing dynamic tag systems, and updating logic settings.

**Explanation:**
This JavaScript file contains several functions that manage the behavior of UI components within the Cubyz Addon Creator. The primary responsibilities include:

1. **handleRotationChange**: Updates checkboxes and dropdowns based on the selected block type.
2. **toggleDropInput**: Toggles the visibility of a custom drop input field.
3. **toggleItemIconInput**: Toggles the visibility of an item icon input field.
4. **autoToggleTransparentTag**: Automatically toggles the transparent tag (not implemented in this snippet).
5. **initDynamicTagSystem**: Initializes a dynamic tag system that allows users to add and remove tags from a block.
6. **handleSimpleTouchChange**: Updates touch interaction settings based on user selection.
7. **handleSimpleInteractChange**: Updates interaction settings based on user selection.
8. **handleSimpleEnvChange**: Updates environmental settings based on user selection.

Each function interacts with specific UI elements identified by their IDs, updating their properties and visibility as needed. The functions also handle form validation and mark the form as dirty when changes are made.

**Symbols:** handleRotationChange, toggleDropInput, toggleItemIconInput, autoToggleTransparentTag, initDynamicTagSystem, handleSimpleTouchChange, handleSimpleInteractChange, handleSimpleEnvChange

**Concepts:** data-binding, form validation, live preview

**Keywords:** block type, checkbox, dropdown, dynamic tag system, touch interaction, environmental settings, UI component, event handler, visibility toggle, form dirty state

**Related Questions:**
- What is the purpose of the handleRotationChange function?
- How does the toggleDropInput function affect the UI?
- What does the initDynamicTagSystem function do?
- How are environmental settings updated in the handleSimpleEnvChange function?
- What happens when a user selects 'cubyz:ore' as the block type?
- How is the visibility of the custom drop input field controlled?
- What is the role of the autoToggleTransparentTag function?
- How does the handleSimpleTouchChange function update touch interaction settings?
- What is the purpose of the toggleItemIconInput function?
- How are tags added and removed in the dynamic tag system?

*Contributed by: Nick*


---
## [hard/addon_creator_app-studio.js] - Chunk 2

**Type:** ui

**Summary:** The chunk initializes a dynamic workspace for editing Cubyz addon elements like blocks, items, recipes, biomes, entities, and particles. It sets up event listeners, form population functions, and UI components specific to each element type.

**Explanation:**
This chunk is responsible for dynamically loading and initializing the UI components of the Cubyz Addon Creator workspace. It handles various UI elements such as input fields, dropdowns, checkboxes, and tags. The code includes event listeners for input changes, form population functions for different types of addon elements (blocks, items, recipes, biomes, entities, particles), and utility functions like `initDynamicTagSystem` and `toggleDropInput`. It also manages the state of unsaved changes and initializes dropdowns based on the current panel name. The chunk ensures that the UI is responsive to user interactions and accurately reflects the data being edited.

**Symbols:** loadStudioPanel, populateBlockFormValues, populateItemFormValues, populateRecipeFormValues, populateBiomeFormValues, dynamicWorkspace, blockRotation, blockTagsContainer, tagTextInput, dropAuto, dropSearch, hasItemIcon, itemIconSearch, topSearch, frontSearch, leftSearch, rightSearch, upSearch, bottomSearch, logicTouchType, logicTouchMode, logicTouchTypeVariant, logicUpdateType, logicDecayReplacement, logicDecayPrevention, logicUpdateReplaceBlockSearch, logicTickType, logicDecayTickReplacement, logicDecayTickPrevention, logicTickReplaceBlockSearch, logicBreakType, logicBreakReplaceBlockSearch, logicInteractType, logicInteractWindowName, simpleTouchPresetSearch, simpleEnvPreset, simpleEnvPresetSearch, advTickReplaceWrapper, advBreakReplaceWrapper, advInteractWindowWrapper

**Concepts:** data-binding, form validation, live preview, dynamic UI generation, event handling, state management

**Keywords:** dynamic workspace, form population, event listeners, UI components, unsaved changes, dropdowns, tags, input validation, live preview, data binding

**Related Questions:**
- What is the purpose of the `loadStudioPanel` function?
- How does the code handle input changes in the dynamic workspace?
- What specific UI components are initialized for editing blocks?
- How does the form population work for different types of addon elements?
- What utility functions are used to manage tags and dropdowns in the UI?
- How is the state of unsaved changes managed in this chunk?
- What event handlers are attached to input fields and dropdowns?
- How does the code ensure that the UI accurately reflects the data being edited?
- What is the role of `initDynamicTagSystem` in the UI components?
- How does the code handle errors when rendering panel views?

*Contributed by: Nick*


---
## [hard/addon_creator_app-save.js] - Chunk 1

**Type:** ui

**Summary:** This chunk handles saving items, recipes, and biomes to the project data structure. It updates UI components and alerts the user upon successful saves.

**Explanation:**
The chunk includes functions for saving different types of project elements: items, recipes, and biomes. Each function retrieves input values from HTML elements, validates them, and then updates the `window.projectData` object accordingly. After saving, it resets certain UI state variables and triggers updates to reflect changes in the sidebar project tree. Alerts notify users of successful saves.

**Symbols:** saveItemToProject, saveRecipeToProject, saveBiomeToProject, hslToHex, getHexColorAsRGBVector, autoNamespaceBlock

**Concepts:** data-binding, form validation, UI state management, project data structure updates

**Keywords:** saveItemToProject, saveRecipeToProject, saveBiomeToProject, window.projectData, document.getElementById, Object.assign, updateSidebarProjectTree, alert, form validation, UI state management

**Related Questions:**
- What is the purpose of the `saveItemToProject` function?
- How does the chunk validate input values before saving a recipe?
- What happens to the UI state after successfully saving an item?
- How are colors converted from HSL to HEX in this chunk?
- What is the role of the `autoNamespaceBlock` function in saving biomes?
- How does the chunk handle structural layers when saving a biome?
- What is the significance of the `window.projectData` object in this context?
- How are alerts used to notify users about successful saves?
- What UI elements are involved in saving a recipe?
- How does the chunk ensure that only valid inputs are saved?

*Contributed by: Nick*


---
## [hard/addon_creator_app-save.js] - Chunk 2

**Type:** ui

**Summary:** This chunk handles saving biome, entity, and particle configurations to the project data and exporting the full addon as a ZIP file.

**Explanation:**
The chunk includes functions for saving biomes, entities, and particles to the project data. Each function retrieves values from input fields, validates them, and updates the corresponding section in `window.projectData`. The `exportFullAddon` function checks if the project is empty, creates a ZIP archive with necessary folders, and writes configuration files based on the project data. It also handles texture and model file inclusion.

**Symbols:** saveBiomeToProject, saveEntityToProject, saveParticleToProject, exportFullAddon

**Concepts:** data-binding, form validation, file export

**Keywords:** biome, entity, particle, project data, ZIP export, input fields, validation, texture inclusion, model files

**Related Questions:**
- What is the purpose of the `saveBiomeToProject` function?
- How does the `exportFullAddon` function handle empty projects?
- What validation checks are performed when saving an entity?
- How are textures and models included in the exported ZIP file?
- What happens if a user tries to save a biome without specifying an ID?
- How is the project data updated after saving a particle configuration?
- What is the role of `autoNamespaceBlock` in the biome saving process?
- How does the chunk ensure that only valid IDs are used for entities and particles?
- What steps are taken to prevent duplicate entries when saving configurations?
- How is the sidebar project tree updated after saving a configuration?

*Contributed by: Nick*


---
## [hard/addon_creator_app-save.js] - Chunk 3

**Type:** ui

**Summary:** This chunk handles the serialization of project data into a format suitable for saving, including blocks, items, and biomes.

**Explanation:**
The code processes various elements of an addon project, such as blocks, items, and biomes. It constructs configuration strings in a specific format (likely Zig) that describe properties like textures, health, resistance, callbacks, and more. The data is then saved to files within the project's directory structure. Key operations include finding matching textures from a server list, formatting property values, and handling conditional logic based on block or item attributes.

**Symbols:** dropDec, baseMatch, bZon, compHook, iZon, bioZon, fmtB

**Concepts:** data-binding, configuration generation, file handling, property serialization

**Keywords:** blocks, items, biomes, serialization, configuration, properties, callbacks, textures, files, addons

**Related Questions:**
- How does the code handle the serialization of block properties?
- What is the purpose of the `compHook` function in the context of block callbacks?
- How are item textures and stack sizes serialized into the configuration?
- Can you explain how biomes are formatted and saved in this chunk?
- What role do conditional checks play in generating the configuration strings?
- How does the code ensure that only valid textures are used for blocks and items?
- What is the significance of the `dropDec` variable in the block serialization process?
- How are block callbacks like `onTouch`, `onUpdate`, and `onBreak` handled in this chunk?
- Can you describe the structure of the configuration strings generated for each element type?
- What mechanisms are in place to prevent duplicate or conflicting configurations?

*Contributed by: Nick*


---
## [hard/addon_creator_app-save.js] - Chunk 4

**Type:** ui

**Summary:** Handles the saving of addon data, including biomes, recipes, entities, and particles into a ZIP file.

**Explanation:**
This JavaScript code snippet is responsible for exporting an entire Cubyz addon project. It processes various types of data such as biomes, recipes, entities, and particles, formatting them into specific Zig.ZON files. The script ensures that each element's properties are correctly serialized, including handling optional fields and default values. For example, it formats chance values to two decimal places and checks if certain conditions (like `isCave`) are met before adding additional properties. It also manages the creation of subfolders based on the data's structure and writes files accordingly. The final step is to generate a ZIP file containing all these formatted files and prompt the user to download it.

**Symbols:** bio, bioZon, rZon, ent, pZon, packs, folders, writeTex, exportFullAddon

**Concepts:** data serialization, file generation, ZIP file creation, conditional data inclusion

**Keywords:** biomes, recipes, entities, particles, Zig.ZON, ZIP export, data formatting, optional fields, default values, file structure

**Related Questions:**
- How does the script handle optional properties when generating Zig.ZON files?
- What is the purpose of the `writeTex` function in this code snippet?
- How are biomes with structures handled differently compared to those without?
- Can you explain how the script ensures that each entity's model and texture paths are correctly formatted?
- What steps does the script take to generate a ZIP file containing all the addon data?
- How does the script manage the creation of subfolders for different types of data (e.g., biomes, recipes)?
- What is the role of the `exportFullAddon` function in this context?
- How are default values applied when serializing properties to Zig.ZON files?
- Can you describe how the script handles different types of structures within biomes?
- What mechanisms does the script use to ensure that all necessary textures are included in the final ZIP file?

*Contributed by: Nick*


---
## [medium/addon_creator_app-core.js] - Chunk 0

**Type:** ui

**Summary:** The script initializes server asset data and UI components for the Cubyz Addon Creator, handling asynchronous loading of assets and updating UI elements based on loaded data.

**Explanation:**
This JavaScript file is part of the Cubyz Addon Creator application. It defines several global variables to store server asset data such as blocks, items, textures, recipes, music, entities, and particles. The `loadServerAssets` function asynchronously fetches these assets from a specified version path and updates the corresponding global arrays. It also processes texture paths to categorize them into block, item, entity, or particle textures, updating metrics accordingly. The `renderMetricsUI` function updates the UI with status information and metrics based on the loaded data. Additionally, there are placeholders for other functions like `updateSearchableItems`, `rebuildDropdowns`, and `updateSidebarProjectTree` which are assumed to be defined elsewhere in the application.

**Symbols:** serverBlocks, serverItems, serverTextures, serverMusicList, serverEntityModels, serverParticles, blockTexturesOnly, itemTexturesOnly, particleTexturesOnly, allSearchableItems, dropdownsGenerated, VERSION_PATH, hasUnsavedChanges, currentPanelName, editingId, projectData, metricsExpandedState, metricCounts, loadServerAssets, renderMetricsUI

**Concepts:** data-binding, asynchronous data loading, UI updates based on data, error handling in UI

**Keywords:** server assets, async loading, texture categorization, UI metrics, status updates, global variables, fetch API, Promise.all, error handling, UI rendering

**Related Questions:**
- What is the purpose of the `loadServerAssets` function?
- How does the script handle errors when loading server assets?
- What data structures are used to store server asset information?
- How are textures categorized in this script?
- What UI elements are updated based on the loaded metrics?
- What is the role of the `renderMetricsUI` function?
- How does the script manage unsaved changes?
- What global variables are defined for project data management?
- How are dropdowns generated and managed in this script?
- What is the structure of the `projectData` object?

*Contributed by: Nick*


---
## [medium/addon_creator_app-core.js] - Chunk 1

**Type:** ui

**Summary:** The chunk implements UI rendering and interaction for displaying server metrics, updating dropdown options, marking form changes as dirty, and rebuilding sidebar project trees.

**Explanation:**
This JavaScript code snippet is part of the Cubyz Addon Creator workspace. It defines several functions and event handlers related to UI components such as metrics display, dropdowns, and form validation. The `renderMetricsUI` function updates the status container with server database metrics based on the expanded state. The `toggleMetricsPanel` function toggles the visibility of the metrics panel. The `updateSearchableItems` function generates a list of searchable items based on project data. The `markFormAsDirty` function marks the form as having unsaved changes. The `renderDropdownOptions` function populates dropdowns with texture options, and `rebuildDropdowns` rebuilds all relevant dropdowns. The `updateSidebarProjectTree` function updates the sidebar tree view for different project elements like blocks, items, biomes, entities, and particles.

**Symbols:** loadServerAssets, renderMetricsUI, toggleMetricsPanel, updateSearchableItems, markFormAsDirty, renderDropdownOptions, rebuildDropdowns, deletedAddonElements, updateSidebarProjectTree

**Concepts:** data-binding, form validation, live preview, UI rendering, event handling

**Keywords:** metrics display, dropdown options, form changes, sidebar project tree, server database metrics, searchable items, texture options, unsaved changes, UI components, event handlers

**Related Questions:**
- What function is responsible for updating the server metrics UI?
- How does the `toggleMetricsPanel` function affect the UI?
- What items are included in the searchable items list?
- When is the form marked as dirty?
- How are dropdown options populated and filtered?
- What elements are updated in the sidebar project tree?
- How does the code handle errors when loading server assets?
- What CSS classes are used to style the status container?
- How are custom block and item IDs generated?
- What is the purpose of the `deletedAddonElements` object?

*Contributed by: Nick*


---
## [medium/addon_creator_app-core.js] - Chunk 3

**Type:** ui

**Summary:** The chunk manages UI components for dropdowns and search inputs in the addon creator app, including dynamic filtering and event handling.

**Explanation:**
This JavaScript code snippet is part of the Cubyz Addon Creator workspace. It defines functions to handle dropdown menus and search inputs within the application. The `window.showRecipeDropdown` function populates a dropdown with options based on a given type (e.g., blocks, music) and dispatches input and change events when an option is selected. The `window.filterDropdown` function filters dropdown options based on user input in the corresponding search field. The `window.renderDropOptions` function initializes these components by attaching event listeners to search inputs and creating dropdown elements if they don't exist. The code also includes a `DOMContentLoaded` event listener to load server assets when the document is ready.

**Symbols:** input, dropdown, opt, filterDropdown, renderDropOptions, showRecipeDropdown

**Concepts:** data-binding, form validation, live preview

**Keywords:** dropdown, search input, event handling, dynamic filtering, server assets, DOM manipulation, input events, change events, UI components, addon creation

**Related Questions:**
- How does the `showRecipeDropdown` function populate the dropdown options?
- What is the purpose of the `filterDropdown` function in this code?
- How are event listeners attached to search inputs in the `renderDropOptions` function?
- What happens when a user selects an option from the dropdown menu?
- How does the code ensure that the dropdown is displayed only when there are visible options?
- What role do the `DOMContentLoaded` and `input.onfocus` events play in this UI component?
- How is the visibility of dropdown options dynamically controlled based on user input?
- What types of assets are loaded when the document content is fully loaded?
- How does the code handle cases where the search input or dropdown elements do not exist?
- What is the relationship between the `showRecipeDropdown` and `filterDropdown` functions in managing the dropdown UI?

*Contributed by: Nick*


---
## [medium/addon_creator_biomes.html] - Chunk 1

**Type:** ui

**Summary:** The UI component in this chunk is responsible for configuring various biome properties such as height limits, terrain factors, environmental settings, and underground cave generation.

**Explanation:**
This HTML snippet defines a section of the Cubyz Addon Creator's UI where users can configure different aspects of a biome. It includes input fields for numerical values (e.g., Min Height, Max Height), checkboxes (e.g., Smooth Beaches, Valid Spawn), color pickers (e.g., Sky Tint, Fog Atmospheric Tint), and file inputs for custom audio tracks. The UI is organized into sections with headers like 'Environment, Audio & Atmospheric Tints' and 'Underground Cave Gen'. Event handlers are attached to buttons for actions such as playing music previews, adding custom audio files, toggling cave settings visibility, and saving the biome configuration to the project.

**Symbols:** bioMinHeight, bioMaxHeight, bioSmoothBeaches, bioMinHeightLimit, bioMaxHeightLimit, bioRoughness, bioHills, bioMountains, bioSoilCreep, bioKeepOriginalTerrain, bioMusic, btnPlayMusic, bioFogDensity, bioSkyColor, bioFogColor, bioSpawn, bioIsCave, caveSettings, bioCaves, bioCaveRadiusFactor, bioCrystals, biomeStructuresContainer

**Concepts:** data-binding, form validation, live preview

**Keywords:** Min Height, Max Height, Smooth Beaches, Roughness Factor, Hills Factor, Mountains Factor, Soil Creep Slip Factor, Keep Original Mix, Ambient Music Track, Fog Thickness Density, Sky Tint, Fog Atmospheric Tint, Valid Spawn, Enable Cave Biome Properties, Cave Density Scale

**Related Questions:**
- What is the purpose of the 'bioSmoothBeaches' checkbox in the UI?
- How does the UI handle custom audio file uploads for ambient music?
- What event handler is triggered when the user clicks the 'Save Biome to Project' button?
- How are color values selected and bound in the UI?
- What validation checks are applied to numerical input fields like 'bioMinHeight'?
- How does the UI toggle the visibility of cave settings based on user interaction?
- What is the functionality of the '+ Add Structure Layer' button in the Foliage, Decor & Structures section?
- How does the UI generate a live preview of the biome configuration?
- What data-binding techniques are used to update the project with the configured biome properties?
- How does the UI manage and display dropdown options for music tracks?

*Contributed by: Nick*


---
## [medium/addon_creator_app-io.js] - Chunk 0

**Type:** ui

**Summary:** Handles the import of existing addons by parsing a ZIP file and updating project data accordingly.

**Explanation:**
The `importExistingAddon` function is responsible for importing an existing addon from a ZIP file. It processes the uploaded file, extracts relevant data, and updates the project's internal state. The function reads the ZIP file using JSZip, determines the namespace name based on the file structure, and initializes various arrays in `window.projectData` to store blocks, items, recipes, biomes, entities, and particles. It then iterates over the files in the ZIP, extracting textures and metadata for blocks, items, and other elements, updating the project data with this information. The function also includes helper functions like `parseIntegerToHexColor`, `extractVal`, and `extractMinMax` to parse specific values from file content.

**Symbols:** importExistingAddon, JSZip.loadAsync, document.getElementById, window.projectData.blocks, window.projectData.items, window.projectData.recipes, window.projectData.biomes, window.projectData.entities, window.projectData.particles, window.serverTextures, parseIntegerToHexColor, extractVal, extractMinMax

**Concepts:** data-binding, file parsing, project data update, texture extraction, metadata parsing

**Keywords:** importExistingAddon, JSZip, ZIP file, namespace name, project data, serverTextures, parseIntegerToHexColor, extractVal, extractMinMax, blocks, items, recipes, biomes, entities, particles

**Related Questions:**
- What is the purpose of the `importExistingAddon` function?
- How does the function determine the namespace name from the ZIP file?
- What data structures are updated in `window.projectData` during the import process?
- How are textures extracted and stored from the ZIP file?
- What helper functions are used to parse specific values from file content?
- How is the project's internal state updated after importing an addon?
- What types of files are processed during the import of an existing addon?
- How does the function handle different categories like blocks, items, and recipes?
- What validation or error handling is implemented in the `importExistingAddon` function?
- How does the function ensure that textures are not duplicated in `window.serverTextures`?

*Contributed by: Nick*


---
## [medium/addon_creator_app-io.js] - Chunk 2

**Type:** ui

**Summary:** Handles the import and parsing of addon files, specifically for biomes with '.zig.zon' extension.

**Explanation:**
This code snippet is responsible for processing imported addon files that are related to biomes. It checks if the file path includes '/biomes/' and ends with '.zig.zon'. If so, it reads the content of the file and extracts various properties such as structures, climate, humidity, zone, growth, elevation type, surface block, sub-block, stone block, and other biome-specific attributes. The extracted data is then added to the `window.projectData.biomes` array. Additionally, it updates searchable items and the sidebar project tree if the respective functions are available.

**Symbols:** inputsParsed, content, parsedStructures, startIdx, openBrace, idx, braceCount, structuresText, sIdx, openObj, subCount, subIdx, objText, lines, attrs, structObj, climate, humidity, zone, growth, elevationType, properties, propMatch, props, groundMatch, surfaceBlock, subBlock, nameToken, extractedSubFolder

**Concepts:** data-binding, file parsing, biome configuration, project data management

**Keywords:** import, parse, addon, biome, zig.zon, structures, properties, updateSearchableItems, updateSidebarProjectTree, alert

**Related Questions:**
- What is the purpose of the `inputsParsed` variable in this code snippet?
- How does the code extract and parse structures from the biome file content?
- What conditions are checked to determine if a file should be processed as a biome file?
- How are climate, humidity, zone, growth, and elevation type properties determined from the file content?
- What is the role of the `updateSearchableItems` function in this code snippet?
- How does the code handle errors during the parsing process?
- What specific attributes are extracted for each structure type (e.g., 'cubyz:simple_tree')?
- How is the surface block and sub-block determined from the file content?
- What is the significance of the `isValidPlayerSpawn` property in the biome configuration?
- How does the code manage to update the sidebar project tree after parsing a new biome file?

*Contributed by: Nick*


---
## [medium/addon_creator_blocks.html] - Chunk 1

**Type:** configuration

**Summary:** The provided HTML snippet is a form for configuring block properties in a game or application. It includes sections for setting the block's name, texture, and various behaviors such as touch effects, automatic drops, and inventory icons. The form uses checkboxes to toggle advanced options and dropdowns for selecting textures and behaviors. There are also input fields for customizing specific behaviors like replacing blocks on certain actions.

**Explanation:**
The HTML snippet is a detailed configuration form designed for setting up block properties in a game or application, likely related to a modding environment or a similar development scenario. The form is structured into several sections, each focusing on different aspects of the block's behavior and appearance.

1. **Block Name**: A text input field where users can enter the name of the block.
2. **Texture Configuration**: This section allows users to select textures for different sides of the block (top, bottom, front, back, left, right) using dropdowns populated with texture options. There's also an option to add custom PNG textures.
3. **Touch Effects**: Users can configure what happens when a player touches the block, such as causing damage or healing. This section includes a checkbox to toggle advanced touch effects and dropdowns for selecting specific behaviors.
4. **Automatic Drops**: A checkbox allows users to enable automatic drops of the block itself when broken by a player. There's an option to specify custom drop items using a search input field with a dropdown for selection.
5. **Inventory Icon**: Users can set a 2D inventory icon for the block, which is displayed in the player's hand and inventory. This section includes a checkbox to toggle this feature and a search input field for selecting or adding custom textures.

The form uses JavaScript to dynamically show or hide certain sections based on user interactions (e.g., toggling advanced options) and to filter dropdown options as users type in search fields. The overall design is clean, with a dark theme that matches the style of many game development tools and editors.

**Symbols:** blockName, topSearch, bottomSearch, frontSearch, backSearch, leftSearch, rightSearch, toggleAdvancedLogic, logicTouchType, logicUpdateType, logicInteractType, logicTickType, logicBreakType, interactWindowName, updateReplaceBlockSearch, tickReplaceBlockSearch, breakReplaceBlockSearch, decayTickReplacement, decayTickPrevention, logicTouchMode, dropAuto, dropSearch, hasItemIcon, itemIconSearch

**Concepts:** block configuration, texture selection, behavior customization, automatic drops, inventory icon, touch effects, advanced logic, game development, modding environment

**Keywords:** HTML form, block properties, texture configuration, touch effects, automatic drops, inventory icon, JavaScript interactions, dropdowns, search fields, dark theme

**Related Questions:**
- How do I configure the block's texture in this form?
- What options are available for setting touch effects on the block?
- Can I customize what happens when a player breaks the block?
- How do I add a custom inventory icon to the block?
- What advanced logic can be applied to the block using this form?
- Is it possible to enable automatic drops for the block?

*Contributed by: Nick*


---
## [medium/addon_creator_blocks.html] - Chunk 2

**Type:** ui

**Summary:** The provided HTML code snippet is a user interface for creating and managing custom block textures in a project. It includes input fields for selecting or uploading textures, a preview of the texture layout, and a button to save the block configuration to the project.

**Explanation:**
This HTML code represents a part of a web-based application designed for users to create and manage custom block textures within a larger project. The interface is structured around several key components:

1. **Texture Selection**: There are 16 texture slots (from tex0 to tex15) where users can either type in the name of an existing texture or upload a new PNG file. Each slot has an input field and a dropdown menu that appears when focused, allowing for quick selection from available textures. Additionally, there's a button next to each input field that allows users to add a custom PNG file.

2. **Texture Layout Preview**: Below the texture selection area, there is a visual representation of how these textures will be laid out on a block. This preview includes images for six faces of a cube (top, left, front, right, bottom, back), each labeled with its corresponding face name. Users can see how their selected textures will appear when applied to the different sides of the block.

3. **Save Button**: At the bottom of the interface, there is a button labeled 'Save Block to Project'. When clicked, this button triggers a JavaScript function (`window.saveBlockToProject()`) that presumably saves the current block configuration, including all selected textures and their layout, back into the project.

The code also includes some CSS styles for styling the interface elements, such as input fields, dropdown menus, labels, and buttons. These styles help to ensure a clean and user-friendly appearance for the interface.

Overall, this interface is designed to be intuitive and efficient, allowing users to easily manage their block textures and preview how they will appear in their project.

**Symbols:** tex0, tex1, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9, tex10, tex11, tex12, tex13, tex14, tex15, view_up, view_left, view_front, view_right, view_bottom, view_back

**Concepts:** Custom Block Textures, Texture Selection, Texture Layout Preview, Project Management, User Interface Design, JavaScript Functionality, CSS Styling

**Keywords:** HTML, CSS, JavaScript, Block Texture, Project, User Interface, Dropdown Menu, File Input, Image Preview, Save Button

**Related Questions:**
- How does the texture selection dropdown work in this interface?
- What is the purpose of the 'Save Block to Project' button?
- How are custom textures added to the project through this UI?
- Can you explain the layout preview section and its components?
- What JavaScript functions are used in this code snippet, and what do they likely do?
- How does the CSS styling contribute to the overall user experience of this interface?

*Contributed by: Nick*


---
## [easy/addon_creator_particles.html] - Chunk 0

**Type:** ui

**Summary:** The Particle Creator UI allows users to define particle properties such as ID, texture, emission settings, and various physical attributes like speed, lifetime, and rotation.

**Explanation:**
This HTML snippet defines a user interface for creating particles in the Cubyz Addon Studio. The UI includes several form groups for different particle properties:

1. **Particle ID**: A text input for specifying the particle's unique identifier (filename), with validation to ensure lowercase alphanumeric characters and underscores.
2. **Particle Texture**: An input field with a dropdown for selecting textures, including an option to upload custom PNG files. The UI also displays a thumbnail preview of the selected texture.
3. **Emission Texture**: A checkbox to enable emission texture support, accompanied by a warning message when enabled.
4. **Particle Settings (Min / Max)**: Multiple input fields for defining particle attributes such as spawn speed, lifetime, density, rotation speed, and drag, with min/max values.
5. **Spawn Shape & Direction**: Dropdowns for selecting the shape and direction of particle spawning, along with additional fields that appear based on the selected options (e.g., direction vector for fixed direction).

The UI also includes a 'Save Particle to Project' button to finalize the particle configuration and add it to the project.

Event handlers are attached to various inputs and dropdowns to manage user interactions, such as filtering texture options, toggling additional fields based on selections, and handling custom file uploads.

**Symbols:** particleId, particleTextureSearch, thumb_particleTextureSearch, particleTextureDropdown, particleHasEmission, emissionWarning, particleSpeedMin, particleSpeedMax, particleLifeMin, particleLifeMax, particleDensityMin, particleDensityMax, particleRotVelMin, particleRotVelMax, particleRandomRotate, particleCollides, particleSpawnShape, particleSpawnShapeSearch, particleSpawnShapeDropdown, shapeParamWrapper, particleDirectionMode, particleDirectionModeSearch, particleDirectionModeDropdown, directionVectorWrapper, particleDirX, particleDirY, particleDirZ

**Concepts:** data-binding, form validation, dropdown selection, file upload, conditional rendering

**Keywords:** Particle Creator, ID, Texture, Emission, Settings, Min/Max, Spawn Shape, Direction, Save, Validation, Dropdown, File Upload, Conditional Fields

**Related Questions:**
- What is the purpose of the 'particleId' input field?
- How does the UI handle custom texture uploads for particles?
- What validation is applied to the 'particleId' input?
- How are additional fields conditionally rendered based on user selections?
- What event handlers are attached to the dropdowns for spawn shape and direction?
- How does the UI manage the display of emission warnings?
- What is the role of the 'Save Particle to Project' button in the UI?
- How are min/max values handled for particle attributes like speed and lifetime?
- What CSS classes are used for styling the dropdown options?
- How does the UI ensure that only valid characters are entered for the particle ID?

*Contributed by: Nick*


---
## [easy/addon_creator_README.md] - Chunk 0

**Type:** ui

**Summary:** The Cubyz Addon Creator is a web-based tool for creating and managing addons for the game Cubyz. It includes panels for blocks, items, recipes, biomes, entities, and particles.

**Explanation:**
The UI consists of multiple panels each dedicated to different aspects of addon creation such as blocks, items, recipes, etc. The core logic is split across several JavaScript files including setup and initialization, import handling, export handling, and interface control.

**Symbols:** index.html, blocks.html, items.html, recipes.html, biomes.html, entities.html, particles.html, app-core.js, app-io.js, app-save.js, app-studio.js

**Concepts:** data-binding, form-validation, live-preview

**Keywords:** Cubyz Addon Creator, web-based tool, game development, addon creation, interface control

**Related Questions:**
- What panels are available in the Cubyz Addon Creator?
- Which JavaScript files handle different aspects of addon creation?
- How is data binding implemented in the UI components?
- What kind of validation is performed on form inputs?
- How does the live preview feature work in the Cubyz Addon Creator?
- Where can I find the main page and other panels in the project structure?
- Which file initializes the application setup?
- How is import handling implemented in the Cubyz Addon Creator?
- What functionality is provided by app-save.js?
- Who controls the interface elements in the Cubyz Addon Creator?
- How are different aspects of addon creation organized in the project?

*Contributed by: NickMac*


---
