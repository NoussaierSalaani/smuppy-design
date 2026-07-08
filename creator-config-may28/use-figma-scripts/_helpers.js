// SHARED HELPERS — copy/paste into every screen-build script's `code` field.
// These build canonical V2 atoms with bound variables when available, fallback to hex.

const V2 = {
  MINT: { r: 0.149, g: 0.757, b: 0.643 },      // #26C1A4
  MINT_HI: { r: 0.066, g: 0.890, b: 0.640 },    // #11E3A3
  MINT_DEEP: { r: 0, g: 0.701, b: 0.780 },      // #00B3C7
  DANGER: { r: 0.937, g: 0.267, b: 0.267 },     // #EF4444
  WARN: { r: 0.961, g: 0.620, b: 0.043 },       // #F59E0B
  SUB: { r: 0.545, g: 0.545, b: 0.584 },        // #8B8B95
  TEXT_DARK: { r: 0.945, g: 0.957, b: 0.965 },  // #F1F4F6
  TEXT_LIGHT: { r: 0.059, g: 0.090, b: 0.165 }, // #0F172A
  PAGE_DARK: { r: 0, g: 0, b: 0 },              // #000000
  PAGE_LIGHT: { r: 0.965, g: 0.972, b: 0.980 },  // #F6F8FA
  CARD_DARK: { r: 0.078, g: 0.078, b: 0.102 },  // #14141A
  CARD_LIGHT: { r: 1, g: 1, b: 1 },             // #FFFFFF
  BORDER_DARK: { r: 1, g: 1, b: 1, a: 0.06 },
  BORDER_LIGHT: { r: 0.933, g: 0.945, b: 0.957 }, // #EEF1F4
};

const FONT_JAKARTA_400 = { family: "Plus Jakarta Sans", style: "Regular" };
const FONT_JAKARTA_500 = { family: "Plus Jakarta Sans", style: "Medium" };
const FONT_JAKARTA_600 = { family: "Plus Jakarta Sans", style: "Semi Bold" };
const FONT_JAKARTA_700 = { family: "Plus Jakarta Sans", style: "Bold" };
const FONT_JAKARTA_800 = { family: "Plus Jakarta Sans", style: "Extra Bold" };

async function loadFonts() {
  await Promise.all([
    figma.loadFontAsync(FONT_JAKARTA_400),
    figma.loadFontAsync(FONT_JAKARTA_500),
    figma.loadFontAsync(FONT_JAKARTA_600),
    figma.loadFontAsync(FONT_JAKARTA_700),
    figma.loadFontAsync(FONT_JAKARTA_800),
  ]);
}

// Create a phone-root frame at exact 393×852 device dimensions.
function createPhoneRoot(name, dark = true) {
  const frame = figma.createFrame();
  frame.name = name;
  frame.resize(393, 852);
  frame.clipsContent = true;
  frame.fills = [{ type: "SOLID", color: dark ? V2.PAGE_DARK : V2.PAGE_LIGHT }];
  frame.cornerRadius = 0;
  return frame;
}

// Place a frame in clear space on the canvas (right of existing content).
function placeInClearSpace(frame, padX = 60) {
  let maxX = 0;
  for (const child of figma.currentPage.children) {
    maxX = Math.max(maxX, child.x + child.width);
  }
  frame.x = maxX + padX;
  frame.y = 0;
}

// Mint glow effect — for canonical action buttons / active tabs.
function mintGlowEffect(intensity = 0.35) {
  return [
    { type: "DROP_SHADOW", color: { ...V2.MINT, a: intensity }, offset: { x: 0, y: 0 },
      radius: 18, spread: 0, visible: true, blendMode: "NORMAL" },
    { type: "INNER_SHADOW", color: { ...V2.MINT, a: 0.45 }, offset: { x: 0, y: 0 },
      radius: 0, spread: 1, visible: true, blendMode: "NORMAL" },
  ];
}

// Canonical T1 chip (32x32 colored circle with halo glow).
function createChip(iconChar, hue = V2.MINT, size = 32) {
  const chip = figma.createFrame();
  chip.resize(size, size);
  chip.cornerRadius = size / 3;
  chip.fills = [{ type: "SOLID", color: hue, opacity: 0.10 }];
  chip.strokes = [{ type: "SOLID", color: hue, opacity: 0.40 }];
  chip.strokeWeight = 1;
  chip.strokeAlign = "INSIDE";
  chip.effects = [
    { type: "DROP_SHADOW", color: { ...hue, a: 0.33 }, offset: { x: 0, y: 0 },
      radius: 18, spread: 0, visible: true, blendMode: "NORMAL" },
  ];
  chip.layoutMode = "HORIZONTAL";
  chip.primaryAxisAlignItems = "CENTER";
  chip.counterAxisAlignItems = "CENTER";
  chip.itemSpacing = 0;
  chip.paddingLeft = 0; chip.paddingRight = 0; chip.paddingTop = 0; chip.paddingBottom = 0;
  // Icon placeholder text (replace with real ion-icon vector when DS provides)
  const icon = figma.createText();
  icon.fontName = FONT_JAKARTA_700;
  icon.fontSize = 14;
  icon.characters = iconChar; // emoji or 1-char symbol as placeholder
  icon.fills = [{ type: "SOLID", color: hue }];
  chip.appendChild(icon);
  return chip;
}

// Canonical v5 pill button (active = card bg + mint text + mint border + mint halo).
function createPillButton(label, hueColor = V2.MINT, active = true) {
  const pill = figma.createFrame();
  pill.layoutMode = "HORIZONTAL";
  pill.primaryAxisAlignItems = "CENTER";
  pill.counterAxisAlignItems = "CENTER";
  pill.paddingLeft = 14; pill.paddingRight = 14;
  pill.paddingTop = 8; pill.paddingBottom = 8;
  pill.itemSpacing = 6;
  pill.cornerRadius = 999;
  pill.fills = [{ type: "SOLID", color: active ? V2.CARD_DARK : V2.PAGE_DARK, opacity: active ? 1 : 0 }];
  pill.strokes = active ? [{ type: "SOLID", color: hueColor, opacity: 0.45 }] : [];
  pill.strokeWeight = 1.5;
  pill.effects = active ? mintGlowEffect(0.30) : [];

  const txt = figma.createText();
  txt.fontName = FONT_JAKARTA_700;
  txt.fontSize = 13;
  txt.characters = label;
  txt.fills = [{ type: "SOLID", color: active ? hueColor : V2.SUB }];
  pill.appendChild(txt);
  return pill;
}

// Canonical primary CTA (gradient mint full-width).
function createPrimaryCTA(label) {
  const cta = figma.createFrame();
  cta.layoutMode = "HORIZONTAL";
  cta.primaryAxisAlignItems = "CENTER";
  cta.counterAxisAlignItems = "CENTER";
  cta.layoutSizingHorizontal = "FILL";
  cta.paddingTop = 14; cta.paddingBottom = 14;
  cta.cornerRadius = 999;
  cta.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { ...V2.MINT_HI, a: 1 } },
      { position: 1, color: { ...V2.MINT_DEEP, a: 1 } },
    ],
    gradientTransform: [[0.7071, 0.7071, 0], [-0.7071, 0.7071, 0.5]],
  }];
  cta.effects = [
    { type: "DROP_SHADOW", color: { ...V2.MINT, a: 0.45 }, offset: { x: 0, y: 8 },
      radius: 24, spread: 0, visible: true, blendMode: "NORMAL" },
  ];
  const txt = figma.createText();
  txt.fontName = FONT_JAKARTA_800;
  txt.fontSize = 15;
  txt.characters = label;
  txt.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
  cta.appendChild(txt);
  return cta;
}

// Canonical settings-style row (chip + label + chevron).
function createSettingsRow(chipChar, chipHue, label, subLabel = "") {
  const row = figma.createFrame();
  row.layoutMode = "HORIZONTAL";
  row.counterAxisAlignItems = "CENTER";
  row.itemSpacing = 14;
  row.paddingLeft = 14; row.paddingRight = 14;
  row.paddingTop = 12; row.paddingBottom = 12;
  row.layoutSizingHorizontal = "FILL";
  row.fills = [];

  const chip = createChip(chipChar, chipHue, 32);
  row.appendChild(chip);

  const labelStack = figma.createFrame();
  labelStack.layoutMode = "VERTICAL";
  labelStack.itemSpacing = 2;
  labelStack.layoutGrow = 1;
  labelStack.fills = [];
  const lbl = figma.createText();
  lbl.fontName = FONT_JAKARTA_700;
  lbl.fontSize = 14;
  lbl.characters = label;
  lbl.fills = [{ type: "SOLID", color: V2.TEXT_DARK }];
  labelStack.appendChild(lbl);
  if (subLabel) {
    const sub = figma.createText();
    sub.fontName = FONT_JAKARTA_500;
    sub.fontSize = 12;
    sub.characters = subLabel;
    sub.fills = [{ type: "SOLID", color: V2.SUB }];
    labelStack.appendChild(sub);
  }
  row.appendChild(labelStack);

  const chev = figma.createText();
  chev.fontName = FONT_JAKARTA_400;
  chev.fontSize = 16;
  chev.characters = "›";
  chev.fills = [{ type: "SOLID", color: V2.SUB, opacity: 0.55 }];
  row.appendChild(chev);
  return row;
}
