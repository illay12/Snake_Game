class GameStats:
    """Track statistics for Snake."""

    def __init__(self,sk_game):
        """Initialize statistics."""
        self.settings = sk_game.settings
        self.game_active = False
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        self.score = 0
