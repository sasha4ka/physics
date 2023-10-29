import objects
import pygame
from id_list import id_list

class Game:
    def __init__(self, win: list[int], caption: str):
        self.win = pygame.display.set_mode(win)
        pygame.display.set_caption(caption)

        self.object_list = []
        self.run = True

        self.update()

    def main(self):
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False

    def update(self): pass
    def add_listener(self, listener, event_type: list[str]): pass
    def get_objects(self, distance: float = -1) -> list[objects.Object]: pass
    def create_object(self, object: objects.Object) -> objects.Object: pass
    def delete_object(self, object: objects.Object) -> objects.Object: pass
    def get_keys(self) -> list: pass
    def get_mouse(self) -> list: pass

class Event:
    def __init__(self, event_type: str):
        self.type = event_type