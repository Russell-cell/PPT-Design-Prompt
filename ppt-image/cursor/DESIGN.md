# PPT-image Design System Inspired by Cursor

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Cursor.

Source reference: `source/cursor/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Cursor's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Cursor's website is a study in warm minimalism meets code-editor elegance.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Cursor's website is a study in warm minimalism meets code-editor elegance. The entire experience is built on a warm off-white canvas (`#f2f1ed`) with dark warm-brown text (`#26251e`) -- not pure black, not neutral gray, but a deeply warm near-black with a yellowish undertone that evokes old paper, ink, and craft. This warmth permeates every surface: backgrounds lean toward cream (`#e6e5e0`, `#ebeae5`), borders dissolve into transparent warm overlays using `oklab` color space, and even the error state (`#cf2d56`) carries warmth rather than clinical red. The result feels more like a premium print publication than a tech website.

The custom CursorGothic font is the typographic signature -- a gothic sans-serif with aggressive negative letter-spacing at display sizes (-2.16px at 72px) that creates a compressed, engineered feel. As a secondary voice, the jjannon serif font (with OpenType `"cswh"` contextual swash alternates) provides literary counterpoint for body copy and editorial passages. The monospace voice comes from berkeleyMono, a refined coding font that connects the marketing site to Cursor's core identity as a code editor. This three-font system (gothic display, serif body, mono code) gives Cursor one of the most typographically rich palettes in developer tooling.

The border system is particularly distinctive -- Cursor uses `oklab()` color space for border colors, applying warm brown at various alpha levels (0.1, 0.2, 0.55) to create borders that feel organic rather than mechanical. The signature border color `oklab(0.263084 -0.00230259 0.0124794 / 0.1)` is not a simple rgba value but a perceptually uniform color that maintains visual consistency across different backgrounds.

**Key Characteristics:**
- CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings
- jjannon serif for body text with OpenType `"cswh"` (contextual swash alternates)
- berkeleyMono for code and technical labels
- Warm off-white background (`#f2f1ed`) instead of pure white -- the entire system is warm-shifted
- Primary text color `#26251e` (warm near-black with yellow undertone)
- Accent orange `#f54e00` for brand highlight and links
- oklab-space borders at various alpha levels for perceptually uniform edge treatment
- Pill-shaped elements with extreme radius (33.5M px, effectively full-pill)
- 8px base spacing system with fine-grained sub-8px increments (1.5px, 2px, 2.5px, 3px, 4px, 5px, 6px)


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), berkeleyMono for code and technical labels, and Warm off-white background (#f2f1ed) instead of pure white -- the entire system is warm-shifted.
- Use Cursor Orange (#f54e00) as the highest-signal accent when color needs to carry emphasis.
- Let Cursor Cream (#f2f1ed) carry calmer title-safe zones and quieter data-support slides.
- Use Cursor Dark (#26251e) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Cursor Dark** (`#26251e`): Primary text, headings, dark UI surfaces. A warm near-black with distinct yellow-brown undertone -- the defining color of the system.
- **Cursor Cream** (`#f2f1ed`): Page background, primary surface. Not white but a warm cream that sets the entire warm tone.
- **Cursor Light** (`#e6e5e0`): Secondary surface, button backgrounds, card fills. A slightly warmer, slightly darker cream.
- **Pure White** (`#ffffff`): Used sparingly for maximum contrast elements and specific surface highlights.
- **True Black** (`#000000`): Minimal use, specific code/console contexts.

### Accent
- **Cursor Orange** (`#f54e00`): Brand accent, `--color-accent`. A vibrant red-orange used for primary CTAs, active links, and brand moments. Warm and urgent.
- **Gold** (`#c08532`): Secondary accent, warm gold for premium or highlighted contexts.

### Semantic
- **Error** (`#cf2d56`): `--color-error`. A warm crimson-rose rather than cold red.
- **Success** (`#1f8a65`): `--color-success`. A muted teal-green, warm-shifted.

### Timeline / Feature Colors
- **Thinking** (`#dfa88f`): Warm peach for "thinking" state in AI timeline.
- **Grep** (`#9fc9a2`): Soft sage green for search/grep operations.
- **Read** (`#9fbbe0`): Soft blue for file reading operations.
- **Edit** (`#c0a8dd`): Soft lavender for editing operations.

### Surface Scale
- **Surface 100** (`#f7f7f4`): Lightest button/card surface, barely tinted.
- **Surface 200** (`#f2f1ed`): Primary page background.
- **Surface 300** (`#ebeae5`): Button default background, subtle emphasis.
- **Surface 400** (`#e6e5e0`): Card backgrounds, secondary surfaces.
- **Surface 500** (`#e1e0db`): Tertiary button background, deeper emphasis.

### Border Colors
- **Border Primary** (`oklab(0.263084 -0.00230259 0.0124794 / 0.1)`): Standard border, 10% warm brown in oklab space.
- **Border Medium** (`oklab(0.263084 -0.00230259 0.0124794 / 0.2)`): Emphasized border, 20% warm brown.
- **Border Strong** (`rgba(38, 37, 30, 0.55)`): Strong borders, table rules.
- **Border Solid** (`#26251e`): Full-opacity dark border for maximum contrast.
- **Border Light** (`#f2f1ed`): Light border matching page background.

### Shadows & Depth
- **Card Shadow** (`rgba(0,0,0,0.14) 0px 28px 70px, rgba(0,0,0,0.1) 0px 14px 32px, oklab(0.263084 -0.00230259 0.0124794 / 0.1) 0px 0px 0px 1px`): Heavy elevated card with warm oklab border ring.
- **Ambient Shadow** (`rgba(0,0,0,0.02) 0px 0px 16px, rgba(0,0,0,0.008) 0px 0px 8px`): Subtle ambient glow for floating elements.


### PPT-image Deployment

- Base canvas: prefer Cursor Cream (#f2f1ed) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Cursor Dark (#26251e) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Cursor Orange (#f54e00) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Display/Headlines**: `CursorGothic`, with fallbacks: `CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial`
- **Body/Editorial**: `jjannon`, with fallbacks: `Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times`
- **Code/Technical**: `berkeleyMono`, with fallbacks: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New`
- **UI/System**: `system-ui`, with fallbacks: `-apple-system, Segoe UI, Helvetica Neue, Arial`
- **Icons**: `CursorIcons16` (icon font at 14px and 12px)
- **OpenType Features**: `"cswh"` on jjannon body text, `"ss09"` on CursorGothic buttons/captions

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | CursorGothic | 72px (4.50rem) | 400 | 1.10 (tight) | -2.16px | Maximum compression, hero statements |
| Section Heading | CursorGothic | 36px (2.25rem) | 400 | 1.20 (tight) | -0.72px | Feature sections, CTA headlines |
| Sub-heading | CursorGothic | 26px (1.63rem) | 400 | 1.25 (tight) | -0.325px | Card headings, sub-sections |
| Title Small | CursorGothic | 22px (1.38rem) | 400 | 1.30 (tight) | -0.11px | Smaller titles, list headings |
| Body Serif | jjannon | 19.2px (1.20rem) | 500 | 1.50 | normal | Editorial body with `"cswh"` |
| Body Serif SM | jjannon | 17.28px (1.08rem) | 400 | 1.35 | normal | Standard body text, descriptions |
| Body Sans | CursorGothic | 16px (1.00rem) | 400 | 1.50 | normal/0.08px | UI body text |
| Button Label | CursorGothic | 14px (0.88rem) | 400 | 1.00 (tight) | normal | Primary button text |
| Button Caption | CursorGothic | 14px (0.88rem) | 400 | 1.50 | 0.14px | Secondary button with `"ss09"` |
| Caption | CursorGothic | 11px (0.69rem) | 400-500 | 1.50 | normal | Small captions, metadata |
| System Heading | system-ui | 20px (1.25rem) | 700 | 1.55 | normal | System UI headings |
| System Caption | system-ui | 13px (0.81rem) | 500-600 | 1.33 | normal | System UI labels |
| System Micro | system-ui | 11px (0.69rem) | 500 | 1.27 (tight) | 0.048px | Uppercase micro labels |
| Mono Body | berkeleyMono | 12px (0.75rem) | 400 | 1.67 (relaxed) | normal | Code blocks |
| Mono Small | berkeleyMono | 11px (0.69rem) | 400 | 1.33 | -0.275px | Inline code, terminal |
| Lato Heading | Lato | 16px (1.00rem) | 600 | 1.33 | normal | Lato section headings |
| Lato Caption | Lato | 14px (0.88rem) | 400-600 | 1.33 | normal | Lato captions |
| Lato Micro | Lato | 12px (0.75rem) | 400-600 | 1.27 (tight) | 0.053px | Lato small labels |

### Principles
- **Gothic compression for impact**: CursorGothic at display sizes uses -2.16px letter-spacing at 72px, progressively relaxing: -0.72px at 36px, -0.325px at 26px, -0.11px at 22px, normal at 16px and below. The tracking creates a sense of precision engineering.
- **Serif for soul**: jjannon provides literary warmth. The `"cswh"` feature adds contextual swash alternates that give body text a calligraphic quality.
- **Three typographic voices**: Gothic (display/UI), serif (editorial/body), mono (code/technical). Each serves a distinct communication purpose.
- **Weight restraint**: CursorGothic uses weight 400 almost exclusively, relying on size and tracking for hierarchy rather than weight. System-ui components use 500-700 for functional emphasis.


### PPT-image Type Deployment

- Use `CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary (Warm Surface)**
- Background: `#ebeae5` (Surface 300)
- Text: `#26251e` (Cursor Dark)
- Padding: 10px 12px 10px 14px
- Radius: 8px
- Outline: none
- Hover: text shifts to `var(--color-error)` (`#cf2d56`)
- Focus shadow: `rgba(0,0,0,0.1) 0px 4px 12px`
- Use: Primary actions, main CTAs

**Secondary Pill**
- Background: `#e6e5e0` (Surface 400)
- Text: `oklab(0.263 / 0.6)` (60% warm brown)
- Padding: 3px 8px
- Radius: full pill (33.5M px)
- Hover: text shifts to `var(--color-error)`
- Use: Tags, filters, secondary actions

**Tertiary Pill**
- Background: `#e1e0db` (Surface 500)
- Text: `oklab(0.263 / 0.6)` (60% warm brown)
- Radius: full pill
- Use: Active filter state, selected tags

**Ghost (Transparent)**
- Background: `rgba(38, 37, 30, 0.06)` (6% warm brown)
- Text: `rgba(38, 37, 30, 0.55)` (55% warm brown)
- Padding: 6px 12px
- Use: Tertiary actions, dismiss buttons

**Light Surface**
- Background: `#f7f7f4` (Surface 100) or `#f2f1ed` (Surface 200)
- Text: `#26251e` or `oklab(0.263 / 0.9)` (90%)
- Padding: 0px 8px 1px 12px
- Use: Dropdown triggers, subtle interactive elements

### Cards & Containers
- Background: `#e6e5e0` or `#f2f1ed`
- Border: `1px solid oklab(0.263 / 0.1)` (warm brown at 10%)
- Radius: 8px (standard), 4px (compact), 10px (featured)
- Shadow: `rgba(0,0,0,0.14) 0px 28px 70px, rgba(0,0,0,0.1) 0px 14px 32px` for elevated cards
- Hover: shadow intensification

### Inputs & Forms
- Background: transparent or surface
- Text: `#26251e`
- Padding: 8px 8px 6px (textarea)
- Border: `1px solid oklab(0.263 / 0.1)`
- Focus: border shifts to `oklab(0.263 / 0.2)` or accent orange

### Navigation
- Clean horizontal nav on warm cream background
- Cursor logotype left-aligned (~96x24px)
- Links: 14px CursorGothic or system-ui, weight 500
- CTA button: warm surface with Cursor Dark text
- Tab navigation: bottom border `1px solid oklab(0.263 / 0.1)` with active tab differentiation

### Image Treatment
- Code editor screenshots with `1px solid oklab(0.263 / 0.1)` border
- Rounded corners: 8px standard
- AI chat/timeline screenshots dominate feature sections
- Warm gradient or solid cream backgrounds behind hero images

### Distinctive Components

**AI Timeline**
- Vertical timeline showing AI operations: thinking (peach), grep (sage), read (blue), edit (lavender)
- Each step uses its semantic color with matching text
- Connected with vertical lines
- Core visual metaphor for Cursor's AI-first coding experience

**Code Editor Previews**
- Dark code editor screenshots with warm cream border frame
- berkeleyMono for code text
- Syntax highlighting using timeline colors

**Pricing Cards**
- Warm surface backgrounds with bordered containers
- Feature lists using jjannon serif for readability
- CTA buttons with accent orange or primary dark styling


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Cursor's strongest visual cues as one large, unmistakable scene or object.
- Let Cursor Orange (#f54e00), Cursor Cream (#f2f1ed), and Cursor Dark (#26251e) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Cursor.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Cursor Cream (#f2f1ed) versus Cursor Dark (#26251e), with Cursor Orange (#f54e00) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System, Grid & Container, and Whitespace Philosophy) to create clean fields for charts, numerals, or callouts.
- Avoid hero subjects that fight the actual data layer.

#### System / Workflow Plate

- Convert the original component logic into presentation diagrams, route maps, or structural visuals rather than literal product UI.
- Keep the image designed, not tool-generated: large shapes, few node types, deliberate connectors, and brand-consistent type.
- Depth should follow Decorative Depth instead of generic infographic shadows.

#### Closing Poster

- Compress the deck's final judgment into one memorable frame.
- Use the same brand surfaces and accent hierarchy, but simplify harder than the cover.
- The closing image should resolve the story, not reopen complexity.

## 5. Layout Principles

### Original Layout DNA

### Spacing System
- Base unit: 8px
- Fine scale: 1.5px, 2px, 2.5px, 3px, 4px, 5px, 6px (sub-8px for micro-adjustments)
- Standard scale: 8px, 10px, 12px, 14px (derived from extraction)
- Extended scale (inferred): 16px, 24px, 32px, 48px, 64px, 96px
- Notable: fine-grained sub-8px increments for precise icon/text alignment

### Grid & Container
- Max content width: approximately 1200px
- Hero: centered single-column with generous top padding (80-120px)
- Feature sections: 2-3 column grids for cards and features
- Full-width sections with warm cream or slightly darker backgrounds
- Sidebar layouts for documentation and settings pages

### Whitespace Philosophy
- **Warm negative space**: The cream background means whitespace has warmth and texture, unlike cold white minimalism. Large empty areas feel cozy rather than clinical.
- **Compressed text, open layout**: Aggressive negative letter-spacing on CursorGothic headlines is balanced by generous surrounding margins. Text is dense; space around it breathes.
- **Section variation**: Alternating surface tones (cream → lighter cream → cream) create subtle section differentiation without harsh boundaries.

### Border Radius Scale
- Micro (1.5px): Fine detail elements
- Small (2px): Inline elements, code spans
- Medium (3px): Small containers, inline badges
- Standard (4px): Cards, images, compact buttons
- Comfortable (8px): Primary buttons, cards, menus
- Featured (10px): Larger containers, featured cards
- Full Pill (33.5M px / 9999px): Pill buttons, tags, badges


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
| Flat (Level 0) | No shadow | Page background, text blocks |
| Border Ring (Level 1) | `oklab(0.263 / 0.1) 0px 0px 0px 1px` | Standard card/container border (warm oklab) |
| Border Medium (Level 1b) | `oklab(0.263 / 0.2) 0px 0px 0px 1px` | Emphasized borders, active states |
| Ambient (Level 2) | `rgba(0,0,0,0.02) 0px 0px 16px, rgba(0,0,0,0.008) 0px 0px 8px` | Floating elements, subtle glow |
| Elevated Card (Level 3) | `rgba(0,0,0,0.14) 0px 28px 70px, rgba(0,0,0,0.1) 0px 14px 32px, oklab ring` | Modals, popovers, elevated cards |
| Focus | `rgba(0,0,0,0.1) 0px 4px 12px` on button focus | Interactive focus feedback |

**Shadow Philosophy**: Cursor's depth system is built around two ideas. First, borders use perceptually uniform oklab color space rather than rgba, ensuring warm brown borders look consistent across different background tones. Second, elevation shadows use dramatically large blur values (28px, 70px) with moderate opacity (0.14, 0.1), creating a diffused, atmospheric lift rather than hard-edged drop shadows. Cards don't feel like they float above the page -- they feel like the page has gently opened a space for them.

### Decorative Depth
- Warm cream surface variations create subtle tonal depth without shadows
- oklab borders at 10% and 20% create a spectrum of edge definition
- No harsh divider lines -- section separation through background tone shifts and spacing


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Hover States
- Buttons: text color shifts to `--color-error` (`#cf2d56`) on hover -- a distinctive warm crimson that signals interactivity
- Links: color shift to accent orange (`#f54e00`) or underline decoration with `rgba(38, 37, 30, 0.4)`
- Cards: shadow intensification on hover (ambient → elevated)

### Focus States
- Shadow-based focus: `rgba(0,0,0,0.1) 0px 4px 12px` for depth-based focus indication
- Border focus: `oklab(0.263 / 0.2)` (20% border) for input/form focus
- Consistent warm tone in all focus states -- no cold blue focus rings

### Transitions
- Color transitions: 150ms ease for text/background color changes
- Shadow transitions: 200ms ease for elevation changes
- Transform: subtle scale or translate for interactive feedback


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
| Mobile | <600px | Single column, reduced padding, stacked navigation |
| Tablet Small | 600-768px | 2-column grids begin |
| Tablet | 768-900px | Expanded card grids, sidebar appears |
| Desktop Small | 900-1279px | Full layout forming |
| Desktop | >1279px | Full layout, maximum content width |

### Touch Targets
- Buttons use comfortable padding (6px-14px vertical, 8px-14px horizontal)
- Pill buttons maintain tap-friendly sizing with 3px-10px padding
- Navigation links at 14px with adequate spacing for touch

### Collapsing Strategy
- Hero: 72px CursorGothic → 36px → 26px on smaller screens, maintaining proportional letter-spacing
- Navigation: horizontal links → hamburger menu on mobile
- Feature cards: 3-column → 2-column → single column stacked
- Code editor screenshots: maintain aspect ratio, may shrink with border treatment preserved
- Timeline visualization: horizontal → vertical stacking
- Section spacing: 80px+ → 48px → 32px on mobile

### Image Behavior
- Editor screenshots maintain warm border treatment at all sizes
- AI timeline adapts from horizontal to vertical layout
- Product screenshots use responsive images with consistent border radius
- Full-width hero images scale proportionally


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary CTA background: `#ebeae5` (warm cream button)
- Page background: `#f2f1ed` (warm off-white)
- Text color: `#26251e` (warm near-black)
- Secondary text: `rgba(38, 37, 30, 0.55)` (55% warm brown)
- Accent: `#f54e00` (orange)
- Error/hover: `#cf2d56` (warm crimson)
- Success: `#1f8a65` (muted teal)
- Border: `oklab(0.263084 -0.00230259 0.0124794 / 0.1)` or `rgba(38, 37, 30, 0.1)` as fallback

### Example Component Prompts
- "Create a hero section on `#f2f1ed` warm cream background. Headline at 72px CursorGothic weight 400, line-height 1.10, letter-spacing -2.16px, color `#26251e`. Subtitle at 17.28px jjannon weight 400, line-height 1.35, color `rgba(38,37,30,0.55)`. Primary CTA button (`#ebeae5` bg, 8px radius, 10px 14px padding) with hover text shift to `#cf2d56`."
- "Design a card: `#e6e5e0` background, border `1px solid rgba(38,37,30,0.1)`. Radius 8px. Title at 22px CursorGothic weight 400, letter-spacing -0.11px. Body at 17.28px jjannon weight 400, color `rgba(38,37,30,0.55)`. Use `#f54e00` for link accents."
- "Build a pill tag: `#e6e5e0` background, `rgba(38,37,30,0.6)` text, full-pill radius (9999px), 3px 8px padding, 14px CursorGothic weight 400."
- "Create navigation: sticky `#f2f1ed` background with backdrop-filter blur. 14px system-ui weight 500 for links, `#26251e` text. CTA button right-aligned with `#ebeae5` bg and 8px radius. Bottom border `1px solid rgba(38,37,30,0.1)`."
- "Design an AI timeline showing four steps: Thinking (`#dfa88f`), Grep (`#9fc9a2`), Read (`#9fbbe0`), Edit (`#c0a8dd`). Each step: 14px system-ui label + 16px CursorGothic description + vertical connecting line in `rgba(38,37,30,0.1)`."

### Iteration Guide
1. Always use warm tones -- `#f2f1ed` background, `#26251e` text, never pure white/black for primary surfaces
2. Letter-spacing scales with font size for CursorGothic: -2.16px at 72px, -0.72px at 36px, -0.325px at 26px, normal at 16px
3. Use `rgba(38, 37, 30, alpha)` as a CSS-compatible fallback for oklab borders
4. Three fonts, three voices: CursorGothic (display/UI), jjannon (editorial), berkeleyMono (code)
5. Pill shapes (9999px radius) for tags and filters; 8px radius for primary buttons and cards
6. Hover states use `#cf2d56` text color -- the warm crimson shift is a signature interaction
7. Shadows use large blur values (28px, 70px) for diffused atmospheric depth
8. The sub-8px spacing scale (1.5, 2, 2.5, 3, 4, 5, 6px) is critical for icon/text micro-alignment


### PPT-image Quick Reference

- Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
- Display voice: `CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial`
- Body / label voice: `jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times`
- Primary accent: Cursor Orange (#f54e00)
- Light surface anchor: Cursor Cream (#f2f1ed)
- Dark surface anchor: Cursor Dark (#26251e)
- Signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), berkeleyMono for code and technical labels, and Warm off-white background (#f2f1ed) instead of pure white -- the entire system is warm-shifted
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Cursor.
Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
Use CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial as the display-type reference and jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times for any short in-image labels.
Keep the palette anchored in Cursor Cream (#f2f1ed), Cursor Dark (#26251e), and Cursor Orange (#f54e00).
Preserve these signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), and berkeleyMono for code and technical labels.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Cursor.
Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
Use CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial as the display-type reference and jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times for any short in-image labels.
Keep the palette anchored in Cursor Cream (#f2f1ed), Cursor Dark (#26251e), and Cursor Orange (#f54e00).
Preserve these signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), and berkeleyMono for code and technical labels.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Cursor.
Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
Use CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial as the display-type reference and jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times for any short in-image labels.
Keep the palette anchored in Cursor Cream (#f2f1ed), Cursor Dark (#26251e), and Cursor Orange (#f54e00).
Preserve these signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), and berkeleyMono for code and technical labels.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Cursor.
Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
Use CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial as the display-type reference and jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times for any short in-image labels.
Keep the palette anchored in Cursor Cream (#f2f1ed), Cursor Dark (#26251e), and Cursor Orange (#f54e00).
Preserve these signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), and berkeleyMono for code and technical labels.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Cursor.
Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
Use CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial as the display-type reference and jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times for any short in-image labels.
Keep the palette anchored in Cursor Cream (#f2f1ed), Cursor Dark (#26251e), and Cursor Orange (#f54e00).
Preserve these signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), and berkeleyMono for code and technical labels.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Cursor.
Brand mood: Cursor's website is a study in warm minimalism meets code-editor elegance.
Use CursorGothic, with fallbacks: CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial as the display-type reference and jjannon, with fallbacks: Iowan Old Style, Palatino Linotype, URW Palladio L, P052, ui-serif, Georgia, Cambria, Times New Roman, Times for any short in-image labels.
Keep the palette anchored in Cursor Cream (#f2f1ed), Cursor Dark (#26251e), and Cursor Orange (#f54e00).
Preserve these signature cues: CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px) for compressed display headings, jjannon serif for body text with OpenType "cswh" (contextual swash alternates), and berkeleyMono for code and technical labels.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
