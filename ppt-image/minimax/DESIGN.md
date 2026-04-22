# PPT-image Design System Inspired by MiniMax

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably MiniMax.

Source reference: `source/minimax/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps MiniMax's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility. The design language is predominantly white-space-driven with a light, airy feel — pure white backgrounds (`#ffffff`) dominate, letting colorful product cards and AI model illustrations serve as the visual anchors. The overall aesthetic sits at the intersection of Apple's product marketing clarity and a playful, rounded design language that makes AI technology feel approachable.

The typography system is notably multi-font: DM Sans serves as the primary UI workhorse, Outfit handles display headings with geometric elegance, Poppins appears for mid-tier headings, and Roboto handles data-heavy contexts. This variety reflects a brand in rapid growth — each font serves a distinct communicative purpose rather than competing for attention. The hero heading at 80px weight 500 in both DM Sans and Outfit with a tight 1.10 line-height creates a bold but not aggressive opening statement.

What makes MiniMax distinctive is its pill-button geometry (9999px radius) for navigation and primary actions, combined with softer 8px–24px radiused cards for product showcases. The product cards themselves are richly colorful — vibrant gradients in pink, purple, orange, and blue — creating a "gallery of AI capabilities" feel. Against the white canvas, these colorful cards pop like app icons on a phone home screen, making each AI model/product feel like a self-contained creative tool.

**Key Characteristics:**
- White-dominant layout with colorful product card accents
- Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data)
- Pill buttons (9999px radius) for primary navigation and CTAs
- Generous rounded cards (20px–24px radius) for product showcases
- Brand blue spectrum: from `#1456f0` (brand-6) through `#3b82f6` (primary-500) to `#60a5fa` (light)
- Brand pink (`#ea5ec1`) as secondary accent
- Near-black text (`#222222`, `#18181b`) on white backgrounds
- Purple-tinted shadows (`rgba(44, 30, 116, 0.16)`) creating subtle brand-colored depth
- Dark footer section (`#181e25`) with product/company links


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), Pill buttons (9999px radius) for primary navigation and CTAs, and Generous rounded cards (20px–24px radius) for product showcases.
- Use Brand Blue (#1456f0) as the highest-signal accent when color needs to carry emphasis.
- Let Sky Blue (#3daeff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#222222) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Brand Primary
- **Brand Blue** (`#1456f0`): `--brand-6`, primary brand identity color
- **Sky Blue** (`#3daeff`): `--col-brand00`, lighter brand variant for accents
- **Brand Pink** (`#ea5ec1`): `--col-brand02`, secondary brand accent

### Blue Scale (Primary)
- **Primary 200** (`#bfdbfe`): `--color-primary-200`, light blue backgrounds
- **Primary Light** (`#60a5fa`): `--color-primary-light`, active states, highlights
- **Primary 500** (`#3b82f6`): `--color-primary-500`, standard blue actions
- **Primary 600** (`#2563eb`): `--color-primary-600`, hover states
- **Primary 700** (`#1d4ed8`): `--color-primary-700`, pressed/active states
- **Brand Deep** (`#17437d`): `--brand-3`, deep blue for emphasis

### Text Colors
- **Near Black** (`#222222`): `--col-text00`, primary text
- **Dark** (`#18181b`): Button text, headings
- **Charcoal** (`#181e25`): Dark surface text, footer background
- **Dark Gray** (`#45515e`): `--col-text04`, secondary text
- **Mid Gray** (`#8e8e93`): Tertiary text, muted labels
- **Light Gray** (`#5f5f5f`): `--brand-2`, helper text

### Surface & Background
- **Pure White** (`#ffffff`): `--col-bg13`, primary background
- **Light Gray** (`#f0f0f0`): Secondary button backgrounds
- **Glass White** (`hsla(0, 0%, 100%, 0.4)`): `--fill-bg-white`, frosted glass overlay
- **Border Light** (`#f2f3f5`): Subtle section dividers
- **Border Gray** (`#e5e7eb`): Component borders

### Semantic
- **Success Background** (`#e8ffea`): `--success-bg`, positive state backgrounds

### Shadows
- **Standard** (`rgba(0, 0, 0, 0.08) 0px 4px 6px`): Default card shadow
- **Soft Glow** (`rgba(0, 0, 0, 0.08) 0px 0px 22.576px`): Ambient soft shadow
- **Brand Purple** (`rgba(44, 30, 116, 0.16) 0px 0px 15px`): Brand-tinted glow
- **Brand Purple Offset** (`rgba(44, 30, 116, 0.11) 6.5px 2px 17.5px`): Directional brand glow
- **Card Elevation** (`rgba(36, 36, 36, 0.08) 0px 12px 16px -4px`): Lifted card shadow


### PPT-image Deployment

- Base canvas: prefer Sky Blue (#3daeff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#222222) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Brand Blue (#1456f0) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Primary UI**: `DM Sans`, with fallbacks: `Helvetica Neue, Helvetica, Arial`
- **Display**: `Outfit`, with fallbacks: `Helvetica Neue, Helvetica, Arial`
- **Mid-tier**: `Poppins`
- **Data/Technical**: `Roboto`, with fallbacks: `Helvetica Neue, Helvetica, Arial`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display Hero | DM Sans / Outfit | 80px (5.00rem) | 500 | 1.10 (tight) | Hero headlines |
| Section Heading | Outfit | 31px (1.94rem) | 600 | 1.50 | Feature section titles |
| Section Heading Alt | Roboto / DM Sans | 32px (2.00rem) | 600 | 0.88 (tight) | Compact headers |
| Card Title | Outfit | 28px (1.75rem) | 500–600 | 1.71 (relaxed) | Product card headings |
| Sub-heading | Poppins | 24px (1.50rem) | 500 | 1.50 | Mid-tier headings |
| Feature Label | Poppins | 18px (1.13rem) | 500 | 1.50 | Feature names |
| Body Large | DM Sans | 20px (1.25rem) | 500 | 1.50 | Emphasized body |
| Body | DM Sans | 16px (1.00rem) | 400–500 | 1.50 | Standard body text |
| Body Bold | DM Sans | 16px (1.00rem) | 700 | 1.50 | Strong emphasis |
| Nav/Link | DM Sans | 14px (0.88rem) | 400–500 | 1.50 | Navigation, links |
| Button Small | DM Sans | 13px (0.81rem) | 600 | 1.50 | Compact buttons |
| Caption | DM Sans / Poppins | 13px (0.81rem) | 400 | 1.70 (relaxed) | Metadata |
| Small Label | DM Sans | 12px (0.75rem) | 500–600 | 1.25–1.50 | Tags, badges |
| Micro | DM Sans / Outfit | 10px (0.63rem) | 400–500 | 1.50–1.80 | Tiny annotations |

### Principles
- **Multi-font purpose**: DM Sans = UI workhorse (body, nav, buttons); Outfit = geometric display (headings, product names); Poppins = friendly mid-tier (sub-headings, features); Roboto = technical/data contexts.
- **Universal 1.50 line-height**: The overwhelming majority of text uses 1.50 line-height, creating a consistent reading rhythm regardless of font or size. Exceptions: display (1.10 tight) and some captions (1.70 relaxed).
- **Weight 500 as default emphasis**: Most headings use 500 (medium) rather than bold, creating a modern, approachable tone. 600 for section titles, 700 reserved for strong emphasis.
- **Compact hierarchy**: The size scale jumps from 80px display straight to 28–32px section, then 16–20px body — a deliberate compression that keeps the visual hierarchy feeling efficient.


### PPT-image Type Deployment

- Use `Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Pill Primary Dark**
- Background: `#181e25`
- Text: `#ffffff`
- Padding: 11px 20px
- Radius: 8px
- Use: Primary CTA ("Get Started", "Learn More")

**Pill Nav**
- Background: `rgba(0, 0, 0, 0.05)` (subtle tint)
- Text: `#18181b`
- Radius: 9999px (full pill)
- Use: Navigation tabs, filter toggles

**Pill White**
- Background: `#ffffff`
- Text: `rgba(24, 30, 37, 0.8)`
- Radius: 9999px
- Opacity: 0.5 (default state)
- Use: Secondary nav, inactive tabs

**Secondary Light**
- Background: `#f0f0f0`
- Text: `#333333`
- Padding: 11px 20px
- Radius: 8px
- Use: Secondary actions

### Product Cards
- Background: Vibrant gradients (pink/purple/orange/blue)
- Radius: 20px–24px (generous rounding)
- Shadow: `rgba(44, 30, 116, 0.16) 0px 0px 15px` (brand purple glow)
- Content: Product name, model version, descriptive text
- Each card has its own color palette matching the product identity

### AI Product Cards (Matrix)
- Background: white with subtle shadow
- Radius: 13px–16px
- Shadow: `rgba(0, 0, 0, 0.08) 0px 4px 6px`
- Icon/illustration centered above product name
- Product name in DM Sans 14–16px weight 500

### Links
- **Primary**: `#18181b` or `#181e25`, underline on dark text
- **Secondary**: `#8e8e93`, muted for less emphasis
- **On Dark**: `rgba(255, 255, 255, 0.8)` for footer and dark sections

### Navigation
- Clean horizontal nav on white background
- MiniMax logo left-aligned (red accent in logo)
- DM Sans 14px weight 500 for nav items
- Pill-shaped active indicators (9999px radius)
- "Login" text link, minimal right-side actions
- Sticky header behavior


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use MiniMax's strongest visual cues as one large, unmistakable scene or object.
- Let Brand Blue (#1456f0), Sky Blue (#3daeff), and Near Black (#222222) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Product Cards, AI Product Cards (Matrix), and Links rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to MiniMax.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Sky Blue (#3daeff) versus Near Black (#222222), with Brand Blue (#1456f0) reserved for the decisive signal.
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
- Scale: 1px, 2px, 4px, 6px, 8px, 10px, 11px, 14px, 16px, 24px, 32px, 40px, 50px, 64px, 80px

### Grid & Container
- Max content width centered on page
- Product card grids: horizontal scroll or 3–4 column layout
- Full-width white sections with contained content
- Dark footer at full-width

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, stacked cards |
| Tablet | 768–1024px | 2-column grids |
| Desktop | >1024px | Full layout, horizontal card scrolls |

### Whitespace Philosophy
- **Gallery spacing**: Products are presented like gallery items with generous white space between cards, letting each AI model breathe as its own showcase.
- **Section rhythm**: Large vertical gaps (64px–80px) between major sections create distinct "chapters" of content.
- **Card breathing**: Product cards use internal padding of 16px–24px with ample whitespace around text.

### Border Radius Scale
- Minimal (4px): Small tags, micro badges
- Standard (8px): Buttons, small cards
- Comfortable (11px–13px): Medium cards, panels
- Generous (16px–20px): Large product cards
- Large (22px–24px): Hero product cards, major containers
- Pill (30px–32px): Badge pills, rounded panels
- Full (9999px): Buttons, nav tabs


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
| Flat (Level 0) | No shadow | White background, text blocks |
| Subtle (Level 1) | `rgba(0, 0, 0, 0.08) 0px 4px 6px` | Standard cards, containers |
| Ambient (Level 2) | `rgba(0, 0, 0, 0.08) 0px 0px 22.576px` | Soft glow around elements |
| Brand Glow (Level 3) | `rgba(44, 30, 116, 0.16) 0px 0px 15px` | Featured product cards |
| Elevated (Level 4) | `rgba(36, 36, 36, 0.08) 0px 12px 16px -4px` | Lifted cards, hover states |

**Shadow Philosophy**: MiniMax uses a distinctive purple-tinted shadow (`rgba(44, 30, 116, ...)`) for featured elements, creating a subtle brand-color glow that connects the shadow system to the blue brand identity. Standard shadows use neutral black but at low opacity (0.08), keeping everything feeling light and airy. The directional shadow variant (6.5px offset) adds dimensional interest to hero product cards.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use white as the dominant background — let product cards provide the color
- Apply pill radius (9999px) for navigation tabs and toggle buttons
- Use generous border radius (20px–24px) for product showcase cards
- Employ the purple-tinted shadow for featured/hero product cards
- Keep body text at DM Sans weight 400–500 — heavier weights for buttons only
- Use Outfit for display headings, DM Sans for everything functional
- Maintain the universal 1.50 line-height across body text
- Let colorful product illustrations/gradients serve as the primary visual interest

### Don't
- Don't add colored backgrounds to main content sections — white is structural
- Don't use sharp corners (0–4px radius) on product cards — the rounded aesthetic is core
- Don't apply the brand pink (`#ea5ec1`) to text or buttons — it's for logo and decorative accents only
- Don't mix more than one display font per section (Outfit OR Poppins, not both)
- Don't use weight 700 for headings — 500–600 is the range, 700 is reserved for strong emphasis in body text
- Don't darken shadows beyond 0.16 opacity — the light, airy feel requires restraint
- Don't use Roboto for headings — it's the data/technical context font only


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
| Mobile | <768px | Single column, stacked product cards, hamburger nav |
| Tablet | 768–1024px | 2-column product grids, condensed spacing |
| Desktop | >1024px | Full horizontal card layouts, expanded spacing |

### Collapsing Strategy
- Hero: 80px → responsive scaling to ~40px on mobile
- Product card grid: horizontal scroll → 2-column → single column stacked
- Navigation: horizontal → hamburger menu
- Footer: multi-column → stacked sections
- Spacing: 64–80px gaps → 32–40px on mobile


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Background: `#ffffff` (primary), `#181e25` (dark/footer)
- Text: `#222222` (primary), `#45515e` (secondary), `#8e8e93` (muted)
- Brand Blue: `#1456f0` (brand), `#3b82f6` (primary-500), `#2563eb` (hover)
- Brand Pink: `#ea5ec1` (accent only)
- Borders: `#e5e7eb`, `#f2f3f5`

### Example Component Prompts
- "Create a hero section on white background. Headline at 80px Outfit weight 500, line-height 1.10, near-black (#222222) text. Sub-text at 16px DM Sans weight 400, line-height 1.50, #45515e. Dark CTA button (#181e25, 8px radius, 11px 20px padding, white text)."
- "Design a product card grid: white cards with 20px border-radius, shadow rgba(44,30,116,0.16) 0px 0px 15px. Product name at 28px Outfit weight 600. Internal gradient background for the product illustration area."
- "Build navigation bar: white background, DM Sans 14px weight 500 for links, #18181b text. Pill-shaped active tab (9999px radius, rgba(0,0,0,0.05) background). MiniMax logo left-aligned."
- "Create an AI product matrix: 4-column grid of cards with 13px radius, subtle shadow rgba(0,0,0,0.08) 0px 4px 6px. Centered icon above product name in DM Sans 16px weight 500."
- "Design footer on dark (#181e25) background. Product links in DM Sans 14px, rgba(255,255,255,0.8). Multi-column layout."

### Iteration Guide
1. Start with white — color comes from product cards and illustrations only
2. Pill buttons (9999px) for nav/tabs, standard radius (8px) for CTA buttons
3. Purple-tinted shadows for featured cards, neutral shadows for everything else
4. DM Sans handles 70% of text — Outfit is display-only, Poppins is mid-tier only
5. Keep weights moderate (500–600 for headings) — the brand tone is confident but approachable
6. Large radius cards (20–24px) for products, smaller radius (8–13px) for UI elements


### PPT-image Quick Reference

- Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
- Display voice: `Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial`
- Body / label voice: `DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial`
- Primary accent: Brand Blue (#1456f0)
- Light surface anchor: Sky Blue (#3daeff)
- Dark surface anchor: Near Black (#222222)
- Signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), Pill buttons (9999px radius) for primary navigation and CTAs, and Generous rounded cards (20px–24px radius) for product showcases
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by MiniMax.
Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
Use Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial as the display-type reference and DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Sky Blue (#3daeff), Near Black (#222222), and Brand Blue (#1456f0).
Preserve these signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), and Pill buttons (9999px radius) for primary navigation and CTAs.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by MiniMax.
Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
Use Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial as the display-type reference and DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Sky Blue (#3daeff), Near Black (#222222), and Brand Blue (#1456f0).
Preserve these signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), and Pill buttons (9999px radius) for primary navigation and CTAs.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by MiniMax.
Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
Use Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial as the display-type reference and DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Sky Blue (#3daeff), Near Black (#222222), and Brand Blue (#1456f0).
Preserve these signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), and Pill buttons (9999px radius) for primary navigation and CTAs.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by MiniMax.
Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
Use Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial as the display-type reference and DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Sky Blue (#3daeff), Near Black (#222222), and Brand Blue (#1456f0).
Preserve these signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), and Pill buttons (9999px radius) for primary navigation and CTAs.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by MiniMax.
Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
Use Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial as the display-type reference and DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Sky Blue (#3daeff), Near Black (#222222), and Brand Blue (#1456f0).
Preserve these signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), and Pill buttons (9999px radius) for primary navigation and CTAs.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by MiniMax.
Brand mood: MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility.
Use Outfit, with fallbacks: Helvetica Neue, Helvetica, Arial as the display-type reference and DM Sans, with fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Sky Blue (#3daeff), Near Black (#222222), and Brand Blue (#1456f0).
Preserve these signature cues: White-dominant layout with colorful product card accents, Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data), and Pill buttons (9999px radius) for primary navigation and CTAs.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
