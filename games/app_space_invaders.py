"""This app intends to replicade space invaders game"""
import pygame, random, math
from pathlib import Path
from pygame import mixer

#init game
pygame.init()

#view
view = pygame.display.set_mode((568, 360))

#title and icon
base_path = Path('C:/Users/Luciano/Desktop/git/pala_time/games/')
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(Path(base_path,'ufo_icon.png'))
pygame.display.set_icon(icon)
background = pygame.image.load(Path(base_path,'si_background.png'))

#add music
mixer.music.load(Path(base_path,'gen_music.mp3'))
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#ship variables
img_ship = pygame.image.load(Path(base_path,'ship.png'))
ship_x = 275
ship_y = 340
ship_x_change = 0

#enemy-alien variables
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_enemies = 10

for e in range(num_enemies):
    img_enemy.append(pygame.image.load(Path(base_path,'alien.png')))
    enemy_x.append(random.randint(0, 568))
    enemy_y.append(random.randint(0, 100))
    enemy_x_change.append(0.5)
    enemy_y_change.append(15)

#bullet variables
img_bullet = pygame.image.load(Path(base_path,'laser.png'))
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
bullet_visible = False

#points
points = 0
font = pygame.font.Font(Path(base_path,'fastest.ttf'), 32)
text_x = 10
text_y = 10

#final text
final_font = pygame.font.Font(Path(base_path,'fastest.ttf'), 40)

#create final text
def final_text():
    my_final_font = final_font.render("GAME OVER", True, (255, 255, 255))
    view.blit(my_final_font, (60, 200))


#show points
def show_points(x, y):
    text = font.render(f"Points: {points}", True, (255, 255, 255))
    view.blit(text, (x, y))


#ship function
def ship(x, y):
    view.blit(img_ship, (x, y))


#enemy function
def enemy(x, y, ene):
    view.blit(img_enemy[ene], (x, y))


#shoot bullet function
def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    view.blit(img_bullet, (x + 16, y + 10))


#detect crash function
def crash(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


#GAME START
executing = True
while executing:

    #background image
    view.blit(background, (0, 0))

    #events
    for event in pygame.event.get():

        #event close game
        if event.type == pygame.QUIT:
            executing = False

        #press keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_x_change = -1
            if event.key == pygame.K_RIGHT:
                ship_x_change = 1
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound(Path(base_path,'shoot.mp3'))
                bullet_sound.play()
                if not bullet_visible:
                    bullet_x = ship_x
                    shoot_bullet(bullet_x, bullet_y)

        #stop pressing keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship_x_change = 0

    #modify ship position
    ship_x += ship_x_change

    #maintain ship inside borders
    if ship_x <= 5:
        ship_x = 5
    elif ship_x >= 550:
        ship_x = 550

    #modify enemy position
    for e in range(num_enemies):

        #game set
        if enemy_y[e] > 500:
            for k in range(num_enemies):
                enemy_y[k] = 1000
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]

    #maintain enemy inside borders
        if enemy_x[e] <= 5:
            enemy_x_change[e] = 0.3
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 550:
            enemy_x_change[e] = -0.3
            enemy_y[e] += enemy_y_change[e]

        #colission
        colission = crash(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if colission:
            crash_sound = mixer.Sound(Path(base_path,'crash.mp3'))
            crash_sound.play()
            bullet_y = 500
            bullet_visible = False
            points += 1
            enemy_x[e] = random.randint(5, 550)
            enemy_y[e] = random.randint(50, 340)

        enemy(enemy_x[e], enemy_y[e], e)

    #bullet movement
    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False

    if bullet_visible:
        shoot_bullet(bullet_y, bullet_y)
        bullet_y -= bullet_y_change

    ship(ship_x, ship_y)

    show_points(text_x, text_y)

    # actualizar
    pygame.display.update()
