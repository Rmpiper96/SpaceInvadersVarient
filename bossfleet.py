import pygame
from boss import Boss
from enemybullet import EnemyBullet
class BossFleet():
    def __init__(self, boss_img, starting_xcor, starting_ycor):
        self.direction = 0.5
        self.ships = self.get_initial_boss_limb_formation(boss_img, starting_xcor, starting_ycor)
        self.enemybullets_fired = []
        self.width = boss_img.get_width()
        self.height = boss_img.get_height()
        self.health = 100
        

    def get_initial_boss_limb_formation(self, boss_img, starting_xcor, starting_ycor):
        initial_formation = []
        for row in range(1):
            for col in range(1):
                current_xcor = starting_xcor + col * boss_img.get_width()
                current_ycor = starting_ycor + row * boss_img.get_height()
                initial_formation.append(Boss(boss_img, current_xcor, current_ycor))
                self.xcor = current_xcor
                self.ycor = current_ycor
        return initial_formation
        

    def enemyshoot(self, enemybullet_image):
        new_enemybullet = EnemyBullet(enemybullet_image, self.xcor + self.width / 10 - enemybullet_image.get_width() / 20, self.ycor)
        self.enemybullets_fired.append(new_enemybullet)

    def handle_wall_collision_for_enemybullets(self, bottom_wall):
        for bullet in self.enemybullets_fired:
            if enemybullet.has_collided_with_bottom_wall(bottom_wall):
                enemybullet.is_alive = False

        self.remove_dead_enemybullets()

    def remove_dead_enemybullets(self):
        for i in range(len(self.enemybullets_fired) -1, -1, -1):
            if self.enemybullets_fired[i].is_alive == False:
                self.enemybullets_fired.pop(i)

    def move_all_enemybullets(self):
        for enemybullet in self.enemybullets_fired:
            enemybullet.move()

    def show_all_enemybullets(self, game_display):
        for enemybullet in self.enemybullets_fired:
            enemybullet.show(game_display)

    def show(self, game_display):
        for ship in self.ships:
            ship.show(game_display)

    def handle_wall_collision(self, left_wall, right_wall):
        for ship in self.ships:
            if ship.has_collided_with_left_wall(left_wall) or ship.has_collided_with_right_wall(right_wall):
                self.move_down()
                self.change_direction()
                break

    def change_direction(self):
        self.direction *= -1

    def move_over(self):
        for ship in self.ships:
            ship.move_over(self.direction * self.speed)

    def remove_dead_ships(self):
        for i in range(len(self.ships) -1, -1, -1):
            if self.ships[i].is_alive == False:
                self.ships.pop(i)
    