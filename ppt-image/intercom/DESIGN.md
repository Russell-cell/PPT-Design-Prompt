# PPT-image Design System Inspired by Intercom

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Intercom.

Source reference: `source/intercom/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Intercom's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language. The page operates on a warm off-white canvas (`#faf9f6`) with off-black (`#111111`) text, creating an intimate, magazine-like reading experience. The signature Fin Orange (`#ff5600`) — named after Intercom's AI agent — serves as the singular vibrant accent against the warm neutral palette.

The typography uses Saans — a custom geometric sans-serif with aggressive negative letter-spacing (-2.4px at 80px, -0.48px at 24px) and a consistent 1.00 line-height across all heading sizes. This creates ultra-compressed, billboard-like headlines that feel engineered and precise. Serrif provides the serif companion for editorial moments, and SaansMono handles code and uppercase technical labels. MediumLL and LLMedium appear for specific UI contexts, creating a rich five-font ecosystem.

What distinguishes Intercom is its remarkably sharp geometry — 4px border-radius on buttons creates near-rectangular interactive elements that feel industrial and precise, contrasting with the warm surface colors. Button hover states use `scale(1.1)` expansion, creating a physical "growing" interaction. The border system uses warm oat tones (`#dedbd6`) and oklab-based opacity values for sophisticated color management.

**Key Characteristics:**
- Warm off-white canvas (`#faf9f6`) with oat-toned borders (`#dedbd6`)
- Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height
- Fin Orange (`#ff5600`) as singular brand accent
- Sharp 4px border-radius — near-rectangular buttons and elements
- Scale(1.1) hover with scale(0.85) active — physical button interaction
- SaansMono uppercase labels with wide tracking (0.6px–1.2px)
- Rich multi-color report palette (blue, green, red, pink, lime, orange)
- oklab color values for sophisticated opacity management


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, Fin Orange (#ff5600) as singular brand accent, and Sharp 4px border-radius — near-rectangular buttons and elements.
- Use Fin Orange (#ff5600) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Black 80 (#313130) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Off Black** (`#111111`): `--color-off-black`, primary text, button backgrounds
- **Pure White** (`#ffffff`): `--wsc-color-content-primary`, primary surface
- **Warm Cream** (`#faf9f6`): Button backgrounds, card surfaces
- **Fin Orange** (`#ff5600`): `--color-fin`, primary brand accent
- **Report Orange** (`#fe4c02`): `--color-report-orange`, data visualization

### Report Palette
- **Report Blue** (`#65b5ff`): `--color-report-blue`
- **Report Green** (`#0bdf50`): `--color-report-green`
- **Report Red** (`#c41c1c`): `--color-report-red`
- **Report Pink** (`#ff2067`): `--color-report-pink`
- **Report Lime** (`#b3e01c`): `--color-report-lime-300`
- **Green** (`#00da00`): `--color-green`
- **Deep Blue** (`#0007cb`): Deep blue accent

### Neutral Scale (Warm)
- **Black 80** (`#313130`): `--wsc-color-black-80`, dark neutral
- **Black 60** (`#626260`): `--wsc-color-black-60`, mid neutral
- **Black 50** (`#7b7b78`): `--wsc-color-black-50`, muted text
- **Content Tertiary** (`#9c9fa5`): `--wsc-color-content-tertiary`
- **Oat Border** (`#dedbd6`): Warm border color
- **Warm Sand** (`#d3cec6`): Light warm neutral


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Black 80 (#313130) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Fin Orange (#ff5600) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Families
- **Primary**: `Saans`, fallbacks: `Saans Fallback, ui-sans-serif, system-ui`
- **Serif**: `Serrif`, fallbacks: `Serrif Fallback, ui-serif, Georgia`
- **Monospace**: `SaansMono`, fallbacks: `SaansMono Fallback, ui-monospace`
- **UI**: `MediumLL` / `LLMedium`, fallbacks: `system-ui, -apple-system`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Saans | 80px | 400 | 1.00 (tight) | -2.4px |
| Section Heading | Saans | 54px | 400 | 1.00 | -1.6px |
| Sub-heading | Saans | 40px | 400 | 1.00 | -1.2px |
| Card Title | Saans | 32px | 400 | 1.00 | -0.96px |
| Feature Title | Saans | 24px | 400 | 1.00 | -0.48px |
| Body Emphasis | Saans | 20px | 400 | 0.95 | -0.2px |
| Nav / UI | Saans | 18px | 400 | 1.00 | normal |
| Body | Saans | 16px | 400 | 1.50 | normal |
| Body Light | Saans | 14px | 300 | 1.40 | normal |
| Button | Saans | 16px / 14px | 400 | 1.50 / 1.43 | normal |
| Button Bold | LLMedium | 16px | 700 | 1.20 | 0.16px |
| Serif Body | Serrif | 16px | 300 | 1.40 | -0.16px |
| Mono Label | SaansMono | 12px | 400–500 | 1.00–1.30 | 0.6px–1.2px uppercase |


### PPT-image Type Deployment

- Use `Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `MediumLL / LLMedium, fallbacks: system-ui, -apple-system` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary Dark**
- Background: `#111111`
- Text: `#ffffff`
- Padding: 0px 14px
- Radius: 4px
- Hover: white background, dark text, scale(1.1)
- Active: green background (`#2c6415`), scale(0.85)

**Outlined**
- Background: transparent
- Text: `#111111`
- Border: `1px solid #111111`
- Radius: 4px
- Same scale hover/active behavior

**Warm Card Button**
- Background: `#faf9f6`
- Text: `#111111`
- Padding: 16px
- Border: `1px solid oklab(... / 0.1)`

### Cards & Containers
- Background: `#faf9f6` (warm cream)
- Border: `1px solid #dedbd6` (warm oat)
- Radius: 8px
- No visible shadows

### Navigation
- Saans 16px for links
- Off-black text on white
- Small 4px–6px radius buttons
- Orange Fin accent for AI features


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Intercom's strongest visual cues as one large, unmistakable scene or object.
- Let Fin Orange (#ff5600), Pure White (#ffffff), and Black 80 (#313130) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Intercom.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Black 80 (#313130), with Fin Orange (#ff5600) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing: 8px, 10px, 12px, 14px, 16px, 20px, 24px, 32px, 40px, 48px, 60px, 64px, 80px, 96px and Border Radius: 4px (buttons), 6px (nav items), 8px (cards, containers)) to create clean fields for charts, numerals, or callouts.
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

### Spacing: 8px, 10px, 12px, 14px, 16px, 20px, 24px, 32px, 40px, 48px, 60px, 64px, 80px, 96px
### Border Radius: 4px (buttons), 6px (nav items), 8px (cards, containers)


### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

### Original Depth System

Minimal shadows. Depth through warm border colors and surface tints.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use Saans with 1.00 line-height and negative tracking on all headings
- Apply 4px radius on buttons — sharp geometry is the identity
- Use Fin Orange (#ff5600) for AI/brand accent only
- Apply scale(1.1) hover on buttons
- Use warm neutrals (#faf9f6, #dedbd6)

### Don't
- Don't round buttons beyond 4px
- Don't use Fin Orange decoratively
- Don't use cool gray borders — always warm oat tones
- Don't skip the negative tracking on headings


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

Breakpoints: 425px, 530px, 600px, 640px, 768px, 896px


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Text: Off Black (`#111111`)
- Background: Warm Cream (`#faf9f6`)
- Accent: Fin Orange (`#ff5600`)
- Border: Oat (`#dedbd6`)
- Muted: `#7b7b78`

### Example Component Prompts
- "Create hero: warm cream (#faf9f6) background. Saans 80px weight 400, line-height 1.00, letter-spacing -2.4px, #111111. Dark button (#111111, 4px radius). Hover: scale(1.1), white bg."


### PPT-image Quick Reference

- Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
- Display voice: `Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui`
- Body / label voice: `MediumLL / LLMedium, fallbacks: system-ui, -apple-system`
- Primary accent: Fin Orange (#ff5600)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Black 80 (#313130)
- Signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, Fin Orange (#ff5600) as singular brand accent, and Sharp 4px border-radius — near-rectangular buttons and elements
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Intercom.
Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
Use Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui as the display-type reference and MediumLL / LLMedium, fallbacks: system-ui, -apple-system for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Black 80 (#313130), and Fin Orange (#ff5600).
Preserve these signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, and Fin Orange (#ff5600) as singular brand accent.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Intercom.
Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
Use Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui as the display-type reference and MediumLL / LLMedium, fallbacks: system-ui, -apple-system for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Black 80 (#313130), and Fin Orange (#ff5600).
Preserve these signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, and Fin Orange (#ff5600) as singular brand accent.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Intercom.
Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
Use Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui as the display-type reference and MediumLL / LLMedium, fallbacks: system-ui, -apple-system for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Black 80 (#313130), and Fin Orange (#ff5600).
Preserve these signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, and Fin Orange (#ff5600) as singular brand accent.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Intercom.
Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
Use Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui as the display-type reference and MediumLL / LLMedium, fallbacks: system-ui, -apple-system for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Black 80 (#313130), and Fin Orange (#ff5600).
Preserve these signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, and Fin Orange (#ff5600) as singular brand accent.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Intercom.
Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
Use Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui as the display-type reference and MediumLL / LLMedium, fallbacks: system-ui, -apple-system for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Black 80 (#313130), and Fin Orange (#ff5600).
Preserve these signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, and Fin Orange (#ff5600) as singular brand accent.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Intercom.
Brand mood: Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language.
Use Saans, fallbacks: Saans Fallback, ui-sans-serif, system-ui as the display-type reference and MediumLL / LLMedium, fallbacks: system-ui, -apple-system for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Black 80 (#313130), and Fin Orange (#ff5600).
Preserve these signature cues: Warm off-white canvas (#faf9f6) with oat-toned borders (#dedbd6), Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height, and Fin Orange (#ff5600) as singular brand accent.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
