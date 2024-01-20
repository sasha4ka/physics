import pygame
import game.game_class
import game.other

class IGame_object:
    rect: pygame.Rect
    position: pygame.Vector2
    last_update: float
    
    def __init__(): pass
    def update(dt: float): pass
    def draw(surface: pygame.Surface): pass
    def add_velocity(velocity: pygame.Vector2): pass
    def add_force(force: pygame.Vector2): pass
    @property
    def all_velocity(): pass
    @property
    def all_force(): pass
    @property
    def mass(): pass
    @property
    def volume(): pass
    @property
    def density(): pass

class Game_object:
    last_update: float

    '''Game object class'''
    def __init__(
            self,
            *,
            master,
            position: pygame.Vector2,
            sizes: pygame.Vector2,
            physics_settings: game.other.Physics_settings,
    ) -> None:
        self.master = master
        self.position = position
        self.width, self.height = sizes.x, sizes.y
        self._physics_settings = physics_settings
        self.rect = pygame.Rect(
            self.position.x, 
            self.position.y, 
            self.width,
            self.height
        )
    
    def update(self, dt: float):
        '''Updates state of game object'''
        self.rect.topleft = self.position

    def draw(self, surface: pygame.Surface):
        '''Draws game object to surface'''
        pygame.draw.rect(
            surface,
            self._physics_settings.material.color.get,
            self.rect
        )
        
    @property
    def mass(self): self.volume * self.density
    @property
    def volume(self): return self.width * self.height * game.other.depth / (game.other.ceil ** 3)
    @property
    def density(self): return self._physics_settings.material.density