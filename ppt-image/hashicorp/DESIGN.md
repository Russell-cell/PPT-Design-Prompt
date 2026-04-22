# PPT-image Design System Inspired by HashiCorp

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably HashiCorp.

Source reference: `source/hashicorp/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps HashiCorp's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable. The visual language splits between two modes: a clean white light-mode for informational sections and a dramatic dark-mode (`#15181e`, `#0d0e12`) for hero areas and product showcases, creating a day/night duality that mirrors the "build in light, deploy in dark" developer workflow.

The typography is anchored by a custom brand font (HashiCorp Sans, loaded as `__hashicorpSans_96f0ca`) that carries substantial weight — literally. Headings use 600–700 weights with tight line-heights (1.17–1.19), creating dense, authoritative text blocks that communicate enterprise confidence. The hero headline at 82px weight 600 with OpenType `"kern"` enabled is not decorative — it's infrastructure-grade typography.

What distinguishes HashiCorp is its multi-product color system. Each product in the portfolio has its own brand color — Terraform purple (`#7b42bc`), Vault yellow (`#ffcf25`), Waypoint teal (`#14c6cb`), Vagrant blue (`#1868f2`) — and these colors appear throughout as accent tokens via a CSS custom property system (`--mds-color-*`). This creates a design system within a design system: the parent brand is black-and-white with blue accents, while each child product injects its own chromatic identity.

The component system uses the `mds` (Markdown Design System) prefix, indicating a systematic, token-driven approach where colors, spacing, and states are all managed through CSS variables. Shadows are remarkably subtle — dual-layer micro-shadows using `rgba(97, 104, 117, 0.05)` that are nearly invisible but provide just enough depth to separate interactive surfaces from the background.

**Key Characteristics:**
- Dual-mode: clean white sections + dramatic dark (`#15181e`) hero/product areas
- Custom HashiCorp Sans font with 600–700 weights and `"kern"` feature
- Multi-product color system via `--mds-color-*` CSS custom properties
- Product brand colors: Terraform purple, Vault yellow, Waypoint teal, Vagrant blue
- Uppercase letter-spaced captions (13px, weight 600, 1.3px letter-spacing)
- Micro-shadows: dual-layer at 0.05 opacity — depth through whisper, not shout
- Token-driven `mds` component system with semantic variable names
- Tight border radius: 2px–8px, nothing pill-shaped or circular
- System-ui fallback stack for secondary text


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, Multi-product color system via --mds-color-* CSS custom properties, and Product brand colors: Terraform purple, Vault yellow, Waypoint teal, Vagrant blue.
- Use Vagrant Blue (#1868f2) as the highest-signal accent when color needs to carry emphasis.
- Let Black (#000000) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#0d0e12) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Brand Primary
- **Black** (`#000000`): Primary brand color, text on light surfaces, `--mds-color-hcp-brand`
- **Dark Charcoal** (`#15181e`): Dark mode backgrounds, hero sections
- **Near Black** (`#0d0e12`): Deepest dark mode surface, form inputs on dark

### Neutral Scale
- **Light Gray** (`#f1f2f3`): Light backgrounds, subtle surfaces
- **Mid Gray** (`#d5d7db`): Borders, button text on dark
- **Cool Gray** (`#b2b6bd`): Border accents (at 0.1–0.4 opacity)
- **Dark Gray** (`#656a76`): Helper text, secondary labels, `--mds-form-helper-text-color`
- **Charcoal** (`#3b3d45`): Secondary text on light, button borders
- **Near White** (`#efeff1`): Primary text on dark surfaces

### Product Brand Colors
- **Terraform Purple** (`#7b42bc`): `--mds-color-terraform-button-background`
- **Vault Yellow** (`#ffcf25`): `--mds-color-vault-button-background`
- **Waypoint Teal** (`#14c6cb`): `--mds-color-waypoint-button-background-focus`
- **Waypoint Teal Hover** (`#12b6bb`): `--mds-color-waypoint-button-background-hover`
- **Vagrant Blue** (`#1868f2`): `--mds-color-vagrant-brand`
- **Purple Accent** (`#911ced`): `--mds-color-palette-purple-300`
- **Visited Purple** (`#a737ff`): `--mds-color-foreground-action-visited`

### Semantic Colors
- **Action Blue** (`#1060ff`): Primary action links on dark
- **Link Blue** (`#2264d6`): Primary links on light
- **Bright Blue** (`#2b89ff`): Active links, hover accent
- **Amber** (`#bb5a00`): `--mds-color-palette-amber-200`, warning states
- **Amber Light** (`#fbeabf`): `--mds-color-palette-amber-100`, warning backgrounds
- **Vault Faint Yellow** (`#fff9cf`): `--mds-color-vault-radar-gradient-faint-stop`
- **Orange** (`#a9722e`): `--mds-color-unified-core-orange-6`
- **Red** (`#731e25`): `--mds-color-unified-core-red-7`, error states
- **Navy** (`#101a59`): `--mds-color-unified-core-blue-7`

### Shadows
- **Micro Shadow** (`rgba(97, 104, 117, 0.05) 0px 1px 1px, rgba(97, 104, 117, 0.05) 0px 2px 2px`): Default card/button elevation
- **Focus Outline**: `3px solid var(--mds-color-focus-action-external)` — systematic focus ring


### PPT-image Deployment

- Base canvas: prefer Black (#000000) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#0d0e12) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Vagrant Blue (#1868f2) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Primary Brand**: `__hashicorpSans_96f0ca` (HashiCorp Sans), with fallback: `__hashicorpSans_Fallback_96f0ca`
- **System UI**: `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | HashiCorp Sans | 82px (5.13rem) | 600 | 1.17 (tight) | normal | `"kern"` enabled |
| Section Heading | HashiCorp Sans | 52px (3.25rem) | 600 | 1.19 (tight) | normal | `"kern"` enabled |
| Feature Heading | HashiCorp Sans | 42px (2.63rem) | 700 | 1.19 (tight) | -0.42px | Negative tracking |
| Sub-heading | HashiCorp Sans | 34px (2.13rem) | 600–700 | 1.18 (tight) | normal | Feature blocks |
| Card Title | HashiCorp Sans | 26px (1.63rem) | 700 | 1.19 (tight) | normal | Card and panel headings |
| Small Title | HashiCorp Sans | 19px (1.19rem) | 700 | 1.21 (tight) | normal | Compact headings |
| Body Emphasis | HashiCorp Sans | 17px (1.06rem) | 600–700 | 1.18–1.35 | normal | Bold body text |
| Body Large | system-ui | 20px (1.25rem) | 400–600 | 1.50 | normal | Hero descriptions |
| Body | system-ui | 16px (1.00rem) | 400–500 | 1.63–1.69 (relaxed) | normal | Standard body text |
| Nav Link | system-ui | 15px (0.94rem) | 500 | 1.60 (relaxed) | normal | Navigation items |
| Small Body | system-ui | 14px (0.88rem) | 400–500 | 1.29–1.71 | normal | Secondary content |
| Caption | system-ui | 13px (0.81rem) | 400–500 | 1.23–1.69 | normal | Metadata, footer links |
| Uppercase Label | HashiCorp Sans | 13px (0.81rem) | 600 | 1.69 (relaxed) | 1.3px | `text-transform: uppercase` |

### Principles
- **Brand/System split**: HashiCorp Sans for headings and brand-critical text; system-ui for body, navigation, and functional text. The brand font carries the weight, system-ui carries the words.
- **Kern always on**: All HashiCorp Sans text enables OpenType `"kern"` — letterfitting is non-negotiable.
- **Tight headings**: Every heading uses 1.17–1.21 line-height, creating dense, stacked text blocks that feel infrastructural — solid, load-bearing.
- **Relaxed body**: Body text uses 1.50–1.69 line-height (notably generous), creating comfortable reading rhythm beneath the dense headings.
- **Uppercase labels as wayfinding**: 13px uppercase with 1.3px letter-spacing serves as the systematic category/section marker — always HashiCorp Sans weight 600.


### PPT-image Type Deployment

- Use `__hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Dark**
- Background: `#15181e`
- Text: `#d5d7db`
- Padding: 9px 9px 9px 15px (asymmetric, more left padding)
- Radius: 5px
- Border: `1px solid rgba(178, 182, 189, 0.4)`
- Shadow: `rgba(97, 104, 117, 0.05) 0px 1px 1px, rgba(97, 104, 117, 0.05) 0px 2px 2px`
- Focus: `3px solid var(--mds-color-focus-action-external)`
- Hover: uses `--mds-color-surface-interactive` token

**Secondary White**
- Background: `#ffffff`
- Text: `#3b3d45`
- Padding: 8px 12px
- Radius: 4px
- Hover: `--mds-color-surface-interactive` + low-shadow elevation
- Focus: `3px solid transparent` outline
- Clean, minimal appearance

**Product-Colored Buttons**
- Terraform: background `#7b42bc`
- Vault: background `#ffcf25` (dark text)
- Waypoint: background `#14c6cb`, hover `#12b6bb`
- Each product button follows the same structural pattern but uses its brand color

### Badges / Pills
- Background: `#42225b` (deep purple)
- Text: `#efeff1`
- Padding: 3px 7px
- Radius: 5px
- Border: `1px solid rgb(180, 87, 255)`
- Font: 16px

### Inputs

**Text Input (Dark Mode)**
- Background: `#0d0e12`
- Text: `#efeff1`
- Border: `1px solid rgb(97, 104, 117)`
- Padding: 11px
- Radius: 5px
- Focus: `3px solid var(--mds-color-focus-action-external)` outline

**Checkbox**
- Background: `#0d0e12`
- Border: `1px solid rgb(97, 104, 117)`
- Radius: 3px

### Links
- **Action Blue on Light**: `#2264d6`, hover → blue-600 variable, underline on hover
- **Action Blue on Dark**: `#1060ff` or `#2b89ff`, underline on hover
- **White on Dark**: `#ffffff`, transparent underline → visible underline on hover
- **Neutral on Light**: `#3b3d45`, transparent underline → visible underline on hover
- **Light on Dark**: `#efeff1`, similar hover pattern
- All links use `var(--wpl-blue-600)` as hover color

### Cards & Containers
- Light mode: white background, micro-shadow elevation
- Dark mode: `#15181e` or darker surfaces
- Radius: 8px for cards and containers
- Product showcase cards with gradient borders or accent lighting

### Navigation
- Clean horizontal nav with mega-menu dropdowns
- HashiCorp logo left-aligned
- system-ui 15px weight 500 for links
- Product categories organized by lifecycle management group
- "Get started" and "Contact us" CTAs in header
- Dark mode variant for hero sections


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use HashiCorp's strongest visual cues as one large, unmistakable scene or object.
- Let Vagrant Blue (#1868f2), Black (#000000), and Near Black (#0d0e12) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Badges / Pills, Inputs, and Links rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to HashiCorp.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Black (#000000) versus Near Black (#0d0e12), with Vagrant Blue (#1868f2) reserved for the decisive signal.
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
- Scale: 2px, 3px, 4px, 6px, 7px, 8px, 9px, 11px, 12px, 16px, 20px, 24px, 32px, 40px, 48px

### Grid & Container
- Max content width: ~1150px (xl breakpoint)
- Full-width dark hero sections with contained content
- Card grids: 2–3 column layouts
- Generous horizontal padding at desktop scale

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Tight single column |
| Mobile | 375–480px | Standard mobile |
| Small Tablet | 480–600px | Minor adjustments |
| Tablet | 600–768px | 2-column grids begin |
| Small Desktop | 768–992px | Full nav visible |
| Desktop | 992–1120px | Standard layout |
| Large Desktop | 1120–1440px | Max-width content |
| Ultra-wide | >1440px | Centered, generous margins |

### Whitespace Philosophy
- **Enterprise breathing room**: Generous vertical spacing between sections (48px–80px+) communicates stability and seriousness.
- **Dense headings, spacious body**: Tight line-height headings sit above relaxed body text, creating visual "weight at the top" of each section.
- **Dark as canvas**: Dark hero sections use extra vertical padding to let 3D illustrations and gradients breathe.

### Border Radius Scale
- Minimal (2px): Links, small inline elements
- Subtle (3px): Checkboxes, small inputs
- Standard (4px): Secondary buttons
- Comfortable (5px): Primary buttons, badges, inputs
- Card (8px): Cards, containers, images


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
| Flat (Level 0) | No shadow | Default surfaces, text blocks |
| Whisper (Level 1) | `rgba(97, 104, 117, 0.05) 0px 1px 1px, rgba(97, 104, 117, 0.05) 0px 2px 2px` | Cards, buttons, interactive surfaces |
| Focus (Level 2) | `3px solid var(--mds-color-focus-action-external)` outline | Focus rings — color-matched to context |

**Shadow Philosophy**: HashiCorp uses arguably the subtlest shadow system in modern web design. The dual-layer shadows at 5% opacity are nearly invisible — they exist not to create visual depth but to signal interactivity. If you can see the shadow, it's too strong. This restraint communicates the enterprise value of stability — nothing floats, nothing is uncertain.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use HashiCorp Sans for headings and brand text, system-ui for body and UI text
- Enable `"kern"` on all HashiCorp Sans text
- Use product brand colors ONLY for their respective products (Terraform = purple, Vault = yellow, etc.)
- Apply uppercase labels at 13px weight 600 with 1.3px letter-spacing for section markers
- Keep shadows at the "whisper" level (0.05 opacity dual-layer)
- Use the `--mds-color-*` token system for consistent color application
- Maintain the tight-heading / relaxed-body rhythm (1.17–1.21 vs 1.50–1.69 line-heights)
- Use `3px solid` focus outlines for accessibility

### Don't
- Don't use product brand colors outside their product context (no Terraform purple on Vault content)
- Don't increase shadow opacity above 0.1 — the whisper level is intentional
- Don't use pill-shaped buttons (>8px radius) — the sharp, minimal radius is structural
- Don't skip the `"kern"` feature on headings — the font requires it
- Don't use HashiCorp Sans for small body text — it's designed for 17px+ heading use
- Don't mix product colors in the same component — each product has one color
- Don't use pure black (`#000000`) for dark backgrounds — use `#15181e` or `#0d0e12`
- Don't forget the asymmetric button padding — 9px 9px 9px 15px is intentional


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
| Mobile | <768px | Single column, hamburger nav, stacked CTAs |
| Tablet | 768–992px | 2-column grids, nav begins expanding |
| Desktop | 992–1150px | Full layout, mega-menu nav |
| Large | >1150px | Max-width centered, generous margins |

### Collapsing Strategy
- Hero: 82px → 52px → 42px heading sizes
- Navigation: mega-menu → hamburger
- Product cards: 3-column → 2-column → stacked
- Dark sections maintain full-width but compress padding
- Buttons: inline → full-width stacked on mobile


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Light bg: `#ffffff`, `#f1f2f3`
- Dark bg: `#15181e`, `#0d0e12`
- Text light: `#000000`, `#3b3d45`
- Text dark: `#efeff1`, `#d5d7db`
- Links: `#2264d6` (light), `#1060ff` (dark), `#2b89ff` (active)
- Helper text: `#656a76`
- Borders: `rgba(178, 182, 189, 0.4)`, `rgb(97, 104, 117)`
- Focus: `3px solid` product-appropriate color

### Example Component Prompts
- "Create a hero on dark background (#15181e). Headline at 82px HashiCorp Sans weight 600, line-height 1.17, kern enabled, white text. Sub-text at 20px system-ui weight 400, line-height 1.50, #d5d7db text. Two buttons: primary dark (#15181e, 5px radius, 9px 15px padding) and secondary white (#ffffff, 4px radius, 8px 12px padding)."
- "Design a product card: white background, 8px radius, dual-layer shadow at rgba(97,104,117,0.05). Title at 26px HashiCorp Sans weight 700, body at 16px system-ui weight 400 line-height 1.63."
- "Build an uppercase section label: 13px HashiCorp Sans weight 600, line-height 1.69, letter-spacing 1.3px, text-transform uppercase, #656a76 color."
- "Create a product-specific CTA button: Terraform → #7b42bc background, Vault → #ffcf25 with dark text, Waypoint → #14c6cb. All: 5px radius, 500 weight text, 16px system-ui."
- "Design a dark form: #0d0e12 input background, #efeff1 text, 1px solid rgb(97,104,117) border, 5px radius, 11px padding. Focus: 3px solid accent-color outline."

### Iteration Guide
1. Always start with the mode decision: light (white) for informational, dark (#15181e) for hero/product
2. HashiCorp Sans for headings only (17px+), system-ui for everything else
3. Shadows are at whisper level (0.05 opacity) — if visible, reduce
4. Product colors are sacred — each product owns exactly one color
5. Focus rings are always 3px solid, color-matched to product context
6. Uppercase labels are the systematic wayfinding pattern — 13px, 600, 1.3px tracking


### PPT-image Quick Reference

- Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
- Display voice: `__hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca`
- Body / label voice: `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial`
- Primary accent: Vagrant Blue (#1868f2)
- Light surface anchor: Black (#000000)
- Dark surface anchor: Near Black (#0d0e12)
- Signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, Multi-product color system via --mds-color-* CSS custom properties, and Product brand colors: Terraform purple, Vault yellow, Waypoint teal, Vagrant blue
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by HashiCorp.
Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
Use __hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca as the display-type reference and system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Black (#000000), Near Black (#0d0e12), and Vagrant Blue (#1868f2).
Preserve these signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, and Multi-product color system via --mds-color-* CSS custom properties.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by HashiCorp.
Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
Use __hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca as the display-type reference and system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Black (#000000), Near Black (#0d0e12), and Vagrant Blue (#1868f2).
Preserve these signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, and Multi-product color system via --mds-color-* CSS custom properties.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by HashiCorp.
Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
Use __hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca as the display-type reference and system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Black (#000000), Near Black (#0d0e12), and Vagrant Blue (#1868f2).
Preserve these signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, and Multi-product color system via --mds-color-* CSS custom properties.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by HashiCorp.
Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
Use __hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca as the display-type reference and system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Black (#000000), Near Black (#0d0e12), and Vagrant Blue (#1868f2).
Preserve these signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, and Multi-product color system via --mds-color-* CSS custom properties.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by HashiCorp.
Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
Use __hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca as the display-type reference and system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Black (#000000), Near Black (#0d0e12), and Vagrant Blue (#1868f2).
Preserve these signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, and Multi-product color system via --mds-color-* CSS custom properties.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by HashiCorp.
Brand mood: HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable.
Use __hashicorpSans_96f0ca (HashiCorp Sans) / fallback: __hashicorpSans_Fallback_96f0ca as the display-type reference and system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in Black (#000000), Near Black (#0d0e12), and Vagrant Blue (#1868f2).
Preserve these signature cues: Dual-mode: clean white sections + dramatic dark (#15181e) hero/product areas, Custom HashiCorp Sans font with 600–700 weights and "kern" feature, and Multi-product color system via --mds-color-* CSS custom properties.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
