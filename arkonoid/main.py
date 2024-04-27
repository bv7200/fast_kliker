import pygame
import os

pygame.font.init()
pygame.init()

display_width = 800
display_height = 600

FPS = pygame.time.Clock()
class Sprite_game:
    def __init__(self, width, height, name_imege, x, y, sped=0, speed_x=0):
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_imege
        self.X = x
        self.Y = y
        self.SPEED = speed_x
        self.END_IMAGE = ""
        self.WIN = 0
        self.RECT = pygame.Rect(x, y, width, height)



    def load_image(self):
        path_image = os.path.join(os.path.abspath(__file__+"/.."),self.NAME_IMAGE)
        image1 = pygame.image.load(path_image)
        self.END_IMAGE = pygame.transform.scale(image1, (self.WIDTH, self.HEIGHT))


list_map = [
    "1111111111"
    "0001111000"
    "1111111111"
    "0001111000"
]
list_block = list()
def start_game():
    screen = pygame.display.set_mode((display_width, display_height))
    sprite = Sprite_Game(150, 30,"image/4.png",display_width / 2, display_height - 30, speed=2)
    sprite.load_image()
    ball = Sprite_game(25, 25, "image/arka.png", display_width / 2, display_height / 2,sped=1, speed_X=)




























