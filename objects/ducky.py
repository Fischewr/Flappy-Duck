import pygame.sprite

import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor


class Ducky(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER2

        self.images = [
            assets.get_sprite("yellowduck-upflap"),
            assets.get_sprite("yellowduck-midflap"),
            assets.get_sprite("yellowduck-downflap")
        ]

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50, 50))

        self.mask = pygame.mask.from_surface(self.image)

        self.flap = 0

        super().__init__(*groups)

    def update(self):
        self.images.insert(0, self.images.pop())
        self.image = self.images[0]

        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x = 6

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.flap = 0
            self.flap -= 6
            assets.play_audio("wing")

    def check_collision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Column or type(sprite) is Floor) and sprite.mask.overlap(self.mask, (
                    self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or
                    self.rect.bottom < 0):
                return True
        return False
