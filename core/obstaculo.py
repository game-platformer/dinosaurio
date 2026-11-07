import random

import pygame

from .config import SUELO


class Obstaculo:
    def __init__(self, x: float):
        self.x = x
        if random.random() < 0.7:
            self.es_pajaro = False
            self.ancho = random.choice([20, 30, 45])
            self.alto = random.choice([35, 50])
            self.y = SUELO - self.alto
        else:
            self.es_pajaro = True
            self.ancho, self.alto = 40, 25
            self.y = random.choice([SUELO - 25, SUELO - 55, SUELO - 95])

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def actualizar(self, velocidad):
        self.x -= velocidad

    def dibujar(self, pantalla):
        color = (200, 60, 60) if self.es_pajaro else (40, 140, 40)
        pygame.draw.rect(pantalla, color, self.rect)
