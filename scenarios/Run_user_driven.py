from src import roll_weapon, load_new

#to ensure full funtionality have is_testing return True

options = load_new.options()
character = load_new.load_or_new(options)
roll_weapon.roll_damage(character)
roll_weapon.roll_damage(character)