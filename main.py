import time
import pygame
import game
import math

my_game = game.Game((500, 500), "Physics game", 60)
obj = game.Physics_object([250, 250], [50, 50], (255, 0, 255), {"weight":2}, my_game)
my_game.add_object(obj, time.time())
obj = game.Physics_object([250, 180], [25, 25], (0, 0, 0), {"weight":4}, my_game)
my_game.add_object(obj, time.time())
platform = game.Base_object([20, 480], [460, 20], (80, 80, 80), my_game)
my_game.add_object(platform, time.time())
my_game.main()