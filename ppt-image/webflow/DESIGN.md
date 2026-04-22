# PPT-image Design System Inspired by Webflow

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Webflow.

Source reference: `source/webflow/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Webflow's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (`#146ef5`), and a rich secondary color palette (purple, pink, green, orange, yellow, red). The custom WF Visual Sans Variable font creates a confident, precise typographic system with weight 600 for display and 500 for body.

**Key Characteristics:**
- White canvas with near-black (`#080808`) text
- Webflow Blue (`#146ef5`) as primary brand + interactive color
- WF Visual Sans Variable — custom variable font with weight 500–600
- Rich secondary palette: purple `#7a3dff`, pink `#ed52cb`, green `#00d722`, orange `#ff6b00`, yellow `#ffae13`, red `#ee1d36`
- Conservative 4px–8px border-radius — sharp, not rounded
- Multi-layer shadow stacks (5-layer cascading shadows)
- Uppercase labels: 10px–15px, weight 500–600, wide letter-spacing (0.6px–1.5px)
- translate(6px) hover animation on buttons


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, WF Visual Sans Variable — custom variable font with weight 500–600, and Rich secondary palette: purple #7a3dff, pink #ed52cb, green #00d722, orange #ff6b00, yellow #ffae13, red #ee1d36.
- Use Webflow Blue (#146ef5) as the highest-signal accent when color needs to carry emphasis.
- Let Blue 400 (#3b89ff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#080808) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Near Black** (`#080808`): Primary text
- **Webflow Blue** (`#146ef5`): `--_color---primary--webflow-blue`, primary CTA and links
- **Blue 400** (`#3b89ff`): `--_color---primary--blue-400`, lighter interactive blue
- **Blue 300** (`#006acc`): `--_color---blue-300`, darker blue variant
- **Button Hover Blue** (`#0055d4`): `--mkto-embed-color-button-hover`

### Secondary Accents
- **Purple** (`#7a3dff`): `--_color---secondary--purple`
- **Pink** (`#ed52cb`): `--_color---secondary--pink`
- **Green** (`#00d722`): `--_color---secondary--green`
- **Orange** (`#ff6b00`): `--_color---secondary--orange`
- **Yellow** (`#ffae13`): `--_color---secondary--yellow`
- **Red** (`#ee1d36`): `--_color---secondary--red`

### Neutral
- **Gray 800** (`#222222`): Dark secondary text
- **Gray 700** (`#363636`): Mid text
- **Gray 300** (`#ababab`): Muted text, placeholder
- **Mid Gray** (`#5a5a5a`): Link text
- **Border Gray** (`#d8d8d8`): Borders, dividers
- **Border Hover** (`#898989`): Hover border

### Shadows
- **5-layer cascade**: `rgba(0,0,0,0) 0px 84px 24px, rgba(0,0,0,0.01) 0px 54px 22px, rgba(0,0,0,0.04) 0px 30px 18px, rgba(0,0,0,0.08) 0px 13px 13px, rgba(0,0,0,0.09) 0px 3px 7px`


### PPT-image Deployment

- Base canvas: prefer Blue 400 (#3b89ff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#080808) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Webflow Blue (#146ef5) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font: `WF Visual Sans Variable`, fallback: `Arial`

| Role | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|--------|-------------|----------------|-------|
| Display Hero | 80px | 600 | 1.04 | -0.8px | |
| Section Heading | 56px | 600 | 1.04 | normal | |
| Sub-heading | 32px | 500 | 1.30 | normal | |
| Feature Title | 24px | 500–600 | 1.30 | normal | |
| Body | 20px | 400–500 | 1.40–1.50 | normal | |
| Body Standard | 16px | 400–500 | 1.60 | -0.16px | |
| Button | 16px | 500 | 1.60 | -0.16px | |
| Uppercase Label | 15px | 500 | 1.30 | 1.5px | uppercase |
| Caption | 14px | 400–500 | 1.40–1.60 | normal | |
| Badge Uppercase | 12.8px | 550 | 1.20 | normal | uppercase |
| Micro Uppercase | 10px | 500–600 | 1.30 | 1px | uppercase |
| Code: Inconsolata (companion monospace font)


### PPT-image Type Deployment

- Use `System Sans` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `System Sans` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- Transparent: text `#080808`, translate(6px) on hover
- White circle: 50% radius, white bg
- Blue badge: `#146ef5` bg, 4px radius, weight 550

### Cards: `1px solid #d8d8d8`, 4px–8px radius
### Badges: Blue-tinted bg at 10% opacity, 4px radius


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Webflow's strongest visual cues as one large, unmistakable scene or object.
- Let Webflow Blue (#146ef5), Blue 400 (#3b89ff), and Near Black (#080808) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards: 1px solid #d8d8d8, 4px–8px radius, and Badges: Blue-tinted bg at 10% opacity, 4px radius rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Webflow.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Blue 400 (#3b89ff) versus Near Black (#080808), with Webflow Blue (#146ef5) reserved for the decisive signal.
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

- Spacing: fractional scale (1px, 2.4px, 3.2px, 4px, 5.6px, 6px, 7.2px, 8px, 9.6px, 12px, 16px, 24px)
- Radius: 2px, 4px, 8px, 50% — conservative, sharp
- Breakpoints: 479px, 768px, 992px


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System




### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

- Do: Use WF Visual Sans Variable at 500–600. Blue (#146ef5) for CTAs. 4px radius. translate(6px) hover.
- Don't: Round beyond 8px for functional elements. Use secondary colors on primary CTAs.


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




### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

- Text: Near Black (`#080808`)
- CTA: Webflow Blue (`#146ef5`)
- Background: White (`#ffffff`)
- Border: `#d8d8d8`
- Secondary: Purple `#7a3dff`, Pink `#ed52cb`, Green `#00d722`


### PPT-image Quick Reference

- Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
- Display voice: `System Sans`
- Body / label voice: `System Sans`
- Primary accent: Webflow Blue (#146ef5)
- Light surface anchor: Blue 400 (#3b89ff)
- Dark surface anchor: Near Black (#080808)
- Signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, WF Visual Sans Variable — custom variable font with weight 500–600, and Rich secondary palette: purple #7a3dff, pink #ed52cb, green #00d722, orange #ff6b00, yellow #ffae13, red #ee1d36
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Webflow.
Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
Use System Sans as the display-type reference and System Sans for any short in-image labels.
Keep the palette anchored in Blue 400 (#3b89ff), Near Black (#080808), and Webflow Blue (#146ef5).
Preserve these signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, and WF Visual Sans Variable — custom variable font with weight 500–600.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Webflow.
Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
Use System Sans as the display-type reference and System Sans for any short in-image labels.
Keep the palette anchored in Blue 400 (#3b89ff), Near Black (#080808), and Webflow Blue (#146ef5).
Preserve these signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, and WF Visual Sans Variable — custom variable font with weight 500–600.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Webflow.
Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
Use System Sans as the display-type reference and System Sans for any short in-image labels.
Keep the palette anchored in Blue 400 (#3b89ff), Near Black (#080808), and Webflow Blue (#146ef5).
Preserve these signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, and WF Visual Sans Variable — custom variable font with weight 500–600.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Webflow.
Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
Use System Sans as the display-type reference and System Sans for any short in-image labels.
Keep the palette anchored in Blue 400 (#3b89ff), Near Black (#080808), and Webflow Blue (#146ef5).
Preserve these signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, and WF Visual Sans Variable — custom variable font with weight 500–600.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Webflow.
Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
Use System Sans as the display-type reference and System Sans for any short in-image labels.
Keep the palette anchored in Blue 400 (#3b89ff), Near Black (#080808), and Webflow Blue (#146ef5).
Preserve these signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, and WF Visual Sans Variable — custom variable font with weight 500–600.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Webflow.
Brand mood: Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (#146ef5), and a rich secondary color palette (purple, pink, green, orange, yellow, red).
Use System Sans as the display-type reference and System Sans for any short in-image labels.
Keep the palette anchored in Blue 400 (#3b89ff), Near Black (#080808), and Webflow Blue (#146ef5).
Preserve these signature cues: White canvas with near-black (#080808) text, Webflow Blue (#146ef5) as primary brand + interactive color, and WF Visual Sans Variable — custom variable font with weight 500–600.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
