from pathlib import Path
class Settings:
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        
        # Background
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 10

        # Bullet
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 16 
        self.bullet_w = 20
        self.bullet_h = 60
        self.bullet_amount = 5

        # Alien
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.fleet_speed = 3
        self.fleet_direction = 1
        self.alien_w = 40
        self.alien_h = 40