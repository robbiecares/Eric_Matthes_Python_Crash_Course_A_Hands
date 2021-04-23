import pygame
import sys
import raindrop
from settings import Settings


class Raindrops:
    """the framework for creating a looping set of raindrops"""

    def __init__(self):
        """Initalize the program, and create its resources"""
        pygame.init()
        self.settings = Settings()

        # create a screen object/rect
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        # Set the background
        self.bg_color = self.settings.bg_color

        # Declare the game objects
        self.drops = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._create_drop()
            self._update_drops()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _check_mouse_events(self, event):
        #TODO: add create new drop on mouse click
        return None

    def _create_drop(self):
        """Create a new drop and add it to the drops group until max drop limit is reached."""
        if len(self.drops) < self.settings.max_drops:
            new_drop = raindrop.Raindrop(self)
            self.drops.add(new_drop)

    def _update_drops(self):
        """Update position of drops and get rid of invisible drops."""
        # update drop position
        self.drops.update()

        # Get rid of invisible drops
        for drop in self.drops.copy():
            if drop.rect.top >= self.settings.screen_height:
                self.drops.remove(drop)

        # move the raindrop down the screen at a random speed (should be relative to the size of the drop)

    # refresh the screen
    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(self.bg_color)
        self.drops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    rd = Raindrops()
    rd.run_game()
