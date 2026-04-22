# PPT-image Design System Inspired by SpaceX

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably SpaceX.

Source reference: `source/spacex/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps SpaceX's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery. The design is pure black (`#000000`) with photography of rockets, space, and planets occupying 100% of the viewport. Text overlays sit directly on these photographs with no background panels, cards, or containers — just type on image, bold and unapologetic.

The typography system uses D-DIN, an industrial geometric typeface with DIN heritage (the German industrial standard). The defining characteristic is that virtually ALL text is uppercase with positive letter-spacing (0.96px–1.17px), creating a military/aerospace labeling system where every word feels stenciled onto a spacecraft hull. D-DIN-Bold at 48px with uppercase and 0.96px tracking for the hero creates headlines that feel like mission briefing titles. Even body text at 16px maintains the uppercase/tracked treatment at smaller scales.

What makes SpaceX distinctive is its radical minimalism: no shadows, no borders (except one ghost button border at `rgba(240,240,250,0.35)`), no color (only black and a spectral near-white `#f0f0fa`), no cards, no grids. The only visual element is photography + text. The ghost button with `rgba(240,240,250,0.1)` background and 32px radius is the sole interactive element — barely visible, floating over the imagery like a heads-up display. This isn't a design system in the traditional sense — it's a photographic exhibition with a type system and a single button.

**Key Characteristics:**
- Pure black canvas with full-viewport cinematic photography — the interface is invisible
- D-DIN / D-DIN-Bold — industrial DIN-heritage typeface
- Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic
- Near-white spectral text (`#f0f0fa`) — not pure white, a slight blue-violet tint
- Zero shadows, zero cards, zero containers — text on image only
- Single ghost button: `rgba(240,240,250,0.1)` background with spectral border
- Full-viewport sections — each section is a cinematic "scene"
- No decorative elements — every pixel serves the photography


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic, and Near-white spectral text (#f0f0fa) — not pure white, a slight blue-violet tint.
- Use Spectral White (#f0f0fa) as the highest-signal accent when color needs to carry emphasis.
- Let Spectral White (#f0f0fa) carry calmer title-safe zones and quieter data-support slides.
- Use Space Black (#000000) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Space Black** (`#000000`): Page background, the void of space — at 50% opacity for overlay gradient
- **Spectral White** (`#f0f0fa`): Text color — not pure white, a slight blue-violet tint that mimics starlight

### Interactive
- **Ghost Surface** (`rgba(240, 240, 250, 0.1)`): Button background — nearly invisible, 10% opacity
- **Ghost Border** (`rgba(240, 240, 250, 0.35)`): Button border — spectral, 35% opacity
- **Hover White** (`var(--white-100)`): Link hover state — full spectral white

### Gradient
- **Dark Overlay** (`rgba(0, 0, 0, 0.5)`): Gradient overlay on photographs to ensure text legibility


### PPT-image Deployment

- Base canvas: prefer Spectral White (#f0f0fa) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Space Black (#000000) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Spectral White (#f0f0fa) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `D-DIN-Bold` — bold industrial geometric
- **Body / UI**: `D-DIN`, fallbacks: `Arial, Verdana`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | D-DIN-Bold | 48px (3.00rem) | 700 | 1.00 (tight) | 0.96px | `text-transform: uppercase` |
| Body | D-DIN | 16px (1.00rem) | 400 | 1.50–1.70 | normal | Standard reading text |
| Nav Link Bold | D-DIN | 13px (0.81rem) | 700 | 0.94 (tight) | 1.17px | `text-transform: uppercase` |
| Nav Link | D-DIN | 12px (0.75rem) | 400 | 2.00 (relaxed) | normal | `text-transform: uppercase` |
| Caption Bold | D-DIN | 13px (0.81rem) | 700 | 0.94 (tight) | 1.17px | `text-transform: uppercase` |
| Caption | D-DIN | 12px (0.75rem) | 400 | 1.00 (tight) | normal | `text-transform: uppercase` |
| Micro | D-DIN | 10px (0.63rem) | 400 | 0.94 (tight) | 1px | `text-transform: uppercase` |

### Principles
- **Universal uppercase**: Nearly every text element uses `text-transform: uppercase`. This creates a systematic military/aerospace voice where all communication feels like official documentation.
- **Positive letter-spacing as identity**: 0.96px on display, 1.17px on nav — the wide tracking creates the stenciled, industrial feel that connects to DIN's heritage as a German engineering standard.
- **Two weights, strict hierarchy**: D-DIN-Bold (700) for headlines and nav emphasis, D-DIN (400) for body. No medium or semibold weights exist in the system.
- **Tight line-heights**: 0.94–1.00 across most text — compressed, efficient, mission-critical communication.


### PPT-image Type Deployment

- Use `D-DIN-Bold — bold industrial geometric` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `D-DIN, fallbacks: Arial, Verdana` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Ghost Button**
- Background: `rgba(240, 240, 250, 0.1)` (barely visible)
- Text: Spectral White (`#f0f0fa`)
- Padding: 18px
- Radius: 32px
- Border: `1px solid rgba(240, 240, 250, 0.35)`
- Hover: background brightens, text to `var(--white-100)`
- Use: The only button variant — "LEARN MORE" CTAs on photography

### Cards & Containers
- **None.** SpaceX does not use cards, panels, or containers. All content is text directly on full-viewport photographs. The absence of containers IS the design.

### Inputs & Forms
- Not present on the homepage. The site is purely presentational.

### Navigation
- Transparent overlay nav on photography
- D-DIN 13px weight 700, uppercase, 1.17px tracking
- Spectral white text on dark imagery
- Logo: SpaceX wordmark at 147x19px
- Mobile: hamburger collapse

### Image Treatment
- Full-viewport (100vh) photography sections
- Professional aerospace photography: rockets, Mars, space
- Dark gradient overlays (`rgba(0,0,0,0.5)`) for text legibility
- Each section = one full-screen photograph with text overlay
- No border radius, no frames — edge-to-edge imagery


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use SpaceX's strongest visual cues as one large, unmistakable scene or object.
- Let Spectral White (#f0f0fa), Spectral White (#f0f0fa), and Space Black (#000000) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to SpaceX.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Spectral White (#f0f0fa) versus Space Black (#000000), with Spectral White (#f0f0fa) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System, Grid & Container, and Whitespace Philosophy) to create clean fields for charts, numerals, or callouts.
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
- Scale: 3px, 5px, 12px, 15px, 18px, 20px, 24px, 30px
- Minimal scale — spacing is not the organizing principle; photography is

### Grid & Container
- No traditional grid — each section is a full-viewport cinematic frame
- Text is positioned absolutely or with generous padding over imagery
- Left-aligned text blocks on photography backgrounds
- No max-width container — content bleeds to viewport edges

### Whitespace Philosophy
- **Photography IS the whitespace**: Empty space in the design is never empty — it's filled with the dark expanse of space, the curve of a planet, or the flame of a rocket engine. Traditional whitespace concepts don't apply.
- **Vertical pacing through viewport**: Each section is exactly one viewport tall, creating a rhythmic scroll where each "page" reveals a new scene.

### Border Radius Scale
- Sharp (4px): Small dividers, utility elements
- Button (32px): Ghost buttons — the only rounded element


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
| Photography (Level 0) | Full-viewport imagery | Background layer — always present |
| Overlay (Level 1) | `rgba(0, 0, 0, 0.5)` gradient | Text legibility layer over photography |
| Text (Level 2) | Spectral white text, no shadow | Content layer — text floats directly on image |
| Ghost (Level 3) | `rgba(240, 240, 250, 0.1)` surface | Barely-visible interactive layer |

**Shadow Philosophy**: SpaceX uses ZERO shadows. In a design built entirely on photography, shadows are meaningless — every surface is already a photograph with natural lighting. Depth comes from the photographic content itself: the receding curvature of Earth, the diminishing trail of a rocket, the atmospheric haze around Mars.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use full-viewport photography as the primary design element — every section is a scene
- Apply uppercase + positive letter-spacing to ALL text — the aerospace stencil voice
- Use D-DIN exclusively — no other fonts exist in the system
- Keep the color palette to black + spectral white (`#f0f0fa`) only
- Use ghost buttons (`rgba(240,240,250,0.1)`) as the sole interactive element
- Apply dark gradient overlays for text legibility on photographs
- Let photography carry the emotional weight — the type system is functional, not expressive

### Don't
- Don't add cards, panels, or containers — text sits directly on photography
- Don't use shadows — they have no meaning in a photographic context
- Don't introduce colors — the palette is strictly achromatic with spectral tint
- Don't use sentence case — everything is uppercase
- Don't use negative letter-spacing — all tracking is positive (0.96px–1.17px)
- Don't reduce photography to thumbnails — every image is full-viewport
- Don't add decorative elements (icons, badges, dividers) — the design is photography + type + one button


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
| Mobile | <600px | Stacked, reduced padding, smaller type |
| Tablet Small | 600–960px | Adjusted layout |
| Tablet | 960–1280px | Standard scaling |
| Desktop | 1280–1350px | Full layout |
| Large Desktop | 1350–1500px | Expanded |
| Ultra-wide | >1500px | Maximum viewport |

### Touch Targets
- Ghost buttons: 18px padding provides adequate touch area
- Navigation links: uppercase with generous letter-spacing aids readability

### Collapsing Strategy
- Photography: maintains full-viewport at all sizes, content reposition
- Hero text: 48px → scales down proportionally
- Navigation: horizontal → hamburger
- Text blocks: reposition but maintain overlay-on-photography pattern
- Full-viewport sections maintained on mobile

### Image Behavior
- Edge-to-edge photography at all viewport sizes
- Background-size: cover with center focus
- Dark overlay gradients adapt to content position
- No art direction changes — same photographs, responsive positioning


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Background: Space Black (`#000000`)
- Text: Spectral White (`#f0f0fa`)
- Button background: Ghost (`rgba(240, 240, 250, 0.1)`)
- Button border: Ghost Border (`rgba(240, 240, 250, 0.35)`)
- Overlay: `rgba(0, 0, 0, 0.5)`

### Example Component Prompts
- "Create a full-viewport hero: background-image covering 100vh, dark gradient overlay rgba(0,0,0,0.5). Headline at 48px D-DIN-Bold, uppercase, letter-spacing 0.96px, spectral white (#f0f0fa) text. Ghost CTA button: rgba(240,240,250,0.1) bg, 1px solid rgba(240,240,250,0.35) border, 32px radius, 18px padding."
- "Design a navigation: transparent over photography. D-DIN 13px weight 700, uppercase, letter-spacing 1.17px, spectral white text. SpaceX wordmark left-aligned."
- "Build a content section: full-viewport height, background photography with dark overlay. Left-aligned text block with 48px D-DIN-Bold uppercase heading, 16px D-DIN body text, and ghost button below."
- "Create a micro label: D-DIN 10px, uppercase, letter-spacing 1px, spectral white, line-height 0.94."

### Iteration Guide
1. Start with photography — the image IS the design
2. All text is uppercase with positive letter-spacing — no exceptions
3. Only two colors: black and spectral white (#f0f0fa)
4. Ghost buttons are the only interactive element — transparent, spectral-bordered
5. Zero shadows, zero cards, zero decorative elements
6. Every section is full-viewport (100vh) — cinematic pacing


### PPT-image Quick Reference

- Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
- Display voice: `D-DIN-Bold — bold industrial geometric`
- Body / label voice: `D-DIN, fallbacks: Arial, Verdana`
- Primary accent: Spectral White (#f0f0fa)
- Light surface anchor: Spectral White (#f0f0fa)
- Dark surface anchor: Space Black (#000000)
- Signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic, and Near-white spectral text (#f0f0fa) — not pure white, a slight blue-violet tint
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by SpaceX.
Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
Use D-DIN-Bold — bold industrial geometric as the display-type reference and D-DIN, fallbacks: Arial, Verdana for any short in-image labels.
Keep the palette anchored in Spectral White (#f0f0fa), Space Black (#000000), and Spectral White (#f0f0fa).
Preserve these signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, and Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by SpaceX.
Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
Use D-DIN-Bold — bold industrial geometric as the display-type reference and D-DIN, fallbacks: Arial, Verdana for any short in-image labels.
Keep the palette anchored in Spectral White (#f0f0fa), Space Black (#000000), and Spectral White (#f0f0fa).
Preserve these signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, and Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by SpaceX.
Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
Use D-DIN-Bold — bold industrial geometric as the display-type reference and D-DIN, fallbacks: Arial, Verdana for any short in-image labels.
Keep the palette anchored in Spectral White (#f0f0fa), Space Black (#000000), and Spectral White (#f0f0fa).
Preserve these signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, and Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by SpaceX.
Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
Use D-DIN-Bold — bold industrial geometric as the display-type reference and D-DIN, fallbacks: Arial, Verdana for any short in-image labels.
Keep the palette anchored in Spectral White (#f0f0fa), Space Black (#000000), and Spectral White (#f0f0fa).
Preserve these signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, and Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by SpaceX.
Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
Use D-DIN-Bold — bold industrial geometric as the display-type reference and D-DIN, fallbacks: Arial, Verdana for any short in-image labels.
Keep the palette anchored in Spectral White (#f0f0fa), Space Black (#000000), and Spectral White (#f0f0fa).
Preserve these signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, and Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by SpaceX.
Brand mood: SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery.
Use D-DIN-Bold — bold industrial geometric as the display-type reference and D-DIN, fallbacks: Arial, Verdana for any short in-image labels.
Keep the palette anchored in Spectral White (#f0f0fa), Space Black (#000000), and Spectral White (#f0f0fa).
Preserve these signature cues: Pure black canvas with full-viewport cinematic photography — the interface is invisible, D-DIN / D-DIN-Bold — industrial DIN-heritage typeface, and Universal uppercase + positive letter-spacing (0.96px–1.17px) — aerospace stencil aesthetic.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
