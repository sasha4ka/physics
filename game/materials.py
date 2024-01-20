'''Contains data of all the materials in the game'''

from game.other import Material, Color

Iron: Material = Material()
Iron.name = "iron"
Iron.color = Color(207, 208, 210)
Iron.density = 7800

Ice: Material = Material()
Ice.name = "ice"
Ice.color = Color(31, 96, 135)
Ice.density = 917