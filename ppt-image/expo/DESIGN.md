# PPT-image Design System Inspired by Expo

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Expo.

Source reference: `source/expo/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Expo's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves. The entire experience lives on a bright, airy canvas — a cool-tinted off-white (`#f0f0f3`) that gives the page a subtle technological coolness without the starkness of pure white. This is a site that breathes: enormous vertical spacing between sections creates a gallery-like pace where each feature gets its own "room."

The design language is decisively monochromatic — pure black (`#000000`) headlines against the lightest possible backgrounds, with a spectrum of cool blue-grays (`#60646c`, `#b0b4ba`, `#555860`) handling all secondary communication. Color is almost entirely absent from the interface itself; when it appears, it's reserved for product screenshots, app icons, and the React universe illustration — making the actual content burst with life against the neutral canvas.

What makes Expo distinctive is its pill-shaped geometry. Buttons, tabs, video containers, and even images use generously rounded or fully pill-shaped corners (24px–9999px), creating an organic, approachable feel that contradicts the typical sharp-edged developer tool aesthetic. Combined with tight letter-spacing on massive headlines (-1.6px to -3px at 64px), the result is a design that's simultaneously premium and friendly — like an Apple product page reimagined for developers.

**Key Characteristics:**
- Luminous cool-white canvas (`#f0f0f3`) with gallery-like vertical spacing
- Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color
- Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius)
- Massive display headlines (64px) with extreme negative letter-spacing (-1.6px to -3px)
- Inter as the sole typeface, used at weights 400–900 for full expressive range
- Whisper-soft shadows that barely lift elements from the surface
- Product screenshots as the only source of color in the interface


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius), and Massive display headlines (64px) with extreme negative letter-spacing (-1.6px to -3px).
- Use Expo Black (#000000) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Charcoal (#333333) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Expo Black** (`#000000`): The absolute anchor — used for primary headlines, CTA buttons, and the brand identity. Pure black on cool white creates maximum contrast without feeling aggressive.
- **Near Black** (`#1c2024`): The primary text color for body content — a barely perceptible blue-black that's softer than pure #000 for extended reading.

### Secondary & Accent
- **Link Cobalt** (`#0d74ce`): The standard link color — a trustworthy, saturated blue that signals interactivity without competing with the monochrome hierarchy.
- **Legal Blue** (`#476cff`): A brighter, more saturated blue for legal/footer links — slightly more attention-grabbing than Link Cobalt.
- **Widget Sky** (`#47c2ff`): A light, friendly cyan-blue for widget branding elements — the brightest accent in the system.
- **Preview Purple** (`#8145b5`): A rich violet used for "preview" or beta feature indicators — creating clear visual distinction from standard content.

### Surface & Background
- **Cloud Gray** (`#f0f0f3`): The primary page background — a cool off-white with the faintest blue-violet tint. Not warm, not sterile — precisely technological.
- **Pure White** (`#ffffff`): Card surfaces, button backgrounds, and elevated content containers. Creates a clear "lifted" distinction from Cloud Gray.
- **Widget Dark** (`#1a1a1a`): Dark surface for dark-theme widgets and overlay elements.
- **Banner Dark** (`#171717`): The darkest surface variant, used for promotional banners and high-contrast containers.

### Neutrals & Text
- **Slate Gray** (`#60646c`): The workhorse secondary text color (305 instances). A cool blue-gray that's authoritative without being heavy.
- **Mid Slate** (`#555860`): Slightly darker than Slate, used for emphasized secondary text.
- **Silver** (`#b0b4ba`): Tertiary text, placeholders, and de-emphasized metadata. Comfortably readable but clearly receded.
- **Pewter** (`#999999`): Accordion icons and deeply de-emphasized UI elements in dark contexts.
- **Light Silver** (`#cccccc`): Arrow icons and decorative elements in dark contexts.
- **Dark Slate** (`#363a3f`): Borders on dark surfaces, switch tracks, and emphasized containment.
- **Charcoal** (`#333333`): Dark mode switch backgrounds and deep secondary surfaces.

### Semantic & Accent
- **Warning Amber** (`#ab6400`): A warm, deep amber for warning states — deliberately not bright yellow, conveying seriousness.
- **Destructive Rose** (`#eb8e90`): A soft pink-coral for disabled destructive actions — gentler than typical red, reducing alarm fatigue.
- **Border Lavender** (`#e0e1e6`): Standard card/container borders — a cool lavender-gray that's visible without being heavy.
- **Input Border** (`#d9d9e0`): Button and form element borders — slightly warmer/darker than card borders for interactive elements.
- **Dark Focus Ring** (`#2547d0`): Deep blue for keyboard focus indicators in dark theme contexts.

### Gradient System
- The design is notably **gradient-free** in the interface layer. Visual richness comes from product screenshots, the React universe illustration, and careful shadow layering rather than color gradients. This absence IS the design decision — gradients would undermine the clinical precision.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Charcoal (#333333) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Expo Black (#000000) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Primary**: `Inter`, with fallbacks: `-apple-system, system-ui`
- **Monospace**: `JetBrains Mono`, with fallback: `ui-monospace`
- **System Fallback**: `system-ui, Segoe UI, Roboto, Helvetica, Arial, Apple Color Emoji, Segoe UI Emoji`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | Inter | 64px (4rem) | 700–900 | 1.10 (tight) | -1.6px to -3px | Maximum impact, extreme tracking |
| Section Heading | Inter | 48px (3rem) | 600 | 1.10 (tight) | -2px | Feature section anchors |
| Sub-heading | Inter | 20px (1.25rem) | 600 | 1.20 (tight) | -0.25px | Card titles, feature names |
| Body Large | Inter | 18px (1.13rem) | 400–500 | 1.40 | normal | Intro paragraphs, section descriptions |
| Body / Button | Inter | 16px (1rem) | 400–700 | 1.25–1.40 | normal | Standard text, nav links, buttons |
| Caption / Label | Inter | 14px (0.88rem) | 400–600 | 1.00–1.40 | normal | Descriptions, metadata, badge text |
| Tag / Small | Inter | 12px (0.75rem) | 500 | 1.00–1.60 | normal | Smallest sans-serif text, badges |
| Code Body | JetBrains Mono | 16px (1rem) | 400–600 | 1.40 | normal | Inline code, terminal commands |
| Code Caption | JetBrains Mono | 14px (0.88rem) | 400–600 | 1.40 | normal | Code snippets, technical labels |
| Code Small | JetBrains Mono | 12px (0.75rem) | 400 | 1.60 | normal | Uppercase tech tags |

### Principles
- **One typeface, full expression**: Inter is the only sans-serif, used from weight 400 (regular) through 900 (black). This gives the design a unified voice while still achieving dramatic contrast between whisper-light body text and thundering display headlines.
- **Extreme negative tracking at scale**: Headlines at 64px use -1.6px to -3px letter-spacing, creating ultra-dense text blocks that feel like logotypes. This aggressive compression is the signature typographic move.
- **Weight as hierarchy**: 700–900 for display, 600 for headings, 500 for emphasis, 400 for body. The jumps are decisive — no ambiguous in-between weights.
- **Consistent 1.40 body line-height**: Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency.


### PPT-image Type Deployment

- Use `Inter, with fallbacks: -apple-system, system-ui` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency.` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary (White on border)**
- Background: Pure White (`#ffffff`)
- Text: Near Black (`#1c2024`)
- Padding: 0px 12px (compact, content-driven height)
- Border: thin solid Input Border (`1px solid #d9d9e0`)
- Radius: subtly rounded (6px)
- Shadow: subtle combined shadow on hover
- The understated default — clean, professional, unheroic

**Primary Pill**
- Same as Primary but with pill-shaped radius (9999px)
- Used for hero CTAs and high-emphasis actions
- The extra roundness signals "start here"

**Dark Primary**
- Background: Expo Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Pill-shaped (9999px) or generously rounded (32–36px)
- No border (black IS the border)
- The maximum-emphasis CTA — reserved for primary conversion actions

### Cards & Containers
- Background: Pure White (`#ffffff`) — clearly lifted from Cloud Gray page
- Border: thin solid Border Lavender (`1px solid #e0e1e6`) for standard cards
- Radius: comfortably rounded (8px) for standard cards; generously rounded (16–24px) for featured containers
- Shadow Level 1: Whisper (`rgba(0,0,0,0.08) 0px 3px 6px, rgba(0,0,0,0.07) 0px 2px 4px`) — barely perceptible lift
- Shadow Level 2: Standard (`rgba(0,0,0,0.1) 0px 10px 20px, rgba(0,0,0,0.05) 0px 3px 6px`) — clear floating elevation
- Hover: likely subtle shadow deepening or background shift

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Text: Near Black (`#1c2024`)
- Border: thin solid Input Border (`1px solid #d9d9e0`)
- Padding: 0px 12px (inline with button sizing)
- Radius: subtly rounded (6px)
- Focus: blue ring shadow via CSS custom property

### Navigation
- Sticky top nav on transparent/blurred background
- Logo: Expo wordmark in black
- Links: Near Black (`#1c2024`) or Slate Gray (`#60646c`) at 14–16px Inter weight 500
- CTA: Black pill button ("Sign Up") on the right
- GitHub star badge as social proof
- Status indicator ("All Systems Operational") with green dot

### Image Treatment
- Product screenshots and device mockups are the visual heroes
- Generously rounded corners (24px) on video and image containers
- Screenshots shown in realistic device frames
- Dark UI screenshots provide contrast against the light canvas
- Full-bleed within rounded containers

### Distinctive Components

**Universe React Logo**
- Animated/illustrated React logo as the visual centerpiece
- Connects Expo's identity to the React ecosystem
- The only illustrative element on an otherwise photographic page

**Device Preview Grid**
- Multiple device types (phone, tablet, web) shown simultaneously
- Demonstrates cross-platform capability visually
- Each device uses realistic device chrome

**Status Badge**
- "All Systems Operational" pill in the nav
- Green dot + text — compact trust signal
- Pill-shaped (36px radius)


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Expo's strongest visual cues as one large, unmistakable scene or object.
- Let Expo Black (#000000), Pure White (#ffffff), and Charcoal (#333333) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Expo.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Charcoal (#333333), with Expo Black (#000000) reserved for the decisive signal.
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
- Scale: 1px, 2px, 4px, 8px, 12px, 16px, 24px, 32px, 40px, 48px, 64px, 80px, 96px, 144px
- Button padding: 0px 12px (unusually compact — height driven by line-height)
- Card internal padding: approximately 24–32px
- Section vertical spacing: enormous (estimated 96–144px between major sections)
- Component gap: 16–24px between sibling elements

### Grid & Container
- Max container width: approximately 1200–1400px, centered
- Hero: centered single-column with massive breathing room
- Feature sections: alternating layouts (image left/right, full-width showcases)
- Card grids: 2–3 column for feature highlights
- Full-width sections with contained inner content

### Whitespace Philosophy
- **Gallery-like pacing**: Each section feels like its own exhibit, surrounded by vast empty space. This creates a premium, unhurried browsing experience.
- **Breathing room is the design**: The generous whitespace IS the primary design element — it communicates confidence, quality, and that each feature deserves individual attention.
- **Content islands**: Sections float as isolated "islands" in the white space, connected by scrolling rather than visual continuation.

### Border Radius Scale
- Nearly squared (4px): Small inline elements, tags
- Subtly rounded (6px): Buttons, form inputs, combo boxes — the functional interactive radius
- Comfortably rounded (8px): Standard content cards, containers
- Generously rounded (16px): Feature tabs, content panels
- Very rounded (24px): Buttons, video/image containers, tabpanels — the signature softness
- Highly rounded (32–36px): Hero CTAs, status badges, nav buttons
- Pill-shaped (9999px): Primary action buttons, tags, avatars — maximum friendliness


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
| Flat (Level 0) | No shadow | Cloud Gray page background, inline text |
| Surface (Level 1) | White bg, no shadow | Standard white cards on Cloud Gray |
| Whisper (Level 2) | `rgba(0,0,0,0.08) 0px 3px 6px` + `rgba(0,0,0,0.07) 0px 2px 4px` | Subtle card lift, hover states |
| Elevated (Level 3) | `rgba(0,0,0,0.1) 0px 10px 20px` + `rgba(0,0,0,0.05) 0px 3px 6px` | Feature showcases, product screenshots |
| Modal (Level 4) | Dark overlay (`--dialog-overlay-background-color`) + heavy shadow | Dialogs, overlays |

**Shadow Philosophy**: Expo uses shadows as gentle whispers rather than architectural statements. The primary depth mechanism is **background color contrast** — white cards floating on Cloud Gray — rather than shadow casting. When shadows appear, they're soft, diffused, and directional (downward), creating the feeling of paper hovering millimeters above a desk.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Cloud Gray (`#f0f0f3`) as the page background and Pure White (`#ffffff`) for elevated cards — the two-tone light system is essential
- Keep display headlines at extreme negative letter-spacing (-1.6px to -3px at 64px) for the signature compressed look
- Use pill-shaped (9999px) radius for primary CTA buttons — the organic shape is core to the identity
- Reserve black (`#000000`) for headlines and primary CTAs — it carries maximum authority on the light canvas
- Use Slate Gray (`#60646c`) for secondary text — it's the precise balance between readable and receded
- Maintain enormous vertical spacing between sections (96px+) — the gallery pacing defines the premium feel
- Use product screenshots as the primary visual content — the interface stays monochrome, the products bring color
- Apply Inter at the full weight range (400–900) — weight contrast IS the hierarchy

### Don't
- Don't introduce decorative colors into the interface chrome — the monochromatic palette is intentional
- Don't use sharp corners (border-radius < 6px) on interactive elements — the pill/rounded geometry is the signature
- Don't reduce section spacing below 64px — the breathing room is the design
- Don't use heavy drop shadows — depth comes from background contrast and whisper-soft shadows
- Don't mix in additional typefaces — Inter handles everything from display to caption
- Don't use letter-spacing wider than -0.25px on body text — extreme tracking is reserved for display only
- Don't use borders heavier than 2px — containment is subtle, achieved through background color and gentle borders
- Don't add gradients to the interface — visual richness comes from content, not decoration
- Don't use saturated colors outside of semantic contexts — the palette is strictly grayscale + functional blue


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
| Mobile | <640px | Single column, hamburger nav, stacked cards, hero text scales to ~36px |
| Tablet | 640–1024px | 2-column grids, condensed nav, medium hero text |
| Desktop | >1024px | Full multi-column layout, expanded nav, massive hero (64px) |

*Only one explicit breakpoint detected (640px), suggesting a fluid, container-query or min()/clamp()-based responsive system rather than fixed breakpoint snapping.*

### Touch Targets
- Buttons use generous radius (24–36px) creating large, finger-friendly surfaces
- Navigation links spaced with adequate gap
- Status badge sized for touch (36px radius)
- Minimum recommended: 44x44px

### Collapsing Strategy
- **Navigation**: Full horizontal nav with CTA collapses to hamburger on mobile
- **Feature sections**: Multi-column → stacked single column
- **Hero text**: 64px → ~36px progressive scaling
- **Device previews**: Grid → stacked/carousel
- **Cards**: Side-by-side → vertical stacking
- **Spacing**: Reduces proportionally but maintains generous rhythm

### Image Behavior
- Product screenshots scale proportionally
- Device mockups may simplify or show fewer devices on mobile
- Rounded corners maintained at all sizes
- Lazy loading for below-fold content


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary CTA / Headlines: "Expo Black (#000000)"
- Page Background: "Cloud Gray (#f0f0f3)"
- Card Surface: "Pure White (#ffffff)"
- Body Text: "Near Black (#1c2024)"
- Secondary Text: "Slate Gray (#60646c)"
- Borders: "Border Lavender (#e0e1e6)"
- Links: "Link Cobalt (#0d74ce)"
- Tertiary Text: "Silver (#b0b4ba)"

### Example Component Prompts
- "Create a hero section on Cloud Gray (#f0f0f3) with a massive headline at 64px Inter weight 700, line-height 1.10, letter-spacing -3px. Text in Expo Black (#000000). Below, add a subtitle in Slate Gray (#60646c) at 18px. Place a black pill-shaped CTA button (9999px radius) beneath."
- "Design a feature card on Pure White (#ffffff) with a 1px solid Border Lavender (#e0e1e6) border and comfortably rounded corners (8px). Title in Near Black (#1c2024) at 20px Inter weight 600, description in Slate Gray (#60646c) at 16px. Add a whisper shadow (rgba(0,0,0,0.08) 0px 3px 6px)."
- "Build a navigation bar with Expo logo on the left, text links in Near Black (#1c2024) at 14px Inter weight 500, and a black pill CTA button on the right. Background: transparent with blur backdrop. Bottom border: 1px solid Border Lavender (#e0e1e6)."
- "Create a code block using JetBrains Mono at 14px on a Pure White surface with Border Lavender border and 8px radius. Code in Near Black, keywords in Link Cobalt (#0d74ce)."
- "Design a status badge pill (9999px radius) with a green dot and 'All Systems Operational' text in Inter 12px weight 500. Background: Pure White, border: 1px solid Input Border (#d9d9e0)."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names and hex codes — "use Slate Gray (#60646c)" not "make it gray"
3. Use radius values deliberately — 6px for buttons, 8px for cards, 24px for images, 9999px for pills
4. Describe the "feel" alongside measurements — "enormous breathing room with 96px section spacing"
5. Always specify Inter and the exact weight — weight contrast IS the hierarchy
6. For shadows, specify "whisper shadow" or "standard elevation" from the elevation table
7. Keep the interface monochrome — let product content be the color


### PPT-image Quick Reference

- Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
- Display voice: `Inter, with fallbacks: -apple-system, system-ui`
- Body / label voice: `Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency.`
- Primary accent: Expo Black (#000000)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Charcoal (#333333)
- Signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius), and Massive display headlines (64px) with extreme negative letter-spacing (-1.6px to -3px)
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Expo.
Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
Use Inter, with fallbacks: -apple-system, system-ui as the display-type reference and Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Charcoal (#333333), and Expo Black (#000000).
Preserve these signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, and Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius).
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Expo.
Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
Use Inter, with fallbacks: -apple-system, system-ui as the display-type reference and Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Charcoal (#333333), and Expo Black (#000000).
Preserve these signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, and Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius).
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Expo.
Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
Use Inter, with fallbacks: -apple-system, system-ui as the display-type reference and Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Charcoal (#333333), and Expo Black (#000000).
Preserve these signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, and Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius).
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Expo.
Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
Use Inter, with fallbacks: -apple-system, system-ui as the display-type reference and Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Charcoal (#333333), and Expo Black (#000000).
Preserve these signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, and Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius).
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Expo.
Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
Use Inter, with fallbacks: -apple-system, system-ui as the display-type reference and Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Charcoal (#333333), and Expo Black (#000000).
Preserve these signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, and Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius).
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Expo.
Brand mood: Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves.
Use Inter, with fallbacks: -apple-system, system-ui as the display-type reference and Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Charcoal (#333333), and Expo Black (#000000).
Preserve these signature cues: Luminous cool-white canvas (#f0f0f3) with gallery-like vertical spacing, Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color, and Pill-shaped geometry everywhere — buttons, tabs, containers, images (24px–9999px radius).
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
