from pathlib import Path
class Settings:
    def __init__(self) -> None:
        # Game and window
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.difficulty_scale = 1.2
        
        # Background
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60

        # Bullet
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        # Alien
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        # Button
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)
        
        self.text_color = (255, 255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        
    def initialize_dynamic_settings(self) -> None:
        self.ship_speed = 10
        self.starting_ship_count = 3

        self.bullet_w = 20
        self.bullet_h = 60
        self.bullet_speed = 16 
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale