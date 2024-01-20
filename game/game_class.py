import time
import pygame
import game.other
import game.game_objects

class game_class:
    '''Primary game class'''
    def __init__(
            self,
            *,
            window_options: game.other.Window_options,
            game_options: game.other.Game_options,
            object_list: list[game.game_objects.IGame_object] = []
    ) -> None:
        self._game_options = game_options
        self._window_options = window_options

        self._window_init(window_options)
        self._objects_init(object_list)

        self.run = True
        self.timer = pygame.time.Clock()
    
    def _window_init(self, window_options: game.other.Window_options):
        self.win = pygame.display.set_mode(
            (window_options.width, window_options.height), 
            *window_options.settings
        )
        self.window_points = {
            "topleft": pygame.Vector2(0, 0),
            "bottomleft": pygame.Vector2(0, window_options.height),
            "topright": pygame.Vector2(window_options.width, 0),
            "bottomright": pygame.Vector2(window_options.width, window_options.height),
            "center": pygame.Vector2(window_options.width // 2, window_options.height // 2)
        }
    
    def _objects_init(self, object_list: list[game.game_objects.IGame_object]):
        self.object_list = object_list
        start_time = time.time()

        for game_object in self.object_list:
            game_object.last_update = start_time
    

    def add_object(self, game_object: game.game_objects.IGame_object):
        '''Adds object to the game'''
        self.object_list.append(game_object)
        game_object.last_update = time.time()

    def delete_object(self, game_object: game.game_objects.IGame_object):
        '''Deletes object from the game'''
        self.object_list.remove(game_object)

    def change_framerate(self, framerate: int):
        '''Changes games framerate'''
        self._game_options.framerate = framerate

    def start(self):
        '''Starts the game mainloop'''
        self._mainloop()
    
    def close(self):
        '''Closes the game'''
        pygame.quit()
        self.run = False


    def _events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.run = False

    def _update(self):
        update_time = time.time()
        for game_object in self.object_list:
            game_object.update(update_time - game_object.last_update)
            game_object.last_update = update_time

    def _draw(self):
        self.win.fill(self._window_options.background.get)
        for game_object in self.object_list:
            game_object.draw(self.win)
        pygame.display.flip()

    def _mainloop(self):
        while self.run:
            self._events()
            self._update()
            self._draw()
            self.timer.tick(self._game_options.framerate)