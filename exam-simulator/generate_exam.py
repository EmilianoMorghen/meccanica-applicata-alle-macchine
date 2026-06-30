#!/usr/bin/env python3
"""
generate_exam.py — Randomized Exam Simulator for "Meccanica Applicata alle Macchine"

Reads questions from question_bank.md, selects them according to the exam structure
rules, and outputs a formatted Markdown exam.

Usage:
    python generate_exam.py                    # Print one exam to stdout
    python generate_exam.py --n 3             # Print 3 exams to stdout
    python generate_exam.py --output exam.md  # Write one exam to file
    python generate_exam.py --seed 42 --n 5   # Reproducible batch of 5 exams
"""

import argparse
import random
import re
import sys
from datetime import date
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────────────
# Parsing
# ──────────────────────────────────────────────────────────────────────────────


def parse_question_bank(filepath: Path) -> dict[str, list[str]]:
    """
    Parse a Markdown question bank file and return a dict mapping
    category names (e.g. "Categoria 1: Cinematica (Problemi con Figura)")
    to lists of question strings.

    Expected format:
        ## Categoria N: Name
        ### N.M — Title [Difficulty]
        Question text (may span multiple lines until next `###` or `##`)
    """
    text = filepath.read_text(encoding="utf-8")
    categories: dict[str, list[str]] = {}

    current_category: str | None = None
    current_question_lines: list[str] = []

    def flush_question():
        """Save the accumulated question lines into the current category."""
        if current_category and current_question_lines:
            question = "\n".join(current_question_lines).strip()
            if question:
                categories.setdefault(current_category, []).append(question)

    for line in text.splitlines():
        # Detect category headers: ## Categoria N: ...
        header_match = re.match(r"^##\s+(Categoria\s+\d+:.*)$", line.strip())
        if header_match:
            flush_question()
            current_category = header_match.group(1).strip()
            current_question_lines = []
            continue

        # Detect a new question: ### N.M — Title [Difficulty]
        question_match = re.match(r"^###\s+\d+\.\d+", line.strip())
        if question_match and current_category is not None:
            flush_question()
            current_question_lines = [line.strip()]
            continue

        # Continuation line for multi-line questions (skip separators and blank lines)
        stripped = line.strip()
        if stripped and not re.match(r"^-{3,}$", stripped) and current_question_lines:
            current_question_lines.append(stripped)

    # Don't forget the last question in the file
    flush_question()

    return categories


# ──────────────────────────────────────────────────────────────────────────────
# Exam generation logic
# ──────────────────────────────────────────────────────────────────────────────

# Short aliases for categories used in selection rules
CAT_CINEMATICA = "Categoria 1: Cinematica (Problemi con Figura)"
CAT_RUOTE = "Categoria 2: Ruote Dentate e Ingranaggi"
CAT_LUBRIFICAZIONE = "Categoria 3: Lubrificazione e Cuscinetti"
CAT_VIBRAZIONI = "Categoria 4: Vibrazioni"
CAT_TRIBOLOGIA = "Categoria 5: Tribologia e Attrito"
CAT_DINAMICA = "Categoria 6: Dinamica e MBS"
CAT_TEORIA = "Categoria 7: Esposizioni Teoriche"
CAT_DIMOSTRAZIONI = "Categoria 8: Dimostrazioni e Derivazioni"
CAT_CAMME_GIUNTI = "Categoria 9: Camme, Giunti, Freni"

# Pools for Q2, Q3, Q5 as specified in the requirements
Q2_POOL = [CAT_RUOTE, CAT_LUBRIFICAZIONE, CAT_VIBRAZIONI, CAT_TRIBOLOGIA]
Q3_POOL = [
    CAT_RUOTE,
    CAT_LUBRIFICAZIONE,
    CAT_VIBRAZIONI,
    CAT_TRIBOLOGIA,
    CAT_CAMME_GIUNTI,
]
Q5_POOL = [CAT_DINAMICA, CAT_DIMOSTRAZIONI]


def pick_question(
    rng: random.Random, categories: dict[str, list[str]], cat: str
) -> str:
    """Pick a random question from the given category."""
    questions = categories.get(cat, [])
    if not questions:
        return f"[ERRORE: nessuna domanda disponibile per '{cat}']"
    return rng.choice(questions)


def generate_single_exam(
    rng: random.Random,
    categories: dict[str, list[str]],
) -> list[tuple[str, str]]:
    """
    Generate one exam (list of 5 (category, question) tuples) following the rules:
      Q1: Categoria 1 (Cinematica)
      Q2: One of {Cat 2, 3, 4, 5}
      Q3: A DIFFERENT one of {Cat 2, 3, 4, 5, 9} than Q2's category
      Q4: Categoria 7 (Esposizioni Teoriche)
      Q5: One of {Cat 6, 8}
    """
    exam: list[tuple[str, str]] = []

    # Q1: always Cinematica
    q1_cat = CAT_CINEMATICA
    exam.append((q1_cat, pick_question(rng, categories, q1_cat)))

    # Q2: random category from the applied-calculation pool
    q2_cat = rng.choice(Q2_POOL)
    exam.append((q2_cat, pick_question(rng, categories, q2_cat)))

    # Q3: different category from the extended pool (excludes Q2's category)
    q3_candidates = [c for c in Q3_POOL if c != q2_cat]
    q3_cat = rng.choice(q3_candidates)
    exam.append((q3_cat, pick_question(rng, categories, q3_cat)))

    # Q4: always Esposizioni Teoriche
    q4_cat = CAT_TEORIA
    exam.append((q4_cat, pick_question(rng, categories, q4_cat)))

    # Q5: dynamics / derivations
    q5_cat = rng.choice(Q5_POOL)
    exam.append((q5_cat, pick_question(rng, categories, q5_cat)))

    return exam


# ──────────────────────────────────────────────────────────────────────────────
# Formatting
# ──────────────────────────────────────────────────────────────────────────────


def format_exam(
    exam: list[tuple[str, str]],
    exam_number: int,
    total: int,
) -> str:
    """Render a single exam as a Markdown string."""
    today = date.today().strftime("%d/%m/%Y")

    lines: list[str] = []

    if total > 1:
        lines.append(f"# Simulazione d'Esame #{exam_number}")
    else:
        lines.append("# Simulazione d'Esame")

    lines.append("")
    lines.append(f"**Corso:** Meccanica Applicata alle Macchine")
    lines.append(f"**Data:** {today}")
    if total > 1:
        lines.append(f"**Esame:** {exam_number}/{total}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for i, (cat, question) in enumerate(exam, start=1):
        lines.append(f"### Domanda {i}")
        lines.append(f"*[{cat}]*")
        lines.append("")
        lines.append(f"{question}")
        lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate randomized exam simulations for Meccanica Applicata alle Macchine.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        metavar="FILE",
        help="Output file path (default: print to stdout).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        metavar="N",
        help="Random seed for reproducibility.",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=1,
        metavar="N",
        help="Number of exams to generate (default: 1).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Locate the question bank relative to this script
    script_dir = Path(__file__).resolve().parent
    bank_path = script_dir / "question_bank.md"

    if not bank_path.exists():
        print(f"Error: question bank not found at {bank_path}", file=sys.stderr)
        sys.exit(1)

    # Parse questions
    categories = parse_question_bank(bank_path)

    if not categories:
        print("Error: no categories found in question bank.", file=sys.stderr)
        sys.exit(1)

    # Validate that required categories exist
    required_cats = [
        CAT_CINEMATICA,
        CAT_RUOTE,
        CAT_LUBRIFICAZIONE,
        CAT_VIBRAZIONI,
        CAT_TRIBOLOGIA,
        CAT_DINAMICA,
        CAT_TEORIA,
        CAT_DIMOSTRAZIONI,
        CAT_CAMME_GIUNTI,
    ]
    missing = [c for c in required_cats if c not in categories]
    if missing:
        print(
            f"Warning: the following categories are missing from the question bank:\n"
            + "\n".join(f"  - {c}" for c in missing),
            file=sys.stderr,
        )

    # Initialize RNG
    rng = random.Random(args.seed)

    # Generate exams
    output_parts: list[str] = []
    for i in range(1, args.n + 1):
        exam = generate_single_exam(rng, categories)
        output_parts.append(format_exam(exam, exam_number=i, total=args.n))

    full_output = "\n".join(output_parts)

    # Write or print
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(full_output, encoding="utf-8")
        print(f"✓ Generated {args.n} exam(s) → {output_path}", file=sys.stderr)
    else:
        print(full_output)


if __name__ == "__main__":
    main()
