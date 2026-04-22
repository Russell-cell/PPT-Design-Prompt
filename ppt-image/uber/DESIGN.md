# PPT-image Design System Inspired by Uber

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Uber.

Source reference: `source/uber/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Uber's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place. The entire experience is built on a stark duality: jet black (`#000000`) and pure white (`#ffffff`), with virtually no mid-tone grays diluting the message. This isn't the sterile minimalism of a startup that hasn't finished designing -- it's the deliberate restraint of a brand so established it can afford to whisper.

The signature typeface, UberMove, is a proprietary geometric sans-serif with a distinctly square, engineered quality. Headlines in UberMove Bold at 52px carry the weight of a billboard -- authoritative, direct, unapologetic. The companion face UberMoveText handles body copy and buttons with a slightly softer, more readable character at medium weight (500). Together, they create a typographic system that feels like a transit map: clear, efficient, built for scanning at speed.

What makes Uber's design truly distinctive is its use of full-bleed photography and illustration paired with pill-shaped interactive elements (999px border-radius). Navigation chips, CTA buttons, and category selectors all share this capsule shape, creating a tactile, thumb-friendly interface language that's unmistakably Uber. The illustrations -- warm, slightly stylized scenes of drivers, riders, and cityscapes -- inject humanity into what could otherwise be a cold, monochrome system. The site alternates between white content sections and a full-black footer, with card-based layouts using the gentlest possible shadows (rgba(0,0,0,0.12-0.16)) to create subtle lift without breaking the flat aesthetic.

**Key Characteristics:**
- Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome
- UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family
- Pill-shaped everything: buttons, chips, nav items all use 999px border-radius
- Warm, human illustrations contrasting the stark monochrome interface
- Card-based layout with whisper-soft shadows (0.12-0.16 opacity)
- 8px spacing grid with compact, information-dense layouts
- Bold photography integrated as full-bleed hero backgrounds
- Black footer anchoring the page with a dark, high-contrast environment


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, Pill-shaped everything: buttons, chips, nav items all use 999px border-radius, and Warm, human illustrations contrasting the stark monochrome interface.
- Use Uber Black (#000000) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Uber Black (#000000) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Uber Black** (`#000000`): The defining brand color -- used for primary buttons, headlines, navigation text, and the footer. Not "near-black" or "off-black," but true, uncompromising black.
- **Pure White** (`#ffffff`): The primary surface color and inverse text. Used for page backgrounds, card surfaces, and text on black elements.

### Interactive & Button States
- **Hover Gray** (`#e2e2e2`): White button hover state -- a clean, cool light gray that provides clear feedback without warmth.
- **Hover Light** (`#f3f3f3`): Subtle hover for elevated white buttons -- barely-there gray for gentle interaction feedback.
- **Chip Gray** (`#efefef`): Background for secondary/filter buttons and navigation chips -- a neutral, ultra-light gray.

### Text & Content
- **Body Gray** (`#4b4b4b`): Secondary text and footer links -- a true mid-gray with no warm or cool bias.
- **Muted Gray** (`#afafaf`): Tertiary text, de-emphasized footer links, and placeholder content.

### Borders & Separation
- **Border Black** (`#000000`): Thin 1px borders for structural containment -- used sparingly on dividers and form containers.

### Shadows & Depth
- **Shadow Light** (`rgba(0, 0, 0, 0.12)`): Standard card elevation -- a featherweight lift for content cards.
- **Shadow Medium** (`rgba(0, 0, 0, 0.16)`): Slightly stronger elevation for floating action buttons and overlays.
- **Button Press** (`rgba(0, 0, 0, 0.08)`): Inset shadow for active/pressed states on secondary buttons.

### Link States
- **Default Link Blue** (`#0000ee`): Standard browser blue for text links with underline -- used in body content.
- **Link White** (`#ffffff`): Links on dark surfaces -- used in footer and dark sections.
- **Link Black** (`#000000`): Links on light surfaces with underline decoration.

### Gradient System
- Uber's design is **entirely gradient-free**. The black/white duality and flat color blocks create all visual hierarchy. No gradients appear anywhere in the system -- every surface is a solid color, every transition is a hard edge or a shadow.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Uber Black (#000000) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Uber Black (#000000) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Headline / Display**: `UberMove`, with fallbacks: `UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif`
- **Body / UI**: `UberMoveText`, with fallbacks: `system-ui, Helvetica Neue, Helvetica, Arial, sans-serif`

*Note: UberMove and UberMoveText are proprietary typefaces. For external implementations, use `system-ui` or Inter as the closest available substitute. The geometric, square-proportioned character of UberMove can be approximated with Inter or DM Sans.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display / Hero | UberMove | 52px (3.25rem) | 700 | 1.23 (tight) | Maximum impact, billboard presence |
| Section Heading | UberMove | 36px (2.25rem) | 700 | 1.22 (tight) | Major section anchors |
| Card Title | UberMove | 32px (2rem) | 700 | 1.25 (tight) | Card and feature headings |
| Sub-heading | UberMove | 24px (1.5rem) | 700 | 1.33 | Secondary section headers |
| Small Heading | UberMove | 20px (1.25rem) | 700 | 1.40 | Compact headings, list titles |
| Nav / UI Large | UberMoveText | 18px (1.13rem) | 500 | 1.33 | Navigation links, prominent UI text |
| Body / Button | UberMoveText | 16px (1rem) | 400-500 | 1.25-1.50 | Standard body text, button labels |
| Caption | UberMoveText | 14px (0.88rem) | 400-500 | 1.14-1.43 | Metadata, descriptions, small links |
| Micro | UberMoveText | 12px (0.75rem) | 400 | 1.67 (relaxed) | Fine print, legal text |

### Principles
- **Bold headlines, medium body**: UberMove headings are exclusively weight 700 (bold) -- every headline hits with billboard force. UberMoveText body and UI text uses 400-500, creating a clear visual hierarchy through weight contrast.
- **Tight heading line-heights**: All headlines use line-heights between 1.22-1.40 -- compact and punchy, designed for scanning rather than reading.
- **Functional typography**: There is no decorative type treatment anywhere. No letter-spacing, no text-transform, no ornamental sizing. Every text element serves a direct communication purpose.
- **Two fonts, strict roles**: UberMove is exclusively for headings. UberMoveText is exclusively for body, buttons, links, and UI. The boundary is never crossed.


### PPT-image Type Deployment

- Use `UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Black (CTA)**
- Background: Uber Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Padding: 10px 12px
- Radius: 999px (full pill)
- Outline: none
- Focus: inset ring `rgb(255,255,255) 0px 0px 0px 2px`
- The primary action button -- bold, high-contrast, unmissable

**Secondary White**
- Background: Pure White (`#ffffff`)
- Text: Uber Black (`#000000`)
- Padding: 10px 12px
- Radius: 999px (full pill)
- Hover: background shifts to Hover Gray (`#e2e2e2`)
- Focus: background shifts to Hover Gray, inset ring appears
- Used on dark surfaces or as a secondary action alongside Primary Black

**Chip / Filter**
- Background: Chip Gray (`#efefef`)
- Text: Uber Black (`#000000`)
- Padding: 14px 16px
- Radius: 999px (full pill)
- Active: inset shadow `rgba(0,0,0,0.08)`
- Navigation chips, category selectors, filter toggles

**Floating Action**
- Background: Pure White (`#ffffff`)
- Text: Uber Black (`#000000`)
- Padding: 14px
- Radius: 999px (full pill)
- Shadow: `rgba(0,0,0,0.16) 0px 2px 8px 0px`
- Transform: `translateY(2px)` slight offset
- Hover: background shifts to `#f3f3f3`
- Map controls, scroll-to-top, floating CTAs

### Cards & Containers
- Background: Pure White (`#ffffff`) on white pages; no distinct card background differentiation
- Border: none by default -- cards are defined by shadow, not stroke
- Radius: 8px for standard content cards; 12px for featured/promoted cards
- Shadow: `rgba(0,0,0,0.12) 0px 4px 16px 0px` for standard lift
- Cards are content-dense with minimal internal padding
- Image-led cards use full-bleed imagery with text overlay or below

### Inputs & Forms
- Text: Uber Black (`#000000`)
- Background: Pure White (`#ffffff`)
- Border: 1px solid Black (`#000000`) -- the only place visible borders appear prominently
- Radius: 8px
- Padding: standard comfortable spacing
- Focus: no extracted custom focus state -- relies on standard browser focus ring

### Navigation
- Sticky top navigation with white background
- Logo: Uber wordmark/icon at 24x24px in black
- Links: UberMoveText at 14-18px, weight 500, in Uber Black
- Pill-shaped nav chips with Chip Gray (`#efefef`) background for category navigation ("Ride", "Drive", "Business", "Uber Eats")
- Menu toggle: circular button with 50% border-radius
- Mobile: hamburger menu pattern

### Image Treatment
- Warm, hand-illustrated scenes (not photographs for feature sections)
- Illustration style: slightly stylized people, warm color palette within illustrations, contemporary vibe
- Hero sections use bold photography or illustration as full-width backgrounds
- QR codes for app download CTAs
- All imagery uses standard 8px or 12px border-radius when contained in cards

### Distinctive Components

**Category Pill Navigation**
- Horizontal row of pill-shaped buttons for top-level navigation ("Ride", "Drive", "Business", "Uber Eats", "About")
- Each pill: Chip Gray background, black text, 999px radius
- Active state indicated by black background with white text (inversion)

**Hero with Dual Action**
- Split hero: text/CTA on left, map/illustration on right
- Two input fields side by side for pickup/destination
- "See prices" CTA button in black pill

**Plan-Ahead Cards**
- Cards promoting features like "Uber Reserve" and trip planning
- Illustration-heavy with warm, human-centric imagery
- Black CTA buttons with white text at bottom


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Uber's strongest visual cues as one large, unmistakable scene or object.
- Let Uber Black (#000000), Pure White (#ffffff), and Uber Black (#000000) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Uber.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Uber Black (#000000), with Uber Black (#000000) reserved for the decisive signal.
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
- Scale: 4px, 6px, 8px, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 32px
- Button padding: 10px 12px (compact) or 14px 16px (comfortable)
- Card internal padding: approximately 24-32px
- Section vertical spacing: generous but efficient -- approximately 64-96px between major sections

### Grid & Container
- Max container width: approximately 1136px, centered
- Hero: split layout with text left, visual right
- Feature sections: 2-column card grids or full-width single-column
- Footer: multi-column link grid on black background
- Full-width sections extending to viewport edges

### Whitespace Philosophy
- **Efficient, not airy**: Uber's whitespace is functional -- enough to separate, never enough to feel empty. This is transit-system spacing: compact, clear, purpose-driven.
- **Content-dense cards**: Cards pack information tightly with minimal internal spacing, relying on shadow and radius to define boundaries.
- **Section breathing room**: Major sections get generous vertical spacing, but within sections, elements are closely grouped.

### Border Radius Scale
- Sharp (0px): No square corners used in interactive elements
- Standard (8px): Content cards, input fields, listboxes
- Comfortable (12px): Featured cards, larger containers, link cards
- Full Pill (999px): All buttons, chips, navigation items, pills
- Circle (50%): Avatar images, icon containers, circular controls


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
| Flat (Level 0) | No shadow, solid background | Page background, inline content, text sections |
| Subtle (Level 1) | `rgba(0,0,0,0.12) 0px 4px 16px` | Standard content cards, feature blocks |
| Medium (Level 2) | `rgba(0,0,0,0.16) 0px 4px 16px` | Elevated cards, overlay elements |
| Floating (Level 3) | `rgba(0,0,0,0.16) 0px 2px 8px` + translateY(2px) | Floating action buttons, map controls |
| Pressed (Level 4) | `rgba(0,0,0,0.08) inset` (999px spread) | Active/pressed button states |
| Focus Ring | `rgb(255,255,255) 0px 0px 0px 2px inset` | Keyboard focus indicators |

**Shadow Philosophy**: Uber uses shadow purely as a structural tool, never decoratively. Shadows are always black at very low opacity (0.08-0.16), creating the bare minimum lift needed to separate content layers. The blur radii are moderate (8-16px) -- enough to feel natural but never dramatic. There are no colored shadows, no layered shadow stacks, and no ambient glow effects. Depth is communicated more through the black/white section contrast than through shadow elevation.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use true black (`#000000`) and pure white (`#ffffff`) as the primary palette -- the stark contrast IS Uber
- Use 999px border-radius for all buttons, chips, and pill-shaped navigation elements
- Keep all headings in UberMove Bold (700) for billboard-level impact
- Use whisper-soft shadows (0.12-0.16 opacity) for card elevation -- barely visible
- Maintain the compact, information-dense layout style -- Uber prioritizes efficiency over airiness
- Use warm, human-centric illustrations to soften the monochrome interface
- Apply 8px radius for content cards and 12px for featured containers
- Use UberMoveText at weight 500 for navigation and prominent UI text
- Pair black primary buttons with white secondary buttons for dual-action layouts

### Don't
- Don't introduce color into the UI chrome -- Uber's interface is strictly black, white, and gray
- Don't use rounded corners less than 999px on buttons -- the full-pill shape is a core identity element
- Don't apply heavy shadows or drop shadows with high opacity -- depth is whisper-subtle
- Don't use serif fonts anywhere -- Uber's typography is exclusively geometric sans-serif
- Don't create airy, spacious layouts with excessive whitespace -- Uber's density is intentional
- Don't use gradients or color overlays -- every surface is a flat, solid color
- Don't mix UberMove into body text or UberMoveText into headlines -- the hierarchy is strict
- Don't use decorative borders -- borders are functional (inputs, dividers) or absent entirely
- Don't soften the black/white contrast with off-whites or near-blacks -- the duality is deliberate


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
| Mobile Small | 320px | Minimum layout, single column, stacked inputs, compact typography |
| Mobile | 600px | Standard mobile, stacked layout, hamburger nav |
| Tablet Small | 768px | Two-column grids begin, expanded card layouts |
| Tablet | 1119px | Full tablet layout, side-by-side hero content |
| Desktop Small | 1120px | Desktop grid activates, horizontal nav pills |
| Desktop | 1136px | Full desktop layout, maximum container width, split hero |

### Touch Targets
- All pill buttons: minimum 44px height (10-14px vertical padding + line-height)
- Navigation chips: generous 14px 16px padding for comfortable thumb tapping
- Circular controls (menu, close): 50% radius ensures large, easy-to-hit targets
- Card surfaces serve as full-area touch targets on mobile

### Collapsing Strategy
- **Navigation**: Horizontal pill nav collapses to hamburger menu with circular toggle
- **Hero**: Split layout (text + map/visual) stacks to single column -- text above, visual below
- **Input fields**: Side-by-side pickup/destination inputs stack vertically
- **Feature cards**: 2-column grid collapses to full-width stacked cards
- **Headings**: 52px display scales down through 36px, 32px, 24px, 20px
- **Footer**: Multi-column link grid collapses to accordion or stacked single column
- **Category pills**: Horizontal scroll with overflow on smaller screens

### Image Behavior
- Illustrations scale proportionally within their containers
- Hero imagery maintains aspect ratio, may crop on smaller screens
- QR code sections hide on mobile (app download shifts to direct store links)
- Card imagery maintains 8-12px border radius at all sizes


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary Button: "Uber Black (#000000)"
- Page Background: "Pure White (#ffffff)"
- Button Text (on black): "Pure White (#ffffff)"
- Button Text (on white): "Uber Black (#000000)"
- Secondary Text: "Body Gray (#4b4b4b)"
- Tertiary Text: "Muted Gray (#afafaf)"
- Chip Background: "Chip Gray (#efefef)"
- Hover State: "Hover Gray (#e2e2e2)"
- Card Shadow: "rgba(0,0,0,0.12) 0px 4px 16px"
- Footer Background: "Uber Black (#000000)"

### Example Component Prompts
- "Create a hero section on Pure White (#ffffff) with a headline at 52px UberMove Bold (700), line-height 1.23. Use Uber Black (#000000) text. Add a subtitle in Body Gray (#4b4b4b) at 16px UberMoveText weight 400 with 1.50 line-height. Place an Uber Black (#000000) pill CTA button with Pure White text, 999px radius, padding 10px 12px."
- "Design a category navigation bar with horizontal pill buttons. Each pill: Chip Gray (#efefef) background, Uber Black (#000000) text, 14px 16px padding, 999px border-radius. Active pill inverts to Uber Black background with Pure White text. Use UberMoveText at 14px weight 500."
- "Build a feature card on Pure White (#ffffff) with 8px border-radius and shadow rgba(0,0,0,0.12) 0px 4px 16px. Title in UberMove at 24px weight 700, description in Body Gray (#4b4b4b) at 16px UberMoveText. Add a black pill CTA button at the bottom."
- "Create a dark footer on Uber Black (#000000) with Pure White (#ffffff) heading text in UberMove at 20px weight 700. Footer links in Muted Gray (#afafaf) at 14px UberMoveText. Links hover to Pure White. Multi-column grid layout."
- "Design a floating action button with Pure White (#ffffff) background, 999px radius, 14px padding, and shadow rgba(0,0,0,0.16) 0px 2px 8px. Hover shifts background to #f3f3f3. Use for scroll-to-top or map controls."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference the strict black/white palette -- "use Uber Black (#000000)" not "make it dark"
3. Always specify 999px radius for buttons and pills -- this is non-negotiable for the Uber identity
4. Describe the font family explicitly -- "UberMove Bold for the heading, UberMoveText Medium for the label"
5. For shadows, use "whisper shadow (rgba(0,0,0,0.12) 0px 4px 16px)" -- never heavy drop shadows
6. Keep layouts compact and information-dense -- Uber is efficient, not airy
7. Illustrations should be warm and human -- describe "stylized people in warm tones" not abstract shapes
8. Pair black CTAs with white secondaries for balanced dual-action layouts


### PPT-image Quick Reference

- Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
- Display voice: `UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif`
- Body / label voice: `UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif`
- Primary accent: Uber Black (#000000)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Uber Black (#000000)
- Signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, Pill-shaped everything: buttons, chips, nav items all use 999px border-radius, and Warm, human illustrations contrasting the stark monochrome interface
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Uber.
Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
Use UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif as the display-type reference and UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Uber Black (#000000), and Uber Black (#000000).
Preserve these signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, and Pill-shaped everything: buttons, chips, nav items all use 999px border-radius.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Uber.
Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
Use UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif as the display-type reference and UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Uber Black (#000000), and Uber Black (#000000).
Preserve these signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, and Pill-shaped everything: buttons, chips, nav items all use 999px border-radius.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Uber.
Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
Use UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif as the display-type reference and UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Uber Black (#000000), and Uber Black (#000000).
Preserve these signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, and Pill-shaped everything: buttons, chips, nav items all use 999px border-radius.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Uber.
Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
Use UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif as the display-type reference and UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Uber Black (#000000), and Uber Black (#000000).
Preserve these signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, and Pill-shaped everything: buttons, chips, nav items all use 999px border-radius.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Uber.
Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
Use UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif as the display-type reference and UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Uber Black (#000000), and Uber Black (#000000).
Preserve these signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, and Pill-shaped everything: buttons, chips, nav items all use 999px border-radius.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Uber.
Brand mood: Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place.
Use UberMove, with fallbacks: UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif as the display-type reference and UberMoveText, with fallbacks: system-ui, Helvetica Neue, Helvetica, Arial, sans-serif for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Uber Black (#000000), and Uber Black (#000000).
Preserve these signature cues: Pure black-and-white foundation with virtually no mid-tone grays in the UI chrome, UberMove (headlines) + UberMoveText (body/UI) -- proprietary geometric sans-serif family, and Pill-shaped everything: buttons, chips, nav items all use 999px border-radius.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
