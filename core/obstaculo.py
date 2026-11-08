import random

import pygame

from .config import SUELO
from .sprite import Sprite


class Obstaculo:
    def __init__(self, x: float, sprites: Sprite):
        self.x = x
        self.frame = 0
        if random.random() < 0.7:
            self.es_pajaro = False
            self.imagenes = [random.choice(sprites.cactus)]
            self.y = SUELO - self.imagenes[0].get_height()
        else:
            self.es_pajaro = True
            self.imagenes = sprites.pajaro
            self.y = random.choice([SUELO - 25, SUELO - 55, SUELO - 95])

        self.ancho = self.imagenes[0].get_width()
        self.alto = self.imagenes[0].get_height()

    def imagen(self):
        return self.imagenes[(self.frame // 10) % len(self.imagenes)]

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def actualizar(self, velocidad):
        self.x -= velocidad
        self.frame += 1

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen(), self.rect)
