import random

import pygame

from .config import FUERZA_SALTO, GRAVEDAD, SUELO


class Dino:
    def __init__(self):
        self.x = 60
        self.y = SUELO
        self.vel_y = 0
        self.agachado = False
        self.color = (
            random.randint(40, 200),
            random.randint(40, 200),
            random.randint(40, 200),
        )

    @property
    def rect(self):
        if self.agachado:
            return pygame.Rect(self.x, self.y - 26, 55, 26)
        return pygame.Rect(self.x, self.y - 44, 40, 44)

    def en_suelo(self):
        return self.y >= SUELO

    def saltar(self):
        if self.en_suelo():
            self.vel_y = FUERZA_SALTO

    def actualizar(self):
        self.vel_y += GRAVEDAD
        self.y = min(self.y + self.vel_y, SUELO)

        if self.en_suelo():
            self.vel_y = 0

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
