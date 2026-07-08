# use_figma scripts — ready to fire on MCP unblock

Pre-written JS scripts that build EDITABLE Figma maquettes (AutoLayout frames, native components, bound variables) when the Figma MCP rate limit is lifted.

## Why this exists

Founder may30 hard lock : "je ne vais pas drag drop des png je veux des maquettes avec les composants" — wants editable Figma frames with native components, not raster PNG.

Figma MCP `use_figma` + `upload_assets` + `generate_figma_design` all hit the same rate limit (Professional plan View seat). Until upgrade or reset, no MCP writes possible.

Solution : pre-write the build scripts. When MCP unblocks, fire them sequentially — each call produces 1 editable Figma frame at exact 393×852 device dimensions.

## Order to fire

1. **00_discover_design_system.js** — REQUIRED FIRST. Returns JSON map of existing DS components/variables/styles in the file. Output informs subsequent scripts (which DS components to instance vs build from scratch).
2. **01_post_create_menu_dark.js** — BottomSheet "Que veux-tu créer ?" (4 options with mint glow chips)
3. **02_post_create_menu_light.js** — Same as 01, light theme variant
4. **03_post_gallery_dark.js** — Photo picker with topbar Suivant + 4-col grid + source tabs
5. **04_post_gallery_light.js**
6. **05_post_details_dark.js** — Caption + hashtags v5 + 3-row glass card (Location/Tag/Visibility) + Publier gradient
7. **06_post_details_light.js**
8. **07_post_success_dark.js** — Mint check halo + Post publié! + 2 CTAs + status mini-card
9. **08_post_success_light.js**
10. **09_peak_camera_dark.js** — TikTok-style camera (close/music/flash + side action stack + speed/duration pills + record red button)
11. **10_peak_camera_light.js**
12. **11_packages_edit_dark.js** — Sprint D Pack editor edit mode (thumbnail + stats + identity + tarif + services + danger zone)
13. **12_packages_edit_light.js**

## How to fire

Each script is meant to be the `code` field of a single `mcp__plugin_figma_figma__use_figma` invocation. Required prefix : paste `_helpers.js` ABOVE the script content in the same `code` field — helpers define `V2`, `createPhoneRoot`, `createChip`, etc.

Invocation template :

```
mcp__plugin_figma_figma__use_figma
  fileKey: <FILE_KEY>
  description: "Sprint E · 01 · post_create_menu_v2_dark"
  skillNames: figma-use,figma-generate-design
  code: <_helpers.js content>\n\n<01_post_create_menu_dark.js content>
```

Each script returns `{ ok: true, nodeId: "X:Y", name: "..." }` on success. Use returned `nodeId` for sanity-check screenshots via `get_screenshot`.

## What the scripts produce

Each script creates a top-level frame on the current page at exact 393×852 device dimensions, placed in clear space to the right of existing content. Each frame is FULLY EDITABLE :

- AutoLayout-driven sections (vertical/horizontal flex)
- Component instances where DS provides them (Button, Card, Avatar)
- Bound variables for color/spacing/radius when discoverable
- Text uses Plus Jakarta Sans family (Regular / Medium / Semi Bold / Bold / Extra Bold)
- Effects = drop-shadow + inner-shadow for canonical mint glow halos
- Icons currently use emoji placeholders (📷/🎬/📹/🏃/✓/›) — replace with real ion-icon vectors once founder confirms which Figma icon library to bind to

## Estimated cost (when MCP unblocked)

- 1 discover call
- 12 build calls (10 post-creation + 2 pack-editor)
- 12 verification screenshots
= **~25 MCP calls** to produce all editable maquettes.

## Local preview (works now, no MCP)

All 13 screens already render at 393×852 in browser : http://127.0.0.1:8765/maquettes/harmonized/<key>/code.html

| Script | Localhost URL |
|---|---|
| 01-02 | `post_create_menu_v2_{dark,light}` |
| 03-04 | `post_gallery_v2_{dark,light}` |
| 05-06 | `post_details_v2_{dark,light}` |
| 07-08 | `post_success_v2_{dark,light}` |
| 09-10 | `peak_camera_v2_{dark,light}` |
| 11-12 | `creator_packages_edit_v2_{dark,light}` |

## Status

- ✅ `00_discover_design_system.js` — written
- ✅ `_helpers.js` — written (atoms : phone-root, chip, pill, CTA, settings-row)
- ✅ `01_post_create_menu_dark.js` — written (reference implementation)
- ⏳ `02-12` — pattern locked, scripts to be written when first one validates against live MCP

The reference script (`01`) is intentionally complete so founder can validate one full screen before mass-generating the remaining 11. If founder approves the visual + structure, the remaining scripts follow the same pattern with sub-30 min of effort each (or auto-generated via a Python codegen reading the HTML maquettes).

## Next steps

1. **Founder** : upgrade Figma plan OR wait for MCP rate reset
2. **Claude** : fire `00_discover_design_system.js` → review output
3. **Claude** : fire `01_post_create_menu_dark.js` → screenshot the produced frame → founder validates
4. **If validated** : auto-generate the remaining 11 scripts from the HTML maquettes (via Python codegen) and fire them
5. **If NOT validated** : iterate on script `01` until visuals match canonical, then proceed
