depth = 100
ceil = 100

class Color:
    r: int
    g: int
    b: int
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    @property
    def get(self) -> list[int]:
        return [self.r, self.g, self.b]

class Colors:
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 0, 255)
    black = Color(0, 0, 0)
    white = Color(255, 255, 255)

    purple = Color(255, 0, 255)

class Material:
    name: str
    density: float
    color: Color

    def __init__(self):
        self.name = "404"
        self.density = 10**6
        self.color = Colors.purple

class Physics_settings:
    name: str
    material: Material

    def __init__(self):
        self.name = "Object"
        self.material = Material()

class Window_options:
    name: str
    width: int
    height: int
    settings: list
    background: Color

    def __init__(self):
        self.name = "Physics"
        self.width = 300
        self.height = 100
        self.settings = []
        self.background = Color(0, 0, 0)

class Game_options:
    framerate: int

    def __init_(self):
        self.framerate = 20