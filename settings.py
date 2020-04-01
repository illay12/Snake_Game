class Settings:
    """Settings for the game."""
    def __init__(self):
        #Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #Snake settings
        self.snake_speed = 50
        self.scale = 50

        #Scoring
        self.alien_points = 50