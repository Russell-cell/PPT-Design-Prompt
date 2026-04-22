# PPT-image Design System Inspired by Miro

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Miro.

Source reference: `source/miro/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Miro's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font. The design uses a predominantly white canvas with near-black text (`#1c1c1e`) and a distinctive pastel color palette — coral, rose, teal, orange, yellow, moss — each representing different collaboration contexts.

The typography uses Roobert PRO Medium as the primary display font with OpenType character variants (`"blwf", "cv03", "cv04", "cv09", "cv11"`) and negative letter-spacing (-1.68px at 56px). Noto Sans handles body text with its own stylistic set (`"liga" 0, "ss01", "ss04", "ss05"`). The design is built with Framer, giving it smooth animations and modern component patterns.

**Key Characteristics:**
- White canvas with near-black (`#1c1c1e`) text
- Roobert PRO Medium with multiple OpenType character variants
- Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs)
- Blue 450 (`#5b76fe`) as primary interactive color
- Success green (`#00b473`) for positive states
- Generous border-radius: 8px–50px range
- Framer-built with smooth motion patterns
- Ring shadow border: `rgb(224,226,232) 0px 0px 0px 1px`


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs), and Blue 450 (#5b76fe) as primary interactive color.
- Use Blue 450 (#5b76fe) as the highest-signal accent when color needs to carry emphasis.
- Let White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#1c1c1e) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Near Black** (`#1c1c1e`): Primary text
- **White** (`#ffffff`): `--tw-color-white`, primary surface
- **Blue 450** (`#5b76fe`): `--tw-color-blue-450`, primary interactive
- **Actionable Pressed** (`#2a41b6`): `--tw-color-actionable-pressed`

### Pastel Accents (Light/Dark pairs)
- **Coral**: Light `#ffc6c6` / Dark `#600000`
- **Rose**: Light `#ffd8f4` / Dark (implied)
- **Teal**: Light `#c3faf5` / Dark `#187574`
- **Orange**: Light `#ffe6cd`
- **Yellow**: Dark `#746019`
- **Moss**: Dark `#187574`
- **Pink** (`#fde0f0`): Soft pink surface
- **Red** (`#fbd4d4`): Light red surface
- **Dark Red** (`#e3c5c5`): Muted red

### Semantic
- **Success** (`#00b473`): `--tw-color-success-accent`

### Neutral
- **Slate** (`#555a6a`): Secondary text
- **Input Placeholder** (`#a5a8b5`): `--tw-color-input-placeholder`
- **Border** (`#c7cad5`): Button borders
- **Ring** (`rgb(224,226,232)`): Shadow-as-border


### PPT-image Deployment

- Base canvas: prefer White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#1c1c1e) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Blue 450 (#5b76fe) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `Roobert PRO Medium`, fallback: Placeholder — `"blwf", "cv03", "cv04", "cv09", "cv11"`
- **Display Variants**: `Roobert PRO SemiBold`, `Roobert PRO SemiBold Italic`, `Roobert PRO`
- **Body**: `Noto Sans` — `"liga" 0, "ss01", "ss04", "ss05"`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Roobert PRO Medium | 56px | 400 | 1.15 | -1.68px |
| Section Heading | Roobert PRO Medium | 48px | 400 | 1.15 | -1.44px |
| Card Title | Roobert PRO Medium | 24px | 400 | 1.15 | -0.72px |
| Sub-heading | Noto Sans | 22px | 400 | 1.35 | -0.44px |
| Feature | Roobert PRO Medium | 18px | 600 | 1.35 | normal |
| Body | Noto Sans | 18px | 400 | 1.45 | normal |
| Body Standard | Noto Sans | 16px | 400–600 | 1.50 | -0.16px |
| Button | Roobert PRO Medium | 17.5px | 700 | 1.29 | 0.175px |
| Caption | Roobert PRO Medium | 14px | 400 | 1.71 | normal |
| Small | Roobert PRO Medium | 12px | 400 | 1.15 | -0.36px |
| Micro Uppercase | Roobert PRO | 10.5px | 400 | 0.90 | uppercase |


### PPT-image Type Deployment

- Use `Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11"` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Noto Sans — "liga" 0, "ss01", "ss04", "ss05"` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- Outlined: transparent bg, `1px solid #c7cad5`, 8px radius, 7px 12px padding
- White circle: 50% radius, white bg with shadow
- Blue primary (implied from interactive color)

### Cards: 12px–24px radius, pastel backgrounds
### Inputs: white bg, `1px solid #e9eaef`, 8px radius, 16px padding


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Miro's strongest visual cues as one large, unmistakable scene or object.
- Let Blue 450 (#5b76fe), White (#ffffff), and Near Black (#1c1c1e) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards: 12px–24px radius, pastel backgrounds, and Inputs: white bg, 1px solid #e9eaef, 8px radius, 16px padding rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Miro.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: White (#ffffff) versus Near Black (#1c1c1e), with Blue 450 (#5b76fe) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (the source brand's strongest visual cues) to create clean fields for charts, numerals, or callouts.
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

- Spacing: 1–24px base scale
- Radius: 8px (buttons), 10px–12px (cards), 20px–24px (panels), 40px–50px (large containers)
- Ring shadow: `rgb(224,226,232) 0px 0px 0px 1px`


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System

Minimal — ring shadow + pastel surface contrast


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use pastel light/dark pairs for feature sections
- Apply Roobert PRO with OpenType character variants
- Use Blue 450 (#5b76fe) for interactive elements
### Don't
- Don't use heavy shadows
- Don't mix more than 2 pastel accents per section


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

Breakpoints: 425px, 576px, 768px, 896px, 1024px, 1200px, 1280px, 1366px, 1700px, 1920px


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Text: Near Black (`#1c1c1e`)
- Background: White (`#ffffff`)
- Interactive: Blue 450 (`#5b76fe`)
- Success: `#00b473`
- Border: `#c7cad5`
### Example Component Prompts
- "Create hero: white background. Roobert PRO Medium 56px, line-height 1.15, letter-spacing -1.68px. Blue CTA (#5b76fe). Outlined secondary (1px solid #c7cad5, 8px radius)."


### PPT-image Quick Reference

- Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
- Display voice: `Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11"`
- Body / label voice: `Noto Sans — "liga" 0, "ss01", "ss04", "ss05"`
- Primary accent: Blue 450 (#5b76fe)
- Light surface anchor: White (#ffffff)
- Dark surface anchor: Near Black (#1c1c1e)
- Signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs), and Blue 450 (#5b76fe) as primary interactive color
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Miro.
Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
Use Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11" as the display-type reference and Noto Sans — "liga" 0, "ss01", "ss04", "ss05" for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#1c1c1e), and Blue 450 (#5b76fe).
Preserve these signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, and Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs).
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Miro.
Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
Use Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11" as the display-type reference and Noto Sans — "liga" 0, "ss01", "ss04", "ss05" for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#1c1c1e), and Blue 450 (#5b76fe).
Preserve these signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, and Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs).
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Miro.
Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
Use Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11" as the display-type reference and Noto Sans — "liga" 0, "ss01", "ss04", "ss05" for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#1c1c1e), and Blue 450 (#5b76fe).
Preserve these signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, and Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs).
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Miro.
Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
Use Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11" as the display-type reference and Noto Sans — "liga" 0, "ss01", "ss04", "ss05" for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#1c1c1e), and Blue 450 (#5b76fe).
Preserve these signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, and Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs).
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Miro.
Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
Use Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11" as the display-type reference and Noto Sans — "liga" 0, "ss01", "ss04", "ss05" for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#1c1c1e), and Blue 450 (#5b76fe).
Preserve these signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, and Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs).
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Miro.
Brand mood: Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font.
Use Roobert PRO Medium, fallback: Placeholder — "blwf", "cv03", "cv04", "cv09", "cv11" as the display-type reference and Noto Sans — "liga" 0, "ss01", "ss04", "ss05" for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#1c1c1e), and Blue 450 (#5b76fe).
Preserve these signature cues: White canvas with near-black (#1c1c1e) text, Roobert PRO Medium with multiple OpenType character variants, and Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs).
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
