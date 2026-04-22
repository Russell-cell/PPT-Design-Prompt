# PPT-image Design System Inspired by Ollama

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably Ollama.

Source reference: `source/ollama/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps Ollama's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color. The design philosophy mirrors the product itself: strip away everything unnecessary until only the essential tool remains. This is the digital equivalent of a Dieter Rams object — every pixel earns its place, and the absence of design IS the design.

The entire page exists in pure grayscale. There is zero chromatic color in the interface — no brand blue, no accent green, no semantic red. The only colors that exist are shades between pure black (`#000000`) and pure white (`#ffffff`), creating a monochrome environment that lets the user's mental model of "open models" remain uncolored by brand opinion. The Ollama llama mascot, rendered in simple black line art, is the only illustration — and even it's monochrome.

What makes Ollama distinctive is the combination of SF Pro Rounded (Apple's rounded system font) with an exclusively pill-shaped geometry (9999px radius on everything interactive). The rounded letterforms + rounded buttons + rounded containers create a cohesive "softness language" that makes a developer CLI tool feel approachable and friendly rather than intimidating. This is minimalism with warmth — not cold Swiss-style grid minimalism, but the kind where the edges are literally softened.

**Key Characteristics:**
- Pure white canvas with zero chromatic color — completely grayscale
- SF Pro Rounded headlines creating a distinctively Apple-like softness
- Binary border-radius system: 12px (containers) or 9999px (everything interactive)
- Zero shadows — depth comes exclusively from background color shifts and borders
- Pill-shaped geometry on all interactive elements (buttons, tabs, inputs, tags)
- The Ollama llama as the sole illustration — black line art, no color
- Extreme content restraint — the homepage is short, focused, and uncluttered


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, Binary border-radius system: 12px (containers) or 9999px (everything interactive), and Zero shadows — depth comes exclusively from background color shifts and borders.
- Use Pure Black (#000000) as the highest-signal accent when color needs to carry emphasis.
- Let Pure White (#ffffff) carry calmer title-safe zones and quieter data-support slides.
- Use Pure Black (#000000) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Pure Black** (`#000000`): Primary headlines, primary links, and the darkest text. The only "color" that demands attention.
- **Near Black** (`#262626`): Button text on light surfaces, secondary headline weight.
- **Darkest Surface** (`#090909`): The darkest possible surface — barely distinguishable from pure black, used for footer or dark containers.

### Surface & Background
- **Pure White** (`#ffffff`): The primary page background — not off-white, not cream, pure white. Button surfaces for secondary actions.
- **Snow** (`#fafafa`): The subtlest possible surface distinction from white — used for section backgrounds and barely-elevated containers.
- **Light Gray** (`#e5e5e5`): Button backgrounds, borders, and the primary containment color. The workhorse neutral.

### Neutrals & Text
- **Stone** (`#737373`): Secondary body text, footer links, and de-emphasized content. The primary "muted" tone.
- **Mid Gray** (`#525252`): Emphasized secondary text, slightly darker than Stone.
- **Silver** (`#a3a3a3`): Tertiary text, placeholders, and deeply de-emphasized metadata.
- **Button Text Dark** (`#404040`): Specific to white-surface button text.

### Semantic & Accent
- **Ring Blue** (`#3b82f6` at 50%): The ONLY non-gray color in the entire system — Tailwind's default focus ring, used exclusively for keyboard accessibility. Never visible in normal interaction flow.
- **Border Light** (`#d4d4d4`): A slightly darker gray for white-surface button borders.

### Gradient System
- **None.** Ollama uses absolutely no gradients. Visual separation comes from flat color blocks and single-pixel borders. This is a deliberate, almost philosophical design choice.


### PPT-image Deployment

- Base canvas: prefer Pure White (#ffffff) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Pure Black (#000000) when the deck needs cinematic weight or a chapter reset.
- Primary accent: Pure Black (#000000) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Display**: `SF Pro Rounded`, with fallbacks: `system-ui, -apple-system, system-ui`
- **Body / UI**: `ui-sans-serif`, with fallbacks: `system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji`
- **Monospace**: `ui-monospace`, with fallbacks: `SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New`

*Note: SF Pro Rounded is Apple's system font — it renders with rounded terminals on macOS/iOS and falls back to the system sans-serif on other platforms.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | SF Pro Rounded | 48px (3rem) | 500 | 1.00 (tight) | normal | Maximum impact, rounded letterforms |
| Section Heading | SF Pro Rounded | 36px (2.25rem) | 500 | 1.11 (tight) | normal | Feature section titles |
| Sub-heading | SF Pro Rounded / ui-sans-serif | 30px (1.88rem) | 400–500 | 1.20 (tight) | normal | Card headings, feature names |
| Card Title | ui-sans-serif | 24px (1.5rem) | 400 | 1.33 | normal | Medium emphasis headings |
| Body Large | ui-sans-serif | 18px (1.13rem) | 400–500 | 1.56 | normal | Hero descriptions, button text |
| Body / Link | ui-sans-serif | 16px (1rem) | 400–500 | 1.50 | normal | Standard body text, navigation |
| Caption | ui-sans-serif | 14px (0.88rem) | 400 | 1.43 | normal | Metadata, descriptions |
| Small | ui-sans-serif | 12px (0.75rem) | 400 | 1.33 | normal | Smallest sans-serif text |
| Code Body | ui-monospace | 16px (1rem) | 400 | 1.50 | normal | Inline code, commands |
| Code Caption | ui-monospace | 14px (0.88rem) | 400 | 1.43 | normal | Code snippets, secondary |
| Code Small | ui-monospace | 12px (0.75rem) | 400–700 | 1.63 | normal | Tags, labels |

### Principles
- **Rounded display, standard body**: SF Pro Rounded carries display headlines with its distinctive rounded terminals, while the standard system sans handles all body text. The rounded font IS the brand expression.
- **Weight restraint**: Only two weights matter — 400 (regular) for body and 500 (medium) for headings. No bold, no light, no black weight. This extreme restraint reinforces the minimal philosophy.
- **Tight display, comfortable body**: Headlines compress to 1.0 line-height, while body text relaxes to 1.43–1.56. The contrast creates clear hierarchy without needing weight contrast.
- **Monospace for developer identity**: Code blocks and terminal commands appear throughout as primary content, using the system monospace stack.


### PPT-image Type Deployment

- Use `SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons

**Gray Pill (Primary)**
- Background: Light Gray (`#e5e5e5`)
- Text: Near Black (`#262626`)
- Padding: 10px 24px
- Border: thin solid Light Gray (`1px solid #e5e5e5`)
- Radius: pill-shaped (9999px)
- The primary action button — understated, grayscale, always pill-shaped

**White Pill (Secondary)**
- Background: Pure White (`#ffffff`)
- Text: Button Text Dark (`#404040`)
- Padding: 10px 24px
- Border: thin solid Border Light (`1px solid #d4d4d4`)
- Radius: pill-shaped (9999px)
- Secondary action — visually lighter than Gray Pill

**Black Pill (CTA)**
- Background: Pure Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Radius: pill-shaped (9999px)
- Inferred from "Create account" and "Explore" buttons
- Maximum emphasis — black on white

### Cards & Containers
- Background: Pure White or Snow (`#fafafa`)
- Border: thin solid Light Gray (`1px solid #e5e5e5`) when needed
- Radius: comfortably rounded (12px) — the ONLY non-pill radius in the system
- Shadow: **none** — zero shadows on any element
- Hover: likely subtle background shift or border darkening

### Inputs & Forms
- Background: Pure White
- Border: `1px solid #e5e5e5`
- Radius: pill-shaped (9999px) — search inputs and form fields are pill-shaped
- Focus: Ring Blue (`#3b82f6` at 50%) ring
- Placeholder: Silver (`#a3a3a3`)

### Navigation
- Clean horizontal nav with minimal elements
- Logo: Ollama llama icon + wordmark in black
- Links: "Models", "Docs", "Pricing" in black at 16px, weight 400
- Search bar: pill-shaped with placeholder text
- Right side: "Sign in" link + "Download" black pill CTA
- No borders, no background — transparent nav on white page

### Image Treatment
- The Ollama llama mascot is the only illustration — black line art on white
- Code screenshots/terminal outputs shown in bordered containers (12px radius)
- Integration logos displayed as simple icons in a grid
- No photographs, no gradients, no decorative imagery

### Distinctive Components

**Tab Pills**
- Pill-shaped tab selectors (e.g., "Coding" | "OpenClaw")
- Active: Light Gray bg; Inactive: transparent
- All pill-shaped (9999px)

**Model Tags**
- Small pill-shaped tags (e.g., "ollama", "launch", "claude")
- Light Gray background, dark text
- The primary way to browse models

**Terminal Command Block**
- Monospace code showing `ollama run` commands
- Minimal styling — just a bordered 12px-radius container
- Copy button integrated

**Integration Grid**
- Grid of integration logos (Codex, Claude Code, OpenCode, LangChain, etc.)
- Each in a bordered pill or card with icon + name
- Tabbed by category (Coding, Documents & RAG, Automation, Chat)


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use Ollama's strongest visual cues as one large, unmistakable scene or object.
- Let Pure Black (#000000), Pure White (#ffffff), and Pure Black (#000000) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to Ollama.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Pure White (#ffffff) versus Pure Black (#000000), with Pure Black (#000000) reserved for the decisive signal.
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
- Scale: 4px, 6px, 8px, 9px, 10px, 12px, 14px, 16px, 20px, 24px, 32px, 40px, 48px, 88px, 112px
- Button padding: 10px 24px (consistent across all buttons)
- Card internal padding: approximately 24–32px
- Section vertical spacing: very generous (88px–112px)

### Grid & Container
- Max container width: approximately 1024–1280px, centered
- Hero: centered single-column with llama illustration
- Feature sections: 2-column layout (text left, code right)
- Integration grid: responsive multi-column
- Footer: clean single-row

### Whitespace Philosophy
- **Emptiness as luxury**: The page is remarkably short and sparse — no feature section overstays its welcome. Each concept gets minimal but sufficient space.
- **Content density is low by design**: Where other AI companies pack feature after feature, Ollama presents three ideas (run models, use with apps, integrations) and stops.
- **The white space IS the brand**: Pure white space with zero decoration communicates "this tool gets out of your way."

### Border Radius Scale
- Comfortably rounded (12px): The sole container radius — code blocks, cards, panels
- Pill-shaped (9999px): Everything interactive — buttons, tabs, inputs, tags, badges

*This binary system is extreme and distinctive. There is no 4px, no 8px, no gradient of roundness. Elements are either containers (12px) or interactive (pill).*


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
| Flat (Level 0) | No shadow, no border | Page background, most content |
| Bordered (Level 1) | `1px solid #e5e5e5` | Cards, code blocks, buttons |

**Shadow Philosophy**: Ollama uses **zero shadows**. This is not an oversight — it's a deliberate design decision. Every other major AI product site uses at least subtle shadows. Ollama's flat, shadowless approach creates a paper-like experience where elements are distinguished purely by background color and single-pixel borders. Depth is communicated through **content hierarchy and typography weight**, not visual layering.


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use pure white (`#ffffff`) as the page background — never off-white or cream
- Use pill-shaped (9999px) radius on all interactive elements — buttons, tabs, inputs, tags
- Use 12px radius on all non-interactive containers — code blocks, cards, panels
- Keep the palette strictly grayscale — no chromatic colors except the blue focus ring
- Use SF Pro Rounded at weight 500 for display headings — the rounded terminals are the brand expression
- Maintain zero shadows — depth comes from borders and background shifts only
- Keep content density low — each section should present one clear idea
- Use monospace for terminal commands and code — it's primary content, not decoration
- Keep all buttons at 10px 24px padding with pill shape — consistency is absolute

### Don't
- Don't introduce any chromatic color — no brand blue, no accent green, no warm tones
- Don't use border-radius between 12px and 9999px — the system is binary
- Don't add shadows to any element — the flat aesthetic is intentional
- Don't use font weights above 500 — no bold, no black weight
- Don't add decorative illustrations beyond the llama mascot
- Don't use gradients anywhere — flat blocks and borders only
- Don't overcomplicate the layout — two columns maximum, no complex grids
- Don't use borders heavier than 1px — containment is always the lightest possible touch
- Don't add hover animations or transitions — interactions should feel instant and direct


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
| Mobile | <640px | Single column, stacked everything, hamburger nav |
| Small Tablet | 640–768px | Minor adjustments to spacing |
| Tablet | 768–850px | 2-column layouts begin |
| Desktop | 850–1024px | Standard layout, expanded features |
| Large Desktop | 1024–1280px | Maximum content width |

### Touch Targets
- All buttons are pill-shaped with generous padding (10px 24px)
- Navigation links at comfortable 16px size
- Minimum touch area easily exceeds 44x44px

### Collapsing Strategy
- **Navigation**: Collapses to hamburger menu on mobile
- **Feature sections**: 2-column → stacked single column
- **Hero text**: 48px → 36px → 30px progressive scaling
- **Integration grid**: Multi-column → 2-column → single column
- **Code blocks**: Horizontal scroll maintained

### Image Behavior
- Llama mascot scales proportionally
- Code blocks maintain monospace formatting
- Integration icons reflow to fewer columns
- No art direction changes


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary Text: "Pure Black (#000000)"
- Page Background: "Pure White (#ffffff)"
- Secondary Text: "Stone (#737373)"
- Button Background: "Light Gray (#e5e5e5)"
- Borders: "Light Gray (#e5e5e5)"
- Muted Text: "Silver (#a3a3a3)"
- Dark Text: "Near Black (#262626)"
- Subtle Surface: "Snow (#fafafa)"

### Example Component Prompts
- "Create a hero section on pure white (#ffffff) with an illustration centered above a headline at 48px SF Pro Rounded weight 500, line-height 1.0. Use Pure Black (#000000) text. Below, add a black pill-shaped CTA button (9999px radius, 10px 24px padding) and a gray pill button."
- "Design a code block with a 12px border-radius, 1px solid Light Gray (#e5e5e5) border on white background. Use ui-monospace at 16px for the terminal command. No shadow."
- "Build a tab bar with pill-shaped tabs (9999px radius). Active tab: Light Gray (#e5e5e5) background, Near Black (#262626) text. Inactive: transparent background, Stone (#737373) text."
- "Create an integration card grid. Each card is a bordered pill (9999px radius) or a 12px-radius card with 1px solid #e5e5e5 border. Icon + name inside. Grid of 4 columns on desktop."
- "Design a navigation bar: transparent background, no border. Ollama logo on the left, 3 text links (Pure Black, 16px, weight 400), pill search input in the center, 'Sign in' text link and black pill 'Download' button on the right."

### Iteration Guide
1. Focus on ONE component at a time
2. Keep all values grayscale — "Stone (#737373)" not "use a light color"
3. Always specify pill (9999px) or container (12px) radius — nothing in between
4. Shadows are always zero — never add them
5. Weight is always 400 or 500 — never bold
6. If something feels too decorated, remove it — less is always more for Ollama


### PPT-image Quick Reference

- Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
- Display voice: `SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui`
- Body / label voice: `ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji`
- Primary accent: Pure Black (#000000)
- Light surface anchor: Pure White (#ffffff)
- Dark surface anchor: Pure Black (#000000)
- Signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, Binary border-radius system: 12px (containers) or 9999px (everything interactive), and Zero shadows — depth comes exclusively from background color shifts and borders
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by Ollama.
Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
Use SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui as the display-type reference and ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Pure Black (#000000).
Preserve these signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, and Binary border-radius system: 12px (containers) or 9999px (everything interactive).
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by Ollama.
Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
Use SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui as the display-type reference and ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Pure Black (#000000).
Preserve these signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, and Binary border-radius system: 12px (containers) or 9999px (everything interactive).
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by Ollama.
Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
Use SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui as the display-type reference and ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Pure Black (#000000).
Preserve these signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, and Binary border-radius system: 12px (containers) or 9999px (everything interactive).
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by Ollama.
Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
Use SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui as the display-type reference and ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Pure Black (#000000).
Preserve these signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, and Binary border-radius system: 12px (containers) or 9999px (everything interactive).
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by Ollama.
Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
Use SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui as the display-type reference and ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Pure Black (#000000).
Preserve these signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, and Binary border-radius system: 12px (containers) or 9999px (everything interactive).
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by Ollama.
Brand mood: Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color.
Use SF Pro Rounded, with fallbacks: system-ui, -apple-system, system-ui as the display-type reference and ui-sans-serif, with fallbacks: system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji for any short in-image labels.
Keep the palette anchored in Pure White (#ffffff), Pure Black (#000000), and Pure Black (#000000).
Preserve these signature cues: Pure white canvas with zero chromatic color — completely grayscale, SF Pro Rounded headlines creating a distinctively Apple-like softness, and Binary border-radius system: 12px (containers) or 9999px (everything interactive).
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
