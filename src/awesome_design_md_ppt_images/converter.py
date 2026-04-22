from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s*$", flags=re.MULTILINE)
COLOR_RE = re.compile(r"^- \*\*(.+?)\*\* \(`([^`]+)`\):\s*(.+)$", flags=re.MULTILINE)
FONT_RE = re.compile(r"^- \*\*(.+?)\*\*:\s*(.+)$", flags=re.MULTILINE)
H3_RE = re.compile(r"^###\s+(.+?)\s*$", flags=re.MULTILINE)

NEUTRAL_KEYWORDS = {
    "white",
    "black",
    "gray",
    "grey",
    "charcoal",
    "graphite",
    "silver",
    "stone",
    "sand",
    "ivory",
    "parchment",
    "cream",
    "canvas",
    "surface",
    "dark",
    "light",
    "near black",
    "near-black",
    "warm dark",
    "deep dark",
    "mid gray",
    "frost",
    "border",
    "paper",
    "ash",
    "pewter",
    "cloud",
    "carbon",
    "void",
    "navy",
}


@dataclass(frozen=True)
class ColorToken:
    name: str
    value: str
    description: str

    @property
    def summary(self) -> str:
        return f"{self.name} ({self.value})"


@dataclass(frozen=True)
class FontPair:
    display: str
    body: str


def strip_md(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.strip()


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", strip_md(text)).strip()


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Unknown Design System"


def brand_from_title(title: str) -> str:
    match = re.match(r"Design System Inspired by (.+)", title, flags=re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return title.strip()


def parse_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(text))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        sections[f"{match.group(1)}. {match.group(2)}"] = text[start:end].strip()
    return sections


def get_section(sections: dict[str, str], number: int) -> str:
    prefix = f"{number}."
    for key, value in sections.items():
        if key.startswith(prefix):
            return value
    raise KeyError(f"Missing section {number}")


def first_paragraphs(text: str, count: int = 2) -> list[str]:
    parts = [part.strip() for part in text.split("\n\n") if part.strip()]
    paragraphs: list[str] = []
    for part in parts:
        if part.startswith(("- ", "###", "|", "**")):
            continue
        paragraphs.append(normalize_space(part))
        if len(paragraphs) >= count:
            break
    return paragraphs


def first_sentence(text: str) -> str:
    paragraphs = first_paragraphs(text, count=1)
    if not paragraphs:
        return "Keep the source brand's original visual attitude intact."
    match = re.match(r"(.+?[.!?])(?:\s|$)", paragraphs[0])
    return match.group(1).strip() if match else paragraphs[0]


def extract_key_bullets(text: str, limit: int = 5) -> list[str]:
    lines = text.splitlines()
    bullets: list[str] = []
    collecting = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("**Key Characteristics"):
            collecting = True
            continue
        if collecting:
            if stripped.startswith("- "):
                bullets.append(strip_md(stripped[2:].strip()))
            elif stripped and not stripped.startswith("- "):
                break
    if bullets:
        return bullets[:limit]

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(strip_md(stripped[2:].strip()))
        if len(bullets) >= limit:
            break
    return bullets[:limit]


def parse_colors(text: str) -> list[ColorToken]:
    return [
        ColorToken(
            name=strip_md(match.group(1)),
            value=match.group(2).strip(),
            description=normalize_space(match.group(3)),
        )
        for match in COLOR_RE.finditer(text)
    ]


def score_color(token: ColorToken, mode: str) -> int:
    haystack = f"{token.name.lower()} {token.description.lower()}"
    score = 0
    if mode == "light":
        for word in ("white", "ivory", "cream", "parchment", "light", "paper", "canvas", "mint", "sand", "surface"):
            if word in haystack:
                score += 2
    elif mode == "dark":
        for word in ("black", "dark", "charcoal", "graphite", "carbon", "void", "navy", "near-black", "near black", "deep"):
            if word in haystack:
                score += 2
    elif mode == "accent":
        for word in ("brand", "accent", "cta", "primary", "electric", "green", "blue", "red", "orange", "pink", "gold", "purple", "lime", "yellow"):
            if word in haystack:
                score += 2
        if not any(word in haystack for word in NEUTRAL_KEYWORDS):
            score += 1
    return score


def pick_color(tokens: list[ColorToken], mode: str, fallback_index: int = 0) -> ColorToken | None:
    if not tokens:
        return None
    ranked = sorted(tokens, key=lambda token: (score_color(token, mode), -tokens.index(token)), reverse=True)
    choice = ranked[0]
    if score_color(choice, mode) <= 0:
        return tokens[min(fallback_index, len(tokens) - 1)]
    return choice


def parse_fonts(text: str) -> FontPair:
    def clean_font_value(value: str) -> str:
        value = strip_md(value)
        value = re.split(r"\s+[鈥?]\s+", value, maxsplit=1)[0].strip()
        value = re.sub(r",\s*with fallback:\s*", " / fallback: ", value, flags=re.IGNORECASE)
        return value

    fonts = [(strip_md(match.group(1)).lower(), clean_font_value(match.group(2))) for match in FONT_RE.finditer(text)]
    display = ""
    body = ""
    for label, value in fonts:
        if not display and any(word in label for word in ("display", "headline", "title", "hero")):
            display = value
        if not body and any(word in label for word in ("body", "text/ui", "body / ui", "body/ui", "text", "ui")):
            body = value
    if not display and fonts:
        display = fonts[0][1]
    if not body and len(fonts) > 1:
        body = fonts[1][1]
    if not body:
        body = display or "System Sans"
    if not display:
        display = body
    return FontPair(display=display, body=body)


def subheadings(text: str, limit: int = 6) -> list[str]:
    return [strip_md(match.group(1)) for match in H3_RE.finditer(text)][:limit]


def compact_list(items: Iterable[str], limit: int = 3) -> str:
    cleaned = [normalize_space(item) for item in items if normalize_space(item)]
    if not cleaned:
        return "the source brand's strongest visual cues"
    trimmed = cleaned[:limit]
    if len(trimmed) == 1:
        return trimmed[0]
    if len(trimmed) == 2:
        return f"{trimmed[0]} and {trimmed[1]}"
    return ", ".join(trimmed[:-1]) + f", and {trimmed[-1]}"


def blockquote_section(title: str, body: str) -> str:
    return f"### {title}\n\n{body.strip()}\n"


def wrap_codeblock(text: str) -> str:
    return "```text\n" + text.strip() + "\n```"


def build_prompt_block(
    brand: str,
    mood: str,
    display_font: str,
    body_font: str,
    accent: str,
    light_surface: str,
    dark_surface: str,
    cues: list[str],
    role: str,
    body: str,
) -> str:
    cue_line = compact_list(cues, limit=3)
    prompt = f"""
Create a {role} for a presentation inspired by {brand}.
Brand mood: {mood}
Use {display_font} as the display-type reference and {body_font} for any short in-image labels.
Keep the palette anchored in {light_surface}, {dark_surface}, and {accent}.
Preserve these signature cues: {cue_line}.
{body}
Always leave a clean title-safe zone, keep the image readable in thumbnail view, and avoid generic stock scenes or literal webpage screenshots unless the slide explicitly needs product UI.
"""
    return wrap_codeblock(prompt)


def relative_source_reference(source_path: Path, project_root: Path | None) -> str:
    if project_root is not None:
        try:
            return source_path.relative_to(project_root).as_posix()
        except ValueError:
            pass
    return source_path.as_posix()


def generate_ppt_image_design(source_path: Path, project_root: Path | None = None, generated_on: date | None = None) -> str:
    generated_on = generated_on or date.today()
    text = source_path.read_text(encoding="utf-8")
    title = extract_title(text)
    brand = brand_from_title(title)
    sections = parse_sections(text)

    sec1 = get_section(sections, 1)
    sec2 = get_section(sections, 2)
    sec3 = get_section(sections, 3)
    sec4 = get_section(sections, 4)
    sec5 = get_section(sections, 5)
    sec6 = get_section(sections, 6)
    sec7 = get_section(sections, 7)
    sec8 = get_section(sections, 8)
    sec9 = get_section(sections, 9)

    mood = first_sentence(sec1)
    key_bullets = extract_key_bullets(sec1)
    colors = parse_colors(sec2)
    accent = pick_color(colors, "accent", fallback_index=0)
    light_surface = pick_color(colors, "light", fallback_index=1)
    dark_surface = pick_color(colors, "dark", fallback_index=0)
    fonts = parse_fonts(sec3)
    ui_motifs = subheadings(sec4, limit=5)
    layout_motifs = subheadings(sec5, limit=4)
    depth_motifs = subheadings(sec6, limit=4)

    accent_text = accent.summary if accent else "the primary brand accent"
    light_text = light_surface.summary if light_surface else "the lightest brand surface"
    dark_text = dark_surface.summary if dark_surface else "the darkest brand surface"
    motif_line = compact_list(key_bullets or ui_motifs, limit=4)
    ui_motif_line = compact_list(ui_motifs, limit=4)
    layout_line = compact_list(layout_motifs, limit=3)
    depth_line = compact_list(depth_motifs, limit=3)
    source_rel = relative_source_reference(source_path, project_root)

    return f"""# PPT-image Design System Inspired by {brand}

This file adapts the original web/UI-focused design system into a presentation-image system for slides.
Use it to generate cover art, chapter dividers, concept visuals, comparison plates, system diagrams, data backdrops, and closing posters that still feel unmistakably {brand}.

Source reference: `{source_rel}`
Adaptation date: `{generated_on.isoformat()}`

## 1. Visual Theme & Atmosphere

This PPT-image adaptation keeps {brand}'s brand DNA intact, but compresses it into slide-ready visuals instead of webpage UI.
The first priority is to preserve the original atmosphere: {mood}
The second priority is to make every image behave like a presentation asset: one slide thesis, one dominant focal point, and enough calm space for editable overlay text.

{blockquote_section("Original Brand DNA", sec1)}

### PPT-image Translation

- Treat every image as a slide asset, not a webpage screenshot.
- Preserve the brand's strongest cues: {motif_line}.
- Use {accent_text} as the highest-signal accent when color needs to carry emphasis.
- Let {light_text} carry calmer title-safe zones and quieter data-support slides.
- Use {dark_text} for cinematic divider slides, closing posters, or contrast-heavy cover moments.
- Keep 25% to 35% of the frame visibly calmer than the hero area so the slide layer can hold live text.
- When in doubt, choose one dominant subject, one support layer, and one background atmosphere layer instead of recreating dense UI layouts.

## 2. Color Palette & Roles

{blockquote_section("Original Brand Palette", sec2)}

### PPT-image Deployment

- Base canvas: prefer {light_text} when the deck needs editorial calm or readable overlay copy.
- Bold contrast canvas: prefer {dark_text} when the deck needs cinematic weight or a chapter reset.
- Primary accent: {accent_text} should carry the strongest callout, hero focal area, or high-signal data accent.
- Chart and callout rule: stay inside the original palette above; do not import generic presentation blues or purples if they are not already part of the brand.
- Safe-zone rule: overlay areas should be one contrast step quieter than the hero area.
- Series rule: the same accent/surface hierarchy should repeat across cover, divider, body images, and closing slides so the deck reads as one system.

## 3. Typography Rules

{blockquote_section("Original Brand Typography", sec3)}

### PPT-image Type Deployment

- Use `{fonts.display}` as the reference voice for cover words, chapter titles, or one-line in-image headlines when baked text is necessary.
- Use `{fonts.body}` for labels, short annotations, numerals, or tiny UI-like callouts inside the art.
- Do not bake full slide titles, speaker notes, or body paragraphs into generated images.
- Favor one hero word, one short divider title, one oversized number, or 1 to 3 diagram labels that can survive projection.
- Preserve the original brand's weight, tracking, and casing personality instead of flattening everything into generic presentation typography.

## 4. Component Stylings

{blockquote_section("Original UI Motifs", sec4)}

### PPT-image Asset Translation

#### Cover / Opening Hero

- Use {brand}'s strongest visual cues as one large, unmistakable scene or object.
- Let {accent_text}, {light_text}, and {dark_text} establish the hierarchy before adding any text.
- Pull attitude from {ui_motif_line} rather than recreating literal buttons, nav bars, or forms.
- Keep the cover readable in thumbnail view and leave one obvious title-safe zone.

#### Section Divider

- Simplify the composition relative to the cover.
- Keep the brand mood intact, but reduce detail density so the divider feels like a chapter reset rather than a second homepage hero.
- Reuse the same material and depth language instead of inventing a new visual style mid-deck.

#### Concept Visualization

- Translate abstract ideas into one visual metaphor that still feels native to {brand}.
- Borrow the brand's surface language, shape logic, and spacing restraint from the original system above.
- Avoid icon soup, dashboard screenshots, or five competing metaphors in one frame.

#### Comparison Plate

- When the slide is about contrast, use split composition, confrontation, or mirrored structure without abandoning the brand system.
- Let the palette do part of the comparison work: {light_text} versus {dark_text}, with {accent_text} reserved for the decisive signal.
- Keep both sides visually disciplined so the comparison reads at a glance.

#### Data Backdrop

- Data-support images should be calmer than cover or divider art.
- Use the brand's layout and spacing DNA ({layout_line}) to create clean fields for charts, numerals, or callouts.
- Avoid hero subjects that fight the actual data layer.

#### System / Workflow Plate

- Convert the original component logic into presentation diagrams, route maps, or structural visuals rather than literal product UI.
- Keep the image designed, not tool-generated: large shapes, few node types, deliberate connectors, and brand-consistent type.
- Depth should follow {depth_line} instead of generic infographic shadows.

#### Closing Poster

- Compress the deck's final judgment into one memorable frame.
- Use the same brand surfaces and accent hierarchy, but simplify harder than the cover.
- The closing image should resolve the story, not reopen complexity.

## 5. Layout Principles

{blockquote_section("Original Layout DNA", sec5)}

### PPT-image Layout Translation

- Default output: `16:9` horizontal, ideally `3840x2160`.
- Keep meaning-critical content inside the central 80% width and height so mild crop or projector overscan does not break the slide.
- Translate the brand's spacing philosophy above into image composition rather than scroll rhythm.
- Reuse the original radius/edge discipline inside objects, cards, frames, or image masks.
- Let asymmetry create cleaner title-safe zones when possible; use symmetry only when the concept itself is ceremonial, confrontational, or product-showroom centered.

## 6. Depth & Elevation

{blockquote_section("Original Depth System", sec6)}

### PPT-image Depth Translation

- Use the same elevation language above in image form: hero subject, support plane, background atmosphere.
- Preserve the brand's native depth behavior instead of defaulting to generic 3D gloss or floating glass panels.
- If the original system is flat, keep slide art flatter and more graphic.
- If the original system uses rings, glow, or border-defined depth, let those cues appear in the image edges, frames, and callout objects.

## 7. Do's and Don'ts

{blockquote_section("Original Guardrails", sec7)}

### PPT-image Guardrails

- Do preserve the original mood before adding presentation convenience.
- Do generate from the slide thesis, not from the overall deck topic alone.
- Do leave room for editable slide text instead of baking everything into the image.
- Do keep one dominant idea per frame.
- Don't turn every slide into a homepage hero.
- Don't import off-brand gradients, stock photography tropes, or default AI wallpaper aesthetics.
- Don't bake unreadable microtext, fake dashboards, or dense UI chrome into supporting images unless the slide explicitly needs product UI.

## 8. Responsive Behavior

{blockquote_section("Original UI Responsiveness", sec8)}

### PPT-image Crop & Export Behavior

- Treat responsiveness as crop resilience, PDF export resilience, and projector readability.
- Generate the master in `16:9`, but keep essential meaning safe under a mild crop to `4:3`.
- Prepare left-safe, right-safe, or center-safe variants when the final slide layout is not locked.
- Avoid placing critical labels, faces, or symbols near the outer 8% margins.
- If a deck will carry heavy overlay copy, request a calmer variant with more negative space.

## 9. Agent Prompt Guide

{blockquote_section("Original UI Prompt Reference", sec9)}

### PPT-image Quick Reference

- Brand mood: {mood}
- Display voice: `{fonts.display}`
- Body / label voice: `{fonts.body}`
- Primary accent: {accent_text}
- Light surface anchor: {light_text}
- Dark surface anchor: {dark_text}
- Signature cues: {compact_list(key_bullets, limit=4)}
- Avoid: literal webpage screenshots, unreadable body copy baked into the art, generic stock scenes, and off-brand accents

### PPT-image Prompt Templates

#### Cover / Opening Hero

{build_prompt_block(
    brand=brand,
    mood=mood,
    display_font=fonts.display,
    body_font=fonts.body,
    accent=accent_text,
    light_surface=light_text,
    dark_surface=dark_text,
    cues=key_bullets or ui_motifs,
    role="presentation cover image",
    body="Slide thesis: [fill in]. Use one dominant subject, a cinematic but controlled composition, and a clean [left/right/top] title-safe zone. Make the frame feel like the brand at first glance, even before any text is added.",
)}

#### Section Divider

{build_prompt_block(
    brand=brand,
    mood=mood,
    display_font=fonts.display,
    body_font=fonts.body,
    accent=accent_text,
    light_surface=light_text,
    dark_surface=dark_text,
    cues=key_bullets or ui_motifs,
    role="section divider image",
    body="Chapter theme: [fill in]. Reduce detail density compared with the cover, keep more negative space, and make the image feel like a chapter reset rather than a second homepage hero.",
)}

#### Concept Visualization

{build_prompt_block(
    brand=brand,
    mood=mood,
    display_font=fonts.display,
    body_font=fonts.body,
    accent=accent_text,
    light_surface=light_text,
    dark_surface=dark_text,
    cues=key_bullets or ui_motifs,
    role="concept visualization image",
    body="Slide thesis: [fill in]. Translate the abstract idea into one clear visual metaphor that still belongs to the brand system. Do not create an infographic or icon collage.",
)}

#### Comparison Plate

{build_prompt_block(
    brand=brand,
    mood=mood,
    display_font=fonts.display,
    body_font=fonts.body,
    accent=accent_text,
    light_surface=light_text,
    dark_surface=dark_text,
    cues=key_bullets or ui_motifs,
    role="comparison image",
    body="Compare [A] versus [B]. Make the difference obvious without captions. Use split composition or asymmetric confrontation, and keep the comparison inside the original brand palette.",
)}

#### Data Backdrop

{build_prompt_block(
    brand=brand,
    mood=mood,
    display_font=fonts.display,
    body_font=fonts.body,
    accent=accent_text,
    light_surface=light_text,
    dark_surface=dark_text,
    cues=key_bullets or layout_motifs,
    role="data-support backdrop image",
    body="This image supports a chart or big number slide. Keep it calmer than a cover image, leave generous negative space, and let surfaces/structure support the data instead of overpowering it.",
)}

#### Closing Poster

{build_prompt_block(
    brand=brand,
    mood=mood,
    display_font=fonts.display,
    body_font=fonts.body,
    accent=accent_text,
    light_surface=light_text,
    dark_surface=dark_text,
    cues=key_bullets or ui_motifs,
    role="closing poster image",
    body="Final judgment: [fill in]. Make the image feel resolved, memorable, and simpler than the cover. It should summarize the deck emotionally without introducing new visual complexity.",
)}
"""


def write_missing_source_placeholder(brand_slug: str, reason: str, output_root: Path, generated_on: date) -> None:
    out_dir = output_root / brand_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    content = f"""# PPT-image Design System Inspired by {brand_slug}

Source status: unavailable.

This catalog still contains `{brand_slug}`, but the live source `DESIGN.md` was not available on `{generated_on.isoformat()}`.
Reason: {reason}

This file is intentionally a placeholder instead of a fabricated conversion.
Do not treat it as a real PPT-image design system until a genuine source `DESIGN.md` becomes available again.

## Next Action

- restore or add `source/{brand_slug}/DESIGN.md`
- rerun the converter
"""
    (out_dir / "DESIGN.md").write_text(content, encoding="utf-8")


def load_brand_catalog(brands_file: Path | None) -> list[str]:
    if brands_file is None or not brands_file.exists():
        return []
    brands: list[str] = []
    for line in brands_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        brands.append(stripped)
    return brands


def discover_source_brands(source_root: Path) -> list[str]:
    return sorted(path.parent.name for path in source_root.glob("*/DESIGN.md"))


def convert_all(
    *,
    source_root: Path,
    output_root: Path,
    manifest_path: Path,
    brands_file: Path | None = None,
    generated_on: date | None = None,
    project_root: Path | None = None,
) -> dict:
    generated_on = generated_on or date.today()
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    manifest_path = manifest_path.resolve()
    project_root = project_root.resolve() if project_root else output_root.parent.resolve()

    output_root.mkdir(parents=True, exist_ok=True)

    source_brands = discover_source_brands(source_root) if source_root.exists() else []
    repo_brands = load_brand_catalog(brands_file) or source_brands
    missing_repo_brands = [brand for brand in repo_brands if brand not in source_brands]

    generated_brands: list[str] = []
    for brand in source_brands:
        source_path = source_root / brand / "DESIGN.md"
        out_dir = output_root / brand
        out_dir.mkdir(parents=True, exist_ok=True)
        content = generate_ppt_image_design(source_path, project_root=project_root, generated_on=generated_on)
        (out_dir / "DESIGN.md").write_text(content, encoding="utf-8")
        generated_brands.append(brand)

    missing_details: dict[str, str] = {}
    for brand in missing_repo_brands:
        reason = "Source DESIGN.md missing from the local source directory."
        write_missing_source_placeholder(brand, reason, output_root, generated_on)
        missing_details[brand] = reason

    manifest = {
        "generated_on": generated_on.isoformat(),
        "repo_index_count": len(repo_brands),
        "source_count": len(source_brands),
        "generated_count": len(generated_brands),
        "missing_source_count": len(missing_repo_brands),
        "generated_brands": generated_brands,
        "missing_sources": missing_details,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest

