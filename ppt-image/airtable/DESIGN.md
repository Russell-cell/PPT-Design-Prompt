# PPT-image Design System Inspired by Airtable

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Airtable.

Source reference: `source/airtable/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Airtable's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (`#181d26`) and Airtable Blue (`#1b61c9`) as the primary interactive accent. The Haas font family (display + text variants) creates a Swiss-precision typography system with positive letter-spacing throughout.

**Key Characteristics:**
- White canvas with deep navy text (`#181d26`)
- Airtable Blue (`#1b61c9`) as primary CTA and link color
- Haas + Haas Groot Disp dual font system
- Positive letter-spacing on body text (0.08px–0.28px)
- 12px radius buttons, 16px–32px for cards
- Multi-layer blue-tinted shadow: `rgba(45,127,249,0.28) 0px 1px 3px`
- Semantic theme tokens: `--theme_*` CSS variable naming


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, Haas + Haas Groot Disp dual font system, and Positive letter-spacing on body text (0.08px–0.28px).
- Use Airtable Blue (#1b61c9) as the highest-signal accent when color needs to carry emphasis.
- Let White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Deep Navy (#181d26) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Deep Navy** (`#181d26`): Primary text
- **Airtable Blue** (`#1b61c9`): CTA buttons, links
- **White** (`#ffffff`): Primary surface
- **Spotlight** (`rgba(249,252,255,0.97)`): `--theme_button-text-spotlight`

### Semantic
- **Success Green** (`#006400`): `--theme_success-text`
- **Weak Text** (`rgba(4,14,32,0.69)`): `--theme_text-weak`
- **Secondary Active** (`rgba(7,12,20,0.82)`): `--theme_button-text-secondary-active`

### Neutral
- **Dark Gray** (`#333333`): Secondary text
- **Mid Blue** (`#254fad`): Link/accent blue variant
- **Border** (`#e0e2e6`): Card borders
- **Light Surface** (`#f8fafc`): Subtle surface

### Shadows
- **Blue-tinted** (`rgba(0,0,0,0.32) 0px 0px 1px, rgba(0,0,0,0.08) 0px 0px 2px, rgba(45,127,249,0.28) 0px 1px 3px, rgba(0,0,0,0.06) 0px 0px 0px 0.5px inset`)
- **Soft** (`rgba(15,48,106,0.05) 0px 0px 20px`)


### PPT-image Deployment

- Base canvas: prefer White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Deep Navy (#181d26) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Airtable Blue (#1b61c9) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Primary**: `Haas`, fallbacks: `-apple-system, system-ui, Segoe UI, Roboto`
- **Display**: `Haas Groot Disp`, fallback: `Haas`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Haas | 48px | 400 | 1.15 | normal |
| Display Bold | Haas Groot Disp | 48px | 900 | 1.50 | normal |
| Section Heading | Haas | 40px | 400 | 1.25 | normal |
| Sub-heading | Haas | 32px | 400–500 | 1.15–1.25 | normal |
| Card Title | Haas | 24px | 400 | 1.20–1.30 | 0.12px |
| Feature | Haas | 20px | 400 | 1.25–1.50 | 0.1px |
| Body | Haas | 18px | 400 | 1.35 | 0.18px |
| Body Medium | Haas | 16px | 500 | 1.30 | 0.08–0.16px |
| Button | Haas | 16px | 500 | 1.25–1.30 | 0.08px |
| Caption | Haas | 14px | 400–500 | 1.25–1.35 | 0.07–0.28px |


### PPT-image Type Deployment

- Use `Haas Groot Disp, fallback: Haas` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Haas Groot Disp, fallback: Haas` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- **Primary Blue**: `#1b61c9`, white text, 16px 24px padding, 12px radius
- **White**: white bg, `#181d26` text, 12px radius, 1px border white
- **Cookie Consent**: `#1b61c9` bg, 2px radius (sharp)

### Cards: `1px solid #e0e2e6`, 16px–24px radius
### Inputs: Standard Haas styling


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Airtable's strongest visual cues as one large, unmistakable scene or object.
- Let Airtable Blue (#1b61c9), White (#ffffff), and Deep Navy (#181d26) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards: 1px solid #e0e2e6, 16px–24px radius, and Inputs: Standard Haas styling rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Airtable.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: White (#ffffff) versus Deep Navy (#181d26), with Airtable Blue (#1b61c9) reserved for the decisive signal.
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

- Spacing: 1–48px (8px base)
- Radius: 2px (small), 12px (buttons), 16px (cards), 24px (sections), 32px (large), 50% (circles)


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System

- Blue-tinted multi-layer shadow system
- Soft ambient: `rgba(15,48,106,0.05) 0px 0px 20px`


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do: Use Airtable Blue for CTAs, Haas with positive tracking, 12px radius buttons
### Don't: Skip positive letter-spacing, use heavy shadows


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

Breakpoints: 425–1664px (23 breakpoints)


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

- Text: Deep Navy (`#181d26`)
- CTA: Airtable Blue (`#1b61c9`)
- Background: White (`#ffffff`)
- Border: `#e0e2e6`


### PPT-image Quick Reference

- Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
- Display voice: `Haas Groot Disp, fallback: Haas`
- Body / label voice: `Haas Groot Disp, fallback: Haas`
- Primary accent: Airtable Blue (#1b61c9)
- Light surface anchor: White (#ffffff)
- Dark surface anchor: Deep Navy (#181d26)
- Signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, Haas + Haas Groot Disp dual font system, and Positive letter-spacing on body text (0.08px–0.28px)
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Airtable.
Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
Use Haas Groot Disp, fallback: Haas as the display-type reference and Haas Groot Disp, fallback: Haas for any short in-image labels.
Keep the palette anchored in White (#ffffff), Deep Navy (#181d26), and Airtable Blue (#1b61c9).
Preserve these signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, and Haas + Haas Groot Disp dual font system.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Airtable.
Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
Use Haas Groot Disp, fallback: Haas as the display-type reference and Haas Groot Disp, fallback: Haas for any short in-image labels.
Keep the palette anchored in White (#ffffff), Deep Navy (#181d26), and Airtable Blue (#1b61c9).
Preserve these signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, and Haas + Haas Groot Disp dual font system.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Airtable.
Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
Use Haas Groot Disp, fallback: Haas as the display-type reference and Haas Groot Disp, fallback: Haas for any short in-image labels.
Keep the palette anchored in White (#ffffff), Deep Navy (#181d26), and Airtable Blue (#1b61c9).
Preserve these signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, and Haas + Haas Groot Disp dual font system.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Airtable.
Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
Use Haas Groot Disp, fallback: Haas as the display-type reference and Haas Groot Disp, fallback: Haas for any short in-image labels.
Keep the palette anchored in White (#ffffff), Deep Navy (#181d26), and Airtable Blue (#1b61c9).
Preserve these signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, and Haas + Haas Groot Disp dual font system.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Airtable.
Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
Use Haas Groot Disp, fallback: Haas as the display-type reference and Haas Groot Disp, fallback: Haas for any short in-image labels.
Keep the palette anchored in White (#ffffff), Deep Navy (#181d26), and Airtable Blue (#1b61c9).
Preserve these signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, and Haas + Haas Groot Disp dual font system.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Airtable.
Brand mood: Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas with deep navy text (#181d26) and Airtable Blue (#1b61c9) as the primary interactive accent.
Use Haas Groot Disp, fallback: Haas as the display-type reference and Haas Groot Disp, fallback: Haas for any short in-image labels.
Keep the palette anchored in White (#ffffff), Deep Navy (#181d26), and Airtable Blue (#1b61c9).
Preserve these signature cues: White canvas with deep navy text (#181d26), Airtable Blue (#1b61c9) as primary CTA and link color, and Haas + Haas Groot Disp dual font system.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
