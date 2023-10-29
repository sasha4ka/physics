import pygame
from id_list import id_list

class game:
    def __init__(self, win, caption):
        self.win = pygame.display.set_mode(win)
        pygame.display.set_caption(caption)

class Event:
    pass

class IObject:
    def __init__(): pass
    def update(deltatime: float): pass
    def draw(win: pygame.surface.Surface): pass
    def listener(event: Event): pass

class object():
    def __init__(self, pos: list[float], size:list[float], master: game):
        self.rect = pygame.rect.Rect(*pos, *size)
        self.master = master

class physics_object(object):
    def __init__(self, pos: list[float], size: list[float], physics: dict, master: game):
        self.rect = pygame.rect.Rect(*pos, *size)
        self.physics = physics
        self.master = master