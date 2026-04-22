# PPT-image Design System Inspired by OpenCode

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably OpenCode.

Source reference: `source/opencode.ai/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps OpenCode's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent. The entire visual system is built on a stark dark-on-light contrast using a near-black background (`#201d1d`) with warm off-white text (`#fdfcfc`). This isn't a generic dark theme -- it's a warm, slightly reddish-brown dark that feels like a sophisticated terminal emulator rather than a cold IDE. The warm undertone in both the darks and lights (notice the subtle red channel in `#201d1d` -- rgb(32, 29, 29)) creates a cohesive, lived-in quality.

Berkeley Mono is the sole typeface, establishing an unapologetic monospace identity. Every element -- headings, body text, buttons, navigation -- shares this single font family, creating a unified "everything is code" philosophy. The heading at 38px bold with 1.50 line-height is generous and readable, while body text at 16px with weight 500 provides a slightly heavier-than-normal reading weight that enhances legibility on screen. The monospace grid naturally enforces alignment and rhythm across the layout.

The color system is deliberately minimal. The primary palette consists of just three functional tones: the warm near-black (`#201d1d`), a medium warm gray (`#9a9898`), and a bright off-white (`#fdfcfc`). Semantic colors borrow from the Apple HIG palette -- blue accent (`#007aff`), red danger (`#ff3b30`), green success (`#30d158`), orange warning (`#ff9f0a`) -- giving the interface familiar, trustworthy signal colors without adding brand complexity. Borders use a subtle warm transparency (`rgba(15, 0, 0, 0.12)`) that ties into the warm undertone of the entire system.

**Key Characteristics:**
- Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices
- Warm near-black primary (`#201d1d`) with reddish-brown undertone, not pure black
- Off-white text (`#fdfcfc`) with warm tint, not pure white
- Minimal 4px border radius throughout -- sharp, utilitarian corners
- 8px base spacing system scaling up to 96px
- Apple HIG-inspired semantic colors (blue, red, green, orange)
- Transparent warm borders using `rgba(15, 0, 0, 0.12)`
- Email input with generous 20px padding and 6px radius -- the most generous component radius
- Single button variant: dark background, light text, tight vertical padding (4px 20px)
- Underlined links as default link style, reinforcing the text-centric identity


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, Off-white text (#fdfcfc) with warm tint, not pure white, and Minimal 4px border radius throughout -- sharp, utilitarian corners.
- Use Accent Blue (#007aff) as the highest-signal accent when color needs to carry emphasis.
- Let OpenCode Light (#fdfcfc) carry calmer title-safe zones and quieter data-support slides.
- Use OpenCode Dark (#201d1d) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **OpenCode Dark** (`#201d1d`): Primary background, button fills, link text. A warm near-black with subtle reddish-brown warmth -- rgb(32, 29, 29).
- **OpenCode Light** (`#fdfcfc`): Primary text on dark surfaces, button text. A barely-warm off-white that avoids clinical pure white.
- **Mid Gray** (`#9a9898`): Secondary text, muted links. A neutral warm gray that bridges dark and light.

### Secondary
- **Dark Surface** (`#302c2c`): Slightly lighter than primary dark, used for elevated surfaces and subtle differentiation.
- **Border Gray** (`#646262`): Stronger borders, outline rings on interactive elements.
- **Light Surface** (`#f1eeee`): Light mode surface, subtle background variation.

### Accent
- **Accent Blue** (`#007aff`): Primary accent, links, interactive highlights. Apple system blue.
- **Accent Blue Hover** (`#0056b3`): Darker blue for hover states.
- **Accent Blue Active** (`#004085`): Deepest blue for pressed/active states.

### Semantic
- **Danger Red** (`#ff3b30`): Error states, destructive actions. Apple system red.
- **Danger Hover** (`#d70015`): Darker red for hover on danger elements.
- **Danger Active** (`#a50011`): Deepest red for pressed danger states.
- **Success Green** (`#30d158`): Success states, positive feedback. Apple system green.
- **Warning Orange** (`#ff9f0a`): Warning states, caution signals. Apple system orange.
- **Warning Hover** (`#cc7f08`): Darker orange for hover on warning elements.
- **Warning Active** (`#995f06`): Deepest orange for pressed warning states.

### Text Scale
- **Text Muted** (`#6e6e73`): Muted labels, disabled text, placeholder content.
- **Text Secondary** (`#424245`): Secondary text on light backgrounds, captions.

### Border
- **Border Warm** (`rgba(15, 0, 0, 0.12)`): Primary border color, warm transparent black with red tint.
- **Border Tab** (`#9a9898`): Tab underline border, 2px solid bottom.
- **Border Outline** (`#646262`): 1px solid outline border for containers.


### PPT-image Deployment

- Base canvas: prefer OpenCode Light (#fdfcfc) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer OpenCode Dark (#201d1d) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Accent Blue (#007aff) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Universal**: `Berkeley Mono`, with fallbacks: `IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`

### Hierarchy

| Role | Size | Weight | Line Height | Notes |
|------|------|--------|-------------|-------|
| Heading 1 | 38px (2.38rem) | 700 | 1.50 | Hero headlines, page titles |
| Heading 2 | 16px (1.00rem) | 700 | 1.50 | Section titles, bold emphasis |
| Body | 16px (1.00rem) | 400 | 1.50 | Standard body text, paragraphs |
| Body Medium | 16px (1.00rem) | 500 | 1.50 | Links, button text, nav items |
| Body Tight | 16px (1.00rem) | 500 | 1.00 (tight) | Compact labels, tab items |
| Caption | 14px (0.88rem) | 400 | 2.00 (relaxed) | Footnotes, metadata, small labels |

### Principles
- **One font, one voice**: Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone.
- **Weight as hierarchy**: 700 for headings, 500 for interactive/medium emphasis, 400 for body text. Three weight levels create the entire hierarchy.
- **Generous line-height**: 1.50 as the standard line-height gives text room to breathe within the monospace grid. The relaxed 2.00 line-height on captions creates clear visual separation.
- **Tight for interaction**: Interactive elements (tabs, compact labels) use 1.00 line-height for dense, clickable targets.


### PPT-image Type Deployment

- Use `Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone.` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Primary (Dark Fill)**
- Background: `#201d1d` (OpenCode Dark)
- Text: `#fdfcfc` (OpenCode Light)
- Padding: 4px 20px
- Radius: 4px
- Font: 16px Berkeley Mono, weight 500, line-height 2.00 (relaxed)
- Outline: `rgb(253, 252, 252) none 0px`
- Use: Primary CTAs, main actions

### Inputs

**Email Input**
- Background: `#f8f7f7` (light neutral)
- Text: `#201d1d`
- Border: `1px solid rgba(15, 0, 0, 0.12)`
- Padding: 20px
- Radius: 6px
- Font: Berkeley Mono, standard size
- Use: Form fields, email capture

### Links

**Default Link**
- Color: `#201d1d`
- Decoration: underline 1px
- Font-weight: 500
- Use: Primary text links in body content

**Light Link**
- Color: `#fdfcfc`
- Decoration: none
- Use: Links on dark backgrounds, navigation

**Muted Link**
- Color: `#9a9898`
- Decoration: none
- Use: Footer links, secondary navigation

### Tabs

**Tab Navigation**
- Border-bottom: `2px solid #9a9898` (active tab indicator)
- Font: 16px, weight 500, line-height 1.00
- Use: Section switching, content filtering

### Navigation
- Clean horizontal layout with Berkeley Mono throughout
- Brand logotype left-aligned in monospace
- Links at 16px weight 500 with underline decoration
- Dark background matching page background
- No backdrop blur or transparency -- solid surfaces only

### Image Treatment
- Terminal/code screenshots as hero imagery
- Dark terminal aesthetic with monospace type
- Minimal borders, content speaks for itself

### Distinctive Components

**Terminal Hero**
- Full-width dark terminal window as hero element
- ASCII art / stylized logo within terminal frame
- Monospace command examples with syntax highlighting
- Reinforces the CLI-first identity of the product

**Feature List**
- Bulleted feature items with Berkeley Mono text
- Weight 500 for feature names, 400 for descriptions
- Tight vertical spacing between items
- No cards or borders -- pure text layout

**Email Capture**
- Light background input (`#f8f7f7`) contrasting dark page
- Generous 20px padding for comfortable typing
- 6px radius -- the roundest element in the system
- Newsletter/waitlist pattern


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use OpenCode's strongest visual cues as one large, unmistakable scene or object.
- Let Accent Blue (#007aff), OpenCode Light (#fdfcfc), and OpenCode Dark (#201d1d) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Inputs, Links, and Tabs rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to OpenCode.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: OpenCode Light (#fdfcfc) versus OpenCode Dark (#201d1d), with Accent Blue (#007aff) reserved for the decisive signal.
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
- Fine scale: 1px, 2px, 4px (sub-8px for borders and micro-adjustments)
- Standard scale: 8px, 12px, 16px, 20px, 24px
- Extended scale: 32px, 40px, 48px, 64px, 80px, 96px
- The system follows a clean 4/8px grid with consistent doubling

### Grid & Container
- Max content width: approximately 800-900px (narrow, reading-optimized)
- Single-column layout as the primary pattern
- Centered content with generous horizontal margins
- Hero section: full-width dark terminal element
- Feature sections: single-column text blocks
- Footer: multi-column link grid

### Whitespace Philosophy
- **Monospace rhythm**: The fixed-width nature of Berkeley Mono creates a natural vertical grid. Line-heights of 1.50 and 2.00 maintain consistent rhythm.
- **Narrow and focused**: Content is constrained to a narrow column, creating generous side margins that focus attention on the text.
- **Sections through spacing**: No decorative dividers. Sections are separated by generous vertical spacing (48-96px) rather than borders or background changes.

### Border Radius Scale
- Micro (4px): Default for all elements -- buttons, containers, badges
- Input (6px): Form inputs get slightly more roundness
- The entire system uses just two radius values, reinforcing the utilitarian aesthetic


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
| Flat (Level 0) | No shadow, no border | Default state for most elements |
| Border Subtle (Level 1) | `1px solid rgba(15, 0, 0, 0.12)` | Section dividers, input borders, horizontal rules |
| Border Tab (Level 2) | `2px solid #9a9898` bottom only | Active tab indicator |
| Border Outline (Level 3) | `1px solid #646262` | Container outlines, elevated elements |

**Shadow Philosophy**: OpenCode's depth system is intentionally flat. There are no box-shadows in the extracted tokens -- zero shadow values were detected. Depth is communicated exclusively through border treatments and background color shifts. This flatness is consistent with the terminal aesthetic: terminals don't have shadows, and neither does OpenCode. The three border levels (transparent warm, tab indicator, solid outline) create sufficient visual hierarchy without any elevation illusion.

### Decorative Depth
- Background color shifts between `#201d1d` and `#302c2c` create subtle surface differentiation
- Transparent borders at 12% opacity provide barely-visible structure
- The warm reddish tint in border colors (`rgba(15, 0, 0, 0.12)`) ties borders to the overall warm dark palette
- No gradients, no blurs, no ambient effects -- pure flat terminal aesthetic


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Hover States
- Links: color shift from default to accent blue (`#007aff`) or underline style change
- Buttons: subtle background lightening or border emphasis
- Accent blue provides a three-stage hover sequence: `#007aff` → `#0056b3` → `#004085` (default → hover → active)
- Danger red: `#ff3b30` → `#d70015` → `#a50011`
- Warning orange: `#ff9f0a` → `#cc7f08` → `#995f06`

### Focus States
- Border-based focus: increased border opacity or solid border color
- No shadow-based focus rings -- consistent with the flat, no-shadow aesthetic
- Keyboard focus likely uses outline or border color shift to accent blue

### Transitions
- Minimal transitions expected -- terminal-inspired interfaces favor instant state changes
- Color transitions: 100-150ms for subtle state feedback
- No scale, rotate, or complex transform animations


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
| Mobile | <640px | Single column, reduced padding, heading scales down |
| Tablet | 640-1024px | Content width expands, slight padding increase |
| Desktop | >1024px | Full content width (~800-900px centered), maximum whitespace |

### Touch Targets
- Buttons with 4px 20px padding provide adequate horizontal touch area
- Input fields with 20px padding ensure comfortable mobile typing
- Tab items at 16px with tight line-height may need mobile adaptation

### Collapsing Strategy
- Hero heading: 38px → 28px → 24px on smaller screens
- Navigation: horizontal links → hamburger/drawer on mobile
- Feature lists: maintain single-column, reduce horizontal padding
- Terminal hero: maintain full-width, reduce internal padding
- Footer columns: multi-column → stacked single column
- Section spacing: 96px → 64px → 48px on mobile

### Image Behavior
- Terminal screenshots maintain aspect ratio and border treatment
- Full-width elements scale proportionally
- Monospace type maintains readability at all sizes due to fixed-width nature


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Page background: `#201d1d` (warm near-black)
- Primary text: `#fdfcfc` (warm off-white)
- Secondary text: `#9a9898` (warm gray)
- Muted text: `#6e6e73`
- Accent: `#007aff` (blue)
- Danger: `#ff3b30` (red)
- Success: `#30d158` (green)
- Warning: `#ff9f0a` (orange)
- Button bg: `#201d1d`, button text: `#fdfcfc`
- Border: `rgba(15, 0, 0, 0.12)` (warm transparent)
- Input bg: `#f8f7f7`, input border: `rgba(15, 0, 0, 0.12)`

### Example Component Prompts
- "Create a hero section on `#201d1d` warm dark background. Headline at 38px Berkeley Mono weight 700, line-height 1.50, color `#fdfcfc`. Subtitle at 16px weight 400, color `#9a9898`. Primary CTA button (`#201d1d` bg with `1px solid #646262` border, 4px radius, 4px 20px padding, `#fdfcfc` text at weight 500)."
- "Design a feature list: single-column on `#201d1d` background. Feature name at 16px Berkeley Mono weight 700, color `#fdfcfc`. Description at 16px weight 400, color `#9a9898`. No cards, no borders -- pure text with 16px vertical gap between items."
- "Build an email capture form: `#f8f7f7` background input, `1px solid rgba(15, 0, 0, 0.12)` border, 6px radius, 20px padding. Adjacent dark button (`#201d1d` bg, `#fdfcfc` text, 4px radius, 4px 20px padding). Berkeley Mono throughout."
- "Create navigation: sticky `#201d1d` background. 16px Berkeley Mono weight 500 for links, `#fdfcfc` text. Brand name left-aligned in monospace. Links with underline decoration. No blur, no transparency -- solid dark surface."
- "Design a footer: `#201d1d` background, multi-column link grid. Links at 16px Berkeley Mono weight 400, color `#9a9898`. Section headers at weight 700. Border-top `1px solid rgba(15, 0, 0, 0.12)` separator."

### Iteration Guide
1. Berkeley Mono is the only font -- never introduce a second typeface. Size and weight create all hierarchy.
2. Keep surfaces flat: no shadows, no gradients, no blur effects. Use borders and background shifts only.
3. The warm undertone matters: use `#201d1d` not `#000000`, use `#fdfcfc` not `#ffffff`. The reddish warmth is subtle but essential.
4. Border radius is 4px everywhere except inputs (6px). Never use rounded pills or large radii.
5. Semantic colors follow Apple HIG: `#007aff` blue, `#ff3b30` red, `#30d158` green, `#ff9f0a` orange. Each has hover and active darkened variants.
6. Three-stage interaction: default → hover (darkened) → active (deeply darkened) for all semantic colors.
7. Borders use `rgba(15, 0, 0, 0.12)` -- a warm transparent dark, not neutral gray. This ties borders to the warm palette.
8. Spacing follows an 8px grid: 8, 16, 24, 32, 40, 48, 64, 80, 96px. Use 4px for fine adjustments only.


### PPT-image Quick Reference

- Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
- Display voice: `Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`
- Body / label voice: `Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone.`
- Primary accent: Accent Blue (#007aff)
- Light surface anchor: OpenCode Light (#fdfcfc)
- Dark surface anchor: OpenCode Dark (#201d1d)
- Signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, Off-white text (#fdfcfc) with warm tint, not pure white, and Minimal 4px border radius throughout -- sharp, utilitarian corners
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by OpenCode.
Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
Use Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace as the display-type reference and Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone. for any short in-image labels.
Keep the palette anchored in OpenCode Light (#fdfcfc), OpenCode Dark (#201d1d), and Accent Blue (#007aff).
Preserve these signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, and Off-white text (#fdfcfc) with warm tint, not pure white.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by OpenCode.
Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
Use Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace as the display-type reference and Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone. for any short in-image labels.
Keep the palette anchored in OpenCode Light (#fdfcfc), OpenCode Dark (#201d1d), and Accent Blue (#007aff).
Preserve these signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, and Off-white text (#fdfcfc) with warm tint, not pure white.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by OpenCode.
Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
Use Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace as the display-type reference and Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone. for any short in-image labels.
Keep the palette anchored in OpenCode Light (#fdfcfc), OpenCode Dark (#201d1d), and Accent Blue (#007aff).
Preserve these signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, and Off-white text (#fdfcfc) with warm tint, not pure white.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by OpenCode.
Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
Use Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace as the display-type reference and Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone. for any short in-image labels.
Keep the palette anchored in OpenCode Light (#fdfcfc), OpenCode Dark (#201d1d), and Accent Blue (#007aff).
Preserve these signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, and Off-white text (#fdfcfc) with warm tint, not pure white.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by OpenCode.
Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
Use Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace as the display-type reference and Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone. for any short in-image labels.
Keep the palette anchored in OpenCode Light (#fdfcfc), OpenCode Dark (#201d1d), and Accent Blue (#007aff).
Preserve these signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, and Off-white text (#fdfcfc) with warm tint, not pure white.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by OpenCode.
Brand mood: OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent.
Use Berkeley Mono, with fallbacks: IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace as the display-type reference and Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code -- everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone. for any short in-image labels.
Keep the palette anchored in OpenCode Light (#fdfcfc), OpenCode Dark (#201d1d), and Accent Blue (#007aff).
Preserve these signature cues: Berkeley Mono as the sole typeface -- monospace everywhere, no sans-serif or serif voices, Warm near-black primary (#201d1d) with reddish-brown undertone, not pure black, and Off-white text (#fdfcfc) with warm tint, not pure white.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
