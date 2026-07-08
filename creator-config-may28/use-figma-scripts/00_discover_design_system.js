// Smuppy V2 — Sprint E + D : Step 1/N — DISCOVERY
// Run this first when MCP unblocks. Returns JSON map of existing DS components/variables/styles.
// Pass output to subsequent screen-build scripts.
//
// Invoke via : mcp__plugin_figma_figma__use_figma
//   fileKey: <FILE_KEY>   (provided at invocation time — see README for value)
//   description: "Discover all DS components, variables, styles in file"
//   skillNames: figma-use,figma-generate-design
//   code: <contents of this file>

figma.skipInvisibleInstanceChildren = true;

// 1. Local variables (already-defined V2 tokens)
const localCollections = await figma.variables.getLocalVariableCollectionsAsync();
const localVars = [];
for (const col of localCollections) {
  for (const id of col.variableIds) {
    const v = await figma.variables.getVariableByIdAsync(id);
    if (v) localVars.push({ id: v.id, key: v.key, name: v.name, type: v.resolvedType, collection: col.name });
  }
}

// 2. Existing frames on current page → harvest component instances + bound vars
const pageFrames = figma.currentPage.children.filter(c => c.type === "FRAME").slice(0, 20);
const componentInventory = new Map();
const varInventory = new Map();
const styleInventory = new Map();

for (const frame of pageFrames) {
  // Component instances → main components + sets
  for (const inst of frame.findAllWithCriteria({ types: ["INSTANCE"] })) {
    const mc = inst.mainComponent;
    if (!mc) continue;
    const cs = mc.parent?.type === "COMPONENT_SET" ? mc.parent : null;
    const key = cs ? cs.key : mc.key;
    const name = cs ? cs.name : mc.name;
    if (key && !componentInventory.has(key)) {
      const props = cs ? cs.componentPropertyDefinitions : mc.componentPropertyDefinitions;
      componentInventory.set(key, { name, key, isSet: !!cs, properties: props });
    }
  }
  // Bound variables
  for (const node of frame.findAll(() => true)) {
    const bv = node.boundVariables ?? {};
    for (const val of Object.values(bv)) {
      const arr = Array.isArray(val) ? val : [val];
      for (const b of arr) {
        if (b?.id && !varInventory.has(b.id)) {
          const v = await figma.variables.getVariableByIdAsync(b.id);
          if (v) varInventory.set(b.id, { id: v.id, key: v.key, name: v.name, type: v.resolvedType, remote: v.remote });
        }
      }
    }
    // Text + Effect styles
    if ('textStyleId' in node && node.textStyleId && typeof node.textStyleId === 'string') {
      const s = figma.getStyleById(node.textStyleId);
      if (s && !styleInventory.has(s.id)) styleInventory.set(s.id, { name: s.name, id: s.id, key: s.key, type: 'TEXT' });
    }
    if ('effectStyleId' in node && node.effectStyleId && typeof node.effectStyleId === 'string') {
      const s = figma.getStyleById(node.effectStyleId);
      if (s && !styleInventory.has(s.id)) styleInventory.set(s.id, { name: s.name, id: s.id, key: s.key, type: 'EFFECT' });
    }
  }
}

return {
  pageId: figma.currentPage.id,
  pageName: figma.currentPage.name,
  localVariables: localVars,
  harvestedComponents: [...componentInventory.values()],
  harvestedVariables: [...varInventory.values()],
  harvestedStyles: [...styleInventory.values()],
};
