from .config import FUERZA_SALTO, GRAVEDAD, SUELO


class Dino:
    def __init__(self, sprites):
        self.sprite = sprites
        self.x = 60
        self.y = SUELO
        self.vel_y = 0
        self.agachado = False
        self.muerto = False
        self.frame = 0

    def imagen(self):
        if self.muerto:
            return self.sprite.dino_muerto

        if not self.en_suelo():
            return self.sprite.dino_saltar

        paso = (self.frame // 6) % 2

        if self.agachado:
            return self.sprite.dino_agachado[paso]
        return self.sprite.dino_correr[paso]

    @property
    def rect(self):
        return self.imagen().get_rect(bottomleft=(self.x, self.y))

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

        self.frame += 1

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen(), self.rect)
