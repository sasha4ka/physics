import pygame

class IObject:
    def __init__(): pass
    def update(deltatime: float): pass
    def draw(win: pygame.surface.Surface): pass
    def listener(event: Event): pass

class Object(IObject):
    def __init__(self, pos: list[float], size:list[float], master: Game):
        self.rect = pygame.rect.Rect(*pos, *size)
        self.master = master

class Physics_object(Object):
    def __init__(self, pos: list[float], size: list[float], physics: dict, master: Game):
        self.rect = pygame.rect.Rect(*pos, *size)
        self.physics = physics
        self.master = master