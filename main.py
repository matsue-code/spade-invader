import math
import random
import pygame
screen_width= 800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
pygame.init 
screen = pygame.display.set_mode((screen_height,screen_width))
background=pygame.image.load('')
pygame.display.set_caption("space invader")
icon=pygame.image.load('')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('')
player_start_x=player_start_x
player_start_y=player_start_y
player_start_x-change=0
enemyimg = []
enemyx = []
enemyy =[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(''))
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)
bulleting=pygame.image.load('')
bulletx=0
bullety=player_start_y
bulletx-change=0
bullety_change=bullet_speed_y
bullet_speed_y-state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
over_font=pygame.font("freesansbold.ttf",64)
def show_score (x,y)
    score=font.render("score:" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y,):
    screen.blit(playerimg,x,y)
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulleting,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt{(enemyx-bulletx)**2+(enemyy-bullety)**2}
    return distance<collision_distance