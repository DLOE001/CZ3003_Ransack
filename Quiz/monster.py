import pygame
from spritesheet import Spritesheet

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, quiz):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheet('monsterspritesheet.png').parse_sprite('sprite1')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dead = False
        self.quiz = quiz

    def draw(self, display):
        if self.dead == False:
            display.blit(self.image, (self.rect.x, self.rect.y))
