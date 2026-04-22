# PPT-image Design System Inspired by Framer

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Framer.

Source reference: `source/framer/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Framer's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft. The entire experience is drenched in pure black — not a warm charcoal or a cozy dark gray, but an absolute void (`#000000`) that makes every element, every screenshot, every typographic flourish feel like it's floating in deep space. This is a website that treats its own product UI as the hero art, embedding full-fidelity screenshots and interactive demos directly into the narrative flow.

The typography is the signature move: GT Walsheim with aggressively tight letter-spacing (as extreme as -5.5px on 110px display text) creates headlines that feel compressed, kinetic, almost spring-loaded — like words under pressure that might expand at any moment. The transition to Inter for body text is seamless, with extensive OpenType feature usage (`cv01`, `cv05`, `cv09`, `cv11`, `ss03`, `ss07`) that gives even small text a refined, custom feel. Framer Blue (`#0099ff`) is deployed sparingly but decisively — as link color, border accents, and subtle ring shadows — creating a cold, electric throughline against the warm-less black.

The overall effect is a nightclub for web designers: dark, precise, seductive, and unapologetically product-forward. Every section exists to showcase what the tool can do, with the website itself serving as proof of concept.

**Key Characteristics:**
- Pure black (`#000000`) void canvas — absolute dark, not warm or gray-tinted
- GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px)
- Framer Blue (`#0099ff`) as the sole accent color — cold, electric, precise
- Pill-shaped buttons (40px–100px radius) — no sharp corners on interactive elements
- Product screenshots as hero art — the tool IS the marketing
- Frosted glass button variants using `rgba(255, 255, 255, 0.1)` on dark surfaces
- Extensive OpenType feature usage across Inter for refined micro-typography


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), Framer Blue (#0099ff) as the sole accent color — cold, electric, precise, and Pill-shaped buttons (40px–100px radius) — no sharp corners on interactive elements.
- Use Framer Blue (#0099ff) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Pure Black (#000000) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Pure Black** (`#000000`): Primary background, the void canvas that defines Framer's dark-first identity
- **Pure White** (`#ffffff`): Primary text color on dark surfaces, button text on accent backgrounds
- **Framer Blue** (`#0099ff`): Primary accent color — links, borders, ring shadows, interactive highlights

### Secondary & Accent
- **Muted Silver** (`#a6a6a6`): Secondary text, subdued labels, dimmed descriptions on dark surfaces
- **Near Black** (`#090909`): Elevated dark surface, shadow ring color for subtle depth separation

### Surface & Background
- **Void Black** (`#000000`): Page background, primary canvas
- **Frosted White** (`rgba(255, 255, 255, 0.1)`): Translucent button backgrounds, glass-effect surfaces on dark
- **Subtle White** (`rgba(255, 255, 255, 0.5)`): Slightly more opaque frosted elements for hover states

### Neutrals & Text
- **Pure White** (`#ffffff`): Heading text, high-emphasis body text
- **Muted Silver** (`#a6a6a6`): Body text, descriptions, secondary information
- **Ghost White** (`rgba(255, 255, 255, 0.6)`): Tertiary text, placeholders on dark surfaces

### Semantic & Accent
- **Framer Blue** (`#0099ff`): Links, interactive borders, focus rings
- **Blue Glow** (`rgba(0, 153, 255, 0.15)`): Focus ring shadow, subtle blue halo around interactive elements
- **Default Link Blue** (`#0000ee`): Standard browser link color (used sparingly in content areas)

### Gradient System
- No prominent gradient usage — Framer relies on pure flat black surfaces with occasional blue-tinted glows for depth
- Subtle radial glow effects behind product screenshots using Framer Blue at very low opacity


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Pure Black (#000000) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Framer Blue (#0099ff) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Display**: `GT Walsheim Framer Medium` / `GT Walsheim Medium` — custom geometric sans-serif, weight 500. Fallbacks: `GT Walsheim Framer Medium Placeholder`, system sans-serif
- **Body/UI**: `Inter Variable` / `Inter` — variable sans-serif with extensive OpenType features. Fallbacks: `Inter Placeholder`, `-apple-system`, `system-ui`
- **Accent**: `Mona Sans` — GitHub's open-source font, used for select elements at ultra-light weight (100)
- **Monospace**: `Azeret Mono` — companion mono for code and technical labels
- **Rounded**: `Open Runde` — small rounded companion font for micro-labels

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | GT Walsheim Framer Medium | 110px | 500 | 0.85 | -5.5px | Extreme negative tracking, compressed impact |
| Section Display | GT Walsheim Medium | 85px | 500 | 0.95 | -4.25px | OpenType: ss02, tnum |
| Section Heading | GT Walsheim Medium | 62px | 500 | 1.00 | -3.1px | OpenType: ss02 |
| Feature Heading | GT Walsheim Medium | 32px | 500 | 1.13 | -1px | Tightest of the smaller headings |
| Accent Display | Mona Sans | 61.5px | 100 | 1.00 | -3.1px | Ultra-light weight, ethereal |
| Card Title | Inter Variable | 24px | 400 | 1.30 | -0.01px | OpenType: cv01, cv05, cv09, cv11, ss03, ss07 |
| Feature Title | Inter | 22px | 700 | 1.20 | -0.8px | OpenType: cv05 |
| Sub-heading | Inter | 20px | 600 | 1.20 | -0.8px | OpenType: cv01, cv09 |
| Body Large | Inter Variable | 18px | 400 | 1.30 | -0.01px | OpenType: cv01, cv05, cv09, cv11, ss03, ss07 |
| Body | Inter Variable | 15px | 400 | 1.30 | -0.01px | OpenType: cv11 |
| Nav/UI | Inter Variable | 15px | 400 | 1.00 | -0.15px | OpenType: cv06, cv11, dlig, ss03 |
| Body Readable | Inter Framer Regular | 14px | 400 | 1.60 | normal | Long-form body text |
| Caption | Inter Variable | 14px | 400 | 1.40 | normal | OpenType: cv01, cv06, cv09, cv11, ss03, ss07 |
| Label | Inter | 13px | 500 | 1.60 | normal | OpenType: cv06, cv11, ss03 |
| Small Caption | Inter Variable | 12px | 400 | 1.40 | normal | OpenType: cv01, cv06, cv09, cv11, ss03, ss07 |
| Micro Code | Azeret Mono | 10.4px | 400 | 1.60 | normal | OpenType: cv06, cv11, ss03 |
| Badge | Open Runde | 9px | 600 | 1.11 | normal | OpenType: cv01, cv09 |
| Micro Uppercase | Inter Variable | 7px | 400 | 1.00 | 0.21px | uppercase transform |

### Principles
- **Compression as personality**: GT Walsheim's extreme negative letter-spacing (-5.5px at 110px) is the defining typographic gesture — headlines feel spring-loaded, urgent, almost breathless
- **OpenType maximalism**: Inter is deployed with 6+ OpenType features simultaneously (`cv01`, `cv05`, `cv09`, `cv11`, `ss03`, `ss07`), creating a subtly custom feel even at body sizes
- **Weight restraint on display**: All GT Walsheim usage is weight 500 (medium) — never bold, never regular. This creates a confident-but-not-aggressive display tone
- **Ultra-tight line heights**: Display text at 0.85 line-height means letters nearly overlap vertically — intentional density that rewards reading at arm's length


### PPT-image Type Deployment

- Use `GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- **Frosted Pill**: `rgba(255, 255, 255, 0.1)` background, black text (`#000000`), pill shape (40px radius). The glass-effect button that lives on dark surfaces — translucent, ambient, subtle
- **Solid White Pill**: `rgb(255, 255, 255)` background, black text (`#000000`), full pill shape (100px radius), padding `10px 15px`. The primary CTA — clean, high-contrast on dark, unmissable
- **Ghost**: No visible background, white text, relies on text styling alone. Hover reveals subtle frosted background
- **Transition**: Scale-based animations (matrix transform with 0.85 scale factor), opacity transitions for reveal effects

### Cards & Containers
- **Dark Surface Card**: Black or near-black (`#090909`) background, `rgba(0, 153, 255, 0.15) 0px 0px 0px 1px` blue ring shadow border, rounded corners (10px–15px radius)
- **Elevated Card**: Multi-layer shadow — `rgba(255, 255, 255, 0.1) 0px 0.5px 0px 0.5px` (subtle top highlight) + `rgba(0, 0, 0, 0.25) 0px 10px 30px` (deep ambient shadow)
- **Product Screenshots**: Full-width or padded within dark containers, 8px–12px border-radius for software UI previews
- **Hover**: Subtle glow increase on Framer Blue ring shadow, or brightness shift on frosted surfaces

### Inputs & Forms
- Minimal form presence on the marketing site
- Input fields follow dark theme: dark background, subtle border, white text
- Focus state: Framer Blue (`#0099ff`) ring border, `1px solid #0099ff`
- Placeholder text in `rgba(255, 255, 255, 0.4)`

### Navigation
- **Dark floating nav bar**: Black background with frosted glass effect, white text links
- **Nav links**: Inter at 15px, weight 400, white text with subtle hover opacity change
- **CTA button**: Pill-shaped, white or frosted, positioned at right end of nav
- **Mobile**: Collapses to hamburger menu, maintains dark theme
- **Sticky behavior**: Nav remains fixed at top on scroll

### Image Treatment
- **Product screenshots as hero art**: Full-width embedded UI screenshots with rounded corners (8px–12px)
- **Dark-on-dark composition**: Screenshots placed on black backgrounds with subtle shadow for depth separation
- **16:9 and custom aspect ratios**: Product demos fill their containers
- **No decorative imagery**: All images are functional — showing the tool, the output, or the workflow

### Trust & Social Proof
- Customer logos and testimonials in muted gray on dark surfaces
- Minimal ornamentation — the product screenshots serve as the trust signal


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Framer's strongest visual cues as one large, unmistakable scene or object.
- Let Framer Blue (#0099ff), Pure White (#ffffff), and Pure Black (#000000) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Framer.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Pure Black (#000000), with Framer Blue (#0099ff) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System, Grid & Container, and Whitespace Philosophy) to create clean fields for charts, numerals, or callouts.
- Avoid hero subjects that fight the actual data layer.

#### System / Workflow Plate

- Convert the original component logic into presentation diagrams, route maps, or structural visuals rather than literal product UI.
- Keep the image designed, not tool-generated: large shapes, few node types, deliberate connectors, and brand-consistent type.
- Depth should follow Shadow Philosophy and Decorative Depth instead of generic infographic shadows.

#### Closing Poster

- Compress the deck's final judgment into one memorable frame.
- Use the same brand surfaces and accent hierarchy, but simplify harder than the cover.
- The closing image should resolve the story, not reopen complexity.

## 5. Layout Principles

### Original Layout DNA

### Spacing System
- **Base unit**: 8px
- **Scale**: 1px, 2px, 3px, 4px, 5px, 6px, 8px, 10px, 12px, 15px, 20px, 30px, 35px
- **Section padding**: Large vertical spacing (80px–120px between sections)
- **Card padding**: 15px–30px internal padding
- **Component gaps**: 8px–20px between related elements

### Grid & Container
- **Max width**: ~1200px container, centered
- **Column patterns**: Full-width hero, 2-column feature sections, single-column product showcases
- **Asymmetric layouts**: Feature sections often pair text (40%) with screenshot (60%)

### Whitespace Philosophy
- **Breathe through darkness**: Generous vertical spacing between sections — the black background means whitespace manifests as void, creating dramatic pauses between content blocks
- **Dense within, spacious between**: Individual components are tightly composed (tight line-heights, compressed text) but float in generous surrounding space
- **Product-first density**: Screenshot areas are allowed to be dense and information-rich, contrasting with the sparse marketing text

### Border Radius Scale
- **1px**: Micro-elements, nearly squared precision edges
- **5px–7px**: Small UI elements, image thumbnails — subtly softened
- **8px**: Standard component radius — code blocks, buttons, interactive elements
- **10px–12px**: Cards, product screenshots — comfortably rounded
- **15px–20px**: Large containers, feature cards — generously rounded
- **30px–40px**: Navigation pills, pagination — noticeably rounded
- **100px**: Full pill shape — primary CTAs, tag elements


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
| Level 0 (Flat) | No shadow, pure black surface | Page background, empty areas |
| Level 1 (Ring) | `rgba(0, 153, 255, 0.15) 0px 0px 0px 1px` | Card borders, interactive element outlines — Framer Blue glow ring |
| Level 2 (Contained) | `rgb(9, 9, 9) 0px 0px 0px 2px` | Near-black ring for subtle containment on dark surfaces |
| Level 3 (Floating) | `rgba(255, 255, 255, 0.1) 0px 0.5px 0px 0.5px, rgba(0, 0, 0, 0.25) 0px 10px 30px` | Elevated cards, floating elements — subtle white top-edge highlight + deep ambient shadow |

### Shadow Philosophy
Framer's elevation system is inverted from traditional light-theme designs. Instead of darker shadows on light backgrounds, Framer uses:
- **Blue-tinted ring shadows** at very low opacity (0.15) for containment — a signature move that subtly brands every bordered element
- **White edge highlights** (0.5px) on the top edge of elevated elements — simulating light hitting the top surface
- **Deep ambient shadows** for true floating elements — `rgba(0, 0, 0, 0.25)` at large spread (30px)

### Decorative Depth
- **Blue glow auras**: Subtle Framer Blue (`#0099ff`) radial gradients behind key interactive areas
- **No background blur/glassmorphism**: Despite the frosted button effect, there's no heavy glass blur usage — the translucency is achieved through simple rgba opacity


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use pure black (`#000000`) as the primary background — not dark gray, not charcoal
- Apply extreme negative letter-spacing on GT Walsheim display text (-3px to -5.5px)
- Keep all buttons pill-shaped (40px+ radius) — never use squared or slightly-rounded buttons
- Use Framer Blue (`#0099ff`) exclusively for interactive accents — links, borders, focus states
- Deploy `rgba(255, 255, 255, 0.1)` for frosted glass surfaces on dark backgrounds
- Maintain GT Walsheim at weight 500 only — the medium weight IS the brand
- Use extensive OpenType features on Inter text (cv01, cv05, cv09, cv11, ss03, ss07)
- Let product screenshots be the visual centerpiece — the tool markets itself
- Apply blue ring shadows (`rgba(0, 153, 255, 0.15) 0px 0px 0px 1px`) for card containment

### Don't
- Use warm dark backgrounds (no `#1a1a1a`, `#2d2d2d`, or brownish blacks)
- Apply bold (700+) weight to GT Walsheim display text — medium 500 only
- Introduce additional accent colors beyond Framer Blue — this is a one-accent-color system
- Use large border-radius on non-interactive elements (cards use 10px–15px, only buttons get 40px+)
- Add decorative imagery, illustrations, or icons — the product IS the illustration
- Use positive letter-spacing on headlines — everything is compressed, negative tracking
- Create heavy drop shadows — depth is communicated through subtle rings and minimal ambients
- Place light/white backgrounds behind content sections — the void is sacred
- Use serif or display-weight fonts — the system is geometric sans-serif only


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
| Mobile | <809px | Single column, stacked feature sections, reduced hero text (62px→40px), hamburger nav |
| Tablet | 809px–1199px | 2-column features begin, nav links partially visible, screenshots scale down |
| Desktop | >1199px | Full layout, expanded nav with all links + CTA, 110px display hero, side-by-side features |

### Touch Targets
- Pill buttons: minimum 40px height with 10px vertical padding — exceeds 44px WCAG minimum
- Nav links: 15px text with generous padding for touch accessibility
- Mobile CTA buttons: Full-width pills on mobile for easy thumb reach

### Collapsing Strategy
- **Navigation**: Full horizontal nav → hamburger menu at mobile breakpoint
- **Hero text**: 110px display → 85px → 62px → ~40px across breakpoints, maintaining extreme negative tracking proportionally
- **Feature sections**: Side-by-side (text + screenshot) → stacked vertically on mobile
- **Product screenshots**: Scale responsively within containers, maintaining aspect ratios
- **Section spacing**: Reduces proportionally — 120px desktop → 60px mobile

### Image Behavior
- Product screenshots are responsive, scaling within their container boundaries
- No art direction changes — same crops across breakpoints
- Dark background ensures screenshots maintain visual impact at any size
- Screenshots lazy-load as user scrolls into view


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary Background: Void Black (`#000000`)
- Primary Text: Pure White (`#ffffff`)
- Accent/CTA: Framer Blue (`#0099ff`)
- Secondary Text: Muted Silver (`#a6a6a6`)
- Frosted Surface: Translucent White (`rgba(255, 255, 255, 0.1)`)
- Elevation Ring: Blue Glow (`rgba(0, 153, 255, 0.15)`)

### Example Component Prompts
- "Create a hero section on pure black background with 110px GT Walsheim heading in white, letter-spacing -5.5px, line-height 0.85, and a pill-shaped white CTA button (100px radius) with black text"
- "Design a feature card on black background with a 1px Framer Blue ring shadow border (rgba(0,153,255,0.15)), 12px border-radius, white heading in Inter at 22px weight 700, and muted silver (a6a6a6) body text"
- "Build a navigation bar with black background, white Inter text links at 15px, and a frosted pill button (rgba(255,255,255,0.1) background, 40px radius) as the CTA"
- "Create a product showcase section with a full-width screenshot embedded on black, 10px border-radius, subtle multi-layer shadow (white 0.5px top highlight + rgba(0,0,0,0.25) 30px ambient)"
- "Design a pricing card using pure black surface, Framer Blue (#0099ff) accent for the selected plan border, white text hierarchy (24px Inter bold heading, 14px regular body), and a solid white pill CTA button"

### Iteration Guide
When refining existing screens generated with this design system:
1. Focus on ONE component at a time — the dark canvas makes each element precious
2. Always verify letter-spacing on GT Walsheim headings — the extreme negative tracking is non-negotiable
3. Check that Framer Blue appears ONLY on interactive elements — never as decorative background or text color for non-links
4. Ensure all buttons are pill-shaped — any squared corner immediately breaks the Framer aesthetic
5. Test frosted glass surfaces by checking they have exactly `rgba(255, 255, 255, 0.1)` — too opaque looks like a bug, too transparent disappears


### PPT-image Quick Reference

- Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
- Display voice: `GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif`
- Body / label voice: `Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui`
- Primary accent: Framer Blue (#0099ff)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Pure Black (#000000)
- Signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), Framer Blue (#0099ff) as the sole accent color — cold, electric, precise, and Pill-shaped buttons (40px–100px radius) — no sharp corners on interactive elements
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Framer.
Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
Use GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif as the display-type reference and Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Framer Blue (#0099ff).
Preserve these signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), and Framer Blue (#0099ff) as the sole accent color — cold, electric, precise.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Framer.
Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
Use GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif as the display-type reference and Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Framer Blue (#0099ff).
Preserve these signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), and Framer Blue (#0099ff) as the sole accent color — cold, electric, precise.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Framer.
Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
Use GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif as the display-type reference and Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Framer Blue (#0099ff).
Preserve these signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), and Framer Blue (#0099ff) as the sole accent color — cold, electric, precise.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Framer.
Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
Use GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif as the display-type reference and Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Framer Blue (#0099ff).
Preserve these signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), and Framer Blue (#0099ff) as the sole accent color — cold, electric, precise.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Framer.
Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
Use GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif as the display-type reference and Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Framer Blue (#0099ff).
Preserve these signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), and Framer Blue (#0099ff) as the sole accent color — cold, electric, precise.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Framer.
Brand mood: Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft.
Use GT Walsheim Framer Medium / GT Walsheim Medium — custom geometric sans-serif, weight 500. Fallbacks: GT Walsheim Framer Medium Placeholder, system sans-serif as the display-type reference and Inter Variable / Inter — variable sans-serif with extensive OpenType features. Fallbacks: Inter Placeholder, -apple-system, system-ui for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Framer Blue (#0099ff).
Preserve these signature cues: Pure black (#000000) void canvas — absolute dark, not warm or gray-tinted, GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px), and Framer Blue (#0099ff) as the sole accent color — cold, electric, precise.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
