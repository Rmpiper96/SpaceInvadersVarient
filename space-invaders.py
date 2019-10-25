import pygame
import random
from shooterfleet import ShooterFleet
from limbfleet1 import LimbFleet
from limbfleet2 import LimbFleet
from limbfleet3 import LimbFleet
from limbfleet4 import LimbFleet
from bossfleet import BossFleet
from hero import Hero
from fleet import Fleet
import sys
import pygame as pg



#Game settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3

GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (81, 46, 255)


pygame.init()
#Media Files
stage_background = pygame.image.load('media/Background.png')
player_image = pygame.image.load('media/si-player.png')
bullet_image_large = pygame.image.load('media/si-bullet.png')
boss_image = pygame.image.load('media/boss_edited.png')
limb_image = pygame.image.load('media/limb_edited.png')
bullet_image = pg.transform.rotozoom(bullet_image_large, 0, 0.7)
enemybullet_image = pygame.image.load('media/enemybullet.png')
enemy_image_large = pygame.image.load('media/si-enemy.png')
enemy_image = pg.transform.rotozoom(enemy_image_large, 0, 0.7)
laser_sound = pygame.mixer.Sound('media/si-laser.wav')
explosion_sound = pygame.mixer.Sound('media/si-explode.wav')
monster_arrives = pygame.mixer.Sound('media/MonsterRoar.wav')
monster_dies = pygame.mixer.Sound('media/MonsterDeath.wav')
pygame.mixer.music.load('media/Undertale Asgore Theme.wav')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score_font = pygame.font.SysFont('Arial', 22, True)
title_font = pygame.font.SysFont('Arial', 26, True)
pygame.display.set_caption('OCEAN BATTLE')
title_press_start_font = pygame.font.SysFont('Comic Sans', int(25), True)

#Title Screen
show_title_screen = True
while show_title_screen:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            show_title_screen = False

    title_text = title_font.render("Invaders from Deep Below!", False, WHITE)
    title_press_start_text = title_press_start_font.render('PRESS ANY KEY TO START', False, GREEN)

    game_display.blit(title_text, (310, 50))
    game_display.blit(title_press_start_text, (360, 100))
    pygame.display.flip()
    clock.tick(30)

show_outra_screen = False
while show_title_screen:
    for event in pygame.event.get():
        if score >= 900 or hero.is_alive == False:
            show_outro_screen = True

    title_text = title_font.render("Game Over.", False, WHITE)
    title_press_start_text = title_press_start_font.render('your final score was:', False, GREEN)

    game_display.blit(title_text, (310, 50))
    game_display.blit(title_press_start_text, (360, 100))
    pygame.display.flip()
    clock.tick(30)
    pygame.quit()

def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero.is_alive = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hero.set_direction_left()
                elif event.key == pygame.K_d:
                    hero.set_direction_right()
                elif event.key == pygame.K_SPACE:
                    laser_sound.play()
                    hero.shoot(bullet_image)
                elif event.key == pygame.K_q:
                    laser_sound.play()
                    shooterfleet.enemyshoot(enemybullet_image)
                elif event.key == pygame.K_p:
                    pause_game()
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    hero.set_direction_none()
                elif event.key == pygame.K_d:
                    hero.set_direction_none()

def pause_game():
    is_paused = True
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_paused == False
                hero.is_alive == False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = False
        clock.tick(30)

hero = Hero(player_image, 200, GAME_BOTTOM_WALL - player_image.get_height())

fleet = Fleet(3, 5, 4, enemy_image, GAME_LEFT_WALL +1, GAME_TOP_WALL + 1)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            for enemy in self.fleet:
                if event.type == pygame.QUIT:
                    hero.is_alive = False
                    game_intro = False
                if event.type == pygame.KEYDOWN:
                    game_intro = False
                    pygame.quit()
                    quit()

shooterfleet = ShooterFleet(3, 5, 10, enemy_image, GAME_LEFT_WALL +1, GAME_TOP_WALL + 1)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            for enemy in self.fleet:
                if event.type == pygame.QUIT:
                    hero.is_alive = False
                    game_intro = False
                if event.type == pygame.KEYDOWN:
                    game_intro = False
                    pygame.quit()
                    quit()

bossfleet = BossFleet(boss_image, 440, 120)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                hero.is_alive = False
                game_intro = False
            if event.type == pygame.KEYDOWN:
                game_intro = False
                pygame.quit()
                quit()

limbfleet1 = LimbFleet(limb_image, 220, 100)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero.is_alive = False
                game_intro = False
            if event.type == pygame.KEYDOWN:
                game_intro = False
                pygame.quit()
                quit()
limbfleet2 = LimbFleet(limb_image, 330, 150)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero.is_alive = False
                game_intro = False
            if event.type == pygame.KEYDOWN:
                game_intro = False
                pygame.quit()
                quit()
limbfleet3 = LimbFleet(limb_image, 600, 150)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero.is_alive = False
                game_intro = False
            if event.type == pygame.KEYDOWN:
                game_intro = False
                pygame.quit()
                quit()
limbfleet4 = LimbFleet(limb_image, 700, 100)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero.is_alive = False
                game_intro = False
            if event.type == pygame.KEYDOWN:
                game_intro = False
                pygame.quit()
                quit()

def game_outro():
    outro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero.is_alive = False
                game_intro = False
            if event.type == pygame.KEYDOWN:
                game_intro = False
                pygame.quit()
                quit()
    
score = 0
#Main Game Loop

while hero.is_alive:
    handle_events()

    fleet.handle_wall_collision(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    hero.handle_wall_collision_for_bullets(GAME_TOP_WALL)
    game_display.blit(stage_background, (0, 0))
    

    for bullet in hero.bullets_fired:
        for ship in fleet.ships:
            if bullet.has_collided_with(ship):
                explosion_sound.play()
                bullet.is_alive = False
                ship.is_alive = False
   
                score += 10

    for bullet in hero.bullets_fired:
        for ship in bossfleet.ships:
            if bullet.has_collided_with(ship) and score >= 400 and limbfleet1.health <= 0 and limbfleet2.health <= 0 and limbfleet3.health <= 0 and limbfleet4.health <= 0:
                bullet.is_alive = False
                
                score += 5
                bossfleet.health -= 5
                if bossfleet.health <= 0:
                    monster_dies.play()
                    ship.is_alive = False

    for bullet in hero.bullets_fired:
        for ship in limbfleet1.ships:
            if bullet.has_collided_with(ship) and score >= 400:
                bullet.is_alive = False
                
                score += 5
                limbfleet1.health -= 5
                if limbfleet1.health <= 0:
                    monster_dies.play()
                    ship.is_alive = False

    for bullet in hero.bullets_fired:
        for ship in limbfleet2.ships:
            if bullet.has_collided_with(ship) and score >= 400:
                bullet.is_alive = False
                
                score += 5
                limbfleet2.health -= 5
                if limbfleet2.health <= 0:
                    monster_dies.play()
                    ship.is_alive = False
    
    for bullet in hero.bullets_fired:
        for ship in limbfleet3.ships:
            if bullet.has_collided_with(ship) and score >= 400:
                bullet.is_alive = False
                
                score += 5
                limbfleet3.health -= 5
                if limbfleet3.health <= 0:
                    monster_dies.play()
                    ship.is_alive = False

    for bullet in hero.bullets_fired:
        for ship in limbfleet4.ships:
            if bullet.has_collided_with(ship) and score >= 400:
                bullet.is_alive = False
                
                score += 5
                limbfleet4.health -= 5
                if limbfleet4.health <= 0:
                    monster_dies.play()
                    ship.is_alive = False
                
    
    score_text = score_font.render(str(score), False, BLACK)
    game_display.blit(score_text, (0,0) )

    for enemybullet in shooterfleet.enemybullets_fired:
        if enemybullet.has_collided_with(hero):
            hero.is_alive = False
    
    

                
    fleet.remove_dead_ships()

    bossfleet.remove_dead_ships()
    limbfleet1.remove_dead_ships()
    limbfleet2.remove_dead_ships()
    limbfleet3.remove_dead_ships()
    limbfleet4.remove_dead_ships()

    hero.move(GAME_LEFT_WALL, GAME_RIGHT_WALL)
    fleet.move_over()
    hero.move_all_bullets()
    shooterfleet.move_all_enemybullets()


    hero.show(game_display)
    fleet.show(game_display)
    hero.show_all_bullets(game_display)
    shooterfleet.show_all_enemybullets(game_display)
    if score >= 400:
        bossfleet.show(game_display)
        limbfleet1.show(game_display)
        limbfleet2.show(game_display)
        limbfleet3.show(game_display)
        limbfleet4.show(game_display)
        
    pygame.display.update()

    clock.tick(100)

pygame.quit()