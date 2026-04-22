# PPT-image Design System Inspired by Coinbase

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Coinbase.

Source reference: `source/coinbase/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Coinbase's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette. The design uses Coinbase Blue (`#0052ff`) — a deep, saturated blue — as the singular brand accent against white and near-black surfaces. The proprietary font family includes CoinbaseDisplay for hero headlines, CoinbaseSans for UI text, CoinbaseText for body reading, and CoinbaseIcons for iconography — a comprehensive four-font system.

The button system uses a distinctive 56px radius for pill-shaped CTAs with hover transitions to a lighter blue (`#578bfa`). The design alternates between white content sections and dark (`#0a0b0d`, `#282b31`) feature sections, creating a professional, financial-grade interface.

**Key Characteristics:**
- Coinbase Blue (`#0052ff`) as singular brand accent
- Four-font proprietary family: Display, Sans, Text, Icons
- 56px radius pill buttons with blue hover transition
- Near-black (`#0a0b0d`) dark sections + white light sections
- 1.00 line-height on display headings — ultra-tight
- Cool gray secondary surface (`#eef0f3`) with blue tint
- `text-transform: lowercase` on some button labels — unusual


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, 56px radius pill buttons with blue hover transition, and Near-black (#0a0b0d) dark sections + white light sections.
- Use Coinbase Blue (#0052ff) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#0a0b0d) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Coinbase Blue** (`#0052ff`): Primary brand, links, CTA borders
- **Pure White** (`#ffffff`): Primary light surface
- **Near Black** (`#0a0b0d`): Text, dark section backgrounds
- **Cool Gray Surface** (`#eef0f3`): Secondary button background

### Interactive
- **Hover Blue** (`#578bfa`): Button hover background
- **Link Blue** (`#0667d0`): Secondary link color
- **Muted Blue** (`#5b616e`): Border color at 20% opacity

### Surface
- **Dark Card** (`#282b31`): Dark button/card backgrounds
- **Light Surface** (`rgba(247,247,247,0.88)`): Subtle surface


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#0a0b0d) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Coinbase Blue (#0052ff) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `CoinbaseDisplay` — hero headlines
- **UI / Sans**: `CoinbaseSans` — buttons, headings, nav
- **Body**: `CoinbaseText` — reading text
- **Icons**: `CoinbaseIcons` — icon font

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display Hero | CoinbaseDisplay | 80px | 400 | 1.00 (tight) | Maximum impact |
| Display Secondary | CoinbaseDisplay | 64px | 400 | 1.00 | Sub-hero |
| Display Third | CoinbaseDisplay | 52px | 400 | 1.00 | Third tier |
| Section Heading | CoinbaseSans | 36px | 400 | 1.11 (tight) | Feature sections |
| Card Title | CoinbaseSans | 32px | 400 | 1.13 | Card headings |
| Feature Title | CoinbaseSans | 18px | 600 | 1.33 | Feature emphasis |
| Body Bold | CoinbaseSans | 16px | 700 | 1.50 | Strong body |
| Body Semibold | CoinbaseSans | 16px | 600 | 1.25 | Buttons, nav |
| Body | CoinbaseText | 18px | 400 | 1.56 | Standard reading |
| Body Small | CoinbaseText | 16px | 400 | 1.50 | Secondary reading |
| Button | CoinbaseSans | 16px | 600 | 1.20 | +0.16px tracking |
| Caption | CoinbaseSans | 14px | 600–700 | 1.50 | Metadata |
| Small | CoinbaseSans | 13px | 600 | 1.23 | Tags |


### PPT-image Type Deployment

- Use `CoinbaseDisplay — hero headlines` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `CoinbaseSans — buttons, headings, nav` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Pill (56px radius)**
- Background: `#eef0f3` or `#282b31`
- Radius: 56px
- Border: `1px solid` matching background
- Hover: `#578bfa` (light blue)
- Focus: `2px solid black` outline

**Full Pill (100000px radius)**
- Used for maximum pill shape

**Blue Bordered**
- Border: `1px solid #0052ff`
- Background: transparent

### Cards & Containers
- Radius: 8px–40px range
- Borders: `1px solid rgba(91,97,110,0.2)`


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Coinbase's strongest visual cues as one large, unmistakable scene or object.
- Let Coinbase Blue (#0052ff), Pure White (#ffffff), and Near Black (#0a0b0d) establish the hierarchy before adding any text.
- Pull attitude from Buttons and Cards & Containers rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Coinbase.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Near Black (#0a0b0d), with Coinbase Blue (#0052ff) reserved for the decisive signal.
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
- Base: 8px
- Scale: 1px, 3px, 4px, 5px, 6px, 8px, 10px, 12px, 15px, 16px, 20px, 24px, 25px, 32px, 48px

### Border Radius Scale
- Small (4px–8px): Article links, small cards
- Standard (12px–16px): Cards, menus
- Large (24px–32px): Feature containers
- XL (40px): Large buttons/containers
- Pill (56px): Primary CTAs
- Full (100000px): Maximum pill


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System

Minimal shadow system — depth from color contrast between dark/light sections.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Coinbase Blue (#0052ff) for primary interactive elements
- Apply 56px radius for all CTA buttons
- Use CoinbaseDisplay for hero headings only
- Alternate dark (#0a0b0d) and white sections

### Don't
- Don't use the blue decoratively — it's functional only
- Don't use sharp corners on CTAs — 56px minimum


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

Breakpoints: 400px, 576px, 640px, 768px, 896px, 1280px, 1440px, 1600px


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Brand: Coinbase Blue (`#0052ff`)
- Background: White (`#ffffff`)
- Dark surface: `#0a0b0d`
- Secondary surface: `#eef0f3`
- Hover: `#578bfa`
- Text: `#0a0b0d`

### Example Component Prompts
- "Create hero: white background. CoinbaseDisplay 80px, line-height 1.00. Pill CTA (#eef0f3, 56px radius). Hover: #578bfa."
- "Build dark section: #0a0b0d background. CoinbaseDisplay 64px white text. Blue accent link (#0052ff)."


### PPT-image Quick Reference

- Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
- Display voice: `CoinbaseDisplay — hero headlines`
- Body / label voice: `CoinbaseSans — buttons, headings, nav`
- Primary accent: Coinbase Blue (#0052ff)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Near Black (#0a0b0d)
- Signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, 56px radius pill buttons with blue hover transition, and Near-black (#0a0b0d) dark sections + white light sections
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Coinbase.
Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
Use CoinbaseDisplay — hero headlines as the display-type reference and CoinbaseSans — buttons, headings, nav for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0a0b0d), and Coinbase Blue (#0052ff).
Preserve these signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, and 56px radius pill buttons with blue hover transition.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Coinbase.
Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
Use CoinbaseDisplay — hero headlines as the display-type reference and CoinbaseSans — buttons, headings, nav for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0a0b0d), and Coinbase Blue (#0052ff).
Preserve these signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, and 56px radius pill buttons with blue hover transition.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Coinbase.
Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
Use CoinbaseDisplay — hero headlines as the display-type reference and CoinbaseSans — buttons, headings, nav for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0a0b0d), and Coinbase Blue (#0052ff).
Preserve these signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, and 56px radius pill buttons with blue hover transition.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Coinbase.
Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
Use CoinbaseDisplay — hero headlines as the display-type reference and CoinbaseSans — buttons, headings, nav for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0a0b0d), and Coinbase Blue (#0052ff).
Preserve these signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, and 56px radius pill buttons with blue hover transition.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Coinbase.
Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
Use CoinbaseDisplay — hero headlines as the display-type reference and CoinbaseSans — buttons, headings, nav for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0a0b0d), and Coinbase Blue (#0052ff).
Preserve these signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, and 56px radius pill buttons with blue hover transition.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Coinbase.
Brand mood: Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette.
Use CoinbaseDisplay — hero headlines as the display-type reference and CoinbaseSans — buttons, headings, nav for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0a0b0d), and Coinbase Blue (#0052ff).
Preserve these signature cues: Coinbase Blue (#0052ff) as singular brand accent, Four-font proprietary family: Display, Sans, Text, Icons, and 56px radius pill buttons with blue hover transition.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
