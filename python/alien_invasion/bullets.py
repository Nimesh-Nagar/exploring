"""
Bullet class inherits from "Sprite". 
When you use sprites, you can group related elements in
your game and act on all the grouped elements at once.
"""

import pygame
from pygame.sprite import Sprite

# To manage bullets fired from the ship
class Bullet(Sprite):

    def __init__(self,ai_game):    
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet rect and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # stote bullet's position as a decimal value
        self.y = float(self.rect.y)
    
    # To move bullet up the screen
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

