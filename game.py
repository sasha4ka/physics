import math
import time
import pygame
from id_list import id_list

class Game: pass
class Event: pass
class Object:
    def __init__(self, pos: list[float], size: list[float], master: Game): pass
    def update(self, deltatime: float): pass
    def draw(self, win: pygame.surface.Surface): pass
    def listener(self, event: Event): pass
    def on_start(self): pass
    def add_velocity(self, name, velocity): pass
    def remove_velocity(self, name): pass
    def add_force(self, name, force): pass
    def remove_force(self, name): pass

#maincode
class Game:
    def __init__(self, win: list[int], caption: str, tickrate: int):
        pygame.init()
        self.win = pygame.display.set_mode(win)
        pygame.display.set_caption(caption)

        self.win_size = win

        self.object_list: list[list[Object, float]] = []
        self.run = True

        self.tickrate = tickrate

        self.clock = pygame.time.Clock()

    def main(self):
        for obj in self.object_list:
            obj[0].on_start()

        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
            
            self.update()
            self.draw()

            self.clock.tick(self.tickrate)

    def update(self):
        for i in range(len(self.object_list)):
            start = self.object_list[i][1]
            end = time.time()
            self.object_list[i][0].update(end - start)
            self.object_list[i][1] = end
    
    def draw(self):
        self.win.fill((200, 200, 200))

        for obj in self.object_list:
            obj[0].draw(self.win)
        
        pygame.display.flip()

    def add_listener(self, listener, event_type: list[str]): pass

    def get_objects(self, distance: float = -1) -> list[Object]: pass

    def add_object(self, new_object: Object, runtime: float) -> Object:
        self.object_list.append([new_object, runtime])

    def delete_object(self, new_object: Object) -> Object: pass

    def get_keys(self) -> list: pass

    def get_mouse(self) -> list: pass

    def get_win(self) -> list:
        return self.win_size


class Event:
    def __init__(self, event_type: str):
        self.type = event_type

class Velocity:
    def __init__(self, value, direction):
        self.value = value
        self.direction = direction
    
    def module_in_metres(self):
        return self.value

    def module_in_pixels(self):
        return self.value * 10
    
    def angle_in_radians(self):
        return self.direction
    
    def angle_in_degrees(self):
        return math.degrees(self.direction)
    
    def in_xy(self):
        return self.value * math.cos(self.direction), self.value * math.sin(self.direction)
    
    #todo
    def __iadd__(self, other):
        self.value += other.value

class Force:
    def __init__(self, value, direction):
        self.value = value
        self.direction = direction

class Base_object(Object):
    def __init__(self, pos: list[float], size:list[float], master: Game):
        self.rect = pygame.rect.Rect(*pos, *size)
        self.master = master
    
    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, (50, 50, 200), self.rect)

class Physics_object(Base_object):
    def __init__(self, pos: list[float], size: list[float], physics: dict, master: Game):
        self.rect = pygame.rect.Rect(*pos, *size)
        self.pos = pos
        self.master = master
        self.physics = physics
        self.velocities: dict[str: Velocity] = {"gravity":Velocity(0, math.radians(90))}
        self.forces: dict[str: Force] = {}
        self.bottom = self.master.get_win()[1]
        self.can_fall = True
    
    def update(self, deltatime: float):
        if self.pos[1] + self.rect.height < self.bottom - 10:
            self.add_force("gravity", Force(self.physics["weight"]*10, math.radians(90)))
            self.can_fall = True

        elif self.pos[1] + self.rect.height >= self.bottom - 10:
            self.remove_force("gravity")
            self.velocities["gravity"].value = 0
            self.can_fall = False

        self.math_forces(deltatime)
        self.math_velocities(deltatime)

    def add_velocity(self, name, velocity):
        self.velocities.update({name: velocity})
    
    def remove_velocity(self, name):
        if name in list(self.velocities.keys()): self.velocities.pop(name)
    
    def add_force(self, name, force):
        if name in list(self.forces.keys()): return
        self.forces.update({name: force})

    def remove_force(self, name):
        if name in list(self.forces.keys()): self.forces.pop(name)

    def math_velocities(self, deltatime: float):
        for v in self.velocities.values():
            vx, vy = v.in_xy()
            self.pos[0] += vx * 10 * deltatime
            if self.can_fall and vy > 0: self.pos[1] += vy * 10 * deltatime

    def math_forces(self, deltatime: float):
        for i in range(len(self.forces)):
            name = list(self.forces.keys())[i]
            force: Force = list(self.forces.values())[i]
            
            self.velocities[name].value += force.value * deltatime / self.physics["weight"]

    def draw(self, win):
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
        pygame.draw.rect(win, (20, 100, 200), pygame.Rect(*self.pos, self.rect.width, self.rect.height))