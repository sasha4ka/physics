import pygame
from game.game_class import game_class
from game.game_objects import Game_object
from game.other import Physics_settings, Window_options, Game_options, Color, Material
from game.materials import Iron


def main():
    my_window_options = Window_options()
    my_window_options.name = "My game"
    my_window_options.width = 1000
    my_window_options.height = 500
    my_window_options.background = Color(135, 206, 235)

    my_game_options = Game_options()
    my_game_options.framerate = 40

    my_game = game_class(
        window_options=my_window_options,
        game_options=my_game_options
    )

    my_physics_settings = Physics_settings()
    my_physics_settings.material = Material()
    my_physics_settings.name = "My object"

    my_object = Game_object(
        master = my_game,
        position = my_game.window_points["center"],
        sizes = pygame.Vector2(200, 200),
        physics_settings = my_physics_settings
    )

    my_game.add_object(my_object)

    my_game.start()

if __name__ == "__main__": main()