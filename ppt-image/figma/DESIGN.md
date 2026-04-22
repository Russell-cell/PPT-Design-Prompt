# PPT-image Design System Inspired by Figma

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Figma.

Source reference: `source/figma/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Figma's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore. This granular weight control gives every text element a precisely calibrated visual weight, creating hierarchy through micro-differences rather than the blunt instrument of "regular vs bold."

The page presents a fascinating duality: the interface chrome is strictly black-and-white (literally only `#000000` and `#ffffff` detected as colors), while the hero section and product showcases explode with vibrant multi-color gradients — electric greens, bright yellows, deep purples, hot pinks. This separation means the design system itself is colorless, treating the product's colorful output as the hero content. Figma's marketing page is essentially a white gallery wall displaying colorful art.

What makes Figma distinctive beyond the variable font is its circle-and-pill geometry. Buttons use 50px radius (pill) or 50% (perfect circle for icon buttons), creating an organic, tool-palette-like feel. The dashed-outline focus indicator (`dashed 2px`) is a deliberate design choice that echoes selection handles in the Figma editor itself — the website's UI language references the product's UI language.

**Key Characteristics:**
- Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700
- Strictly black-and-white interface chrome — color exists only in product content
- figmaMono for uppercase technical labels with wide letter-spacing
- Pill (50px) and circular (50%) button geometry
- Dashed focus outlines echoing Figma's editor selection handles
- Vibrant multi-color hero gradients (green, yellow, purple, pink)
- OpenType `"kern"` feature enabled globally
- Negative letter-spacing throughout — even body text at -0.14px to -0.26px


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, figmaMono for uppercase technical labels with wide letter-spacing, and Pill (50px) and circular (50%) button geometry.
- Use Pure White (#ffffff) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Glass Black (rgba(0, 0, 0, 0.08)) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Pure Black** (`#000000`): All text, all solid buttons, all borders. The sole "color" of the interface.
- **Pure White** (`#ffffff`): All backgrounds, white buttons, text on dark surfaces. The other half of the binary.

*Note: Figma's marketing site uses ONLY these two colors for its interface layer. All vibrant colors appear exclusively in product screenshots, hero gradients, and embedded content.*

### Surface & Background
- **Pure White** (`#ffffff`): Primary page background and card surfaces.
- **Glass Black** (`rgba(0, 0, 0, 0.08)`): Subtle dark overlay for secondary circular buttons and glass effects.
- **Glass White** (`rgba(255, 255, 255, 0.16)`): Frosted glass overlay for buttons on dark/colored surfaces.

### Gradient System
- **Hero Gradient**: A vibrant multi-stop gradient using electric green, bright yellow, deep purple, and hot pink. This gradient is the visual signature of the hero section — it represents the creative possibilities of the tool.
- **Product Section Gradients**: Individual product areas (Design, Dev Mode, Prototyping) may use distinct color themes in their showcases.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Glass Black (rgba(0, 0, 0, 0.08)) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Pure White (#ffffff) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Primary**: `figmaSans`, with fallbacks: `figmaSans Fallback, SF Pro Display, system-ui, helvetica`
- **Monospace / Labels**: `figmaMono`, with fallbacks: `figmaMono Fallback, SF Mono, menlo`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | figmaSans | 86px (5.38rem) | 400 | 1.00 (tight) | -1.72px | Maximum impact, extreme tracking |
| Section Heading | figmaSans | 64px (4rem) | 400 | 1.10 (tight) | -0.96px | Feature section titles |
| Sub-heading | figmaSans | 26px (1.63rem) | 540 | 1.35 | -0.26px | Emphasized section text |
| Sub-heading Light | figmaSans | 26px (1.63rem) | 340 | 1.35 | -0.26px | Light-weight section text |
| Feature Title | figmaSans | 24px (1.5rem) | 700 | 1.45 | normal | Bold card headings |
| Body Large | figmaSans | 20px (1.25rem) | 330–450 | 1.30–1.40 | -0.1px to -0.14px | Descriptions, intros |
| Body / Button | figmaSans | 16px (1rem) | 330–400 | 1.40–1.45 | -0.14px to normal | Standard body, nav, buttons |
| Body Light | figmaSans | 18px (1.13rem) | 320 | 1.45 | -0.26px to normal | Light-weight body text |
| Mono Label | figmaMono | 18px (1.13rem) | 400 | 1.30 (tight) | 0.54px | Uppercase section labels |
| Mono Small | figmaMono | 12px (0.75rem) | 400 | 1.00 (tight) | 0.6px | Uppercase tiny tags |

### Principles
- **Variable font precision**: figmaSans uses weights that most systems never touch — 320, 330, 340, 450, 480, 540. This creates hierarchy through subtle weight differences rather than dramatic jumps. The difference between 330 and 340 is nearly imperceptible but structurally significant.
- **Light as the base**: Most body text uses 320–340 (lighter than typical 400 "regular"), creating an ethereal, airy reading experience that matches the design-tool aesthetic.
- **Kern everywhere**: Every text element enables OpenType `"kern"` feature — kerning is not optional, it's structural.
- **Negative tracking by default**: Even body text uses -0.1px to -0.26px letter-spacing, creating universally tight text. Display text compresses further to -0.96px and -1.72px.
- **Mono for structure**: figmaMono in uppercase with positive letter-spacing (0.54px–0.6px) creates technical signpost labels.


### PPT-image Type Deployment

- Use `figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Black Solid (Pill)**
- Background: Pure Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Radius: circle (50%) for icon buttons
- Focus: dashed 2px outline
- Maximum emphasis

**White Pill**
- Background: Pure White (`#ffffff`)
- Text: Pure Black (`#000000`)
- Padding: 8px 18px 10px (asymmetric vertical)
- Radius: pill (50px)
- Focus: dashed 2px outline
- Standard CTA on dark/colored surfaces

**Glass Dark**
- Background: `rgba(0, 0, 0, 0.08)` (subtle dark overlay)
- Text: Pure Black
- Radius: circle (50%)
- Focus: dashed 2px outline
- Secondary action on light surfaces

**Glass Light**
- Background: `rgba(255, 255, 255, 0.16)` (frosted glass)
- Text: Pure White
- Radius: circle (50%)
- Focus: dashed 2px outline
- Secondary action on dark/colored surfaces

### Cards & Containers
- Background: Pure White
- Border: none or minimal
- Radius: 6px (small containers), 8px (images, cards, dialogs)
- Shadow: subtle to medium elevation effects
- Product screenshots as card content

### Navigation
- Clean horizontal nav on white
- Logo: Figma wordmark in black
- Product tabs: pill-shaped (50px) tab navigation
- Links: black text, underline 1px decoration
- CTA: Black pill button
- Hover: text color via CSS variable

### Distinctive Components

**Product Tab Bar**
- Horizontal pill-shaped tabs (50px radius)
- Each tab represents a Figma product area (Design, Dev Mode, Prototyping, etc.)
- Active tab highlighted

**Hero Gradient Section**
- Full-width vibrant multi-color gradient background
- White text overlay with 86px display heading
- Product screenshots floating within the gradient

**Dashed Focus Indicators**
- All interactive elements use `dashed 2px` outline on focus
- References the selection handles in the Figma editor
- A meta-design choice connecting website and product


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Figma's strongest visual cues as one large, unmistakable scene or object.
- Let Pure White (#ffffff), Pure White (#ffffff), and Glass Black (rgba(0, 0, 0, 0.08)) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Navigation, and Distinctive Components rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Figma.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Glass Black (rgba(0, 0, 0, 0.08)), with Pure White (#ffffff) reserved for the decisive signal.
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
- Scale: 1px, 2px, 4px, 4.5px, 8px, 10px, 12px, 16px, 18px, 24px, 32px, 40px, 46px, 48px, 50px

### Grid & Container
- Max container width: up to 1920px
- Hero: full-width gradient with centered content
- Product sections: alternating showcases
- Footer: dark full-width section
- Responsive from 559px to 1920px

### Whitespace Philosophy
- **Gallery-like pacing**: Generous spacing lets each product section breathe as its own exhibit.
- **Color sections as visual breathing**: The gradient hero and product showcases provide chromatic relief between the monochrome interface sections.

### Border Radius Scale
- Minimal (2px): Small link elements
- Subtle (6px): Small containers, dividers
- Comfortable (8px): Cards, images, dialogs
- Pill (50px): Tab buttons, CTAs
- Circle (50%): Icon buttons, circular elements


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
| Flat (Level 0) | No shadow | Page background, most text |
| Surface (Level 1) | White card on gradient/dark section | Cards, product showcases |
| Elevated (Level 2) | Subtle shadow | Floating cards, hover states |

**Shadow Philosophy**: Figma uses shadows sparingly. The primary depth mechanisms are **background contrast** (white content on colorful/dark sections) and the inherent dimensionality of the product screenshots themselves.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use figmaSans with precise variable weights (320–540) — the granular weight control IS the design
- Keep the interface strictly black-and-white — color comes from product content only
- Use pill (50px) and circular (50%) geometry for all interactive elements
- Apply dashed 2px focus outlines — the signature accessibility pattern
- Enable `"kern"` feature on all text
- Use figmaMono in uppercase with positive letter-spacing for labels
- Apply negative letter-spacing throughout (-0.1px to -1.72px)

### Don't
- Don't add interface colors — the monochrome palette is absolute
- Don't use standard font weights (400, 500, 600, 700) — use the variable font's unique stops (320, 330, 340, 450, 480, 540)
- Don't use sharp corners on buttons — pill and circular geometry only
- Don't use solid focus outlines — dashed is the signature
- Don't increase body font weight above 450 — the light-weight aesthetic is core
- Don't use positive letter-spacing on body text — it's always negative


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
| Small Mobile | <560px | Compact layout, stacked |
| Tablet | 560–768px | Minor adjustments |
| Small Desktop | 768–960px | 2-column layouts |
| Desktop | 960–1280px | Standard layout |
| Large Desktop | 1280–1440px | Expanded |
| Ultra-wide | 1440–1920px | Maximum width |

### Collapsing Strategy
- Hero text: 86px → 64px → 48px
- Product tabs: horizontal scroll on mobile
- Feature sections: stacked single column
- Footer: multi-column → stacked


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Everything: "Pure Black (#000000)" and "Pure White (#ffffff)"
- Glass Dark: "rgba(0, 0, 0, 0.08)"
- Glass Light: "rgba(255, 255, 255, 0.16)"

### Example Component Prompts
- "Create a hero on a vibrant multi-color gradient (green, yellow, purple, pink). Headline at 86px figmaSans weight 400, line-height 1.0, letter-spacing -1.72px. White text. White pill CTA button (50px radius, 8px 18px padding)."
- "Design a product tab bar with pill-shaped buttons (50px radius). Active: Black bg, white text. Inactive: transparent, black text. figmaSans at 20px weight 480."
- "Build a section label: figmaMono 18px, uppercase, letter-spacing 0.54px, black text. Kern enabled."
- "Create body text at 20px figmaSans weight 330, line-height 1.40, letter-spacing -0.14px. Pure Black on white."

### Iteration Guide
1. Use variable font weight stops precisely: 320, 330, 340, 450, 480, 540, 700
2. Interface is always black + white — never add colors to chrome
3. Dashed focus outlines, not solid
4. Letter-spacing is always negative on body, always positive on mono labels
5. Pill (50px) for buttons/tabs, circle (50%) for icon buttons


### PPT-image Quick Reference

- Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
- Display voice: `figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica`
- Body / label voice: `figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo`
- Primary accent: Pure White (#ffffff)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Glass Black (rgba(0, 0, 0, 0.08))
- Signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, figmaMono for uppercase technical labels with wide letter-spacing, and Pill (50px) and circular (50%) button geometry
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Figma.
Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
Use figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica as the display-type reference and figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Glass Black (rgba(0, 0, 0, 0.08)), and Pure White (#ffffff).
Preserve these signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, and figmaMono for uppercase technical labels with wide letter-spacing.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Figma.
Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
Use figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica as the display-type reference and figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Glass Black (rgba(0, 0, 0, 0.08)), and Pure White (#ffffff).
Preserve these signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, and figmaMono for uppercase technical labels with wide letter-spacing.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Figma.
Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
Use figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica as the display-type reference and figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Glass Black (rgba(0, 0, 0, 0.08)), and Pure White (#ffffff).
Preserve these signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, and figmaMono for uppercase technical labels with wide letter-spacing.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Figma.
Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
Use figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica as the display-type reference and figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Glass Black (rgba(0, 0, 0, 0.08)), and Pure White (#ffffff).
Preserve these signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, and figmaMono for uppercase technical labels with wide letter-spacing.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Figma.
Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
Use figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica as the display-type reference and figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Glass Black (rgba(0, 0, 0, 0.08)), and Pure White (#ffffff).
Preserve these signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, and figmaMono for uppercase technical labels with wide letter-spacing.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Figma.
Brand mood: Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore.
Use figmaSans, with fallbacks: figmaSans Fallback, SF Pro Display, system-ui, helvetica as the display-type reference and figmaMono, with fallbacks: figmaMono Fallback, SF Mono, menlo for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Glass Black (rgba(0, 0, 0, 0.08)), and Pure White (#ffffff).
Preserve these signature cues: Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700, Strictly black-and-white interface chrome — color exists only in product content, and figmaMono for uppercase technical labels with wide letter-spacing.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
