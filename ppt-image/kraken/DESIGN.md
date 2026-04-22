# PPT-image Design System Inspired by Kraken

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Kraken.

Source reference: `source/kraken/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Kraken's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color. The design operates on white backgrounds with Kraken Purple (`#7132f5`, `#5741d8`, `#5b1ecf`) creating a distinctive, professional crypto identity. The proprietary Kraken-Brand font handles display headings with bold (700) weight and negative tracking, while Kraken-Product (with IBM Plex Sans fallback) serves as the UI workhorse.

**Key Characteristics:**
- Kraken Purple (`#7132f5`) as primary brand with darker variants (`#5741d8`, `#5b1ecf`)
- Kraken-Brand (display) + Kraken-Product (UI) dual font system
- Near-black (`#101114`) text with cool blue-gray neutral scale
- 12px radius buttons (rounded but not pill)
- Subtle shadows (`rgba(0,0,0,0.03) 0px 4px 24px`) — whisper-level
- Green accent (`#149e61`) for positive/success states


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, Near-black (#101114) text with cool blue-gray neutral scale, and 12px radius buttons (rounded but not pill).
- Use Kraken Purple (#7132f5) as the highest-signal accent when color needs to carry emphasis.
- Let White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Near Black (#101114) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Kraken Purple** (`#7132f5`): Primary CTA, brand accent, links
- **Purple Dark** (`#5741d8`): Button borders, outlined variants
- **Purple Deep** (`#5b1ecf`): Deepest purple
- **Purple Subtle** (`rgba(133,91,251,0.16)`): Purple at 16% — subtle button backgrounds
- **Near Black** (`#101114`): Primary text

### Neutral
- **Cool Gray** (`#686b82`): Primary neutral, borders at 24% opacity
- **Silver Blue** (`#9497a9`): Secondary text, muted elements
- **White** (`#ffffff`): Primary surface
- **Border Gray** (`#dedee5`): Divider borders

### Semantic
- **Green** (`#149e61`): Success/positive at 16% opacity for badges
- **Green Dark** (`#026b3f`): Badge text


### PPT-image Deployment

- Base canvas: prefer White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Near Black (#101114) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Kraken Purple (#7132f5) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Display**: `Kraken-Brand`, fallbacks: `IBM Plex Sans, Helvetica, Arial`
- **UI / Body**: `Kraken-Product`, fallbacks: `Helvetica Neue, Helvetica, Arial`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Kraken-Brand | 48px | 700 | 1.17 | -1px |
| Section Heading | Kraken-Brand | 36px | 700 | 1.22 | -0.5px |
| Sub-heading | Kraken-Brand | 28px | 700 | 1.29 | -0.5px |
| Feature Title | Kraken-Product | 22px | 600 | 1.20 | normal |
| Body | Kraken-Product | 16px | 400 | 1.38 | normal |
| Body Medium | Kraken-Product | 16px | 500 | 1.38 | normal |
| Button | Kraken-Product | 16px | 500–600 | 1.38 | normal |
| Caption | Kraken-Product | 14px | 400–700 | 1.43–1.71 | normal |
| Small | Kraken-Product | 12px | 400–500 | 1.33 | normal |
| Micro | Kraken-Product | 7px | 500 | 1.00 | uppercase |


### PPT-image Type Deployment

- Use `Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Purple**
- Background: `#7132f5`
- Text: `#ffffff`
- Padding: 13px 16px
- Radius: 12px

**Purple Outlined**
- Background: `#ffffff`
- Text: `#5741d8`
- Border: `1px solid #5741d8`
- Radius: 12px

**Purple Subtle**
- Background: `rgba(133,91,251,0.16)`
- Text: `#7132f5`
- Padding: 8px
- Radius: 12px

**White Button**
- Background: `#ffffff`
- Text: `#101114`
- Radius: 10px
- Shadow: `rgba(0,0,0,0.03) 0px 4px 24px`

**Secondary Gray**
- Background: `rgba(148,151,169,0.08)`
- Text: `#101114`
- Radius: 12px

### Badges
- Success: `rgba(20,158,97,0.16)` bg, `#026b3f` text, 6px radius
- Neutral: `rgba(104,107,130,0.12)` bg, `#484b5e` text, 8px radius


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Kraken's strongest visual cues as one large, unmistakable scene or object.
- Let Kraken Purple (#7132f5), White (#ffffff), and Near Black (#101114) establish the hierarchy before adding any text.
- Pull attitude from Buttons and Badges rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Kraken.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: White (#ffffff) versus Near Black (#101114), with Kraken Purple (#7132f5) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing: 1px, 2px, 3px, 4px, 5px, 6px, 8px, 10px, 12px, 13px, 15px, 16px, 20px, 24px, 25px and Border Radius: 3px, 6px, 8px, 10px, 12px, 16px, 9999px, 50%) to create clean fields for charts, numerals, or callouts.
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

### Spacing: 1px, 2px, 3px, 4px, 5px, 6px, 8px, 10px, 12px, 13px, 15px, 16px, 20px, 24px, 25px
### Border Radius: 3px, 6px, 8px, 10px, 12px, 16px, 9999px, 50%


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System

- Subtle: `rgba(0,0,0,0.03) 0px 4px 24px`
- Micro: `rgba(16,24,40,0.04) 0px 1px 4px`


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Kraken Purple (#7132f5) for CTAs and links
- Apply 12px radius on all buttons
- Use Kraken-Brand for headings, Kraken-Product for body

### Don't
- Don't use pill buttons — 12px is the max radius for buttons
- Don't use other purples outside the defined scale


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

Breakpoints: 375px, 425px, 640px, 768px, 1024px, 1280px, 1536px


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Brand: Kraken Purple (`#7132f5`)
- Dark variant: `#5741d8`
- Text: Near Black (`#101114`)
- Secondary text: `#9497a9`
- Background: White (`#ffffff`)

### Example Component Prompts
- "Create hero: white background. Kraken-Brand 48px weight 700, letter-spacing -1px. Purple CTA (#7132f5, 12px radius, 13px 16px padding)."


### PPT-image Quick Reference

- Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
- Display voice: `Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial`
- Body / label voice: `Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial`
- Primary accent: Kraken Purple (#7132f5)
- Light surface anchor: White (#ffffff)
- Dark surface anchor: Near Black (#101114)
- Signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, Near-black (#101114) text with cool blue-gray neutral scale, and 12px radius buttons (rounded but not pill)
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Kraken.
Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
Use Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial as the display-type reference and Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#101114), and Kraken Purple (#7132f5).
Preserve these signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, and Near-black (#101114) text with cool blue-gray neutral scale.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Kraken.
Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
Use Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial as the display-type reference and Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#101114), and Kraken Purple (#7132f5).
Preserve these signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, and Near-black (#101114) text with cool blue-gray neutral scale.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Kraken.
Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
Use Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial as the display-type reference and Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#101114), and Kraken Purple (#7132f5).
Preserve these signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, and Near-black (#101114) text with cool blue-gray neutral scale.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Kraken.
Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
Use Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial as the display-type reference and Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#101114), and Kraken Purple (#7132f5).
Preserve these signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, and Near-black (#101114) text with cool blue-gray neutral scale.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Kraken.
Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
Use Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial as the display-type reference and Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#101114), and Kraken Purple (#7132f5).
Preserve these signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, and Near-black (#101114) text with cool blue-gray neutral scale.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Kraken.
Brand mood: Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color.
Use Kraken-Brand, fallbacks: IBM Plex Sans, Helvetica, Arial as the display-type reference and Kraken-Product, fallbacks: Helvetica Neue, Helvetica, Arial for any short in-image labels.
Keep the palette anchored in White (#ffffff), Near Black (#101114), and Kraken Purple (#7132f5).
Preserve these signature cues: Kraken Purple (#7132f5) as primary brand with darker variants (#5741d8, #5b1ecf), Kraken-Brand (display) + Kraken-Product (UI) dual font system, and Near-black (#101114) text with cool blue-gray neutral scale.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
