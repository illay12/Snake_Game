import pygame.font

class ScoreBoard():
    """"A class to represent scoring information."""

    def __init__(self, sk_game):
        """Initialize scorekeeping attributes."""
        self.screen = sk_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sk_game.settings
        self.stats = sk_game.stats

        # Font settings for scoring info.
        self.text_color = (30, 30, 30)
        self.high_score_text_color = (32,178,170)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center
        self.score_rect.bottom = 475
        self.score_rect.left = 325

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                    self.high_score_text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.bottom = 475
        self.high_score_rect.right = 475

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()