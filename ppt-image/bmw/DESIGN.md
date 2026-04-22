# PPT-image Design System Inspired by BMW

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably BMW.

Source reference: `source/bmw/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps BMW's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence. The page alternates between deep dark hero sections (featuring full-bleed automotive photography) and clean white content areas, creating a cinematic rhythm reminiscent of a luxury car showroom where vehicles are lit against darkness. The BMW CI2020 design language (their corporate identity refresh) defines every element.

The typography is built on BMWTypeNextLatin — a proprietary typeface in two variants: BMWTypeNextLatin Light (weight 300) for massive uppercase display headings, and BMWTypeNextLatin Regular for body and UI text. The 60px uppercase headline at weight 300 is the defining typographic gesture — light-weight type that whispers authority rather than shouting it. The fallback stack includes Helvetica and Japanese fonts (Hiragino, Meiryo), reflecting BMW's global presence.

What makes BMW distinctive is its CSS variable-driven theming system. Context-aware variables (`--site-context-highlight-color: #1c69d4`, `--site-context-focus-color: #0653b6`, `--site-context-metainfo-color: #757575`) suggest a design system built for multi-brand, multi-context deployment where colors can be swapped globally. The blue highlight color (`#1c69d4`) is BMW's signature blue — used sparingly for interactive elements and focus states, never decoratively. Zero border-radius was detected — BMW's design is angular, sharp-cornered, and uncompromisingly geometric.

**Key Characteristics:**
- BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority
- BMW Blue (`#1c69d4`) as singular accent — used only for interactive elements
- Zero border-radius detected — angular, sharp-cornered, industrial geometry
- Dark hero photography + white content sections — showroom lighting rhythm
- CSS variable-driven theming: `--site-context-*` tokens for brand flexibility
- Weight 900 for navigation emphasis — extreme contrast with 300 display
- Tight line-heights (1.15–1.30) throughout — compressed, efficient, German engineering
- Full-bleed automotive photography as primary visual content


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, Zero border-radius detected — angular, sharp-cornered, industrial geometry, and Dark hero photography + white content sections — showroom lighting rhythm.
- Use BMW Blue (#1c69d4) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#262626) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary Brand
- **Pure White** (`#ffffff`): `--site-context-theme-color`, primary surface, card backgrounds
- **BMW Blue** (`#1c69d4`): `--site-context-highlight-color`, primary interactive accent
- **BMW Focus Blue** (`#0653b6`): `--site-context-focus-color`, keyboard focus and active states

### Neutral Scale
- **Near Black** (`#262626`): Primary text on light surfaces, dark link text
- **Meta Gray** (`#757575`): `--site-context-metainfo-color`, secondary text, metadata
- **Silver** (`#bbbbbb`): Tertiary text, muted links, footer elements

### Interactive States
- All links hover to white (`#ffffff`) — suggesting primarily dark-surface navigation
- Text links use underline: none on hover — clean interaction

### Shadows
- Minimal shadow system — depth through photography and dark/light section contrast


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#262626) when the deck needs cinematic weight or a chapter reset.
- Primary accent: BMW Blue (#1c69d4) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display Light**: `BMWTypeNextLatin Light`, fallbacks: `Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo`
- **Body / UI**: `BMWTypeNextLatin`, same fallback stack

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display Hero | BMWTypeNextLatin Light | 60px (3.75rem) | 300 | 1.30 (tight) | `text-transform: uppercase` |
| Section Heading | BMWTypeNextLatin | 32px (2.00rem) | 400 | 1.30 (tight) | Major section titles |
| Nav Emphasis | BMWTypeNextLatin | 18px (1.13rem) | 900 | 1.30 (tight) | Navigation bold items |
| Body | BMWTypeNextLatin | 16px (1.00rem) | 400 | 1.15 (tight) | Standard body text |
| Button Bold | BMWTypeNextLatin | 16px (1.00rem) | 700 | 1.20–2.88 | CTA buttons |
| Button | BMWTypeNextLatin | 16px (1.00rem) | 400 | 1.15 (tight) | Standard buttons |

### Principles
- **Light display, heavy navigation**: Weight 300 for hero headlines creates whispered elegance; weight 900 for navigation creates stark authority. This extreme weight contrast (300 vs 900) is the signature typographic tension.
- **Universal uppercase display**: The 60px hero is always uppercase — creating a monumental, architectural quality.
- **Tight everything**: Line-heights from 1.15 to 1.30 across the entire system. Nothing breathes — every line is compressed, efficient, German-engineered.
- **Single font family**: BMWTypeNextLatin handles everything from 60px display to 16px body — unity through one typeface at different weights.


### PPT-image Type Deployment

- Use `BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `BMWTypeNextLatin, same fallback stack` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- Text: 16px BMWTypeNextLatin, weight 700 for primary, 400 for secondary
- Line-height: 1.15–2.88 (large variation suggests padding-driven sizing)
- Border: white bottom-border on dark surfaces (`1px solid #ffffff`)
- No border-radius — sharp rectangular buttons

### Cards & Containers
- No border-radius — all containers are sharp-cornered rectangles
- White backgrounds on light sections
- Dark backgrounds for hero/feature sections
- No visible borders on most elements

### Navigation
- BMWTypeNextLatin 18px weight 900 for primary nav links
- White text on dark header
- BMW logo 54x54px
- Hover: remains white, text-decoration none
- "Home" text link in header

### Image Treatment
- Full-bleed automotive photography
- Dark cinematic lighting
- Edge-to-edge hero images
- Car photography as primary visual content


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use BMW's strongest visual cues as one large, unmistakable scene or object.
- Let BMW Blue (#1c69d4), Pure White (#ffffff), and Near Black (#262626) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Navigation, and Image Treatment rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to BMW.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Near Black (#262626), with BMW Blue (#1c69d4) reserved for the decisive signal.
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
- Scale: 1px, 5px, 8px, 10px, 12px, 15px, 16px, 20px, 24px, 30px, 32px, 40px, 45px, 56px, 60px

### Grid & Container
- Full-width hero photography
- Centered content sections
- Footer: multi-column link grid

### Whitespace Philosophy
- **Showroom pacing**: Dark hero sections with generous padding create the feeling of walking through a showroom where each vehicle is spotlit in its own space.
- **Compressed content**: Body text areas use tight line-heights and compact spacing — information-dense, no waste.

### Border Radius Scale
- **None detected.** BMW uses sharp corners exclusively — every element is a precise rectangle. This is the most angular design system analyzed.


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
| Photography (Level 0) | Full-bleed dark imagery | Hero backgrounds |
| Flat (Level 1) | White surface, no shadow | Content sections |
| Focus (Accessibility) | BMW Focus Blue (`#0653b6`) | Focus states |

**Shadow Philosophy**: BMW uses virtually no shadows. Depth is created entirely through the contrast between dark photographic sections and white content sections — the automotive lighting does the elevation work.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use BMWTypeNextLatin Light (300) uppercase for all display headings
- Keep ALL corners sharp (0px radius) — angular geometry is non-negotiable
- Use BMW Blue (`#1c69d4`) only for interactive elements — never decoratively
- Apply weight 900 for navigation emphasis — the extreme weight contrast is intentional
- Use full-bleed automotive photography for hero sections
- Keep line-heights tight (1.15–1.30) throughout
- Use `--site-context-*` CSS variables for theming

### Don't
- Don't round corners — zero radius is the BMW identity
- Don't use BMW Blue for backgrounds or large surfaces — it's an accent only
- Don't use medium font weights (500–600) — the system uses 300, 400, 700, 900 extremes
- Don't add decorative elements — the photography and typography carry everything
- Don't use relaxed line-heights — BMW text is always compressed
- Don't lighten the dark hero sections — the contrast with white IS the design


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
| Mobile Small | <375px | Minimum supported |
| Mobile | 375–480px | Single column |
| Mobile Large | 480–640px | Slight adjustments |
| Tablet Small | 640–768px | 2-column begins |
| Tablet | 768–920px | Standard tablet |
| Desktop Small | 920–1024px | Desktop layout begins |
| Desktop | 1024–1280px | Standard desktop |
| Large Desktop | 1280–1440px | Expanded |
| Ultra-wide | 1440–1600px | Maximum layout |

### Collapsing Strategy
- Hero: 60px → scales down, maintains uppercase
- Navigation: horizontal → hamburger
- Photography: full-bleed maintained at all sizes
- Content sections: stack vertically
- Footer: multi-column → stacked


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Background: Pure White (`#ffffff`)
- Text: Near Black (`#262626`)
- Secondary text: Meta Gray (`#757575`)
- Accent: BMW Blue (`#1c69d4`)
- Focus: BMW Focus Blue (`#0653b6`)
- Muted: Silver (`#bbbbbb`)

### Example Component Prompts
- "Create a hero: full-width dark automotive photography background. Heading at 60px BMWTypeNextLatin Light weight 300, uppercase, line-height 1.30, white text. No border-radius anywhere."
- "Design navigation: dark background. BMWTypeNextLatin 18px weight 900 for links, white text. BMW logo 54x54. Sharp rectangular layout."
- "Build a button: 16px BMWTypeNextLatin weight 700, line-height 1.20. Sharp corners (0px radius). White bottom border on dark surface."
- "Create content section: white background. Heading at 32px weight 400, line-height 1.30, #262626. Body at 16px weight 400, line-height 1.15."

### Iteration Guide
1. Zero border-radius — every corner is sharp, no exceptions
2. Weight extremes: 300 (display), 400 (body), 700 (buttons), 900 (nav)
3. BMW Blue for interactive only — never as background or decoration
4. Photography carries emotion — the UI is pure precision
5. Tight line-heights everywhere — 1.15 to 1.30 is the range


### PPT-image Quick Reference

- Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
- Display voice: `BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo`
- Body / label voice: `BMWTypeNextLatin, same fallback stack`
- Primary accent: BMW Blue (#1c69d4)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Near Black (#262626)
- Signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, Zero border-radius detected — angular, sharp-cornered, industrial geometry, and Dark hero photography + white content sections — showroom lighting rhythm
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by BMW.
Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
Use BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo as the display-type reference and BMWTypeNextLatin, same fallback stack for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#262626), and BMW Blue (#1c69d4).
Preserve these signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, and Zero border-radius detected — angular, sharp-cornered, industrial geometry.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by BMW.
Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
Use BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo as the display-type reference and BMWTypeNextLatin, same fallback stack for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#262626), and BMW Blue (#1c69d4).
Preserve these signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, and Zero border-radius detected — angular, sharp-cornered, industrial geometry.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by BMW.
Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
Use BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo as the display-type reference and BMWTypeNextLatin, same fallback stack for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#262626), and BMW Blue (#1c69d4).
Preserve these signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, and Zero border-radius detected — angular, sharp-cornered, industrial geometry.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by BMW.
Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
Use BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo as the display-type reference and BMWTypeNextLatin, same fallback stack for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#262626), and BMW Blue (#1c69d4).
Preserve these signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, and Zero border-radius detected — angular, sharp-cornered, industrial geometry.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by BMW.
Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
Use BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo as the display-type reference and BMWTypeNextLatin, same fallback stack for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#262626), and BMW Blue (#1c69d4).
Preserve these signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, and Zero border-radius detected — angular, sharp-cornered, industrial geometry.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by BMW.
Brand mood: BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence.
Use BMWTypeNextLatin Light, fallbacks: Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo as the display-type reference and BMWTypeNextLatin, same fallback stack for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#262626), and BMW Blue (#1c69d4).
Preserve these signature cues: BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority, BMW Blue (#1c69d4) as singular accent — used only for interactive elements, and Zero border-radius detected — angular, sharp-cornered, industrial geometry.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
