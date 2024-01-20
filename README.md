# My physics engine
Hello. My name is Sasha. This is my physics engine. It's write in python.<br>
## Using:
1. Pygame
1. Time (integrated in python)
## Documentation
### Game:
It's a main game class. Updates and draws object and responsible for game window.
#### Creating:
```python
import game.game_class
from game.other import Window_options, Game_options, Color

my_window_options = Window_options()
my_window_options.name = "My game"
my_window_options.width = 1000
my_window_options.height = 700
my_window_options.background = Color(0, 0, 0)

my_game = game.game_class(
    window_options = my_window_options,
    game_options = my_game_options
)
```