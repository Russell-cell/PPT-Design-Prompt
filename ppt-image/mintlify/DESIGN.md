# PPT-image Design System Inspired by Mintlify

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Mintlify.

Source reference: `source/mintlify/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Mintlify's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value. The page opens with a luminous white (`#ffffff`) background, near-black (`#0d0d0d`) text, and a signature green brand accent (`#18E299`) that signals freshness and intelligence without dominating the palette. The overall mood is calm, confident, and engineered for legibility — a design system that whispers "we care about your developer experience" in every pixel.

The Inter font family carries the entire typographic load. At display sizes (40–64px), it uses tight negative letter-spacing (-0.8px to -1.28px) and semibold weight (600), creating headlines that feel focused and compressed like well-written documentation headers. Body text at 16–18px with 150% line-height provides generous reading comfort. Geist Mono appears exclusively for code and technical labels — uppercase, tracked-out, small — the voice of the terminal inside the marketing page.

What distinguishes Mintlify from other documentation platforms is its atmospheric gradient hero. A soft, cloud-like green-to-white gradient wash behind the hero content creates a sense of ethereal intelligence — documentation that floats above the noise. Below the hero, the page settles into a disciplined alternation of white sections separated by subtle 5% opacity borders. Cards use generous padding (24px+) with large radii (16px–24px) and whisper-thin borders, creating containers that feel open rather than boxed.

**Key Characteristics:**
- Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable
- Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice
- Brand green (`#18E299`) used sparingly — CTAs, hover states, focus rings, and accent touches
- Atmospheric gradient hero with cloud-like green-white wash
- Ultra-round corners: 16px for containers, 24px for featured cards, full-round (9999px) for buttons and pills
- Subtle 5% opacity borders (`rgba(0,0,0,0.05)`) creating barely-there separation
- 8px base spacing system with generous section padding (48px–96px)
- Clean white canvas — no gray backgrounds, no color sections, depth through borders and whitespace alone


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches, and Atmospheric gradient hero with cloud-like green-white wash.
- Use Brand Green (#18E299) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#0d0d0d) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Near Black** (`#0d0d0d`): Primary text, headings, dark surfaces. Not pure black — the micro-softness improves reading comfort.
- **Pure White** (`#ffffff`): Page background, card surfaces, input backgrounds.
- **Brand Green** (`#18E299`): The signature accent — CTAs, links on hover, focus rings, brand identity.

### Secondary Accents
- **Brand Green Light** (`#d4fae8`): Tinted green surface for badges, hover states, subtle backgrounds.
- **Brand Green Deep** (`#0fa76e`): Darker green for text on light-green badges, hover states on brand elements.
- **Warm Amber** (`#c37d0d`): Warning states, caution badges — `--twoslash-warn-bg`.
- **Soft Blue** (`#3772cf`): Tag backgrounds, informational annotations — `--twoslash-tag-bg`.
- **Error Red** (`#d45656`): Error states, destructive actions — `--twoslash-error-bg`.

### Neutral Scale
- **Gray 900** (`#0d0d0d`): Primary heading text, nav links.
- **Gray 700** (`#333333`): Secondary text, descriptions, body copy.
- **Gray 500** (`#666666`): Tertiary text, muted labels.
- **Gray 400** (`#888888`): Placeholder text, disabled states, code annotations.
- **Gray 200** (`#e5e5e5`): Borders, dividers, card outlines.
- **Gray 100** (`#f5f5f5`): Subtle surface backgrounds, hover states.
- **Gray 50** (`#fafafa`): Near-white surface tint.

### Interactive
- **Link Default** (`#0d0d0d`): Links match text color, relying on underline/context.
- **Link Hover** (`#18E299`): Brand green on hover — `var(--color-brand)`.
- **Focus Ring** (`#18E299`): Brand green focus outline for inputs and interactive elements.

### Surface & Overlay
- **Card Background** (`#ffffff`): White cards on white background, separated by borders.
- **Border Subtle** (`rgba(0,0,0,0.05)`): 5% black opacity borders — the primary separation mechanism.
- **Border Medium** (`rgba(0,0,0,0.08)`): Slightly stronger borders for interactive elements.
- **Input Border Focus** (`var(--color-brand)`): Green ring on focused inputs.

### Shadows & Depth
- **Card Shadow** (`rgba(0,0,0,0.03) 0px 2px 4px`): Barely-there ambient shadow for subtle lift.
- **Button Shadow** (`rgba(0,0,0,0.06) 0px 1px 2px`): Micro-shadow for button depth.
- **No heavy shadows**: Mintlify relies on borders, not shadows, for depth.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#0d0d0d) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Brand Green (#18E299) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Primary**: `Inter`, with fallback: `Inter Fallback, system-ui, -apple-system, sans-serif`
- **Monospace**: `Geist Mono`, with fallback: `Geist Mono Fallback, ui-monospace, SFMono-Regular, monospace`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Inter | 64px (4.00rem) | 600 | 1.15 (tight) | -1.28px | Maximum impact, hero headlines |
| Section Heading | Inter | 40px (2.50rem) | 600 | 1.10 (tight) | -0.8px | Feature section titles |
| Sub-heading | Inter | 24px (1.50rem) | 500 | 1.30 (tight) | -0.24px | Card headings, sub-sections |
| Card Title | Inter | 20px (1.25rem) | 600 | 1.30 (tight) | -0.2px | Feature card titles |
| Card Title Light | Inter | 20px (1.25rem) | 500 | 1.30 (tight) | -0.2px | Secondary card headings |
| Body Large | Inter | 18px (1.13rem) | 400 | 1.50 | normal | Hero descriptions, introductions |
| Body | Inter | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text |
| Body Medium | Inter | 16px (1.00rem) | 500 | 1.50 | normal | Navigation, emphasized text |
| Button | Inter | 15px (0.94rem) | 500 | 1.50 | normal | Button labels |
| Link | Inter | 14px (0.88rem) | 500 | 1.50 | normal | Navigation links, small CTAs |
| Caption | Inter | 14px (0.88rem) | 400–500 | 1.50–1.71 | normal | Metadata, descriptions |
| Label Uppercase | Inter | 13px (0.81rem) | 500 | 1.50 | 0.65px | `text-transform: uppercase`, section labels |
| Small | Inter | 13px (0.81rem) | 400–500 | 1.50 | -0.26px | Small body text |
| Mono Code | Geist Mono | 12px (0.75rem) | 500 | 1.50 | 0.6px | `text-transform: uppercase`, technical labels |
| Mono Badge | Geist Mono | 12px (0.75rem) | 600 | 1.50 | 0.6px | `text-transform: uppercase`, status badges |
| Mono Micro | Geist Mono | 10px (0.63rem) | 500 | 1.50 | normal | `text-transform: uppercase`, tiny labels |

### Principles
- **Tight tracking at display sizes**: Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy.
- **Relaxed reading at body sizes**: 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort.
- **Two-font system**: Inter for all human-readable content, Geist Mono exclusively for technical/code contexts. The boundary is strict — no mixing.
- **Uppercase as hierarchy signal**: Section labels and technical tags use uppercase + positive tracking (0.6px–0.65px) as a clear visual delimiter between content types.
- **Three weights**: 400 (body/reading), 500 (UI/navigation/emphasis), 600 (headings/titles). No bold (700) in the system.


### PPT-image Type Deployment

- Use `Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy.` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort.` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Brand (Full-round)**
- Background: `#0d0d0d` (near-black)
- Text: `#ffffff`
- Padding: 8px 24px
- Radius: 9999px (full pill)
- Font: Inter 15px weight 500
- Shadow: `rgba(0,0,0,0.06) 0px 1px 2px`
- Hover: opacity 0.9
- Use: Primary CTA ("Get Started", "Start Building")

**Secondary / Ghost (Full-round)**
- Background: `#ffffff`
- Text: `#0d0d0d`
- Padding: 4.5px 12px
- Radius: 9999px (full pill)
- Border: `1px solid rgba(0,0,0,0.08)`
- Font: Inter 15px weight 500
- Hover: opacity 0.9
- Use: Secondary actions ("Request Demo", "View Docs")

**Transparent / Nav Button**
- Background: transparent
- Text: `#0d0d0d`
- Padding: 5px 6px
- Radius: 8px
- Border: none or `1px solid rgba(0,0,0,0.05)`
- Use: Navigation items, icon buttons

**Brand Accent Button**
- Background: `#18E299`
- Text: `#0d0d0d`
- Padding: 8px 24px
- Radius: 9999px
- Use: Special promotional CTAs

### Cards & Containers

**Standard Card**
- Background: `#ffffff`
- Border: `1px solid rgba(0,0,0,0.05)`
- Radius: 16px
- Padding: 24px
- Shadow: `rgba(0,0,0,0.03) 0px 2px 4px`
- Hover: subtle border darkening to `rgba(0,0,0,0.08)`

**Featured Card**
- Background: `#ffffff`
- Border: `1px solid rgba(0,0,0,0.05)`
- Radius: 24px
- Padding: 32px
- Inner content areas may have their own 16px radius containers

**Logo/Trust Card**
- Background: `#fafafa` or `#ffffff`
- Border: `1px solid rgba(0,0,0,0.05)`
- Radius: 16px
- Centered logo/icon with consistent sizing

### Inputs & Forms

**Email Input**
- Background: transparent or `#ffffff`
- Text: `#0d0d0d`
- Padding: 0px 12px (height controlled by line-height)
- Border: `1px solid rgba(0,0,0,0.08)`
- Radius: 9999px (full pill, matching buttons)
- Focus: `1px solid var(--color-brand)` + `outline: 1px solid var(--color-brand)`
- Placeholder: `#888888`

### Navigation
- Clean horizontal nav on white, sticky with backdrop blur
- Brand logotype left-aligned
- Links: Inter 14–15px weight 500, `#0d0d0d` text
- Hover: color shifts to brand green `var(--color-brand)`
- CTA: dark pill button right-aligned ("Get Started")
- Mobile: hamburger menu collapse at 768px

### Image Treatment
- Product screenshots with subtle 1px borders
- Rounded containers: 16px–24px radius
- Atmospheric gradient backgrounds behind hero images
- Cloud/sky imagery with soft green tinting

### Distinctive Components

**Atmospheric Hero**
- Full-width gradient wash: soft green-to-white cloud-like gradient
- Centered headline with tight tracking
- Subtitle in muted gray
- Dual CTA buttons (dark primary + ghost secondary)
- The gradient creates a sense of elevation and intelligence

**Trust Bar / Logo Grid**
- "Loved by your favorite companies" section
- Company logos in muted grayscale
- Grid or horizontal layout with consistent sizing
- Subtle border separation between logos

**Feature Cards with Icons**
- Icon or illustration at top
- Title at 20px weight 600
- Description at 14–16px in gray
- Consistent padding and border treatment
- Grid layout: 2–3 columns on desktop

**CTA Footer Section**
- Dark or gradient background
- Large headline: "Make documentation your winning advantage"
- Email input with pill styling
- Brand green accent on CTAs


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Mintlify's strongest visual cues as one large, unmistakable scene or object.
- Let Brand Green (#18E299), Pure White (#ffffff), and Near Black (#0d0d0d) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Mintlify.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Near Black (#0d0d0d), with Brand Green (#18E299) reserved for the decisive signal.
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
- Scale: 2px, 4px, 5px, 6px, 7px, 8px, 10px, 12px, 16px, 24px, 32px, 48px, 64px
- Section padding: 48px–96px vertical
- Card padding: 24px–32px
- Component gaps: 8px–16px

### Grid & Container
- Max content width: approximately 1200px
- Hero: centered single-column with generous top padding (96px+)
- Feature sections: 2–3 column CSS Grid for cards
- Full-width sections with contained content
- Consistent horizontal padding: 24px (mobile) to 32px (desktop)

### Whitespace Philosophy
- **Documentation-grade breathing room**: Every element has generous surrounding whitespace. Mintlify sells documentation, so the marketing page itself demonstrates reading comfort.
- **Sections as chapters**: Each feature section is a self-contained unit with 48px–96px vertical padding, creating clear "chapter breaks."
- **Content density is low**: Unlike developer tools that pack the page, Mintlify uses 1–2 key messages per section with supporting imagery.

### Border Radius Scale
- Small (4px): Inline code, small tags, tooltips
- Medium (8px): Nav buttons, transparent buttons, small containers
- Standard (16px): Cards, content containers, image wrappers
- Large (24px): Featured cards, hero containers, section panels
- Full Pill (9999px): Buttons, inputs, badges, pills — the signature shape


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
| Subtle Border (Level 1) | `1px solid rgba(0,0,0,0.05)` | Standard card borders, dividers |
| Medium Border (Level 1b) | `1px solid rgba(0,0,0,0.08)` | Interactive elements, input borders |
| Ambient Shadow (Level 2) | `rgba(0,0,0,0.03) 0px 2px 4px` | Cards with subtle lift |
| Button Shadow (Level 2b) | `rgba(0,0,0,0.06) 0px 1px 2px` | Button micro-depth |
| Focus Ring (Accessibility) | `1px solid #18E299` outline | Focused inputs, active interactive elements |

**Shadow Philosophy**: Mintlify barely uses shadows. The depth system is almost entirely border-driven — ultra-subtle 5% opacity borders create separation without visual weight. When shadows appear, they're atmospheric whispers (`0.03 opacity, 2px blur, 4px spread`) that add the barest sense of lift. This restraint keeps the page feeling flat and paper-like — appropriate for a documentation company whose product is about clarity and readability.

### Decorative Depth
- Hero gradient: atmospheric green-white cloud gradient behind hero content
- No background color alternation — white on white throughout
- Depth comes from border opacity variation (5% → 8%) and whitespace


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Color Inversions
- **Background**: `#0d0d0d` (near-black)
- **Text Primary**: `#ededed` (near-white)
- **Text Secondary**: `#a0a0a0` (muted gray)
- **Brand Green**: `#18E299` (unchanged — the green works on both backgrounds)
- **Border**: `rgba(255,255,255,0.08)` (white at 8% opacity)
- **Card Background**: `#141414` (slightly lighter than page)
- **Shadow**: `rgba(0,0,0,0.4) 0px 2px 4px` (stronger shadow for contrast)

### Key Adjustments
- Buttons invert: white background dark text becomes dark background light text
- Badge backgrounds shift to deeper tones with lighter text
- Focus ring remains brand green
- Hero gradient shifts to dark-tinted green atmospheric wash


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
| Mobile | <768px | Single column, stacked layout, hamburger nav |
| Tablet | 768–1024px | Two-column grids begin, expanded padding |
| Desktop | >1024px | Full layout, 3-column grids, maximum content width |

### Touch Targets
- Buttons with full-pill shape have comfortable 8px+ vertical padding
- Navigation links spaced with adequate 16px+ gaps
- Mobile menu provides full-width tap targets

### Collapsing Strategy
- Hero: 64px → 40px headline, maintains tight tracking proportionally
- Navigation: horizontal links + CTA → hamburger menu at 768px
- Feature cards: 3-column → 2-column → single column stacked
- Section spacing: 96px → 48px on mobile
- Footer: multi-column → stacked single column
- Trust bar: grid → horizontal scroll or stacked

### Image Behavior
- Product screenshots maintain aspect ratio with responsive containers
- Hero gradient simplifies on mobile
- Full-width sections maintain edge-to-edge treatment


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary CTA: Near Black (`#0d0d0d`)
- Background: Pure White (`#ffffff`)
- Heading text: Near Black (`#0d0d0d`)
- Body text: Gray 700 (`#333333`)
- Border: `rgba(0,0,0,0.05)` (5% opacity)
- Brand accent: Green (`#18E299`)
- Link hover: Brand Green (`#18E299`)
- Focus ring: Brand Green (`#18E299`)

### Example Component Prompts
- "Create a hero section on white background with atmospheric green-white gradient wash. Headline at 64px Inter weight 600, line-height 1.15, letter-spacing -1.28px, color #0d0d0d. Subtitle at 18px Inter weight 400, line-height 1.50, color #666666. Dark pill CTA (#0d0d0d, 9999px radius, 8px 24px padding) and ghost pill button (white, 1px solid rgba(0,0,0,0.08), 9999px radius)."
- "Design a card: white background, 1px solid rgba(0,0,0,0.05) border, 16px radius, 24px padding, shadow rgba(0,0,0,0.03) 0px 2px 4px. Title at 20px Inter weight 600, letter-spacing -0.2px. Body at 14px weight 400, #666666."
- "Build a pill badge: #d4fae8 background, #0fa76e text, 9999px radius, 4px 12px padding, 13px Inter weight 500, uppercase."
- "Create navigation: white sticky header with backdrop-filter blur(12px). Inter 15px weight 500 for links, #0d0d0d text. Dark pill CTA 'Get Started' right-aligned, 9999px radius. Bottom border: 1px solid rgba(0,0,0,0.05)."
- "Design a trust section showing company logos in muted gray. Grid layout with 16px radius containers, 1px border at 5% opacity. Label above: 'Loved by your favorite companies' at 13px Inter weight 500, uppercase, tracking 0.65px."

### Iteration Guide
1. Always use full-pill radius (9999px) for buttons and inputs — this is Mintlify's signature shape
2. Keep borders at 5% opacity (`rgba(0,0,0,0.05)`) — stronger borders break the airy feeling
3. Letter-spacing scales with font size: -1.28px at 64px, -0.8px at 40px, -0.24px at 24px, normal at 16px
4. Three weights only: 400 (read), 500 (interact), 600 (announce)
5. Brand green (`#18E299`) is used sparingly — CTAs and hover states only, never for decorative fills
6. Geist Mono uppercase for technical labels, Inter for everything else
7. Section padding is generous: 64px–96px on desktop, 48px on mobile
8. No gray background sections — white throughout, separation through borders and whitespace


### PPT-image Quick Reference

- Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
- Display voice: `Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy.`
- Body / label voice: `16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort.`
- Primary accent: Brand Green (#18E299)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Near Black (#0d0d0d)
- Signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches, and Atmospheric gradient hero with cloud-like green-white wash
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Mintlify.
Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
Use Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy. as the display-type reference and 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0d0d0d), and Brand Green (#18E299).
Preserve these signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, and Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Mintlify.
Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
Use Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy. as the display-type reference and 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0d0d0d), and Brand Green (#18E299).
Preserve these signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, and Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Mintlify.
Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
Use Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy. as the display-type reference and 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0d0d0d), and Brand Green (#18E299).
Preserve these signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, and Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Mintlify.
Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
Use Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy. as the display-type reference and 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0d0d0d), and Brand Green (#18E299).
Preserve these signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, and Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Mintlify.
Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
Use Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy. as the display-type reference and 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0d0d0d), and Brand Green (#18E299).
Preserve these signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, and Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Mintlify.
Brand mood: Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value.
Use Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy. as the display-type reference and 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort. for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Near Black (#0d0d0d), and Brand Green (#18E299).
Preserve these signature cues: Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable, Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice, and Brand green (#18E299) used sparingly — CTAs, hover states, focus rings, and accent touches.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
