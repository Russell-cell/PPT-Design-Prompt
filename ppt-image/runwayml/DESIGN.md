# PPT-image Design System Inspired by Runway

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Runway.

Source reference: `source/runwayml/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Runway's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements. This is not a typical tech product page; it's a visual manifesto for AI-powered creativity. Every section feels like a frame from a film: dramatic lighting, sweeping landscapes, and intimate human moments captured in high-quality imagery that dominates the viewport.

The design language is built on a single typeface — abcNormal — a clean, geometric sans-serif that handles everything from 48px display headlines to 11px uppercase labels. This single-font commitment creates an extreme typographic uniformity that lets the visual content speak louder than the text. Headlines use tight line-heights (1.0) with negative letter-spacing (-0.9px to -1.2px), creating compressed text blocks that feel like film titles rather than marketing copy.

What makes Runway distinctive is its complete commitment to visual content as design. Rather than illustrating features with icons or diagrams, Runway shows actual AI-generated and AI-enhanced imagery — cars driving through cinematic landscapes, artistic portraits, architectural renders. The interface itself retreats into near-invisibility: minimal borders, zero shadows, subtle cool-gray text, and a dark palette that puts maximum focus on the photography.

**Key Characteristics:**
- Cinematic full-bleed photography and video as primary UI elements
- Single typeface system: abcNormal for everything from display to micro labels
- Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e)
- Zero shadows, minimal borders — the interface is intentionally invisible
- Tight display typography (line-height 1.0) with negative tracking (-0.9px to -1.2px)
- Uppercase labels with positive letter-spacing for navigational structure
- Weight 450 (unusual intermediate) for small uppercase text — precision craft
- Editorial magazine layout with mixed-size image grids


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e), and Zero shadows, minimal borders — the interface is intentionally invisible.
- Use Runway Black (#000000) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Deep Black (#030303) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Runway Black** (`#000000`): The primary page background and maximum-emphasis text.
- **Deep Black** (`#030303`): A near-imperceptible variant for layered dark surfaces.
- **Dark Surface** (`#1a1a1a`): Card backgrounds and elevated dark containers.
- **Pure White** (`#ffffff`): Primary text on dark surfaces and light-section backgrounds.

### Surface & Background
- **Near White** (`#fefefe`): The lightest surface — barely distinguishable from pure white.
- **Cool Cloud** (`#e9ecf2`): Light section backgrounds with a cool blue-gray tint.
- **Border Dark** (`#27272a`): The single dark-mode border color — barely visible containment.

### Neutrals & Text
- **Charcoal** (`#404040`): Primary body text on light surfaces and secondary text.
- **Near Charcoal** (`#3f3f3f`): Slightly lighter variant for dark-section secondary text.
- **Cool Slate** (`#767d88`): Secondary body text — a distinctly blue-gray cool neutral.
- **Mid Slate** (`#7d848e`): Tertiary text, metadata descriptions.
- **Muted Gray** (`#a7a7a7`): De-emphasized content, timestamps.
- **Cool Silver** (`#c9ccd1`): Light borders and dividers.
- **Light Silver** (`#d0d4d4`): The lightest border/divider variant.
- **Tailwind Gray** (`#6b7280`): Standard Tailwind neutral for supplementary text.
- **Dark Link** (`#0c0c0c`): Darkest link text — nearly black.
- **Footer Gray** (`#999999`): Footer links and deeply muted content.

### Gradient System
- **None in the interface.** Visual richness comes entirely from photographic content — AI-generated and enhanced imagery provides all the color and gradient the design needs. The interface itself is intentionally colorless.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Deep Black (#030303) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Runway Black (#000000) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Universal**: `abcNormal`, with fallback: `abcNormal Fallback`

*Note: abcNormal is a custom geometric sans-serif. For external implementations, Inter or DM Sans serve as close substitutes.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | abcNormal | 48px (3rem) | 400 | 1.00 (tight) | -1.2px | Maximum size, film-title presence |
| Section Heading | abcNormal | 40px (2.5rem) | 400 | 1.00–1.10 | -1px to 0px | Feature section titles |
| Sub-heading | abcNormal | 36px (2.25rem) | 400 | 1.00 (tight) | -0.9px | Secondary section markers |
| Card Title | abcNormal | 24px (1.5rem) | 400 | 1.00 (tight) | normal | Article and card headings |
| Feature Title | abcNormal | 20px (1.25rem) | 400 | 1.00 (tight) | normal | Small headings |
| Body / Button | abcNormal | 16px (1rem) | 400–600 | 1.30–1.50 | -0.16px to normal | Standard body, nav links |
| Caption / Label | abcNormal | 14px (0.88rem) | 500–600 | 1.25–1.43 | 0.35px (uppercase) | Metadata, section labels |
| Small | abcNormal | 13px (0.81rem) | 400 | 1.30 (tight) | -0.16px to -0.26px | Compact descriptions |
| Micro / Tag | abcNormal | 11px (0.69rem) | 450 | 1.30 (tight) | normal | Uppercase tags, tiny labels |

### Principles
- **One typeface, complete expression**: abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching.
- **Tight everywhere**: Nearly every size uses line-height 1.0–1.30 — even body text is relatively compressed. This creates a dense, editorial feel.
- **Weight 450 — the precision detail**: Some small uppercase labels use weight 450, an uncommon intermediate between regular (400) and medium (500). This micro-craft signals typographic sophistication.
- **Negative tracking as default**: Even body text uses -0.16px to -0.26px letter-spacing, keeping everything slightly tighter than default.
- **Uppercase as structure**: Labels at 14px and 11px use `text-transform: uppercase` with positive letter-spacing (0.35px) to create navigational signposts that contrast with the tight lowercase text.


### PPT-image Type Deployment

- Use `abcNormal / fallback: abcNormal Fallback` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching.` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- Text: weight 600 at 14px abcNormal
- Background: likely transparent or dark, with minimal border
- Radius: small (4px) for button-like links
- The button design is extremely restrained — no heavy fills or borders detected
- Interactive elements blend into the editorial flow

### Cards & Containers
- Background: transparent or Dark Surface (`#1a1a1a`)
- Border: `1px solid #27272a` (dark mode) — barely visible containment
- Radius: small (4–8px) for functional elements; 16px for alert-style containers
- Shadow: zero — no shadows on any element
- Cards are primarily photographic — the image IS the card

### Navigation
- Minimal horizontal nav — transparent over hero content
- Logo: Runway wordmark in white/black
- Links: abcNormal at 16px, weight 400–600
- Hover: text shifts to white or higher opacity
- Extremely subtle — designed to not compete with visual content

### Image Treatment
- Full-bleed cinematic photography and video dominate
- AI-generated content shown at large scale as primary visual elements
- Mixed-size image grids creating editorial magazine layouts
- Dark overlays on hero images for text readability
- Product screenshots with subtle rounded corners (8px)

### Distinctive Components

**Cinematic Hero**
- Full-viewport image or video with text overlay
- Headline in 48px abcNormal, white on dark imagery
- The image is always cinematic quality — film-grade composition

**Research Article Cards**
- Photographic thumbnails with article titles
- Mixed-size grid layout (large feature + smaller supporting)
- Clean text overlay or below-image caption style

**Trust Bar**
- Company logos (leading organizations across industries)
- Clean, monochrome treatment
- Horizontal layout with generous spacing

**Mission Statement**
- "We are building AI to simulate the world through imagination, art and aesthetics"
- On a dark background with white text
- The emotional close — artistic and philosophical


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Runway's strongest visual cues as one large, unmistakable scene or object.
- Let Runway Black (#000000), Pure White (#ffffff), and Deep Black (#030303) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Navigation, and Image Treatment rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Runway.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Deep Black (#030303), with Runway Black (#000000) reserved for the decisive signal.
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
- Scale: 4px, 6px, 8px, 12px, 16px, 20px, 24px, 28px, 32px, 48px, 64px, 78px
- Section vertical spacing: generous (48–78px)
- Component gaps: 16–24px

### Grid & Container
- Max container width: up to 1600px (cinema-wide)
- Hero: full-viewport, edge-to-edge
- Content sections: centered with generous margins
- Image grids: asymmetric, magazine-style mixed sizes
- Footer: full-width dark section

### Whitespace Philosophy
- **Cinema-grade breathing**: Large vertical gaps between sections create a scrolling experience that feels like watching scenes change.
- **Images replace whitespace**: Where other sites use empty space, Runway fills it with photography. The visual content IS the breathing room.
- **Editorial grid asymmetry**: The image grid uses intentionally varied sizes — large hero images paired with smaller supporting images, creating visual rhythm.

### Border Radius Scale
- Sharp (4px): Buttons, small interactive elements
- Subtle (6px): Links, small containers
- Comfortable (8px): Standard containers, image cards
- Generous (16px): Alert-style containers, featured elements


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
| Flat (Level 0) | No shadow, no border | Everything — the dominant state |
| Bordered (Level 1) | `1px solid #27272a` | Alert containers only |
| Dark Section (Level 2) | Dark bg (#000000 / #1a1a1a) with light text | Hero, features, footer |
| Light Section (Level 3) | White/Cool Cloud bg with dark text | Content sections, research |

**Shadow Philosophy**: Runway uses **zero shadows**. This is a film-production design decision — in cinema, depth comes from lighting, focus, and composition, not drop shadows. The interface mirrors this philosophy: depth is communicated through dark/light section alternation, photographic depth-of-field, and overlay transparency — never through CSS box-shadow.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use full-bleed cinematic photography as the primary visual element
- Use abcNormal for all text — maintain the single-typeface commitment
- Keep display line-heights at 1.0 with negative letter-spacing for film-title density
- Use the cool-gray neutral palette (#767d88, #7d848e) for secondary text
- Maintain zero shadows — depth comes from photography and section backgrounds
- Use uppercase with letter-spacing for navigational labels (14px, 0.35px spacing)
- Apply small border-radius (4–8px) — the design is NOT pill-shaped
- Let visual content (photos, videos) dominate — the UI should be invisible
- Use weight 450 for micro labels — the precision matters

### Don't
- Don't add decorative colors to the interface — the only color comes from photography
- Don't use heavy borders or shadows — the interface must be nearly invisible
- Don't use pill-shaped radius — Runway's geometry is subtly rounded, not circular
- Don't use bold (700+) weight — 400–600 is the full range, with 450 as a precision tool
- Don't compete with the visual content — text overlays should be minimal and restrained
- Don't use gradient backgrounds in the interface — gradients exist only in photography
- Don't use more than one typeface — abcNormal handles everything
- Don't use body line-height above 1.50 — the tight, editorial feel is core
- Don't reduce image quality — cinematic photography IS the design


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
| Mobile | <640px | Single column, stacked images, reduced hero text |
| Tablet | 640–768px | 2-column image grids begin |
| Small Desktop | 768–1024px | Standard layout |
| Desktop | 1024–1280px | Full layout, expanded hero |
| Large Desktop | 1280–1600px | Maximum cinema-width container |

### Touch Targets
- Navigation links at comfortable 16px
- Article cards serve as large touch targets
- Buttons at 14px weight 600 with adequate padding

### Collapsing Strategy
- **Navigation**: Collapses to hamburger on mobile
- **Hero**: Full-bleed maintained, text scales down
- **Image grids**: Multi-column → 2-column → single column
- **Research articles**: Feature-size cards → stacked full-width
- **Trust logos**: Horizontal scroll or reduced grid

### Image Behavior
- Cinematic images scale proportionally
- Full-bleed hero maintained across all sizes
- Image grids reflow to fewer columns
- Video content maintains aspect ratio


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Background Dark: "Runway Black (#000000)"
- Background Light: "Pure White (#ffffff)"
- Primary Text Dark: "Charcoal (#404040)"
- Secondary Text: "Cool Slate (#767d88)"
- Muted Text: "Muted Gray (#a7a7a7)"
- Light Border: "Cool Silver (#c9ccd1)"
- Dark Border: "Border Dark (#27272a)"
- Card Surface: "Dark Surface (#1a1a1a)"

### Example Component Prompts
- "Create a cinematic hero section: full-bleed dark background with a cinematic image overlay. Headline at 48px abcNormal weight 400, line-height 1.0, letter-spacing -1.2px in white. Minimal text below in Cool Slate (#767d88) at 16px."
- "Design a research article grid: one large card (50% width) with a cinematic image and 24px title, next to two smaller cards stacked. All images with 8px border-radius. Titles in white (dark bg) or Charcoal (#404040, light bg)."
- "Build a section label: 14px abcNormal weight 500, uppercase, letter-spacing 0.35px in Cool Slate (#767d88). No border, no background."
- "Create a trust bar: company logos in monochrome, horizontal layout with generous spacing. On dark background with white/gray logo treatments."
- "Design a mission statement section: Runway Black background, white text at 36px abcNormal, line-height 1.0, letter-spacing -0.9px. Centered, with generous vertical padding."

### Iteration Guide
1. Visual content first — always include cinematic photography
2. Use abcNormal for everything — specify size and weight, never change the font
3. Keep the interface invisible — no heavy borders, no shadows, no bright colors
4. Use the cool slate grays (#767d88, #7d848e) for secondary text — not warm grays
5. Uppercase labels need letter-spacing (0.35px) — never tight uppercase
6. Dark sections should be truly dark (#000000 or #1a1a1a) — no medium grays as surfaces


### PPT-image Quick Reference

- Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
- Display voice: `abcNormal / fallback: abcNormal Fallback`
- Body / label voice: `abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching.`
- Primary accent: Runway Black (#000000)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Deep Black (#030303)
- Signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e), and Zero shadows, minimal borders — the interface is intentionally invisible
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Runway.
Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
Use abcNormal / fallback: abcNormal Fallback as the display-type reference and abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Deep Black (#030303), and Runway Black (#000000).
Preserve these signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, and Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e).
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Runway.
Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
Use abcNormal / fallback: abcNormal Fallback as the display-type reference and abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Deep Black (#030303), and Runway Black (#000000).
Preserve these signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, and Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e).
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Runway.
Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
Use abcNormal / fallback: abcNormal Fallback as the display-type reference and abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Deep Black (#030303), and Runway Black (#000000).
Preserve these signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, and Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e).
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Runway.
Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
Use abcNormal / fallback: abcNormal Fallback as the display-type reference and abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Deep Black (#030303), and Runway Black (#000000).
Preserve these signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, and Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e).
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Runway.
Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
Use abcNormal / fallback: abcNormal Fallback as the display-type reference and abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Deep Black (#030303), and Runway Black (#000000).
Preserve these signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, and Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e).
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Runway.
Brand mood: Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements.
Use abcNormal / fallback: abcNormal Fallback as the display-type reference and abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Deep Black (#030303), and Runway Black (#000000).
Preserve these signature cues: Cinematic full-bleed photography and video as primary UI elements, Single typeface system: abcNormal for everything from display to micro labels, and Dark-dominant palette with cool-toned neutrals (#767d88, #7d848e).
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
