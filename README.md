# Meccanica Applicata alle Macchine

Appunti completi del corso di **Meccanica Applicata alle Macchine** (Politecnico), trascritti da 200 pagine di appunti manoscritti in Markdown strutturato con formule LaTeX.

## Struttura del repository

```
├── markdown/          # 200 file .md (uno per pagina), con formule LaTeX
├── pages/             # 200 immagini PNG degli appunti originali
├── past-exams/        # Foto di temi d'esame passati
├── notes.pdf          # PDF completo degli appunti manoscritti
├── arguments.pdf      # Programma del corso
└── extract_pages.py   # Script per estrarre le pagine dal PDF
```

## Argomenti trattati

| # | Argomento | Pagine |
|---|-----------|--------|
| 1 | Cinematica (elemento, corpo rigido, CIR, polari) | 10–31 |
| 2 | Configurazione dei meccanismi (vincoli, Jacobiano) | 15–19 |
| 3 | Euler-Savary, circonferenza dei flessi e stazionarietà | 27–34 |
| 4 | Profili coniugati (epicicli, Aronhold-Kennedy) | 35–48 |
| 5 | Statica (equazioni cardinali, disgregazione) | 49–55 |
| 6 | Tribologia (Hertz, attrito, usura) | 56–75 |
| 7 | Cuscinetti e lubrificazione (Reynolds, idrostatica) | 76–103 |
| 8 | Dinamica (D'Alembert, lavori virtuali, Lagrange) | 105–133 |
| 9 | Ruote dentate e ingranaggi (evolvente, epicicloidali) | 135–153 |
| 10 | Meccanica delle vibrazioni (libere, forzate, torsionali) | 155–175 |
| 11 | Freni (pattino, ceppi, Reye) | 177–183 |
| 12 | Camme (profili armonico, cicloidale, parabolico) | 185–192 |
| 13 | Giunti di trasmissione (Cardano, Oldham) | 193–200 |

## Formato dei file Markdown

Ogni file segue questo schema:

```markdown
# Page X - [Titolo argomento]

[Testo trascritto con formule $LaTeX$ inline]

$$F = ma$$

> ![](../pages/page_XXX.png)
> Diagramma: [descrizione del disegno]
```

- Formule inline: `$...$`
- Formule a blocco: `$$...$$`
- Formule importanti: `\boxed{}`
- Vettori: `\vec{}`, versori: `\hat{}`, derivate temporali: `\dot{}`
- Lingua: **Italiano** (originale)

## Come usare

Questi appunti sono pensati per essere consultati con qualsiasi viewer Markdown con supporto LaTeX (Obsidian, VS Code, GitHub, ecc.).

Per rigenerare le pagine PNG dal PDF:

```bash
python extract_pages.py
```

## Licenza

Appunti personali ad uso didattico.
