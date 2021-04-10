from data import loadchar
from src import roll_weapon

#to ensure full funtionality have is_testing return True

character = loadchar.load("Zug")
roll_weapon.roll_damage(character, "Axe")
roll_weapon.roll_damage(character, "Firebolt")