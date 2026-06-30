"""
Crop diagrams from pages 1-10 based on visually identified bounding boxes.
Each crop is saved as markdown/figures/page_XXX_figY.png
"""

import os

from PIL import Image

INPUT_DIR = "pages"
OUTPUT_DIR = "markdown/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bounding boxes: (x_left, y_top, x_right, y_bottom)
# Format: page_number: [(box, description), ...]
CROPS = {
    1: [
        ((30, 100, 700, 400), "Corpo rigido C1 con punti A e B, e riferimento C2"),
        (
            (50, 680, 800, 1080),
            "Vincolo cilindrico: corpo C1 con foro e corpo C2 con perno",
        ),
    ],
    2: [
        ((50, 430, 280, 750), "Cerniera (giunto rotoidale) - vista esplosa 3D"),
        ((50, 1100, 310, 1440), "Coppia Prismatica - blocco rettangolare in guida"),
    ],
    3: [
        ((60, 200, 370, 470), "Coppia Sferica (cerniera sferica)"),
        ((230, 1190, 720, 1290), "Membri binari e quaternari"),
        ((60, 1300, 280, 1410), "Membri ternari"),
    ],
    4: [
        ((50, 70, 200, 210), "Catena di Watt - schema a rombo"),
        ((110, 340, 250, 600), "Coppia inferiore e superiore (camma/valvola)"),
        (
            (60, 920, 830, 1130),
            "Catene cinematiche: quadrilatero, pentagonale, Stevenson",
        ),
    ],
    5: [
        ((50, 260, 970, 460), "Manovellismo di spinta con grafo corrispondente"),
        ((50, 600, 730, 1090), "Catena di Watt e Stephenson con grafi corrispondenti"),
    ],
    6: [
        ((370, 80, 810, 390), "Matrice di adiacenza 6x6"),
        (
            (50, 690, 640, 1370),
            "Grafi dei 7 meccanismi (RRRR, RRRP, PRRP, PRRR, RPRP, RRPP, PPRR)",
        ),
    ],
    7: [
        ((100, 490, 520, 650), "Quadrilatero articolato con punti A, B, A0, B0"),
        ((100, 700, 1200, 1150), "Diagramma di flusso del metodo di Grashof"),
    ],
    8: [
        (
            (50, 90, 870, 430),
            "Grafico Newton-Raphson: curva psi(u), tangente, punti iterativi",
        ),
    ],
    9: [
        (
            (40, 160, 530, 330),
            "Manovellismo di spinta: telaio, biella, manovella, stantuffo",
        ),
        ((730, 680, 960, 790), "Catena di Watt con maglie interne"),
    ],
    10: [
        ((40, 150, 280, 350), "Sistema di coordinate 3D con punto E su traiettoria"),
        ((30, 530, 250, 820), "Ascissa curvilinea: curva Omega con punto E"),
        ((30, 1060, 340, 1250), "Definizione limite del versore tangente tau"),
    ],
}


def crop_figures():
    total = 0
    for page_num, figures in CROPS.items():
        img_path = os.path.join(INPUT_DIR, f"page_{page_num:03d}.png")
        img = Image.open(img_path)

        for fig_idx, (box, desc) in enumerate(figures, start=1):
            cropped = img.crop(box)
            out_name = f"page_{page_num:03d}_fig{fig_idx}.png"
            out_path = os.path.join(OUTPUT_DIR, out_name)
            cropped.save(out_path)
            print(f"  {out_name} ({cropped.width}x{cropped.height}) - {desc}")
            total += 1

    print(f"\nDone! {total} figures extracted to '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    crop_figures()
