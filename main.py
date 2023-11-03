import time
import pygame
import game
import math

my_game = game.Game((500, 500), "Physics game", 60)
obj = game.Physics_object([250, 250], [50, 50], {"weight":2}, my_game)
my_game.add_object(obj, time.time())
obj = game.Physics_object([200, 200], [25, 25], {"weight":4}, my_game)
my_game.add_object(obj, time.time())
my_game.main()