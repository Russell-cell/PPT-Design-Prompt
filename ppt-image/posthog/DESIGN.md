# PPT-image Design System Inspired by PostHog

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably PostHog.

Source reference: `source/posthog/DESIGN.md`
Adaptation date: `2026-04-22`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps PostHog's brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

### Original Brand DNA

PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate. The background isn't the expected crisp white or dark void of developer tools; it's a warm, sage-tinted cream (`#fdfdf8`) that gives every surface a handmade, paper-like quality. Colors lean into earthy olive greens and muted sage rather than the conventional blues and purples of the SaaS world. It's as if someone designed a developer analytics platform inside a cozy garden shed.

The personality is the star: hand-drawn hedgehog illustrations, quirky action figures, and playful imagery replace the stock photography and abstract gradients typical of B2B SaaS. IBM Plex Sans Variable serves as the typographic foundation — a font with genuine technical credibility (created by IBM, widely used in developer contexts) deployed here with bold weights (700, 800) on headings and generous line-heights on body text. The typography says "we're serious engineers" while everything around it says "but we don't take ourselves too seriously."

The interaction design carries the same spirit: hover states flash PostHog Orange (`#F54E00`) text — a hidden brand color that doesn't appear at rest but surprises on interaction. Dark near-black buttons (`#1e1f23`) use opacity reduction on hover rather than color shifts, and active states scale slightly. The border system uses sage-tinted grays (`#bfc1b7`) that harmonize with the olive text palette. Built on Tailwind CSS with Radix UI and shadcn/ui primitives, the technical foundation is modern and component-driven, but the visual output is stubbornly unique.

**Key Characteristics:**
- Warm sage/olive color palette instead of conventional blues — earthy and approachable
- IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights
- Hidden brand orange (`#F54E00`) that only appears on hover interactions — a delightful surprise
- Hand-drawn hedgehog illustrations and playful imagery — deliberately anti-corporate
- Sage-tinted borders (`#bfc1b7`) and backgrounds (`#eeefe9`) creating a unified warm-green system
- Dark near-black CTAs (`#1e1f23`) with opacity-based hover states
- Content-heavy editorial layout — the site reads like a magazine, not a typical landing page
- Tailwind CSS + Radix UI + shadcn/ui component architecture


### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise, and Hand-drawn hedgehog illustrations and playful imagery — deliberately anti-corporate.
- Use PostHog Orange (#F54E00) as the highest-signal accent when color needs to carry emphasis.
- Let Sage Cream (#eeefe9) carry calmer title-safe zones and quieter data-support slides.
- Use Deep Olive (#23251d) for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

### Original Brand Palette

### Primary
- **Olive Ink** (`#4d4f46`): Primary text color — a distinctive olive-gray that gives all text a warm, earthy tone
- **Deep Olive** (`#23251d`): Link text and high-emphasis headings — near-black with green undertone
- **PostHog Orange** (`#F54E00`): Hidden brand accent — appears only on hover states, a vibrant orange that surprises

### Secondary & Accent
- **Amber Gold** (`#F7A501`): Secondary hover accent on dark buttons — warm gold that pairs with the orange
- **Gold Border** (`#b17816`): Special button borders — an amber-gold for featured CTAs
- **Focus Blue** (`#3b82f6`): Focus ring color (Tailwind default) — the only blue in the system, reserved for accessibility

### Surface & Background
- **Warm Parchment** (`#fdfdf8`): Primary page background — warm near-white with yellow-green undertone
- **Sage Cream** (`#eeefe9`): Input backgrounds, secondary surfaces — light sage tint
- **Light Sage** (`#e5e7e0`): Button backgrounds, tertiary surfaces — muted sage-green
- **Warm Tan** (`#d4c9b8`): Featured button backgrounds — warm tan/khaki for emphasis
- **Hover White** (`#f4f4f4`): Universal hover background state

### Neutrals & Text
- **Olive Ink** (`#4d4f46`): Primary body and UI text
- **Muted Olive** (`#65675e`): Secondary text, button labels on light backgrounds
- **Sage Placeholder** (`#9ea096`): Placeholder text, disabled states — warm sage-green
- **Sage Border** (`#bfc1b7`): Primary border color — olive-tinted gray for all borders
- **Light Border** (`#b6b7af`): Secondary border, toolbar borders — slightly darker sage

### Semantic & Accent
- **PostHog Orange** (`#F54E00`): Hover text accent — signals interactivity and brand personality
- **Amber Gold** (`#F7A501`): Dark button hover accent — warmth signal
- **Focus Blue** (`#3b82f6` at 50% opacity): Keyboard focus rings — accessibility-only color
- **Dark Text** (`#111827`): High-contrast link text — near-black for important links

### Gradient System
- No gradients on the marketing site — PostHog's visual language is deliberately flat and warm
- Depth is achieved through layered surfaces and border containment, not color transitions


### PPT-image Deployment

- Base canvas: prefer Sage Cream (#eeefe9) when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer Deep Olive (#23251d) when the deck needs cinematic weight or a chapter reset.
- Primary accent: PostHog Orange (#F54E00) should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

### Original Brand Typography

### Font Family
- **Display & Body**: `IBM Plex Sans Variable` — variable font (100–700+ weight range). Fallbacks: `IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New` — system monospace stack
- **Code Display**: `Source Code Pro` — with fallbacks: `Menlo, Consolas, Monaco`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | IBM Plex Sans Variable | 30px | 800 | 1.20 | -0.75px | Extra-bold, tight, maximum impact |
| Section Heading | IBM Plex Sans Variable | 36px | 700 | 1.50 | 0px | Large but generous line-height |
| Feature Heading | IBM Plex Sans Variable | 24px | 700 | 1.33 | 0px | Feature section titles |
| Card Heading | IBM Plex Sans Variable | 21.4px | 700 | 1.40 | -0.54px | Slightly unusual size (scaled) |
| Sub-heading | IBM Plex Sans Variable | 20px | 700 | 1.40 | -0.5px | Content sub-sections |
| Sub-heading Uppercase | IBM Plex Sans Variable | 20px | 700 | 1.40 | 0px | Uppercase transform for labels |
| Body Emphasis | IBM Plex Sans Variable | 19.3px | 600 | 1.56 | -0.48px | Semi-bold callout text |
| Label Uppercase | IBM Plex Sans Variable | 18px | 700 | 1.50 | 0px | Uppercase category labels |
| Body Semi | IBM Plex Sans Variable | 18px | 600 | 1.56 | 0px | Semi-bold body text |
| Body | IBM Plex Sans Variable | 16px | 400 | 1.50 | 0px | Standard reading text |
| Body Medium | IBM Plex Sans Variable | 16px | 500 | 1.50 | 0px | Medium-weight body |
| Body Relaxed | IBM Plex Sans Variable | 15px | 400 | 1.71 | 0px | Relaxed line-height for long reads |
| Nav / UI | IBM Plex Sans Variable | 15px | 600 | 1.50 | 0px | Navigation and UI labels |
| Caption | IBM Plex Sans Variable | 14px | 400–700 | 1.43 | 0px | Small text, various weights |
| Small Label | IBM Plex Sans Variable | 13px | 500–700 | 1.00–1.50 | 0px | Tags, badges, micro labels |
| Micro | IBM Plex Sans Variable | 12px | 400–700 | 1.33 | 0px | Smallest text, some uppercase |
| Code | Source Code Pro | 14px | 500 | 1.43 | 0px | Code snippets and terminal |

### Principles
- **Bold heading dominance**: Headings use 700–800 weight — PostHog's typography is confident and assertive, not whispery
- **Generous body line-heights**: Body text at 1.50–1.71 line-height creates extremely comfortable reading — the site is content-heavy and optimized for long sessions
- **Fractional sizes**: Several sizes (21.4px, 19.3px, 13.7px) suggest a fluid/scaled type system rather than fixed stops — likely computed from Tailwind's rem scale at non-standard base
- **Uppercase as category signal**: Bold uppercase labels (18px–20px weight 700) are used for product category headings — a magazine-editorial convention
- **Selective negative tracking**: Letter-spacing tightens on display text (-0.75px at 30px) but relaxes to 0px on body — headlines compress, body breathes


### PPT-image Type Deployment

- Use `IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

### Original UI Motifs

### Buttons
- **Dark Primary**: `#1e1f23` background, white text, 6px radius, `10px 12px` padding. Hover: opacity 0.7 with Amber Gold text. Active: opacity 0.8 with slight scale transform. The main CTA — dark and confident
- **Sage Light**: `#e5e7e0` background, Olive Ink (`#4d4f46`) text, 4px radius, `4px` padding. Hover: `#f4f4f4` bg with PostHog Orange text. Compact utility button
- **Warm Tan Featured**: `#d4c9b8` background, black text, no visible radius. Hover: same orange text flash. Featured/premium actions
- **Input-style**: `#eeefe9` background, Sage Placeholder (`#9ea096`) text, 4px radius, 1px `#b6b7af` border. Looks like a search/filter control
- **Near-white Ghost**: `#fdfdf8` background, Olive Ink text, 4px radius, transparent 1px border. Minimal presence
- **Hover pattern**: All buttons flash PostHog Orange (`#F54E00`) or Amber Gold (`#F7A501`) text on hover — the brand's signature interaction surprise

### Cards & Containers
- **Bordered Card**: Warm Parchment (`#fdfdf8`) or white background, 1px `#bfc1b7` border, 4px–6px radius — clean and minimal
- **Sage Surface Card**: `#eeefe9` background for secondary content containers
- **Shadow Card**: `0px 25px 50px -12px rgba(0, 0, 0, 0.25)` — a single deep shadow for elevated content (modals, dropdowns)
- **Hover**: Orange text flash on interactive cards — consistent with button behavior

### Inputs & Forms
- **Default**: `#eeefe9` background, `#9ea096` placeholder text, 1px `#b6b7af` border, 4px radius, `2px 0px 2px 8px` padding
- **Focus**: `#3b82f6` ring at 50% opacity (Tailwind blue focus ring)
- **Text color**: `#374151` for input values — darker than primary text for readability
- **Border variations**: Multiple border patterns — some inputs use compound borders (top, left, bottom-only)

### Navigation
- **Top nav**: Warm background, IBM Plex Sans at 15px weight 600
- **Dropdown menus**: Rich mega-menu structure with product categories
- **Link color**: Deep Olive (`#23251d`) for nav links, underline on hover
- **CTA**: Dark Primary button (#1e1f23) in the nav — "Get started - free"
- **Mobile**: Collapses to hamburger with simplified menu

### Image Treatment
- **Hand-drawn illustrations**: Hedgehog mascot and quirky illustrations — the signature visual element
- **Product screenshots**: UI screenshots embedded in device frames or clean containers
- **Action figures**: Playful product photography of hedgehog figurines — anti-corporate
- **Trust logos**: Enterprise logos (Airbus, GOV.UK) displayed in a muted trust bar
- **Aspect ratios**: Mixed — illustrations are irregular, screenshots are 16:9 or widescreen

### AI Chat Widget
- Floating PostHog AI assistant with speech bubble — an interactive product demo embedded in the marketing site


### PPT-image Asset Translation

#### Cover / Opening Hero

- Use PostHog's strongest visual cues as one large, unmistakable scene or object.
- Let PostHog Orange (#F54E00), Sage Cream (#eeefe9), and Deep Olive (#23251d) establish the hierarchy before adding any text.
- Pull attitude from Buttons, Cards & Containers, Inputs & Forms, and Navigation rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to PostHog.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: Sage Cream (#eeefe9) versus Deep Olive (#23251d), with PostHog Orange (#F54E00) reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA (Spacing System, Grid & Container, and Whitespace Philosophy) to create clean fields for charts, numerals, or callouts.
- Avoid hero subjects that fight the actual data layer.

#### System / Workflow Plate

- Convert the original component logic into presentation diagrams, route maps, or structural visuals rather than literal product UI.
- Keep the image designed, not tool-generated: large shapes, few node types, deliberate connectors, and brand-consistent type.
- Depth should follow Shadow Philosophy and Decorative Depth instead of generic infographic shadows.

#### Closing Poster

- Compress the deck's final judgment into one memorable frame.
- Use the same brand surfaces and accent hierarchy, but simplify harder than the cover.
- The closing image should resolve the story, not reopen complexity.

## 5. Layout Principles

### Original Layout DNA

### Spacing System
- **Base unit**: 8px
- **Scale**: 2px, 4px, 6px, 8px, 10px, 12px, 16px, 18px, 24px, 32px, 34px
- **Section padding**: 32px–48px vertical between sections (compact for a content-heavy site)
- **Card padding**: 4px–12px internal (notably compact)
- **Component gaps**: 4px–8px between related elements

### Grid & Container
- **Max width**: 1536px (largest breakpoint), with content containers likely 1200px–1280px
- **Column patterns**: Varied — single column for text content, 2-3 column grids for feature cards, asymmetric layouts for product demos
- **Breakpoints**: 13 defined — 1px, 425px, 482px, 640px, 768px, 767px, 800px, 900px, 1024px, 1076px, 1160px, 1280px, 1536px

### Whitespace Philosophy
- **Content-dense by design**: PostHog's site is information-rich — whitespace is measured, not lavish
- **Editorial pacing**: Content sections flow like a magazine with varied layouts keeping the eye moving
- **Illustrations as breathing room**: Hand-drawn hedgehog art breaks up dense content sections naturally

### Border Radius Scale
- **2px**: Small inline elements, tags (`span`)
- **4px**: Primary UI components — buttons, inputs, dropdowns, menu items (`button`, `div`, `combobox`)
- **6px**: Secondary containers — larger buttons, list items, card variants (`button`, `div`, `li`)
- **9999px**: Pill shape — badges, status indicators, rounded tags (`span`, `div`)


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
| Level 0 (Flat) | No shadow, warm parchment background | Page canvas, most surfaces |
| Level 1 (Border) | `1px solid #bfc1b7` (Sage Border) | Card containment, input borders, section dividers |
| Level 2 (Compound Border) | Multiple 1px borders on different sides | Input groupings, toolbar elements |
| Level 3 (Deep Shadow) | `0px 25px 50px -12px rgba(0, 0, 0, 0.25)` | Modals, floating elements, mega-menu dropdowns |

### Shadow Philosophy
PostHog's elevation system is remarkably minimal — only one shadow definition exists in the entire system. Depth is communicated through:
- **Border containment**: Sage-tinted borders (`#bfc1b7`) at 1px create gentle warm separation
- **Surface color shifts**: Moving from `#fdfdf8` to `#eeefe9` to `#e5e7e0` creates layered depth without shadows
- **The single shadow**: The one defined shadow (`0 25px 50px -12px`) is reserved for floating elements — modals, dropdowns, popovers. It's a deep, dramatic shadow that creates clear separation when needed

### Decorative Depth
- **Illustration layering**: Hand-drawn hedgehog art creates visual depth naturally
- **No gradients or glow**: The flat, warm surface system relies entirely on border and surface-color differentiation
- **No glassmorphism**: Fully opaque surfaces throughout


### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

### Original Guardrails

### Do
- Use the olive/sage color family (#4d4f46, #23251d, #bfc1b7) for text and borders — the warm green undertone is essential to the brand
- Flash PostHog Orange (#F54E00) on hover states — it's the hidden brand signature
- Use IBM Plex Sans at bold weights (700/800) for headings — the font carries technical credibility
- Keep body text at generous line-heights (1.50–1.71) — the content-heavy site demands readability
- Maintain the warm parchment background (#fdfdf8) — not pure white, never cold
- Use 4px border-radius for most UI elements — keep corners subtle and functional
- Include playful, hand-drawn illustration elements — the personality is the differentiator
- Apply opacity-based hover states (0.7 opacity) on dark buttons rather than color shifts

### Don't
- Use blue, purple, or typical tech-SaaS colors — PostHog's palette is deliberately olive/sage
- Add heavy shadows — the system uses one shadow for floating elements only; everything else uses borders
- Make the design look "polished" or "premium" in a conventional sense — PostHog's charm is its irreverent, scrappy energy
- Use tight line-heights on body text — the generous 1.50+ spacing is essential for the content-heavy layout
- Apply large border-radius (12px+) on cards — PostHog uses 4px–6px, keeping things tight and functional
- Remove the orange hover flash — it's a core interaction pattern, not decoration
- Replace illustrations with stock photography — the hand-drawn hedgehog art is the brand
- Use pure white (#ffffff) as page background — the warm sage-cream (#fdfdf8) tint is foundational


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
| Mobile Small | <425px | Single column, compact padding, stacked cards |
| Mobile | 425px–640px | Slight layout adjustments, larger touch targets |
| Tablet | 640px–768px | 2-column grids begin, nav partially visible |
| Tablet Large | 768px–1024px | Multi-column layouts, expanded navigation |
| Desktop | 1024px–1280px | Full layout, 3-column feature grids, expanded mega-menu |
| Large Desktop | 1280px–1536px | Max-width container, generous margins |
| Extra Large | >1536px | Centered container at max-width |

### Touch Targets
- Buttons: 4px–6px radius with `4px–12px` padding — compact but usable
- Nav links: 15px text at weight 600 with adequate padding
- Mobile: Hamburger menu with simplified navigation
- Inputs: Generous vertical padding for thumb-friendly forms

### Collapsing Strategy
- **Navigation**: Full mega-menu with dropdowns → hamburger menu on mobile
- **Feature grids**: 3-column → 2-column → single column stacked
- **Typography**: Display sizes reduce across breakpoints (30px → smaller)
- **Illustrations**: Scale within containers, some may hide on mobile for space
- **Section spacing**: Reduces proportionally while maintaining readability

### Image Behavior
- Illustrations scale responsively within containers
- Product screenshots maintain aspect ratios
- Trust logos reflow into multi-row grids on mobile
- AI chat widget may reposition or simplify on small screens


### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

### Original UI Prompt Reference

### Quick Color Reference
- Primary Text: Olive Ink (`#4d4f46`)
- Dark Text: Deep Olive (`#23251d`)
- Hover Accent: PostHog Orange (`#F54E00`)
- Dark CTA: Near-Black (`#1e1f23`)
- Button Surface: Light Sage (`#e5e7e0`)
- Page Background: Warm Parchment (`#fdfdf8`)
- Border: Sage Border (`#bfc1b7`)
- Placeholder: Sage Placeholder (`#9ea096`)

### Example Component Prompts
- "Create a hero section on warm parchment background (#fdfdf8) with 30px IBM Plex Sans heading at weight 800, line-height 1.20, letter-spacing -0.75px, olive ink text (#4d4f46), and a dark CTA button (#1e1f23, 6px radius, white text, opacity 0.7 on hover)"
- "Design a feature card with #fdfdf8 background, 1px #bfc1b7 border, 4px radius, IBM Plex Sans heading at 20px weight 700, and 16px body text at weight 400 with 1.50 line-height in olive ink (#4d4f46)"
- "Build a navigation bar with warm background, IBM Plex Sans links at 15px weight 600 in deep olive (#23251d), underline on hover, and a dark CTA button (#1e1f23) at the right"
- "Create a button group: primary dark (#1e1f23, white text, 6px radius), secondary sage (#e5e7e0, #4d4f46 text, 4px radius), and ghost/text button — all flash #F54E00 orange text on hover"
- "Design an input field with #eeefe9 background, 1px #b6b7af border, 4px radius, #9ea096 placeholder text, focus ring in #3b82f6 at 50% opacity"

### Iteration Guide
When refining existing screens generated with this design system:
1. Verify the background is warm parchment (#fdfdf8) not pure white — the sage-cream warmth is essential
2. Check that all text uses the olive family (#4d4f46, #23251d) not pure black or neutral gray
3. Ensure hover states flash PostHog Orange (#F54E00) — if hovering feels bland, you're missing this
4. Confirm borders use sage-tinted gray (#bfc1b7) not neutral gray — warmth runs through every element
5. The overall tone should feel like a fun, scrappy startup wiki — never corporate-polished or sterile


### PPT-image Quick Reference

- Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
- Display voice: `IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial`
- Body / label voice: `IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial`
- Primary accent: PostHog Orange (#F54E00)
- Light surface anchor: Sage Cream (#eeefe9)
- Dark surface anchor: Deep Olive (#23251d)
- Signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise, and Hand-drawn hedgehog illustrations and playful imagery — deliberately anti-corporate
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

```text
Create a presentation cover image for a presentation inspired by PostHog.
Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
Use IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial as the display-type reference and IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial for any short in-image labels.
Keep the palette anchored in Sage Cream (#eeefe9), Deep Olive (#23251d), and PostHog Orange (#F54E00).
Preserve these signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, and Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise.
Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Section Divider

```text
Create a section divider image for a presentation inspired by PostHog.
Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
Use IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial as the display-type reference and IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial for any short in-image labels.
Keep the palette anchored in Sage Cream (#eeefe9), Deep Olive (#23251d), and PostHog Orange (#F54E00).
Preserve these signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, and Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise.
Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Concept Visualization

```text
Create a concept visualization image for a presentation inspired by PostHog.
Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
Use IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial as the display-type reference and IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial for any short in-image labels.
Keep the palette anchored in Sage Cream (#eeefe9), Deep Olive (#23251d), and PostHog Orange (#F54E00).
Preserve these signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, and Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise.
Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Comparison Plate

```text
Create a comparison image for a presentation inspired by PostHog.
Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
Use IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial as the display-type reference and IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial for any short in-image labels.
Keep the palette anchored in Sage Cream (#eeefe9), Deep Olive (#23251d), and PostHog Orange (#F54E00).
Preserve these signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, and Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise.
Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Data Backdrop

```text
Create a data-support backdrop image for a presentation inspired by PostHog.
Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
Use IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial as the display-type reference and IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial for any short in-image labels.
Keep the palette anchored in Sage Cream (#eeefe9), Deep Olive (#23251d), and PostHog Orange (#F54E00).
Preserve these signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, and Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise.
This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```

#### Closing Poster

```text
Create a closing poster image for a presentation inspired by PostHog.
Brand mood: PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate.
Use IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial as the display-type reference and IBM Plex Sans Variable — variable font (100–700+ weight range). Fallbacks: IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial for any short in-image labels.
Keep the palette anchored in Sage Cream (#eeefe9), Deep Olive (#23251d), and PostHog Orange (#F54E00).
Preserve these signature cues: Warm sage/olive color palette instead of conventional blues — earthy and approachable, IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights, and Hidden brand orange (#F54E00) that only appears on hover interactions — a delightful surprise.
Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
```
