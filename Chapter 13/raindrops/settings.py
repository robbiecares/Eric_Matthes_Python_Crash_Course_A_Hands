import random


class Settings:
    """A class to store all settings for raindrops."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Raindrop settings
        self.drop_speed = random.randint(1, 10)
        self.max_drops = 5
