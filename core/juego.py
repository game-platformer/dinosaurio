import random

import pygame as py

from .config import ALTO, ANCHO, FPS, SUELO, VELOCIDAD_INICIAL, VELOCIDAD_MAX
from .dino import Dino
from .obstaculo import Obstaculo
from .sprite import Sprite


class Juego:
    def __init__(self):
        py.init()
        self.pantalla = py.display.set_mode((ANCHO, ALTO))
        self.sprites = Sprite()

        py.display.set_caption("Dino")
        self.reloj = py.time.Clock()
        self.fuente = py.font.SysFont("Menlo", 18)
        self.record = 0

        self.reiniciar()

    def reiniciar(self):
        # Dinos
        self.dinos = [Dino(self.sprites)]
        self.suelo_x = 0
        self.puntaje = 0

        # Obstaculos
        self.obstaculos = []
        self.velocidad = VELOCIDAD_INICIAL

        self.proxima_distancia = 0
        self.game_over = False

    def generar_obstaculo(self):
        if (
            not self.obstaculos
            or ANCHO - self.obstaculos[-1].x > self.proxima_distancia
        ):
            self.obstaculos.append(Obstaculo(ANCHO + 20, self.sprites))
            distancia_min = 250 + self.velocidad * 20
            self.proxima_distancia = distancia_min + random.randint(0, 300)

    def choca(self, dino):
        return any(dino.rect.colliderect(obs.rect) for obs in self.obstaculos)

    def ejecutar(self):
        corriendo = True
        while corriendo:
            for evento in py.event.get():
                if evento.type == py.QUIT:
                    corriendo = False

                if evento.type == py.KEYDOWN and evento.key in (py.K_UP, py.K_SPACE):
                    if self.game_over:
                        self.reiniciar()
                    else:
                        for dino in self.dinos:
                            dino.saltar()

            if not self.game_over:
                self.puntaje += 0.15
                self.velocidad = min(self.velocidad + 0.002, VELOCIDAD_MAX)
                self.suelo_x = (self.suelo_x - self.velocidad) % 1200
                teclas = py.key.get_pressed()
                for dino in self.dinos:
                    dino.agachado = teclas[py.K_DOWN] and dino.en_suelo()

                for dino in self.dinos:
                    dino.actualizar()

                self.generar_obstaculo()
                for obs in self.obstaculos:
                    obs.actualizar(self.velocidad)

                self.obstaculos = [o for o in self.obstaculos if o.x + o.ancho > 0]

                vivos = [d for d in self.dinos if not self.choca(d)]
                if vivos:
                    self.dinos = vivos
                else:
                    self.game_over = True
                    self.record = max(self.record, int(self.puntaje))
                    for d in self.dinos:
                        d.muerto = True

            self.pantalla.fill((247, 247, 247))
            # py.draw.line(self.pantalla, (83, 83, 83), (0, SUELO), (ANCHO, SUELO), 2)
            self.pantalla.blit(self.sprites.suelo, (self.suelo_x - 1200, SUELO - 4))
            self.pantalla.blit(self.sprites.suelo, (self.suelo_x, SUELO - 4))

            for obs in self.obstaculos:
                obs.dibujar(self.pantalla)

            for dino in self.dinos:
                dino.dibujar(self.pantalla)

            marcador = f"Hi {self.record:05d} {int(self.puntaje):05d}"
            marcador_velocidad = f"Velocidad {int(self.velocidad):05d}"
            texto = self.fuente.render(marcador, True, (83, 83, 83))
            texto_velocidad = self.fuente.render(marcador_velocidad, True, (83, 83, 83))
            self.pantalla.blit(texto, texto.get_rect(topleft=(20, 15)))
            self.pantalla.blit(
                texto_velocidad, texto_velocidad.get_rect(topright=(ANCHO - 20, 15))
            )

            if self.game_over:
                texto = self.fuente.render(
                    "GAME OVER - Espacio para reiniciar", True, (83, 83, 83)
                )
                self.pantalla.blit(
                    texto, texto.get_rect(center=(ANCHO // 2, ALTO // 2))
                )

            py.display.flip()
            self.reloj.tick(FPS)

        py.quit()
