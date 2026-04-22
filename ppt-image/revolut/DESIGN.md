# PPT-image Design System Inspired by Revolut

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Revolut.

Source reference: `source/revolut/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Revolut's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette. The visual language is built on Aeonik Pro, a geometric grotesque that creates billboard-scale headlines at 136px with weight 500 and aggressive negative tracking (-2.72px). This isn't subtle branding; it's fintech at stadium scale.

The color system is built on a comprehensive `--rui-*` (Revolut UI) token architecture with semantic naming for every state: danger (`#e23b4a`), warning (`#ec7e00`), teal (`#00a87e`), blue (`#494fdf`), deep-pink (`#e61e49`), and more. But the marketing surface itself is remarkably restrained — near-black (`#191c1f`) and pure white (`#ffffff`) dominate, with the colorful semantic tokens reserved for the product interface, not the marketing page.

What distinguishes Revolut is its pill-everything button system. Every button uses 9999px radius — primary dark (`#191c1f`), secondary light (`#f4f4f4`), outlined (`transparent + 2px solid`), and ghost on dark (`rgba(244,244,244,0.1) + 2px solid`). The padding is generous (14px 32px–34px), creating large, confident touch targets. Combined with Inter for body text at various weights and positive letter-spacing (0.16px–0.24px), the result is a design that feels both premium and accessible — banking for the modern era.

**Key Characteristics:**
- Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines
- Near-black (`#191c1f`) + white binary with comprehensive `--rui-*` semantic tokens
- Universal pill buttons (9999px radius) with generous padding (14px 32px)
- Inter for body text with positive letter-spacing (0.16px–0.24px)
- Rich semantic color system: blue, teal, pink, yellow, green, brown, danger, warning
- Zero shadows detected — depth through color contrast only
- Tight display line-heights (1.00) with relaxed body (1.50–1.56)


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, Universal pill buttons (9999px radius) with generous padding (14px 32px), and Inter for body text with positive letter-spacing (0.16px–0.24px).
- Use Revolut Blue (#494fdf) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Revolut Dark (#191c1f) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Revolut Dark** (`#191c1f`): Primary dark surface, button background, near-black text
- **Pure White** (`#ffffff`): `--rui-color-action-label`, primary light surface
- **Light Surface** (`#f4f4f4`): Secondary button background, subtle surface

### Brand / Interactive
- **Revolut Blue** (`#494fdf`): `--rui-color-blue`, primary brand blue
- **Action Blue** (`#4f55f1`): `--rui-color-action-photo-header-text`, header accent
- **Blue Text** (`#376cd5`): `--website-color-blue-text`, link blue

### Semantic
- **Danger Red** (`#e23b4a`): `--rui-color-danger`, error/destructive
- **Deep Pink** (`#e61e49`): `--rui-color-deep-pink`, critical accent
- **Warning Orange** (`#ec7e00`): `--rui-color-warning`, warning states
- **Yellow** (`#b09000`): `--rui-color-yellow`, attention
- **Teal** (`#00a87e`): `--rui-color-teal`, success/positive
- **Light Green** (`#428619`): `--rui-color-light-green`, secondary success
- **Green Text** (`#006400`): `--website-color-green-text`, green text
- **Light Blue** (`#007bc2`): `--rui-color-light-blue`, informational
- **Brown** (`#936d62`): `--rui-color-brown`, warm neutral accent
- **Red Text** (`#8b0000`): `--website-color-red-text`, dark red text

### Neutral Scale
- **Mid Slate** (`#505a63`): Secondary text
- **Cool Gray** (`#8d969e`): Muted text, tertiary
- **Gray Tone** (`#c9c9cd`): `--rui-color-grey-tone-20`, borders/dividers


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Revolut Dark (#191c1f) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Revolut Blue (#494fdf) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `Aeonik Pro` — geometric grotesque, no detected fallbacks
- **Body / UI**: `Inter` — standard system sans
- **Fallback**: `Arial` for specific button contexts

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Mega | Aeonik Pro | 136px (8.50rem) | 500 | 1.00 (tight) | -2.72px | Stadium-scale hero |
| Display Hero | Aeonik Pro | 80px (5.00rem) | 500 | 1.00 (tight) | -0.8px | Primary hero |
| Section Heading | Aeonik Pro | 48px (3.00rem) | 500 | 1.21 (tight) | -0.48px | Feature sections |
| Sub-heading | Aeonik Pro | 40px (2.50rem) | 500 | 1.20 (tight) | -0.4px | Sub-sections |
| Card Title | Aeonik Pro | 32px (2.00rem) | 500 | 1.19 (tight) | -0.32px | Card headings |
| Feature Title | Aeonik Pro | 24px (1.50rem) | 400 | 1.33 | normal | Light headings |
| Nav / UI | Aeonik Pro | 20px (1.25rem) | 500 | 1.40 | normal | Navigation, buttons |
| Body Large | Inter | 18px (1.13rem) | 400 | 1.56 | -0.09px | Introductions |
| Body | Inter | 16px (1.00rem) | 400 | 1.50 | 0.24px | Standard reading |
| Body Semibold | Inter | 16px (1.00rem) | 600 | 1.50 | 0.16px | Emphasized body |
| Body Bold Link | Inter | 16px (1.00rem) | 700 | 1.50 | 0.24px | Bold links |

### Principles
- **Weight 500 as display default**: Aeonik Pro uses medium (500) for ALL headings — no bold. This creates authority through size and tracking, not weight.
- **Billboard tracking**: -2.72px at 136px is extremely compressed — text designed to be read at a glance, like airport signage.
- **Positive tracking on body**: Inter uses +0.16px to +0.24px, creating airy, well-spaced reading text that contrasts with the compressed headings.


### PPT-image Type Deployment

- Use `Aeonik Pro — geometric grotesque, no detected fallbacks` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Inter — standard system sans` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Dark Pill**
- Background: `#191c1f`
- Text: `#ffffff`
- Padding: 14px 32px
- Radius: 9999px (full pill)
- Hover: opacity 0.85
- Focus: `0 0 0 0.125rem` ring

**Secondary Light Pill**
- Background: `#f4f4f4`
- Text: `#000000`
- Padding: 14px 34px
- Radius: 9999px
- Hover: opacity 0.85

**Outlined Pill**
- Background: transparent
- Text: `#191c1f`
- Border: `2px solid #191c1f`
- Padding: 14px 32px
- Radius: 9999px

**Ghost on Dark**
- Background: `rgba(244, 244, 244, 0.1)`
- Text: `#f4f4f4`
- Border: `2px solid #f4f4f4`
- Padding: 14px 32px
- Radius: 9999px

### Cards & Containers
- Radius: 12px (small), 20px (cards)
- No shadows — flat surfaces with color contrast
- Dark and light section alternation

### Navigation
- Aeonik Pro 20px weight 500
- Clean header, hamburger toggle at 12px radius
- Pill CTAs right-aligned


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Revolut's strongest visual cues as one large, unmistakable scene or object.
- Let Revolut Blue (#494fdf), Pure White (#ffffff), and Revolut Dark (#191c1f) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Revolut.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Revolut Dark (#191c1f), with Revolut Blue (#494fdf) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System and Border Radius Scale) to create clean fields for charts, numerals, or callouts.
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
- Scale: 4px, 6px, 8px, 14px, 16px, 20px, 24px, 32px, 40px, 48px, 80px, 88px, 120px
- Large section spacing: 80px–120px

### Border Radius Scale
- Standard (12px): Navigation, small buttons
- Card (20px): Feature cards
- Pill (9999px): All buttons


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
| Flat (Level 0) | No shadow | Everything — Revolut uses zero shadows |
| Focus | `0 0 0 0.125rem` ring | Accessibility focus |

**Shadow Philosophy**: Revolut uses ZERO shadows. Depth comes entirely from the dark/light section contrast and the generous whitespace between elements.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Aeonik Pro weight 500 for all display headings
- Apply 9999px radius to all buttons — pill shape is universal
- Use generous button padding (14px 32px)
- Keep the palette to near-black + white for marketing surfaces
- Apply positive letter-spacing on Inter body text

### Don't
- Don't use shadows — Revolut is flat by design
- Don't use bold (700) for Aeonik Pro headings — 500 is the weight
- Don't use small buttons — the generous padding is intentional
- Don't apply semantic colors to marketing surfaces — they're for the product


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
| Mobile Small | <400px | Compact, single column |
| Mobile | 400–720px | Standard mobile |
| Tablet | 720–1024px | 2-column layouts |
| Desktop | 1024–1280px | Standard desktop |
| Large | 1280–1920px | Full layout |


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Dark: Revolut Dark (`#191c1f`)
- Light: White (`#ffffff`)
- Surface: Light (`#f4f4f4`)
- Blue: Revolut Blue (`#494fdf`)
- Danger: Red (`#e23b4a`)
- Success: Teal (`#00a87e`)

### Example Component Prompts
- "Create a hero: white background. Headline at 136px Aeonik Pro weight 500, line-height 1.00, letter-spacing -2.72px, #191c1f text. Dark pill CTA (#191c1f, 9999px, 14px 32px). Outlined pill secondary (transparent, 2px solid #191c1f)."
- "Build a pill button: #191c1f background, white text, 9999px radius, 14px 32px padding, 20px Aeonik Pro weight 500. Hover: opacity 0.85."

### Iteration Guide
1. Aeonik Pro 500 for headings — never bold
2. All buttons are pills (9999px) with generous padding
3. Zero shadows — flat is the Revolut identity
4. Near-black + white for marketing, semantic colors for product


### PPT-image Quick Reference

- Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
- Display voice: `Aeonik Pro — geometric grotesque, no detected fallbacks`
- Body / label voice: `Inter — standard system sans`
- Primary accent: Revolut Blue (#494fdf)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Revolut Dark (#191c1f)
- Signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, Universal pill buttons (9999px radius) with generous padding (14px 32px), and Inter for body text with positive letter-spacing (0.16px–0.24px)
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Revolut.
Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
Use Aeonik Pro — geometric grotesque, no detected fallbacks as the display-type reference and Inter — standard system sans for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Revolut Dark (#191c1f), and Revolut Blue (#494fdf).
Preserve these signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, and Universal pill buttons (9999px radius) with generous padding (14px 32px).
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Revolut.
Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
Use Aeonik Pro — geometric grotesque, no detected fallbacks as the display-type reference and Inter — standard system sans for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Revolut Dark (#191c1f), and Revolut Blue (#494fdf).
Preserve these signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, and Universal pill buttons (9999px radius) with generous padding (14px 32px).
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Revolut.
Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
Use Aeonik Pro — geometric grotesque, no detected fallbacks as the display-type reference and Inter — standard system sans for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Revolut Dark (#191c1f), and Revolut Blue (#494fdf).
Preserve these signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, and Universal pill buttons (9999px radius) with generous padding (14px 32px).
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Revolut.
Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
Use Aeonik Pro — geometric grotesque, no detected fallbacks as the display-type reference and Inter — standard system sans for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Revolut Dark (#191c1f), and Revolut Blue (#494fdf).
Preserve these signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, and Universal pill buttons (9999px radius) with generous padding (14px 32px).
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Revolut.
Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
Use Aeonik Pro — geometric grotesque, no detected fallbacks as the display-type reference and Inter — standard system sans for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Revolut Dark (#191c1f), and Revolut Blue (#494fdf).
Preserve these signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, and Universal pill buttons (9999px radius) with generous padding (14px 32px).
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Revolut.
Brand mood: Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette.
Use Aeonik Pro — geometric grotesque, no detected fallbacks as the display-type reference and Inter — standard system sans for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Revolut Dark (#191c1f), and Revolut Blue (#494fdf).
Preserve these signature cues: Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines, Near-black (#191c1f) + white binary with comprehensive --rui-* semantic tokens, and Universal pill buttons (9999px radius) with generous padding (14px 32px).
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
