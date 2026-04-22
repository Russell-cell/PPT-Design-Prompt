# PPT-image Design System Inspired by Superhuman

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Superhuman.

Source reference: `source/superhuman/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Superhuman's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention. The hero section is a cinematic purple gradient, a deep twilight wash of `#1b1938` that evokes the moment just before dawn, overlaid with confident white typography. Below this dramatic entrance, the rest of the site is almost entirely white canvas with dark charcoal text, creating a stark but refined reading experience.

The typography is the true signature: Super Sans VF, a custom variable font with unconventional weight stops (460, 540, 600, 700) that sit between traditional font weight categories. Weight 460 — slightly heavier than regular but lighter than medium — is the workhorse, creating text that feels more confident than typical 400-weight but never aggressive. The tight line-heights (0.96 on display text) compress headlines into dense, powerful blocks, while generous 1.50 line-height on body text provides airy readability. This tension between compressed power and breathing room defines the Superhuman typographic voice.

The design philosophy is maximum confidence through minimum decoration. Warm cream buttons (`#e9e5dd`) instead of bright CTAs, a near-absence of borders and shadows, and lavender purple (`#cbb7fb`) as the sole accent color. It's a productivity tool that markets itself like a luxury brand — every pixel earns its place, nothing is merely decorative. The brand naming convention extends to colors: the primary purple is called "Mysteria," straddling blue and purple with deliberate ambiguity.

**Key Characteristics:**
- Deep purple gradient hero (`#1b1938`) contrasting against a predominantly white content body
- Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories
- Ultra-tight display line-height (0.96) creating compressed, powerful headlines
- Warm Cream (`#e9e5dd`) buttons instead of bright/saturated CTAs — understated luxury
- Lavender Purple (`#cbb7fb`) as the singular accent color — a soft, approachable purple
- Minimal border-radius scale: only 8px and 16px — no micro-rounding, no pill shapes
- Product screenshots dominate the content — the UI sells itself with minimal surrounding decoration


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, Ultra-tight display line-height (0.96) creating compressed, powerful headlines, and Warm Cream (#e9e5dd) buttons instead of bright/saturated CTAs — understated luxury.
- Use Mysteria Purple (#1b1938) as the highest-signal accent when color needs to carry emphasis.
- Let Charcoal Ink (#292827) carry calmer title-safe zones and quieter data-support slides.
- Use Charcoal Ink (#292827) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Mysteria Purple** (`#1b1938`): Hero gradient background, deep purple that straddles blue-purple — the darkest expression of the brand
- **Lavender Glow** (`#cbb7fb`): Primary accent and highlight color — soft purple used for emphasis, decorative elements, and interactive highlights
- **Charcoal Ink** (`#292827`): Primary text and heading color on light surfaces — warm near-black with faint brown undertone

### Secondary & Accent
- **Amethyst Link** (`#714cb6`): Underlined link text — mid-range purple that connects to the brand palette while signaling interactivity
- **Translucent White** (`color(srgb 1 1 1 / 0.95)`): Hero overlay text — near-white at 95% opacity for depth layering on dark surfaces
- **Misted White** (`color(srgb 1 1 1 / 0.8)`): Secondary text on dark surfaces — 80% opacity white for hierarchy on the hero gradient

### Surface & Background
- **Pure White** (`#ffffff`): Primary page background — the dominant canvas color for all content sections
- **Warm Cream** (`#e9e5dd`): Button background — a warm, neutral cream that avoids the coldness of pure gray
- **Parchment Border** (`#dcd7d3`): Card and divider borders — warm light gray with slight pink undertone

### Neutrals & Text
- **Charcoal Ink** (`#292827`): Primary heading and body text on white surfaces
- **Amethyst Link** (`#714cb6`): In-content links with underline decoration
- **Translucent White 95%** (`color(srgb 1 1 1 / 0.95)`): Primary text on dark/purple surfaces
- **Translucent White 80%** (`color(srgb 1 1 1 / 0.8)`): Secondary text on dark/purple surfaces

### Semantic & Accent
- Superhuman operates with extreme color restraint — Lavender Glow (`#cbb7fb`) is the only true accent
- Interactive states are communicated through opacity shifts and underline decorations rather than color changes
- The warm cream button palette avoids any saturated semantic colors (no red errors, green success visible on marketing)

### Gradient System
- **Hero Gradient**: Deep purple gradient starting from `#1b1938`, transitioning through purple-to-twilight tones across the hero section — the most dramatic visual element on the entire site
- **Content Transition**: The gradient dissolves into the white content area, creating a cinematic curtain-lift effect as the user scrolls
- No other gradients on the marketing site — the hero gradient is a singular dramatic gesture


### PPT-image Deployment

- Base canvas: prefer Charcoal Ink (#292827) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Charcoal Ink (#292827) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Mysteria Purple (#1b1938) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Display & Body**: `Super Sans VF` — custom variable font with non-standard weight axis. Fallbacks: `system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue`
- **Product UI** (referenced in brand): `Messina Sans` / `Messina Serif` / `Messina Mono` from Luzi Type — used in the product itself for sans-serif-to-serif transitions

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Super Sans VF | 64px | 540 | 0.96 | 0px | Maximum compression, powerful block headlines |
| Section Display | Super Sans VF | 48px | 460 | 0.96 | -1.32px | Lighter weight for section introductions |
| Section Heading | Super Sans VF | 48px | 460 | 0.96 | 0px | Alternate section heading without tracking |
| Feature Title | Super Sans VF | 28px | 540 | 1.14 | -0.63px | Feature block headlines, tighter |
| Sub-heading Large | Super Sans VF | 26px | 460 | 1.30 | 0px | Content sub-sections |
| Card Heading | Super Sans VF | 22px | 460 | 0.76 | -0.315px | Card title with extreme compression |
| Body Heading | Super Sans VF | 20px | 460 | 1.20 | 0px | Bold content intros |
| Body Heading Alt | Super Sans VF | 20px | 460 | 1.10 | -0.55px | Tighter variant for emphasis |
| Body Heading Relaxed | Super Sans VF | 20px | 460 | 1.25 | -0.4px | More breathing room variant |
| Emphasis Body | Super Sans VF | 18px | 540 | 1.50 | -0.135px | Medium-weight body for callouts |
| Body | Super Sans VF | 16px | 460 | 1.50 | 0px | Standard reading text — generous line-height |
| Button / UI Bold | Super Sans VF | 16px | 700 | 1.00 | 0px | Bold UI elements |
| Button / UI Semi | Super Sans VF | 16px | 600 | 1.00 | 0px | Semi-bold navigation and labels |
| Nav Link | Super Sans VF | 16px | 460 | 1.20 | 0px | Navigation items |
| Caption | Super Sans VF | 14px | 500 | 1.20 | -0.315px | Small labels, metadata |
| Caption Semi | Super Sans VF | 14px | 600 | 1.29 | 0px | Emphasized small text |
| Caption Body | Super Sans VF | 14px | 460 | 1.50 | 0px | Small body text |
| Micro Label | Super Sans VF | 12px | 700 | 1.50 | 0px | Smallest text — badges, tags |

### Principles
- **Non-standard weight axis**: Weights 460 and 540 are deliberately between conventional Regular (400) and Medium (500), creating a typographic texture that feels subtly "off" in a confident way — slightly heavier than expected, never quite bold
- **Extreme display compression**: Display headlines at 0.96 line-height collapse lines nearly on top of each other, creating dense typographic blocks that feel architectural
- **Body generosity**: In contrast, body text at 1.50 line-height is extremely spacious, ensuring comfortable reading after the dense headline impact
- **Selective negative tracking**: Letter-spacing is applied surgically — -1.32px on 48px headings, -0.63px on 28px features, but 0px on body text. The larger the text, the tighter the tracking
- **Variable font efficiency**: A single font file serves all weight variations (460–700), enabling smooth weight transitions and micro-adjustments


### PPT-image Type Deployment

- Use `Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- **Warm Cream Primary**: `#e9e5dd` background, Charcoal Ink (`#292827`) text, subtle rounded corners (8px radius), no visible border. The signature CTA — warm, muted, luxurious rather than aggressive
- **Dark Primary** (on light sections): `#292827` background with white text, 8px radius — inverse of the warm cream for contrast sections
- **Ghost / Text Link**: No background, underline decoration, Amethyst Link (`#714cb6`) or Charcoal Ink color depending on context
- **Hero CTA**: Warm Cream on the dark purple gradient — the cream color pops dramatically against `#1b1938`
- **Hover**: Subtle opacity or brightness shift — no dramatic color transformations

### Cards & Containers
- **Content Card**: White background, Parchment Border (`#dcd7d3`) 1px border, 16px border-radius — clean and minimal
- **Dark Surface Card**: `#292827` border on dark sections, maintaining warm-neutral tone
- **Hero Surface**: Semi-transparent white border (`rgba(255, 255, 255, 0.2)`) on purple gradient — ghostly containment
- **Product Screenshot Cards**: Large product UI images with clean edges, minimal framing — the product itself is the visual
- **Hover**: Minimal state changes — consistency and calm over flashy interactions

### Inputs & Forms
- Minimal form presence on the marketing site — Superhuman funnels users directly to signup
- Dark-bordered inputs with Charcoal Ink borders and warm-toned placeholder text
- Focus: Border emphasis increase, likely shifting from Parchment Border to Charcoal Ink

### Navigation
- **Top nav**: Clean white background on content sections, transparent on hero gradient
- **Nav links**: Super Sans VF at 16px, weight 460/600 for hierarchy
- **CTA button**: Warm Cream (`#e9e5dd`) pill in the nav — subtle, not attention-grabbing
- **Sticky behavior**: Nav remains fixed on scroll with background transition
- **Mobile**: Collapses to hamburger menu with simplified layout

### Image Treatment
- **Product screenshots**: Large, dominant product UI images showing the email interface — the product is the hero
- **Lifestyle photography**: A single dramatic image (silhouette against purple/red gradient) in the hero area — cinematic and editorial
- **Full-width presentation**: Screenshots span full container width with subtle shadow or no border
- **Aspect ratios**: Wide landscape ratios (roughly 16:9) for product screenshots
- **Color integration**: Screenshots are carefully color-graded to harmonize with the purple-to-white page flow

### Testimonial / Social Proof
- "Your Superhuman suite" section with product feature grid
- Feature descriptions paired with product screenshots — proof through demonstration rather than quotes
- Clean grid layout with consistent card sizing


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Superhuman's strongest visual cues as one large, unmistakable scene or object.
- Let Mysteria Purple (#1b1938), Charcoal Ink (#292827), and Charcoal Ink (#292827) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Superhuman.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Charcoal Ink (#292827) versus Charcoal Ink (#292827), with Mysteria Purple (#1b1938) reserved for the decisive signal.
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
- **Scale**: 2px, 4px, 6px, 8px, 12px, 16px, 18px, 20px, 24px, 28px, 32px, 36px, 40px, 48px, 56px
- **Section padding**: 48px–80px vertical between major sections
- **Card padding**: 16px–32px internal spacing
- **Component gaps**: 8px–16px between related elements

### Grid & Container
- **Max width**: ~1200px content container, centered
- **Column patterns**: Full-width hero, centered single-column for key messaging, 2-3 column grid for feature cards
- **Feature grid**: Even column distribution for "Your Superhuman suite" product showcase

### Whitespace Philosophy
- **Confident emptiness**: Generous whitespace between sections signals premium positioning — every element has room to breathe
- **Product as content**: Large product screenshots fill space that lesser sites would fill with marketing copy
- **Progressive density**: The hero is spacious and cinematic, content sections become denser with feature grids, then opens up again for CTAs

### Border Radius Scale
- **8px**: Buttons, inline elements (`span`, `button`, `div`) — the universal small radius
- **16px**: Cards, links, larger containers (`a`, card elements) — the universal large radius
- Only two radii in the entire system — radical simplicity. No micro-rounding (2px), no pill shapes (50px+)


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
| Level 0 (Flat) | No shadow, white background | Primary page canvas, most content surfaces |
| Level 1 (Border) | `1px solid #dcd7d3` (Parchment Border) | Card containment, section dividers |
| Level 2 (Dark Border) | `1px solid #292827` | Header elements, dark section separators |
| Level 3 (Glow) | Subtle shadow (from 6 shadow definitions detected) | Product screenshot containers, elevated cards |
| Level 4 (Hero Depth) | `rgba(255, 255, 255, 0.2)` transparent border | Elements on the dark purple gradient hero |

### Shadow Philosophy
Superhuman's elevation system is remarkably restrained on the marketing site. Depth is primarily communicated through:
- **Border containment**: Warm-toned borders (`#dcd7d3`) at 1px create gentle separation
- **Color contrast**: The hero gradient creates massive depth through color shift rather than shadows
- **Product screenshots**: Screenshots themselves create depth by showing a layered UI within the flat page
- **Opacity layering**: Semi-transparent whites on the hero gradient create atmospheric depth layers

### Decorative Depth
- **Hero gradient**: The `#1b1938` → white gradient transition is the primary depth device — a cinematic curtain effect
- **Lavender accents**: `#cbb7fb` Lavender Glow elements float above the dark gradient, creating a stellar/atmospheric effect
- **No glassmorphism**: Despite the translucent borders, there are no blur/frosted-glass effects
- **Photography depth**: The hero silhouette image creates natural atmospheric depth without artificial CSS


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Super Sans VF at weight 460 as the default — it's slightly heavier than regular, which is the brand's typographic signature
- Keep display headlines at 0.96 line-height — the compression is intentional and powerful
- Use Warm Cream (`#e9e5dd`) for primary buttons — not white, not gray, specifically warm cream
- Limit border-radius to 8px (small) and 16px (large) — the binary radius system is deliberate
- Apply negative letter-spacing on headlines only (-0.63px to -1.32px) — body text stays at 0px
- Use Lavender Glow (`#cbb7fb`) as the only accent color — it's the sole color departure from the neutral palette
- Let product screenshots be the primary visual content — the UI sells itself
- Maintain the dramatic hero gradient as a singular gesture — the rest of the page is white

### Don't
- Use conventional font weights (400, 500, 600) — Superhuman's 460 and 540 are deliberately between standard stops
- Add bright or saturated CTA colors (blue, green, red) — buttons are intentionally muted in Warm Cream or Charcoal
- Introduce additional accent colors beyond Lavender Glow — the palette is deliberately restrained to one accent
- Apply shadows generously — depth comes from borders, color contrast, and photography, not box-shadows
- Use tight line-height on body text — display is compressed (0.96) but body is generous (1.50)
- Add decorative elements, icons, or illustrations — Superhuman relies on product UI and minimal typography
- Create pill-shaped buttons — the system uses 8px radius, not rounded pills
- Use pure black (`#000000`) for text — Charcoal Ink (`#292827`) is warmer and softer


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
| Mobile | <768px | Single column, hero text reduces to ~36px, stacked feature cards, hamburger nav |
| Tablet | 768px–1024px | 2-column feature grid begins, hero text ~48px, nav partially visible |
| Desktop | 1024px–1440px | Full layout, 64px hero display, multi-column feature grid, full nav |
| Large Desktop | >1440px | Max-width container centered, generous side margins |

### Touch Targets
- Buttons: 8px radius with comfortable padding — meets touch target guidelines
- Nav links: 16px text with adequate surrounding padding
- Mobile CTAs: Full-width Warm Cream buttons for easy thumb reach
- Links: Underline decoration provides clear tap affordance

### Collapsing Strategy
- **Navigation**: Full horizontal nav → hamburger menu on mobile
- **Hero text**: 64px display → 48px → ~36px across breakpoints
- **Feature grid**: Multi-column product showcase → 2-column → single stacked column
- **Product screenshots**: Scale within containers, maintaining landscape ratios
- **Section spacing**: Reduces proportionally — generous desktop margins compress on mobile

### Image Behavior
- Product screenshots scale responsively while maintaining aspect ratios
- Hero silhouette image crops or scales — maintains dramatic composition
- No art direction changes — same compositions across all breakpoints
- Lazy loading likely on below-fold product screenshots


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Hero Background: Mysteria Purple (`#1b1938`)
- Primary Text (light bg): Charcoal Ink (`#292827`)
- Primary Text (dark bg): Translucent White (`color(srgb 1 1 1 / 0.95)` — use `rgba(255,255,255,0.95)`)
- Accent: Lavender Glow (`#cbb7fb`)
- Button Background: Warm Cream (`#e9e5dd`)
- Border: Parchment Border (`#dcd7d3`)
- Link: Amethyst Link (`#714cb6`)
- Page Background: Pure White (`#ffffff`)

### Example Component Prompts
- "Create a hero section with deep purple gradient background (#1b1938), 64px Super Sans heading at weight 540, line-height 0.96, white text at 95% opacity, and a warm cream button (#e9e5dd, 8px radius, #292827 text)"
- "Design a feature card with white background, 1px #dcd7d3 border, 16px radius, 20px Super Sans heading at weight 460, and 16px body text at weight 460 with 1.50 line-height in #292827"
- "Build a navigation bar with white background, Super Sans links at 16px weight 460, a warm cream CTA button (#e9e5dd, 8px radius), sticky positioning"
- "Create a product showcase section with centered 48px heading (weight 460, -1.32px letter-spacing, #292827), a large product screenshot below, on white background"
- "Design an accent badge using Lavender Glow (#cbb7fb) background, 8px radius, 12px bold text (weight 700), for category labels"

### Iteration Guide
When refining existing screens generated with this design system:
1. Verify font weight is 460 (not 400 or 500) for body and 540 for display — the non-standard weights are essential
2. Check that display line-height is 0.96 — if headlines look too spaced, they're wrong
3. Ensure buttons use Warm Cream (#e9e5dd) not pure white or gray — the warmth is subtle but critical
4. Confirm the only accent color is Lavender Glow (#cbb7fb) — no other hues should appear
5. The overall tone should feel like a luxury product presentation — minimal, confident, with one dramatic color gesture in the hero


### PPT-image Quick Reference

- Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
- Display voice: `Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue`
- Body / label voice: `Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue`
- Primary accent: Mysteria Purple (#1b1938)
- Light surface anchor: Charcoal Ink (#292827)
- Dark surface anchor: Charcoal Ink (#292827)
- Signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, Ultra-tight display line-height (0.96) creating compressed, powerful headlines, and Warm Cream (#e9e5dd) buttons instead of bright/saturated CTAs — understated luxury
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Superhuman.
Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
Use Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue as the display-type reference and Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue for any short in-image labels.
Keep the palette anchored in Charcoal Ink (#292827), Charcoal Ink (#292827), and Mysteria Purple (#1b1938).
Preserve these signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, and Ultra-tight display line-height (0.96) creating compressed, powerful headlines.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Superhuman.
Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
Use Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue as the display-type reference and Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue for any short in-image labels.
Keep the palette anchored in Charcoal Ink (#292827), Charcoal Ink (#292827), and Mysteria Purple (#1b1938).
Preserve these signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, and Ultra-tight display line-height (0.96) creating compressed, powerful headlines.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Superhuman.
Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
Use Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue as the display-type reference and Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue for any short in-image labels.
Keep the palette anchored in Charcoal Ink (#292827), Charcoal Ink (#292827), and Mysteria Purple (#1b1938).
Preserve these signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, and Ultra-tight display line-height (0.96) creating compressed, powerful headlines.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Superhuman.
Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
Use Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue as the display-type reference and Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue for any short in-image labels.
Keep the palette anchored in Charcoal Ink (#292827), Charcoal Ink (#292827), and Mysteria Purple (#1b1938).
Preserve these signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, and Ultra-tight display line-height (0.96) creating compressed, powerful headlines.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Superhuman.
Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
Use Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue as the display-type reference and Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue for any short in-image labels.
Keep the palette anchored in Charcoal Ink (#292827), Charcoal Ink (#292827), and Mysteria Purple (#1b1938).
Preserve these signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, and Ultra-tight display line-height (0.96) creating compressed, powerful headlines.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Superhuman.
Brand mood: Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention.
Use Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue as the display-type reference and Super Sans VF — custom variable font with non-standard weight axis. Fallbacks: system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue for any short in-image labels.
Keep the palette anchored in Charcoal Ink (#292827), Charcoal Ink (#292827), and Mysteria Purple (#1b1938).
Preserve these signature cues: Deep purple gradient hero (#1b1938) contrasting against a predominantly white content body, Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700) — sits between conventional weight categories, and Ultra-tight display line-height (0.96) creating compressed, powerful headlines.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
