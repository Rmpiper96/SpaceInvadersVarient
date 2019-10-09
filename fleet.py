from enemy import Enemy

class Fleet():
    def __init__(self, row_count, column_count, initial_speed, enemy_img, starting_xcor, starting_ycor):
        self.direction = 0.5
        self.speed = initial_speed
        self.ships = self.get_initial_ships(row_count, column_count, enemy_img, starting_xcor, starting_ycor)
        self.enemybullets_fired = []

    def get_initial_ships(self, row_count, column_count, enemy_img, starting_xcor, starting_ycor):
        initial_ships = []
        for row in range(4):
            for col in range(10):
                current_xcor = starting_xcor + col * enemy_img.get_width()
                current_ycor = starting_ycor + row * enemy_img.get_height()
                initial_ships.append(Enemy(enemy_img, current_xcor, current_ycor))
        return initial_ships

    def enemyshoot(self, bullet_image):
        new_enemybullet = EnemyBullet(bullet_image, self.xcor + self.width / 2 - bullet_image.get_width() / 2, self.ycor)
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

    def move_down(self):
        for ship in self.ships:
            ship.move_down(10)

    def change_direction(self):
        self.direction *= -1

    def move_over(self):
        for ship in self.ships:
            ship.move_over(self.direction * self.speed)

    def remove_dead_ships(self):
        for i in range(len(self.ships) -1, -1, -1):
            if self.ships[i].is_alive == False:
                self.ships.pop(i)