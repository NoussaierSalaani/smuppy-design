// Sprint E · Screen 1/10 — post_create_menu_v2_dark
// Output : editable Figma frame 393×852 with AutoLayout sheet + 4 option rows.
// Pre-built canonical V2 (mint glow chips, gradient backdrop, v5 patterns).
// Composer paste the entire content of _helpers.js BEFORE this code, in the same `code` field.

await loadFonts();

const root = createPhoneRoot("Post · Create menu (dark)", true);
placeInClearSpace(root);

// === BACKDROP (silhouette of feed) ===
const backdrop = figma.createFrame();
backdrop.name = "Backdrop";
backdrop.resize(393, 852);
backdrop.x = 0; backdrop.y = 0;
backdrop.fills = [{ type: "SOLID", color: V2.PAGE_DARK }];
// 2 ghost cards top
for (let i = 0; i < 2; i++) {
  const ghost = figma.createFrame();
  ghost.resize(170, 215);
  ghost.x = 14 + (i * 195);
  ghost.y = 46;
  ghost.cornerRadius = 24;
  ghost.fills = [{ type: "SOLID", color: V2.CARD_DARK, opacity: 1 }];
  if (i === 1) {
    ghost.fills = [{
      type: "GRADIENT_LINEAR",
      gradientStops: [
        { position: 0, color: { ...V2.MINT, a: 0.12 } },
        { position: 1, color: { r: 1, g: 1, b: 1, a: 0.04 } },
      ],
      gradientTransform: [[0.7071, 0.7071, 0], [-0.7071, 0.7071, 0.5]],
    }];
  }
  backdrop.appendChild(ghost);
}
root.appendChild(backdrop);

// === BOTTOM SHEET ===
const sheet = figma.createFrame();
sheet.name = "Bottom Sheet";
sheet.layoutMode = "VERTICAL";
sheet.counterAxisAlignItems = "STRETCH";
sheet.itemSpacing = 6;
sheet.paddingTop = 14; sheet.paddingBottom = 28;
sheet.paddingLeft = 20; sheet.paddingRight = 20;
sheet.resize(393, 380); // approximate sheet height
sheet.x = 0; sheet.y = 472;
sheet.cornerRadius = 32;
sheet.topLeftRadius = 32; sheet.topRightRadius = 32;
sheet.bottomLeftRadius = 0; sheet.bottomRightRadius = 0;
sheet.fills = [{ type: "SOLID", color: V2.CARD_DARK }];
sheet.strokes = [{ type: "SOLID", color: V2.MINT, opacity: 0.20 }];
sheet.strokeWeight = 1;
sheet.strokeAlign = "INSIDE";
sheet.effects = [
  { type: "DROP_SHADOW", color: { r: 0, g: 0, b: 0, a: 0.32 }, offset: { x: 0, y: -10 },
    radius: 40, spread: 0, visible: true, blendMode: "NORMAL" },
];

// Handle
const handle = figma.createFrame();
handle.resize(42, 5);
handle.cornerRadius = 999;
handle.fills = [{ type: "SOLID", color: V2.SUB, opacity: 0.40 }];
handle.layoutAlign = "CENTER";
sheet.appendChild(handle);

// Title
const title = figma.createText();
title.fontName = FONT_JAKARTA_800;
title.fontSize = 18;
title.characters = "Que veux-tu créer ?";
title.fills = [{ type: "SOLID", color: V2.TEXT_DARK }];
title.textAlignHorizontal = "CENTER";
title.layoutAlign = "CENTER";
sheet.appendChild(title);

// Spacer 12px
const spacer = figma.createFrame();
spacer.resize(1, 12);
spacer.fills = [];
sheet.appendChild(spacer);

// Option rows
const OPTIONS = [
  { icon: "📷", hue: { r: 0.067, g: 0.776, b: 1 },     title: "Post",     sub: "Photo, carrousel, légende" },
  { icon: "🎬", hue: { r: 0.6, g: 0.4, b: 1 },         title: "Peak",     sub: "Vidéo verticale 15-60s" },
  { icon: "📹", hue: { r: 1, g: 0.275, b: 0.345 },     title: "Go Live",  sub: "Stream en direct avec ta tribu", live: true },
  { icon: "🏃", hue: { r: 1, g: 0.651, b: 0.239 },     title: "Activity", sub: "Run, ride, training, hike" },
];
for (const opt of OPTIONS) {
  const row = figma.createFrame();
  row.layoutMode = "HORIZONTAL";
  row.counterAxisAlignItems = "CENTER";
  row.itemSpacing = 14;
  row.paddingLeft = 12; row.paddingRight = 12;
  row.paddingTop = 14; row.paddingBottom = 14;
  row.layoutSizingHorizontal = "FILL";
  row.cornerRadius = 18;
  row.fills = [{ type: "SOLID", color: V2.PAGE_DARK, opacity: 0.5 }];
  row.strokes = [{ type: "SOLID", color: V2.BORDER_DARK }];
  row.strokeWeight = 1;

  const chip = createChip(opt.icon, opt.hue, 42);
  row.appendChild(chip);

  const textStack = figma.createFrame();
  textStack.layoutMode = "VERTICAL";
  textStack.itemSpacing = 2;
  textStack.layoutGrow = 1;
  textStack.fills = [];

  const titleRow = figma.createFrame();
  titleRow.layoutMode = "HORIZONTAL";
  titleRow.counterAxisAlignItems = "CENTER";
  titleRow.itemSpacing = 6;
  titleRow.fills = [];
  const t = figma.createText();
  t.fontName = FONT_JAKARTA_700;
  t.fontSize = 15;
  t.characters = opt.title;
  t.fills = [{ type: "SOLID", color: V2.TEXT_DARK }];
  titleRow.appendChild(t);
  if (opt.live) {
    const dot = figma.createEllipse();
    dot.resize(8, 8);
    dot.fills = [{ type: "SOLID", color: opt.hue }];
    dot.effects = [
      { type: "DROP_SHADOW", color: { ...opt.hue, a: 0.6 }, offset: { x: 0, y: 0 },
        radius: 8, spread: 0, visible: true, blendMode: "NORMAL" },
    ];
    titleRow.appendChild(dot);
  }
  textStack.appendChild(titleRow);

  const s = figma.createText();
  s.fontName = FONT_JAKARTA_500;
  s.fontSize = 12;
  s.characters = opt.sub;
  s.fills = [{ type: "SOLID", color: V2.SUB }];
  textStack.appendChild(s);

  row.appendChild(textStack);

  const chev = figma.createText();
  chev.fontName = FONT_JAKARTA_400;
  chev.fontSize = 18;
  chev.characters = "›";
  chev.fills = [{ type: "SOLID", color: V2.SUB, opacity: 0.55 }];
  row.appendChild(chev);

  sheet.appendChild(row);
}

root.appendChild(sheet);

return { ok: true, nodeId: root.id, name: root.name };
