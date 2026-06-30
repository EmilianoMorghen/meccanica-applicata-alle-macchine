# Conversion Plan: Handwritten Notes → LLM-readable Markdown

## Goal

Convert 200 pages of handwritten notes on *Meccanica Applicata alle Macchine* into structured Markdown with LaTeX math, preserving diagrams as image references.

---

## Setup

- **Input:** 200 PNG images in `pages/`
- **Output:** Markdown files (one per page) in `markdown/`
- **Naming:** `page_001.md`, `page_002.md`, ..., `page_200.md`
- **Tool:** Vision-capable LLM reading each page image and transcribing

---

## Process per page

For each page:

1. Read the PNG image
2. Transcribe all handwritten text into Markdown
3. Convert all formulas into LaTeX (`$inline$` or `$$block$$`)
4. For diagrams/graphs: describe them briefly and reference the original image
5. Save the result as `markdown/page_XXX.md`

---

## Output format (template)

```markdown
# Page X - [Topic title if identifiable]

[transcribed content with $LaTeX$ formulas]

$$F = ma$$

> **Diagram:** [brief description of what's drawn]
> ![](../pages/page_XXX.png)

[more content...]
```

---

## Batching strategy

- Process pages in batches of ~10, using parallel sub-agents
- Each sub-agent handles 1–2 pages and writes the corresponding `.md` files
- After each batch: review quality, adjust if needed, then continue
- Iterate until all 200 pages are done

---

## Quality checkpoints

After the first batch (pages 1–10):

- [ ] Math formulas render correctly
- [ ] Text is accurate and complete
- [ ] Diagrams are properly referenced and described
- [ ] Format is consistent across pages
- [ ] Level of detail is appropriate

---

## Adjustable parameters

| Parameter | Current choice | Alternatives |
|-----------|---------------|--------------|
| Math format | LaTeX (`$...$`) | Unicode symbols, plain text |
| Diagram handling | Image ref + description | Full text description only, skip entirely |
| File granularity | One `.md` per page | Grouped by topic |
| Language | Keep original (Italian) | Translate to English |

---

## Status

- [x] Extract all pages as PNG images
- [x] Process batch 1 (pages 1–10)
- [x] Review and confirm format
- [x] Process remaining batches (pages 11–200)
- [ ] Final review
