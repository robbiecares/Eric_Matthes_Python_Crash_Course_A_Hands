import pygame
from pygame.sprite import Sprite
import random
from settings import Settings


class Raindrop(Sprite):
    """A class to represent a single drop in a shower."""

    def __init__(self, drops_main):
        """Initialize a raindrop and set its starting position."""
        super().__init__()
        self.screen = drops_main.screen
        self.settings = drops_main.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.jpg')
        self.rect = self.image.get_rect()

        # Start each new drop at a random x coordinate at the top of the screen.
        self.rect.x = random.randint(0, self.settings.screen_width)
        self.rect.y = 0

        # Store the drop's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the drop down the screen"""
        self.y += self.settings.drop_speed
        self.rect.y = self.y
