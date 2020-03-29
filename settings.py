class Settings:
    """Settings for the game."""
    def __init__(self):
        #Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #Snake settings
        self.snake_speed = 25
        self.scale = 25