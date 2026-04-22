# PPT-image Design System Inspired by Sentry

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Sentry.

Source reference: `source/sentry/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Sentry's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows. The entire aesthetic is rooted in deep purple-black backgrounds (`#1f1633`, `#150f23`) that evoke the late-night debugging sessions Sentry was built for. Against this inky canvas, a carefully curated set of purples, pinks, and a distinctive lime-green accent (`#c2ef4e`) create a visual system that feels simultaneously technical and vibrant.

The typography pairing is deliberate: "Dammit Sans" appears at hero scale (88px, weight 700) as a display font with personality and attitude that matches Sentry's irreverent brand voice ("Code breaks. Fix it faster."), while Rubik serves as the workhorse UI font across all functional text — headings, body, buttons, captions, and navigation. Monaco provides the monospace layer for code snippets and technical content, completing the developer-tool trinity.

What makes Sentry distinctive is its embrace of the "dark IDE" aesthetic without feeling cold or sterile. Warm purple tones replace the typical cool grays of developer tools, and bold illustrative elements (3D characters, colorful product screenshots) punctuate the dark canvas. The button system uses a signature muted purple (`#79628c`) with inset shadows that creates a tactile, almost physical quality — buttons feel like they could be pressed into the surface.

**Key Characteristics:**
- Dark purple-black backgrounds (`#1f1633`, `#150f23`) — never pure black
- Warm purple accent spectrum: from deep (`#362d59`) through mid (`#79628c`, `#6a5fc1`) to vibrant (`#422082`)
- Lime-green accent (`#c2ef4e`) for high-visibility CTAs and highlights
- Pink/coral accents (`#ffb287`, `#fa7faa`) for focus states and secondary highlights
- "Dammit Sans" display font for brand personality at hero scale
- Rubik as primary UI font with uppercase letter-spaced labels
- Monaco monospace for code elements
- Inset shadows on buttons creating tactile depth
- Frosted glass effects with `blur(18px) saturate(180%)`


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights, and Pink/coral accents (#ffb287, #fa7faa) for focus states and secondary highlights.
- Use Deep Purple (#1f1633) as the highest-signal accent when color needs to carry emphasis.
- Let Input White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Darker Purple (#150f23) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary Brand
- **Deep Purple** (`#1f1633`): Primary background, the defining color of the brand
- **Darker Purple** (`#150f23`): Deeper sections, footer, secondary backgrounds
- **Border Purple** (`#362d59`): Borders, dividers, subtle structural lines

### Accent Colors
- **Sentry Purple** (`#6a5fc1`): Primary interactive color — links, hover states, focus rings
- **Muted Purple** (`#79628c`): Button backgrounds, secondary interactive elements
- **Deep Violet** (`#422082`): Select dropdowns, active states, high-emphasis surfaces
- **Lime Green** (`#c2ef4e`): High-visibility accent, special links, badge highlights
- **Coral** (`#ffb287`): Focus state backgrounds, warm accent
- **Pink** (`#fa7faa`): Focus outlines, decorative accents

### Text Colors
- **Pure White** (`#ffffff`): Primary text on dark backgrounds
- **Light Gray** (`#e5e7eb`): Secondary text, muted content
- **Code Yellow** (`#dcdcaa`): Syntax highlighting, code tokens

### Surface & Overlay
- **Glass White** (`rgba(255, 255, 255, 0.18)`): Frosted glass button backgrounds
- **Glass Dark** (`rgba(54, 22, 107, 0.14)`): Hover overlay on glass elements
- **Input White** (`#ffffff`): Form input backgrounds (light context)
- **Input Border** (`#cfcfdb`): Form field borders

### Shadows
- **Ambient Glow** (`rgba(22, 15, 36, 0.9) 0px 4px 4px 9px`): Deep purple ambient shadow
- **Button Hover** (`rgba(0, 0, 0, 0.18) 0px 0.5rem 1.5rem`): Elevated hover state
- **Card Shadow** (`rgba(0, 0, 0, 0.1) 0px 10px 15px -3px`): Standard card elevation
- **Inset Button** (`rgba(0, 0, 0, 0.1) 0px 1px 3px 0px inset`): Tactile pressed effect


### PPT-image Deployment

- Base canvas: prefer Input White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Darker Purple (#150f23) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Deep Purple (#1f1633) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `Dammit Sans` — brand personality font for hero headings
- **Primary UI**: `Rubik`, with fallbacks: `-apple-system, system-ui, Segoe UI, Helvetica, Arial`
- **Monospace**: `Monaco`, with fallbacks: `Menlo, Ubuntu Mono`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Dammit Sans | 88px (5.50rem) | 700 | 1.20 (tight) | normal | Maximum impact, brand voice |
| Display Secondary | Dammit Sans | 60px (3.75rem) | 500 | 1.10 (tight) | normal | Secondary hero text |
| Section Heading | Rubik | 30px (1.88rem) | 400 | 1.20 (tight) | normal | Major section titles |
| Sub-heading | Rubik | 27px (1.69rem) | 500 | 1.25 (tight) | normal | Feature section headers |
| Card Title | Rubik | 24px (1.50rem) | 500 | 1.25 (tight) | normal | Card and block headings |
| Feature Title | Rubik | 20px (1.25rem) | 600 | 1.25 (tight) | normal | Emphasized feature names |
| Body | Rubik | 16px (1.00rem) | 400 | 1.50 | normal | Standard body text |
| Body Emphasis | Rubik | 16px (1.00rem) | 500–600 | 1.50 | normal | Bold body, nav items |
| Nav Label | Rubik | 15px (0.94rem) | 500 | 1.40 | normal | Navigation links |
| Uppercase Label | Rubik | 15px (0.94rem) | 500 | 1.25 (tight) | normal | `text-transform: uppercase` |
| Button Text | Rubik | 14px (0.88rem) | 500–700 | 1.14–1.29 (tight) | 0.2px | `text-transform: uppercase` |
| Caption | Rubik | 14px (0.88rem) | 500–700 | 1.00–1.43 | 0.2px | Often uppercase |
| Small Caption | Rubik | 12px (0.75rem) | 600 | 2.00 (relaxed) | normal | Subtle annotations |
| Micro Label | Rubik | 10px (0.63rem) | 600 | 1.80 (relaxed) | 0.25px | `text-transform: uppercase` |
| Code | Monaco | 16px (1.00rem) | 400–700 | 1.50 | normal | Code blocks, technical text |

### Principles
- **Dual personality**: Dammit Sans brings irreverent brand character at display scale; Rubik provides clean professionalism for everything functional.
- **Uppercase as system**: Buttons, captions, labels, and micro-text all use `text-transform: uppercase` with subtle letter-spacing (0.2px–0.25px), creating a systematic "technical label" pattern throughout.
- **Weight stratification**: Rubik uses 400 (body), 500 (emphasis/nav), 600 (titles/strong), 700 (buttons/CTAs) — a clean four-tier weight system.
- **Tight headings, relaxed body**: All headings use 1.10–1.25 line-height; body uses 1.50; small captions expand to 2.00 for readability at tiny sizes.


### PPT-image Type Deployment

- Use `Dammit Sans — brand personality font for hero headings` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Muted Purple**
- Background: `#79628c` (rgb(121, 98, 140))
- Text: `#ffffff`, uppercase, 14px, weight 500–700, letter-spacing 0.2px
- Border: `1px solid #584674`
- Radius: 13px
- Shadow: `rgba(0, 0, 0, 0.1) 0px 1px 3px 0px inset` (tactile inset)
- Hover: elevated shadow `rgba(0, 0, 0, 0.18) 0px 0.5rem 1.5rem`

**Glass White**
- Background: `rgba(255, 255, 255, 0.18)` (frosted glass)
- Text: `#ffffff`
- Padding: 8px
- Radius: 12px (left-aligned variant: `12px 0px 0px 12px`)
- Shadow: `rgba(0, 0, 0, 0.08) 0px 2px 8px`
- Hover background: `rgba(54, 22, 107, 0.14)`
- Use: Secondary actions on dark surfaces

**White Solid**
- Background: `#ffffff`
- Text: `#1f1633`
- Padding: 12px 16px
- Radius: 8px
- Hover: background transitions to `#6a5fc1`, text to white
- Focus: background `#ffb287` (coral), outline `rgb(106, 95, 193) solid 0.125rem`
- Use: High-visibility CTA on dark backgrounds

**Deep Violet (Select/Dropdown)**
- Background: `#422082`
- Text: `#ffffff`
- Padding: 8px 16px
- Radius: 8px

### Inputs

**Text Input**
- Background: `#ffffff`
- Text: `#1f1633`
- Border: `1px solid #cfcfdb`
- Padding: 8px 12px
- Radius: 6px
- Focus: border-color stays `#cfcfdb`, shadow `rgba(0, 0, 0, 0.15) 0px 2px 10px inset`

### Links
- **Default on dark**: `#ffffff`, underline decoration
- **Hover**: color transitions to `#6a5fc1` (Sentry Purple)
- **Purple links**: `#6a5fc1` default, hover underline
- **Lime accent links**: `#c2ef4e` default, hover to `#6a5fc1`
- **Dark context links**: `#362d59`, hover to `#ffffff`

### Cards & Containers
- Background: semi-transparent or dark purple surfaces
- Radius: 8px–12px
- Shadow: `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px`
- Backdrop filter: `blur(18px) saturate(180%)` for glass effects

### Navigation
- Dark transparent header over hero content
- Rubik 15px weight 500 for nav links
- White text, hover to Sentry Purple (`#6a5fc1`)
- Uppercase labels with 0.2px letter-spacing for categories
- Mobile: hamburger menu, full-width expanded


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Sentry's strongest visual cues as one large, unmistakable scene or object.
- Let Deep Purple (#1f1633), Input White (#ffffff), and Darker Purple (#150f23) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Inputs, Links, and Cards & Containers rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Sentry.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Input White (#ffffff) versus Darker Purple (#150f23), with Deep Purple (#1f1633) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System, Grid & Container, and Breakpoints) to create clean fields for charts, numerals, or callouts.
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
- Scale: 1px, 2px, 4px, 5px, 6px, 8px, 12px, 16px, 24px, 32px, 40px, 44px, 45px, 47px

### Grid & Container
- Max content width: 1152px (XL breakpoint)
- Responsive padding: 2rem (mobile) → 4rem (tablet+)
- Content centered within container
- Full-width dark sections with contained inner content

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | < 576px | Single column, stacked layout |
| Small Tablet | 576–640px | Minor width adjustments |
| Tablet | 640–768px | 2-column begins |
| Small Desktop | 768–992px | Full nav visible |
| Desktop | 992–1152px | Standard layout |
| Large Desktop | 1152–1440px | Max-width content |

### Whitespace Philosophy
- **Dark breathing room**: Generous vertical spacing between sections (64px–80px+) lets the dark background serve as a visual rest.
- **Content islands**: Feature sections are self-contained blocks floating in the dark purple sea, each with its own internal spacing rhythm.
- **Asymmetric padding**: Buttons use asymmetric padding patterns (12px 16px, 8px 12px) that feel organic rather than rigid.

### Border Radius Scale
- Minimal (6px): Form inputs, small interactive elements
- Standard (8px): Buttons, cards, containers
- Comfortable (10px–12px): Larger containers, glass panels
- Rounded (13px): Primary muted buttons
- Pill (18px): Image containers, badges


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
| Sunken (Level -1) | Inset shadow `rgba(0, 0, 0, 0.1) 0px 1px 3px inset` | Primary buttons (tactile pressed feel) |
| Flat (Level 0) | No shadow | Default surfaces, dark backgrounds |
| Surface (Level 1) | `rgba(0, 0, 0, 0.08) 0px 2px 8px` | Glass buttons, subtle cards |
| Elevated (Level 2) | `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px` | Cards, floating panels |
| Prominent (Level 3) | `rgba(0, 0, 0, 0.18) 0px 0.5rem 1.5rem` | Hover states, modals |
| Ambient (Level 4) | `rgba(22, 15, 36, 0.9) 0px 4px 4px 9px` | Deep purple ambient glow around hero |

**Shadow Philosophy**: Sentry uses a unique combination of inset shadows (buttons feel pressed INTO the surface) and ambient glows (content radiates from the dark background). The deep purple ambient shadow (`rgba(22, 15, 36, 0.9)`) is the signature — it creates a bioluminescent quality where content seems to emit its own purple-tinted light.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use deep purple backgrounds (`#1f1633`, `#150f23`) — never pure black (`#000000`)
- Apply inset shadows on primary buttons for the tactile pressed effect
- Use Dammit Sans ONLY for hero/display headings — Rubik for everything else
- Apply `text-transform: uppercase` with `letter-spacing: 0.2px` on buttons and labels
- Use the lime-green accent (`#c2ef4e`) sparingly for maximum impact
- Employ frosted glass effects (`blur(18px) saturate(180%)`) for layered surfaces
- Maintain the warm purple shadow tones — shadows should feel purple-tinted, not neutral gray
- Use Rubik's 4-tier weight system: 400 (body), 500 (nav/emphasis), 600 (titles), 700 (CTAs)

### Don't
- Don't use pure black (`#000000`) for backgrounds — always use the warm purple-blacks
- Don't apply Dammit Sans to body text or UI elements — it's display-only
- Don't use standard gray (`#666`, `#999`) for borders — use purple-tinted grays (`#362d59`, `#584674`)
- Don't drop the uppercase treatment on buttons — it's a system-wide pattern
- Don't use sharp corners (0px radius) — minimum 6px for all interactive elements
- Don't mix the lime-green accent with the coral/pink accents in the same component
- Don't use flat (non-inset) shadows on primary buttons — the tactile quality is signature
- Don't forget letter-spacing on uppercase text — 0.2px minimum


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
| Mobile | <576px | Single column, hamburger nav, stacked CTAs |
| Tablet | 576–768px | 2-column feature grids begin |
| Small Desktop | 768–992px | Full navigation, side-by-side layouts |
| Desktop | 992–1152px | Max-width container, full layout |
| Large | >1152px | Content max-width maintained, generous margins |

### Collapsing Strategy
- Hero text: 88px Dammit Sans → 60px → mobile scales
- Navigation: horizontal → hamburger with slide-out
- Feature sections: side-by-side → stacked cards
- Buttons: inline → full-width stacked on mobile
- Container padding: 4rem → 2rem


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Background: `#1f1633` (primary), `#150f23` (deeper)
- Text: `#ffffff` (primary), `#e5e7eb` (secondary)
- Interactive: `#6a5fc1` (links/hover), `#79628c` (buttons)
- Accent: `#c2ef4e` (lime highlight), `#ffb287` (coral focus)
- Border: `#362d59` (dark), `#cfcfdb` (light context)

### Example Component Prompts
- "Create a hero section on deep purple background (#1f1633). Headline at 88px Dammit Sans weight 700, line-height 1.20, white text. Sub-text at 16px Rubik weight 400, line-height 1.50. White solid CTA button (8px radius, 12px 16px padding), hover transitions to #6a5fc1."
- "Design a navigation bar: transparent over dark background. Rubik 15px weight 500, white text. Uppercase category labels with 0.2px letter-spacing. Hover color #6a5fc1."
- "Build a primary button: background #79628c, border 1px solid #584674, inset shadow rgba(0,0,0,0.1) 0px 1px 3px, white uppercase text at 14px Rubik weight 700, letter-spacing 0.2px, radius 13px. Hover: shadow rgba(0,0,0,0.18) 0px 0.5rem 1.5rem."
- "Create a glass card panel: background rgba(255,255,255,0.18), backdrop-filter blur(18px) saturate(180%), radius 12px. White text content inside."
- "Design a feature section: #150f23 background, 24px Rubik weight 500 heading, 16px Rubik weight 400 body text. 14px uppercase lime-green (#c2ef4e) label above heading."

### Iteration Guide
1. Always start with the dark purple background — the color palette is built FOR dark mode
2. Use inset shadows on buttons, ambient purple glows on hero sections
3. Uppercase + letter-spacing is the systematic pattern for labels, buttons, and captions
4. Lime green (#c2ef4e) is the "pop" color — use once per section maximum
5. Frosted glass for overlaid panels, solid purple for primary surfaces
6. Rubik handles 90% of typography — Dammit Sans is hero-only


### PPT-image Quick Reference

- Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
- Display voice: `Dammit Sans — brand personality font for hero headings`
- Body / label voice: `Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial`
- Primary accent: Deep Purple (#1f1633)
- Light surface anchor: Input White (#ffffff)
- Dark surface anchor: Darker Purple (#150f23)
- Signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights, and Pink/coral accents (#ffb287, #fa7faa) for focus states and secondary highlights
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Sentry.
Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
Use Dammit Sans — brand personality font for hero headings as the display-type reference and Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Input White (#ffffff), Darker Purple (#150f23), and Deep Purple (#1f1633).
Preserve these signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), and Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Sentry.
Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
Use Dammit Sans — brand personality font for hero headings as the display-type reference and Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Input White (#ffffff), Darker Purple (#150f23), and Deep Purple (#1f1633).
Preserve these signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), and Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Sentry.
Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
Use Dammit Sans — brand personality font for hero headings as the display-type reference and Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Input White (#ffffff), Darker Purple (#150f23), and Deep Purple (#1f1633).
Preserve these signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), and Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Sentry.
Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
Use Dammit Sans — brand personality font for hero headings as the display-type reference and Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Input White (#ffffff), Darker Purple (#150f23), and Deep Purple (#1f1633).
Preserve these signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), and Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Sentry.
Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
Use Dammit Sans — brand personality font for hero headings as the display-type reference and Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Input White (#ffffff), Darker Purple (#150f23), and Deep Purple (#1f1633).
Preserve these signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), and Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Sentry.
Brand mood: Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows.
Use Dammit Sans — brand personality font for hero headings as the display-type reference and Rubik, with fallbacks: -apple-system, system-ui, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Input White (#ffffff), Darker Purple (#150f23), and Deep Purple (#1f1633).
Preserve these signature cues: Dark purple-black backgrounds (#1f1633, #150f23) — never pure black, Warm purple accent spectrum: from deep (#362d59) through mid (#79628c, #6a5fc1) to vibrant (#422082), and Lime-green accent (#c2ef4e) for high-visibility CTAs and highlights.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
