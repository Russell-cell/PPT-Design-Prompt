# PPT-image Design System Inspired by Wise

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Wise.

Source reference: `source/wise/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Wise's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent. The design operates on a warm off-white canvas with near-black text (`#0e0f0c`) and a signature Wise Green (`#9fe870`) — a fresh, lime-bright color that feels alive and optimistic, unlike the corporate blues of traditional banking.

The typography uses Wise Sans — a proprietary font used at extreme weight 900 (black) for display headings with a remarkably tight line-height of 0.85 and OpenType `"calt"` (contextual alternates). At 126px, the text is so dense it feels like a protest sign — bold, urgent, and impossible to ignore. Inter serves as the body font with weight 600 as the default for emphasis, creating a consistently confident voice.

What distinguishes Wise is its green-on-white-on-black material palette. Lime Green (`#9fe870`) appears on buttons with dark green text (`#163300`), creating a nature-inspired CTA that feels fresh. Hover states use `scale(1.05)` expansion rather than color changes — buttons physically grow on interaction. The border-radius system uses 9999px for buttons (pill), 30px–40px for cards, and the shadow system is minimal — just `rgba(14,15,12,0.12) 0px 0px 0px 1px` ring shadows.

**Key Characteristics:**
- Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines
- Lime Green (`#9fe870`) accent with dark green text (`#163300`) — nature-inspired fintech
- Inter body at weight 600 as default — confident, not light
- Near-black (`#0e0f0c`) primary with warm green undertone
- Scale(1.05) hover animations — buttons physically grow
- OpenType `"calt"` on all text
- Pill buttons (9999px) and large rounded cards (30px–40px)
- Semantic color system with comprehensive state management


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, Inter body at weight 600 as default — confident, not light, and Near-black (#0e0f0c) primary with warm green undertone.
- Use Wise Green (#9fe870) as the highest-signal accent when color needs to carry emphasis.
- Let Light Mint (#e2f6d5) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#0e0f0c) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary Brand
- **Near Black** (`#0e0f0c`): Primary text, background for dark sections
- **Wise Green** (`#9fe870`): Primary CTA button, brand accent
- **Dark Green** (`#163300`): Button text on green, deep green accent
- **Light Mint** (`#e2f6d5`): Soft green surface, badge backgrounds
- **Pastel Green** (`#cdffad`): `--color-interactive-contrast-hover`, hover accent

### Semantic
- **Positive Green** (`#054d28`): `--color-sentiment-positive-primary`, success
- **Danger Red** (`#d03238`): `--color-interactive-negative-hover`, error/destructive
- **Warning Yellow** (`#ffd11a`): `--color-sentiment-warning-hover`, warnings
- **Background Cyan** (`rgba(56,200,255,0.10)`): `--color-background-accent`, info tint
- **Bright Orange** (`#ffc091`): `--color-bright-orange`, warm accent

### Neutral
- **Warm Dark** (`#454745`): Secondary text, borders
- **Gray** (`#868685`): Muted text, tertiary
- **Light Surface** (`#e8ebe6`): Subtle green-tinted light surface


### PPT-image Deployment

- Base canvas: prefer Light Mint (#e2f6d5) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#0e0f0c) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Wise Green (#9fe870) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `Wise Sans`, fallback: `Inter` — OpenType `"calt"` on all text
- **Body / UI**: `Inter`, fallbacks: `Helvetica, Arial`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Mega | Wise Sans | 126px (7.88rem) | 900 | 0.85 (ultra-tight) | normal | `"calt"` |
| Display Hero | Wise Sans | 96px (6.00rem) | 900 | 0.85 | normal | `"calt"` |
| Section Heading | Wise Sans | 64px (4.00rem) | 900 | 0.85 | normal | `"calt"` |
| Sub-heading | Wise Sans | 40px (2.50rem) | 900 | 0.85 | normal | `"calt"` |
| Alt Heading | Inter | 78px (4.88rem) | 600 | 1.10 (tight) | -2.34px | `"calt"` |
| Card Title | Inter | 26px (1.62rem) | 600 | 1.23 (tight) | -0.39px | `"calt"` |
| Feature Title | Inter | 22px (1.38rem) | 600 | 1.25 (tight) | -0.396px | `"calt"` |
| Body | Inter | 18px (1.13rem) | 400 | 1.44 | 0.18px | `"calt"` |
| Body Semibold | Inter | 18px (1.13rem) | 600 | 1.44 | -0.108px | `"calt"` |
| Button | Inter | 18px–22px | 600 | 1.00–1.44 | -0.108px | `"calt"` |
| Caption | Inter | 14px (0.88rem) | 400–600 | 1.50–1.86 | -0.084px to -0.108px | `"calt"` |
| Small | Inter | 12px (0.75rem) | 400–600 | 1.00–2.17 | -0.084px to -0.108px | `"calt"` |

### Principles
- **Weight 900 as identity**: Wise Sans Black (900) is used exclusively for display — the heaviest weight in any analyzed system. It creates text that feels stamped, pressed, physical.
- **0.85 line-height**: The tightest display line-height analyzed. Letters overlap vertically, creating dense, billboard-like text blocks.
- **"calt" everywhere**: Contextual alternates enabled on ALL text — both Wise Sans and Inter.
- **Weight 600 as body default**: Inter Semibold is the standard reading weight — confident, not light.


### PPT-image Type Deployment

- Use `Wise Sans, fallback: Inter — OpenType "calt" on all text` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Inter, fallbacks: Helvetica, Arial` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Green Pill**
- Background: `#9fe870` (Wise Green)
- Text: `#163300` (Dark Green)
- Padding: 5px 16px
- Radius: 9999px
- Hover: scale(1.05) — button physically grows
- Active: scale(0.95) — button compresses
- Focus: inset ring + outline

**Secondary Subtle Pill**
- Background: `rgba(22, 51, 0, 0.08)` (dark green at 8% opacity)
- Text: `#0e0f0c`
- Padding: 8px 12px 8px 16px
- Radius: 9999px
- Same scale hover/active behavior

### Cards & Containers
- Radius: 16px (small), 30px (medium), 40px (large cards/tables)
- Border: `1px solid rgba(14,15,12,0.12)` or `1px solid #9fe870` (green accent)
- Shadow: `rgba(14,15,12,0.12) 0px 0px 0px 1px` (ring shadow)

### Navigation
- Green-tinted navigation hover: `rgba(211,242,192,0.4)`
- Clean header with Wise wordmark
- Pill CTAs right-aligned


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Wise's strongest visual cues as one large, unmistakable scene or object.
- Let Wise Green (#9fe870), Light Mint (#e2f6d5), and Near Black (#0e0f0c) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Wise.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Light Mint (#e2f6d5) versus Near Black (#0e0f0c), with Wise Green (#9fe870) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System and Border Radius Scale) to create clean fields for charts, numerals, or callouts.
- Avoid hero subjects that fight the actual data layer.

#### System / Workflow Plate

- Convert the original component logic into presentation diagrams, route maps, or structural visuals rather than literal product UI.
- Keep the image designed, not tool-generated: large shapes, few node types, deliberate connectors, and brand-consistent type.
- Depth should follow the source brand's strongest visual cues instead of generic infographic shadows.

#### Closing Poster

- Compress the deck's final judgment into one memorable frame.
- Use the same brand surfaces and accent hierarchy, but simplify harder than the cover.
- The closing image should resolve the story, not reopen complexity.

## 5. Layout Principles

### Original Layout DNA

### Spacing System
- Base unit: 8px
- Scale: 1px, 2px, 3px, 4px, 5px, 8px, 10px, 11px, 12px, 16px, 18px, 19px, 20px, 22px, 24px

### Border Radius Scale
- Minimal (2px): Links, inputs
- Standard (10px): Comboboxes, inputs
- Card (16px): Small cards, buttons, radio
- Medium (20px): Links, medium cards
- Large (30px): Feature cards
- Section (40px): Tables, large cards
- Mega (1000px): Presentation elements
- Pill (9999px): All buttons, images
- Circle (50%): Icons, badges


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Default |
| Ring (Level 1) | `rgba(14,15,12,0.12) 0px 0px 0px 1px` | Card borders |
| Inset (Level 2) | `rgb(134,134,133) 0px 0px 0px 1px inset` | Input focus |

**Shadow Philosophy**: Wise uses minimal shadows — ring shadows only. Depth comes from the bold green accent against the neutral canvas.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Wise Sans weight 900 for display — the extreme boldness IS the brand
- Apply line-height 0.85 on Wise Sans display — ultra-tight is intentional
- Use Lime Green (#9fe870) for primary CTAs with Dark Green (#163300) text
- Apply scale(1.05) hover and scale(0.95) active on buttons
- Enable "calt" on all text
- Use Inter weight 600 as the body default

### Don't
- Don't use light font weights for Wise Sans — only 900
- Don't relax the 0.85 line-height on display — the density is the identity
- Don't use the Wise Green as background for large surfaces — it's for buttons and accents
- Don't skip the scale animation on buttons
- Don't use traditional shadows — ring shadows only


### PPT-image Guardrails

- Do preserve the original mood before adding presentation convenience.
- Do generate from the slide thesis, not from the overall deck topic alone.
- Do leave room for editable slide text instead of baking everything into the image.
- Do keep one dominant idea per frame.
- Don't turn every slide into a homepage hero.
- Don't import off-brand gradients, stock photography tropes, or default AI wallpaper aesthetics.
- Don't bake unreadable microtext, fake dashboards, or dense UI chrome into supporting images unless the slide explicitly needs product UI.

## 8. Responsive Behavior

### Original UI Responsiveness

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <576px | Single column |
| Tablet | 576–992px | 2-column |
| Desktop | 992–1440px | Full layout |
| Large | >1440px | Expanded |


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Text: Near Black (`#0e0f0c`)
- Background: White (`#ffffff` / off-white)
- Accent: Wise Green (`#9fe870`)
- Button text: Dark Green (`#163300`)
- Secondary: Gray (`#868685`)

### Example Component Prompts
- "Create hero: white background. Headline at 96px Wise Sans weight 900, line-height 0.85, 'calt' enabled, #0e0f0c text. Green pill CTA (#9fe870, 9999px radius, 5px 16px padding, #163300 text). Hover: scale(1.05)."
- "Build a card: 30px radius, 1px solid rgba(14,15,12,0.12). Title at 22px Inter weight 600, body at 18px weight 400."

### Iteration Guide
1. Wise Sans 900 at 0.85 line-height — the extreme weight IS the brand
2. Lime Green for buttons only — dark green text on green background
3. Scale animations (1.05 hover, 0.95 active) on all interactive elements
4. "calt" on everything — contextual alternates are mandatory
5. Inter 600 for body — confident reading weight


### PPT-image Quick Reference

- Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
- Display voice: `Wise Sans, fallback: Inter — OpenType "calt" on all text`
- Body / label voice: `Inter, fallbacks: Helvetica, Arial`
- Primary accent: Wise Green (#9fe870)
- Light surface anchor: Light Mint (#e2f6d5)
- Dark surface anchor: Near Black (#0e0f0c)
- Signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, Inter body at weight 600 as default — confident, not light, and Near-black (#0e0f0c) primary with warm green undertone
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Wise.
Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
Use Wise Sans, fallback: Inter — OpenType "calt" on all text as the display-type reference and Inter, fallbacks: Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Light Mint (#e2f6d5), Near Black (#0e0f0c), and Wise Green (#9fe870).
Preserve these signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, and Inter body at weight 600 as default — confident, not light.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Wise.
Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
Use Wise Sans, fallback: Inter — OpenType "calt" on all text as the display-type reference and Inter, fallbacks: Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Light Mint (#e2f6d5), Near Black (#0e0f0c), and Wise Green (#9fe870).
Preserve these signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, and Inter body at weight 600 as default — confident, not light.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Wise.
Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
Use Wise Sans, fallback: Inter — OpenType "calt" on all text as the display-type reference and Inter, fallbacks: Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Light Mint (#e2f6d5), Near Black (#0e0f0c), and Wise Green (#9fe870).
Preserve these signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, and Inter body at weight 600 as default — confident, not light.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Wise.
Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
Use Wise Sans, fallback: Inter — OpenType "calt" on all text as the display-type reference and Inter, fallbacks: Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Light Mint (#e2f6d5), Near Black (#0e0f0c), and Wise Green (#9fe870).
Preserve these signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, and Inter body at weight 600 as default — confident, not light.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Wise.
Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
Use Wise Sans, fallback: Inter — OpenType "calt" on all text as the display-type reference and Inter, fallbacks: Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Light Mint (#e2f6d5), Near Black (#0e0f0c), and Wise Green (#9fe870).
Preserve these signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, and Inter body at weight 600 as default — confident, not light.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Wise.
Brand mood: Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent.
Use Wise Sans, fallback: Inter — OpenType "calt" on all text as the display-type reference and Inter, fallbacks: Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Light Mint (#e2f6d5), Near Black (#0e0f0c), and Wise Green (#9fe870).
Preserve these signature cues: Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines, Lime Green (#9fe870) accent with dark green text (#163300) — nature-inspired fintech, and Inter body at weight 600 as default — confident, not light.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
