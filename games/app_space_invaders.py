"""This code intends to replicate space invaders game"""
#import required libraries
import pygame, time
from pathlib import Path

#title, icon, background, ship
pygame.display.set_caption('Space Invaders')
size = pygame.display.set_mode((568,360))
base_path = Path('C:/Users/Luciano/Desktop/git/pala_time/games/')
iconos = pygame.image.load(Path(base_path,'ufo_icon.png'))
pygame.display.set_icon(iconos)
background = Path(base_path,'si_background.png')
ship = pygame.image.load(Path(base_path,'ship.png'))
init_x = 250
init_y = 300
def ship_position(position_x: int,position_y: int):
    size.blit(ship,(position_x,position_y))

#start game until quit
pygame.init()
game_start = True

while game_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False

    size.blit(pygame.image.load(background),(0,0))
    ship_position(init_x,init_y)
    pygame.display.update()


