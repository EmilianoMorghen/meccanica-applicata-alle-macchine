# Meccanica Applicata alle Macchine

Appunti completi del corso di **Meccanica Applicata alle Macchine** (Politecnico), trascritti da 200 pagine di appunti manoscritti in Markdown strutturato con formule LaTeX. Include temi d'esame passati e un simulatore d'esame.

## Struttura del repository

```
├── markdown/              # 200 file .md (uno per pagina), con formule LaTeX
├── pages/                 # 200 immagini PNG degli appunti originali
├── past-exams/            # 8 temi d'esame passati (compito A–H) con trascrizioni .md
├── exam-simulator/        # Simulatore d'esame (question bank + generatore + tutor)
│   ├── question_bank.md   #   78 domande suddivise in 9 categorie
│   ├── generate_exam.py   #   Generatore di esami randomizzati
│   └── TUTOR_PROMPT.md    #   Prompt per simulare un esame orale con un LLM
├── notes.pdf              # PDF completo degli appunti manoscritti
├── arguments.pdf          # Programma del corso
└── extract_pages.py       # Script per estrarre le pagine dal PDF
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

## Temi d'esame passati

8 compiti trascritti in Markdown (`past-exams/compito_A.md` ... `compito_H.md`), ciascuno con 5 domande. Struttura tipica:

| Posizione | Contenuto |
|-----------|-----------|
| Q1 | **Sempre** cinematica di un meccanismo (con figura) |
| Q2–Q3 | Calcoli applicati (ruote dentate / lubrificazione / vibrazioni / tribologia) |
| Q4 | Esposizione teorica ("Illustrare...") |
| Q5 | Dimostrazione / formulazione MBS |

## Simulatore d'esame

### Generare un esame scritto

```bash
python3 exam-simulator/generate_exam.py                    # un esame su stdout
python3 exam-simulator/generate_exam.py --n 5              # 5 esami
python3 exam-simulator/generate_exam.py --seed 42 --output sim.md  # riproducibile, su file
```

Il generatore segue le regole dei compiti reali: Q1 sempre cinematica, Q2–Q3 da argomenti diversi, Q4 teorica, Q5 dinamica/dimostrazione.

### Simulare un esame orale

Copiare il contenuto di `exam-simulator/TUTOR_PROMPT.md` in una chat con un LLM (ChatGPT, Claude, ecc.) per avviare una simulazione interattiva di esame orale. Il tutor:

- Fa domande una alla volta, valuta le risposte
- Adatta la difficoltà in base alla performance
- Assegna un voto finale (scala 18–30L)
- Indica le aree deboli e le pagine degli appunti da ripassare

### Banca domande

`exam-simulator/question_bank.md` contiene **78 domande** suddivise in 9 categorie con 3 livelli di difficoltà:

| Categoria | Domande |
|-----------|:-------:|
| Cinematica (problemi con figura) | 10 |
| Ruote dentate e ingranaggi | 8 |
| Lubrificazione e cuscinetti | 8 |
| Vibrazioni | 8 |
| Tribologia e attrito | 8 |
| Dinamica e MBS | 8 |
| Esposizioni teoriche | 12 |
| Dimostrazioni e derivazioni | 8 |
| Camme, giunti, freni | 8 |

## Formato dei file Markdown

Ogni file degli appunti segue questo schema:

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
python3 extract_pages.py
```

## Licenza

Appunti personali ad uso didattico.
