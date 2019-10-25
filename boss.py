from game_object import Game_Object
from enemybullet import EnemyBullet

class Boss(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        super().__init__(image, x_coordinate, y_coordinate)
