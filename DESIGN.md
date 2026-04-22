# PPT Image DESIGN.md

This `DESIGN.md` adapts the `awesome-design-md` structure from website UI generation to presentation-image generation.

Use it when the goal is to generate visual assets for slides, not full slides, not HTML pages, and not product UI.

The image is a slide asset.
It should strengthen the slide's thesis, leave room for editable text, and remain legible in a live presentation, exported PDF, and thumbnail view.

Unless explicitly requested otherwise, default to:

- horizontal `16:9`
- `3840x2160` or higher
- one dominant focal point
- 25% to 35% clean text-safe space
- minimal or no baked-in text

## 1. Visual Theme & Atmosphere

PPT images should feel presentation-first, not web-first.

They are not decorative fillers.
They are visual arguments.

Every image must communicate one slide-level thesis at a glance.
If the viewer cannot understand the emotional or conceptual direction within one second, the image is too vague for presentation use.

The overall atmosphere should sit closer to:

- editorial poster
- concept visualization
- structured visual essay
- cinematic still with information discipline

It should sit farther away from:

- stock-photo business scenes
- generic SaaS illustrations
- overly literal icon collages
- noisy "AI art wallpaper" aesthetics

Series consistency matters more than single-image cleverness.
Across a deck, the images should feel like they belong to one visual system through repeated choices in:

- palette
- light direction
- texture
- geometry
- framing
- contrast behavior

**Key Characteristics**

- one image = one thesis
- strong thumbnail readability at small sizes
- obvious focal hierarchy from back-row viewing distance
- controlled negative space for slide titles and callouts
- high intentionality, low randomness
- premium but not flashy
- vivid enough to anchor a slide, restrained enough to support overlaid content

## 2. Color Palette & Roles

Use a restrained presentation palette.
Most decks should live on 1 base mode and 1 accent family, not six unrelated colors.

### Core Neutrals

- **Paper White** (`#F6F1E8`)
  Warm off-white for light-background decks, charts, paper-like sections, and editorial calm.
- **Ink Black** (`#111317`)
  Primary dark anchor for dark decks, typography contrast areas, and cinematic negative space.
- **Graphite** (`#2A2F36`)
  Neutral support tone for surfaces, diagrams, shadows, and low-noise structure.
- **Stone Gray** (`#A8A29A`)
  Secondary neutral for separators, subtle texture, thin annotation areas, and low-emphasis support.

### Signal Accents

- **Steel Blue** (`#345D7E`)
  Rational, technical accent for data, systems, and explanatory slides.
- **Signal Orange** (`#D96A31`)
  Energy accent for transformation, motion, change, and urgency.
- **Signal Red** (`#B6422E`)
  Reserved for warning, conflict, fracture, loss, or strategic tension.
- **Muted Gold** (`#B08A46`)
  Premium accent for summary posters, milestones, and high-value emphasis.

### Functional Rules

- Use 1 accent as the deck's dominant energy source.
- A second accent is allowed only when the slide needs contrast or comparison.
- Backgrounds should stay calmer than the main focal object.
- Text-safe areas should have lower contrast noise than hero areas.
- If a deck already has a brand color, map that brand color into the accent role instead of introducing extra saturation.

### Gradient Rules

- Prefer restrained gradients with 2 to 3 stops maximum.
- Gradients should guide depth or mood, not become the subject by themselves.
- Avoid default purple-blue "AI gradient" treatment unless the topic explicitly demands it.

## 3. Typography Rules

Typography inside generated PPT images is optional, not mandatory.

In most cases, the best slide image has:

- no text
- or one short label
- or one oversized number
- or one short chapter marker

Do not bake full slide titles, long Chinese paragraphs, bullet lists, or explanatory body copy into the image.
That text belongs to the editable slide layer.

### Text-In-Image Hierarchy

| Role | Suggested Character | Length | Use |
|------|----------------------|--------|-----|
| Hero Word | condensed grotesk / bold editorial sans | 1 to 4 words | cover and chapter images |
| Section Marker | uppercase label / wide tracking | 1 to 2 words | divider slides |
| Data Numeral | mono or grotesk numeral | 1 number | stat-driven slides |
| Diagram Label | clean sans / high contrast | 1 to 3 words | concept plates and system visuals |
| Micro Label | only when necessary | very short | annotations that survive projection |

### Rules

- If text is used, it must survive projection and screenshot compression.
- Prefer large labels over multiple small labels.
- English all-caps and large numerals are safer than dense mixed-language microtext.
- Chinese text is allowed only when it is short, large, and essential.
- Do not simulate perfect font accuracy as the primary design goal; prioritize hierarchy, legibility, and tone.

## 4. Component Stylings

In this PPT-image version, "components" means slide asset types rather than web UI controls.

### Cover / Opening Hero

- Purpose: stop attention and establish the deck's core emotional premise
- Composition: one dominant hero object or scene, one supporting layer, one clear title-safe region
- Visual behavior: strongest contrast and clearest identity in the whole deck
- Avoid: evenly spread collage, tiny details everywhere, poster text filling the frame

### Section Divider

- Purpose: reset rhythm between chapters
- Composition: simplified subject, more negative space, clearer geometry than the cover
- Visual behavior: acts like a breath, not a second cover
- Avoid: narrative overload and heavy detail density

### Concept Visualization

- Purpose: explain one abstract idea through one visual metaphor
- Composition: one metaphor + one structural support layer
- Visual behavior: faster than a paragraph, cleaner than an infographic
- Avoid: explaining five ideas in one frame

### Comparison Plate

- Purpose: visualize tension, tradeoff, before/after, or two competing systems
- Composition: split field, mirrored objects, or asymmetric confrontation
- Visual behavior: the contrast should be readable without captions
- Avoid: equal clutter on both sides or generic "left bad/right good" cliches

### Data Backdrop

- Purpose: support a stat or chart-heavy slide without overpowering the data layer
- Composition: subdued structure, clean title area, calm edges
- Visual behavior: more architectural than illustrative
- Avoid: intense focal subjects that fight the chart

### System / Workflow Plate

- Purpose: visualize flow, hierarchy, routing, sequence, or architecture
- Composition: large blocks, deliberate connectors, few node types
- Visual behavior: should feel designed, not like a screenshot of a diagram tool
- Avoid: micro labels, crowded arrows, and literal software-window chrome

### Closing Poster

- Purpose: compress the deck's final judgment into one memorable image
- Composition: bold, simple, emotionally resolved
- Visual behavior: summary energy, not new information
- Avoid: reopening complexity at the end

## 5. Layout Principles

PPT images must be designed with slide overlay in mind.

### Framing

- Default aspect ratio is `16:9`.
- Keep the most important subject matter inside the central 80% width and 80% height.
- Reserve a clean title-safe zone on the left, right, or top depending on slide layout.
- Let the safe zone be visibly calmer than the hero zone.

### Hierarchy

- one dominant focal point
- one secondary support layer
- one background atmosphere layer

If the image has four equally loud focal points, it will usually fail on a slide.

### Density

- cover slides can carry moderate visual density
- body slides should be cleaner
- data-support images should be the calmest
- divider slides should be simpler than body slides

### Spatial Rules

- edges should tolerate mild cropping
- avoid placing critical faces, symbols, or labels near the outer 8% margin
- asymmetry is preferred when it creates cleaner text placement
- symmetry is acceptable only when the concept itself is confrontation or ritual

### Presentation Rule

The image must work from three distances:

- full-screen presentation
- exported PDF page
- thumbnail in slide sorter view

## 6. Depth & Elevation

Depth in PPT images should come from planes, light, atmosphere, and material contrast, not from gimmicky 3D effects.

### Preferred Depth Signals

- foreground / midground / background separation
- directional light
- controlled shadow edges
- atmospheric haze or subtle gradient falloff
- texture contrast between matte and reflective surfaces
- restrained film grain or paper grain

### Material Guidance

- matte paper, brushed metal, smoked glass, ink, fabric, concrete, and soft light all work well
- use glossy glassmorphism only when the topic explicitly needs digital futurism
- avoid plastic, toy-like, over-rendered 3D icon surfaces in serious decks

### Elevation Logic

- foreground carries emotion
- midground carries structure
- background carries tone

Do not let background texture become louder than the message.

## 7. Do's and Don'ts

### Do

- translate each slide into a single sentence before generating the image
- choose the image type from the slide role, not from the overall deck topic
- keep a recurring visual language across the whole deck
- design with title overlay, subtitle overlay, and crop safety in mind
- prefer fewer stronger elements over many average elements
- make the image help the slide communicate faster

### Don't

- don't generate full-slide text posters unless explicitly requested
- don't use generic office people, handshakes, laptops-on-table stock scenes
- don't fill the canvas with tiny symbolic objects
- don't default to neon purple, cyberpunk rain, or abstract AI-glow wallpaper
- don't make every slide image equally loud
- don't embed complex charts, dense UI screenshots, or unreadable tiny labels into the art
- don't confuse "visually rich" with "visually noisy"

## 8. Responsive Behavior

For presentation images, "responsive" means crop resilience and export behavior rather than browser breakpoints.

### Master Output

- preferred master size: `3840x2160`
- acceptable fallback: `1920x1080`
- use horizontal composition unless the deck explicitly needs portrait or social variants

### Crop Safety

- critical visual meaning must survive a mild crop to `4:3`
- keep essential subject matter away from extreme corners
- if the image contains labels, they must survive safe-area cropping

### Variant Guidance

When a slide's layout is unknown, generate one of these safer variants:

- left-safe: focal subject on right, text-safe area on left
- right-safe: focal subject on left, text-safe area on right
- center-safe: focal subject central but with top-safe negative space

### Export Behavior

- avoid tiny detail that disappears in PDF export
- avoid ultra-dark shadow regions that crush into black on projectors
- avoid thin low-contrast lines that vanish in compressed screenshots
- if the slide needs heavy overlay copy, request a calmer second version with more negative space

## 9. Agent Prompt Guide

### Quick Reference

- slide role first
- slide thesis second
- safe zone third
- style direction fourth
- banned elements always explicit

### Core Prompt Skeleton

```text
Create a [slide role] image for a presentation.
Topic: [topic].
Slide thesis: [one-sentence judgment].
Visual direction: editorial, presentation-first, high signal, not stock.
Composition: one dominant focal point, one supporting layer, clean [left/right/top] title-safe zone.
Aspect ratio: 16:9 horizontal, 4K.
Palette: [base colors] with [accent color].
Texture and depth: [grain/material/light direction].
Text in image: minimal or none. If needed, only [short label / big numeral / chapter marker].
Series consistency: match the deck's existing palette, lighting, geometry, and contrast behavior.
Avoid: stock office scenes, generic SaaS illustration, tiny labels, neon purple AI wallpaper, clutter, watermark.
```

### Cover Prompt Template

```text
Create a presentation cover image.
The slide thesis is: [thesis].
The image should stop attention in one second and explain the deck's main conflict at a glance.
Use one dominant hero subject, cinematic but controlled composition, and a clean top-left title-safe zone.
Make it feel like an editorial poster rather than a movie poster or startup ad.
16:9 horizontal, 4K, minimal text, strong thumbnail readability.
```

### Section Divider Prompt Template

```text
Create a section divider image for a presentation chapter.
The chapter theme is: [theme].
Use a simplified visual language, stronger negative space, and a cleaner composition than the cover.
The image should feel like a reset in rhythm, not another busy hero scene.
Leave a large [left/right/top] safe zone for the chapter title.
16:9 horizontal, 4K.
```

### Concept Visualization Prompt Template

```text
Create a concept visualization for a presentation slide.
Slide thesis: [thesis].
Translate the abstract idea into one clear visual metaphor.
Do not create an infographic, dashboard, or icon soup.
Use one metaphorical scene plus one structural support layer.
Leave room for slide text overlay.
16:9 horizontal, 4K.
```

### Comparison Prompt Template

```text
Create a comparison image for a presentation slide.
Compare: [A] versus [B].
The difference should be obvious even without captions.
Use a split composition or asymmetric confrontation with a clean title-safe zone.
Avoid cliche before/after stock imagery.
16:9 horizontal, 4K.
```

### Closing Poster Prompt Template

```text
Create a closing poster image for the final slide of a presentation.
Final judgment: [judgment].
The image should feel resolved, memorable, and compress the whole deck into one emotional frame.
Use bold simplicity, controlled contrast, and generous negative space for a short final statement.
Do not introduce new complexity.
16:9 horizontal, 4K.
```

### Working Rule For Agents

Before generating any image, convert the slide into this checklist:

1. What is the slide role?
2. What is the single sentence thesis?
3. Where is the safe zone?
4. What should the viewer feel in one second?
5. What must be avoided?

If any of these are missing, infer them before generating.
