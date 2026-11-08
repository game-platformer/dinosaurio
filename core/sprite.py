from pathlib import Path

import pygame as py

RUTA = Path(__file__).resolve().parent / "assets" / "sprites" / "100-offline-sprite.png"


class Sprite:
    def __init__(self):
        self.hoja = py.image.load(RUTA).convert_alpha()

        self.dino_saltar = self.cortar(848, 2, 44, 47)
        self.dino_correr = [self.cortar(936, 2, 44, 47), self.cortar(980, 2, 44, 47)]

        self.dino_muerto = self.cortar(1068, 2, 44, 47)
        self.dino_agachado = [
            self.cortar(1112, 19, 59, 30),
            self.cortar(1171, 19, 59, 30),
        ]

        self.cactus = [self.cortar(228, 2, 17 * n, 35) for n in (1, 2, 3)]
        self.cactus += [self.cortar(332, 2, 25 * n, 50) for n in (1, 2, 3)]

        self.pajaro = [self.cortar(134, 2, 46, 40), self.cortar(180, 2, 46, 40)]
        self.suelo = self.cortar(2, 54, 1200, 12)

    def cortar(self, x, y, ancho, alto):
        return self.hoja.subsurface((x, y, ancho, alto))
