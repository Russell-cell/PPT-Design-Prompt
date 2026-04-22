# PPT-image Design System Inspired by Together AI

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Together AI.

Source reference: `source/together.ai/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Together AI's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic. The hero section blooms with soft pink-blue-lavender gradients and abstract, painterly illustrations that evoke clouds and flight, establishing a visual metaphor for the "AI-Native Cloud" proposition. Against this softness, the typography cuts through with precision: "The Future" display font at 64px with aggressive negative tracking (-1.92px) creates dense, authoritative headline blocks.

The design straddles two worlds: a bright, white-canvas light side where pastel gradients and stats cards create an approachable platform overview, and a dark navy universe (`#010120` — not gray-black but a deep midnight blue) where research papers and technical content live. This dual-world approach elegantly separates the "business" messaging (light, friendly, stat-driven) from the "research" messaging (dark, serious, academic).

What makes Together AI distinctive is its type system. "The Future" handles all display and body text with a geometric modernist aesthetic, while "PP Neue Montreal Mono" provides uppercase labels with meticulous letter-spacing — creating a "technical infrastructure company with taste" personality. The brand accents — magenta (`#ef2cc1`) and orange (`#fc4c02`) — appear sparingly in the gradient and illustrations, never polluting the clean UI.

**Key Characteristics:**
- Soft pastel gradients (pink, blue, lavender) against pure white canvas
- Deep midnight blue (`#010120`) for dark/research sections — not gray-black
- Custom "The Future" font with aggressive negative letter-spacing throughout
- PP Neue Montreal Mono for uppercase technical labels
- Sharp geometry (4px, 8px radius) — not rounded, not pill
- Magenta (#ef2cc1) + orange (#fc4c02) brand accents in illustrations only
- Lavender (#bdbbff) as a soft secondary accent
- Enterprise stats prominently displayed (2x, 60%, 90%)
- Dark-blue-tinted shadows (rgba(1, 1, 32, 0.1))


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, Custom "The Future" font with aggressive negative letter-spacing throughout, and PP Neue Montreal Mono for uppercase technical labels.
- Use Brand Magenta (#ef2cc1) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Dark Blue (#010120) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Brand Magenta** (`#ef2cc1`): The primary brand accent — a vivid pink-magenta used in gradient illustrations and the highest-signal brand moments. Never used as UI chrome.
- **Brand Orange** (`#fc4c02`): The secondary brand accent — a vivid orange for gradient endpoints and warm accent moments.
- **Dark Blue** (`#010120`): The primary dark surface — a deep midnight blue-black used for research sections, footer, and dark containers. Not gray, not black — distinctly blue.

### Secondary & Accent
- **Soft Lavender** (`#bdbbff`): A gentle blue-violet used for subtle accents, secondary indicators, and soft UI highlights.
- **Black 40** (`#00000066`): Semi-transparent black for de-emphasized overlays and secondary text.

### Surface & Background
- **Pure White** (`#ffffff`): The primary light-section page background.
- **Dark Blue** (`#010120`): Dark-section backgrounds — research, footer, technical content.
- **Glass Light** (`rgba(255, 255, 255, 0.12)`): Frosted glass button backgrounds on dark sections.
- **Glass Dark** (`rgba(0, 0, 0, 0.08)`): Subtle tinted surfaces on light sections.

### Neutrals & Text
- **Pure Black** (`#000000`): Primary text on light surfaces.
- **Pure White** (`#ffffff`): Primary text on dark surfaces.
- **Black 8%** (`rgba(0, 0, 0, 0.08)`): Borders and subtle containment on light surfaces.
- **White 12%** (`rgba(255, 255, 255, 0.12)`): Borders and containment on dark surfaces.

### Gradient System
- **Pastel Cloud Gradient**: Soft pink → lavender → soft blue gradients in hero illustrations. These appear in abstract, painterly forms — clouds, feathers, flowing shapes — that create visual warmth without literal meaning.
- **Hero Gradient**: The hero background uses soft pastel tints layered over white, creating a dawn-like atmospheric effect.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Dark Blue (#010120) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Brand Magenta (#ef2cc1) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Primary**: `The Future`, with fallback: `Arial`
- **Monospace / Labels**: `PP Neue Montreal Mono`, with fallback: `Georgia`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | The Future | 64px (4rem) | 400–500 | 1.00–1.10 (tight) | -1.92px | Maximum impact, dense blocks |
| Section Heading | The Future | 40px (2.5rem) | 500 | 1.20 (tight) | -0.8px | Feature section titles |
| Sub-heading | The Future | 28px (1.75rem) | 500 | 1.15 (tight) | -0.42px | Card headings |
| Feature Title | The Future | 22px (1.38rem) | 500 | 1.15 (tight) | -0.22px | Small feature headings |
| Body Large | The Future | 18px (1.13rem) | 400–500 | 1.30 (tight) | -0.18px | Descriptions, sections |
| Body / Button | The Future | 16px (1rem) | 400–500 | 1.25–1.30 | -0.16px | Standard body, nav, buttons |
| Caption | The Future | 14px (0.88rem) | 400–500 | 1.40 | normal | Metadata, descriptions |
| Mono Label | PP Neue Montreal Mono | 16px (1rem) | 500 | 1.00 (tight) | 0.08px | Uppercase section labels |
| Mono Small | PP Neue Montreal Mono | 11px (0.69rem) | 500 | 1.00–1.40 | 0.055–0.08px | Small uppercase tags |
| Mono Micro | PP Neue Montreal Mono | 10px (0.63rem) | 400 | 1.40 | 0.05px | Smallest uppercase labels |

### Principles
- **Negative tracking everywhere**: Every size of "The Future" uses negative letter-spacing (-0.16px to -1.92px), creating consistently tight, modern text.
- **Mono for structure**: PP Neue Montreal Mono in uppercase with positive letter-spacing creates technical "label" moments that structure the page without competing with display text.
- **Weight 500 as emphasis**: The system uses 400 (regular) and 500 (medium) — no bold. Medium weight marks headings and emphasis.
- **Tight line-heights throughout**: Even body text uses 1.25–1.30 line-height — tighter than typical, creating a dense, information-rich feel.


### PPT-image Type Deployment

- Use `The Future / fallback: Arial` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `PP Neue Montreal Mono / fallback: Georgia` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Glass on Dark**
- Background: `rgba(255, 255, 255, 0.12)` (frosted glass)
- Text: Pure White (`#ffffff`)
- Radius: sharp (4px)
- Opacity: 0.5
- Hover: transparent dark overlay
- Used on dark sections — subtle, glass-like

**Dark Solid**
- Background: Dark Blue (`#010120`) or Pure Black
- Text: Pure White
- Radius: sharp (4px)
- The primary CTA on light surfaces

**Outlined Light**
- Border: `1px solid rgba(0, 0, 0, 0.08)`
- Background: transparent or subtle glass
- Text: Pure Black
- Radius: sharp (4px)
- Secondary actions on light surfaces

### Cards & Containers
- Background: Pure White or subtle glass tint
- Border: `1px solid rgba(0, 0, 0, 0.08)` on light; `1px solid rgba(255, 255, 255, 0.12)` on dark
- Radius: sharp (4px) for badges and small elements; comfortable (8px) for larger containers
- Shadow: dark-blue-tinted (`rgba(1, 1, 32, 0.1) 0px 4px 10px`) — warm and subtle
- Stats cards with large numbers prominently displayed

### Badges / Tags
- Background: `rgba(0, 0, 0, 0.04)` (light) or `rgba(255, 255, 255, 0.12)` (dark)
- Text: Black (light) or White (dark)
- Padding: 2px 8px (compact)
- Radius: sharp (4px)
- Border: `1px solid rgba(0, 0, 0, 0.08)`
- PP Neue Montreal Mono, uppercase, 16px

### Navigation
- Clean horizontal nav on white/transparent
- Logo: Together AI wordmark
- Links: The Future at 16px, weight 400
- CTA: Dark solid button
- Hover: no text-decoration

### Image Treatment
- Abstract pastel gradient illustrations (cloud/feather forms)
- Product UI screenshots on dark/light surfaces
- Team photos in editorial style
- Research paper cards with dark backgrounds

### Distinctive Components

**Stats Bar**
- Large performance metrics (2x, 60%, 90%)
- Bold display numbers
- Short descriptive captions beneath
- Clean horizontal layout

**Mono Section Labels**
- PP Neue Montreal Mono, uppercase, 11px, letter-spacing 0.055px
- Used as navigational signposts throughout the page
- Technical, structured feel

**Research Section**
- Dark Blue (#010120) background
- White text, research paper thumbnails
- Creates a distinct "academic" zone

**Large Footer Logo**
- "together" wordmark rendered at massive scale in the dark footer
- Creates a brand-statement closing moment


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Together AI's strongest visual cues as one large, unmistakable scene or object.
- Let Brand Magenta (#ef2cc1), Pure White (#ffffff), and Dark Blue (#010120) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Badges / Tags, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Together AI.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Dark Blue (#010120), with Brand Magenta (#ef2cc1) reserved for the decisive signal.
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
- Scale: 1px, 2px, 4px, 8px, 10px, 12px, 16px, 20px, 24px, 32px, 44px, 48px, 80px, 100px, 120px
- Button/badge padding: 2px 8px (compact)
- Card internal padding: approximately 24–32px
- Section vertical spacing: generous (80–120px)

### Grid & Container
- Max container width: approximately 1200px, centered
- Hero: centered with pastel gradient background
- Feature sections: multi-column card grids
- Stats: horizontal row of metric cards
- Research: dark full-width section

### Whitespace Philosophy
- **Optimistic breathing room**: Generous spacing between sections creates an open, inviting feel that makes enterprise AI infrastructure feel accessible.
- **Dual atmosphere**: Light sections breathe with whitespace; dark sections are denser with content.
- **Stats as visual anchors**: Large numbers with small captions create natural focal points.

### Border Radius Scale
- Sharp (4px): Buttons, badges, tags, small interactive elements — the primary radius
- Comfortable (8px): Larger containers, feature cards

*This is a deliberately restrained radius system — no pills, no generous rounding. The sharp geometry contrasts with the soft pastel gradients.*


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
| Flat (Level 0) | No shadow, no border | Page background, text blocks |
| Contained (Level 1) | `1px solid rgba(0,0,0,0.08)` (light) or `rgba(255,255,255,0.12)` (dark) | Cards, badges, containers |
| Elevated (Level 2) | `rgba(1, 1, 32, 0.1) 0px 4px 10px` | Feature cards, hover states |
| Dark Zone (Level 3) | Dark Blue (#010120) full-width background | Research, footer, technical sections |

**Shadow Philosophy**: Together AI uses a single, distinctive shadow — tinted with Dark Blue (`rgba(1, 1, 32, 0.1)`) rather than generic black. This gives elevated elements a subtle blue-ish cast that ties them to the brand's midnight-blue dark mode. The shadow is soft (10px blur, 4px offset) and always downward — creating gentle paper-hover elevation.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use pastel gradients (pink/blue/lavender) for hero illustrations and decorative backgrounds
- Use Dark Blue (#010120) for dark sections — never generic gray-black
- Apply negative letter-spacing on all "The Future" text (scaled by size)
- Use PP Neue Montreal Mono in uppercase for section labels and technical markers
- Keep border-radius sharp (4px) for badges and interactive elements
- Use the dark-blue-tinted shadow for elevation
- Maintain the light/dark section duality — business (light) vs research (dark)
- Show enterprise stats prominently with large display numbers

### Don't
- Don't use Brand Magenta (#ef2cc1) or Brand Orange (#fc4c02) as UI colors — they're for illustrations only
- Don't use pill-shaped or generously rounded corners — the geometry is sharp
- Don't use generic gray-black for dark sections — always Dark Blue (#010120)
- Don't use positive letter-spacing on "The Future" — it's always negative
- Don't use bold (700+) weight — 400–500 is the full range
- Don't use warm-toned shadows — always dark-blue-tinted
- Don't reduce section spacing below 48px — the open feeling is core
- Don't mix in additional typefaces — "The Future" + PP Neue Montreal Mono is the pair


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
| Mobile | <479px | Compact layout, stacked everything |
| Large Mobile | 479–767px | Single column, hamburger nav |
| Tablet | 768–991px | 2-column grids begin |
| Desktop | 992px+ | Full multi-column layout |

### Touch Targets
- Buttons with adequate padding
- Card surfaces as touch targets
- Navigation links at comfortable 16px

### Collapsing Strategy
- **Navigation**: Collapses to hamburger on mobile
- **Hero text**: 64px → 40px → 28px progressive scaling
- **Stats bar**: Horizontal → stacked vertical
- **Feature grids**: Multi-column → single column
- **Research section**: Cards stack vertically

### Image Behavior
- Pastel illustrations scale proportionally
- Product screenshots maintain aspect ratio
- Team photos scale within containers


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary Text (light): "Pure Black (#000000)"
- Primary Text (dark): "Pure White (#ffffff)"
- Page Background: "Pure White (#ffffff)"
- Dark Surface: "Dark Blue (#010120)"
- Brand Accent 1: "Brand Magenta (#ef2cc1)"
- Brand Accent 2: "Brand Orange (#fc4c02)"
- Soft Accent: "Soft Lavender (#bdbbff)"
- Border (light): "rgba(0, 0, 0, 0.08)"

### Example Component Prompts
- "Create a hero section on white with soft pastel gradients (pink → lavender → blue) as background. Headline at 64px 'The Future' weight 500, line-height 1.10, letter-spacing -1.92px. Pure Black text. Include a dark blue CTA button (#010120, 4px radius)."
- "Design a stats card: large display number (64px, weight 500) with a small caption below (14px). White background, 8px radius, dark-blue-tinted shadow (rgba(1, 1, 32, 0.1) 0px 4px 10px)."
- "Build a section label: PP Neue Montreal Mono, 11px, weight 500, uppercase, letter-spacing 0.055px. Black text on light, white on dark."
- "Create a dark research section: Dark Blue (#010120) background. White text, section heading at 40px 'The Future' weight 500, letter-spacing -0.8px. Cards with rgba(255, 255, 255, 0.12) border."
- "Design a badge: 4px radius, rgba(0, 0, 0, 0.04) background, 1px solid rgba(0, 0, 0, 0.08) border, 'The Future' 16px text. Padding: 2px 8px."

### Iteration Guide
1. Always specify negative letter-spacing for "The Future" — it's scaled by size
2. Dark sections use #010120 (midnight blue), never generic black
3. Shadows are always dark-blue-tinted: rgba(1, 1, 32, 0.1)
4. Mono labels are always uppercase with positive letter-spacing
5. Keep radius sharp (4px or 8px) — no pills, no generous rounding
6. Pastel gradients are for decoration, not UI chrome


### PPT-image Quick Reference

- Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
- Display voice: `The Future / fallback: Arial`
- Body / label voice: `PP Neue Montreal Mono / fallback: Georgia`
- Primary accent: Brand Magenta (#ef2cc1)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Dark Blue (#010120)
- Signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, Custom "The Future" font with aggressive negative letter-spacing throughout, and PP Neue Montreal Mono for uppercase technical labels
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Together AI.
Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
Use The Future / fallback: Arial as the display-type reference and PP Neue Montreal Mono / fallback: Georgia for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Dark Blue (#010120), and Brand Magenta (#ef2cc1).
Preserve these signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, and Custom "The Future" font with aggressive negative letter-spacing throughout.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Together AI.
Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
Use The Future / fallback: Arial as the display-type reference and PP Neue Montreal Mono / fallback: Georgia for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Dark Blue (#010120), and Brand Magenta (#ef2cc1).
Preserve these signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, and Custom "The Future" font with aggressive negative letter-spacing throughout.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Together AI.
Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
Use The Future / fallback: Arial as the display-type reference and PP Neue Montreal Mono / fallback: Georgia for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Dark Blue (#010120), and Brand Magenta (#ef2cc1).
Preserve these signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, and Custom "The Future" font with aggressive negative letter-spacing throughout.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Together AI.
Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
Use The Future / fallback: Arial as the display-type reference and PP Neue Montreal Mono / fallback: Georgia for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Dark Blue (#010120), and Brand Magenta (#ef2cc1).
Preserve these signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, and Custom "The Future" font with aggressive negative letter-spacing throughout.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Together AI.
Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
Use The Future / fallback: Arial as the display-type reference and PP Neue Montreal Mono / fallback: Georgia for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Dark Blue (#010120), and Brand Magenta (#ef2cc1).
Preserve these signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, and Custom "The Future" font with aggressive negative letter-spacing throughout.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Together AI.
Brand mood: Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic.
Use The Future / fallback: Arial as the display-type reference and PP Neue Montreal Mono / fallback: Georgia for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Dark Blue (#010120), and Brand Magenta (#ef2cc1).
Preserve these signature cues: Soft pastel gradients (pink, blue, lavender) against pure white canvas, Deep midnight blue (#010120) for dark/research sections — not gray-black, and Custom "The Future" font with aggressive negative letter-spacing throughout.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
