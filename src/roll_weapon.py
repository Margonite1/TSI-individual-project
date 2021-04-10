from data.database_stub import database_weapons
from src.dice import roll_dice
from src.show_weapons_spells import weapons_spell_list

def roll_damage(character, weapon=0):
    valid_choice = False
    weapon_list = weapons_spell_list()
    if weapon in weapon_list:
        valid_choice = True
    weapon_dict = database_weapons()

    while valid_choice == False:
        print(weapon_list)
        weapon = input("select what you want to use ")
        if weapon in weapon_list:
            valid_choice = True
        else:
            print("Not a valid option")
    damage_dice = roll_dice(weapon_dict[weapon][0], weapon_dict[weapon][1])
    character_stat = character[1]
    modifier_stat = character_stat[weapon_dict[weapon][2]]
    modifier = (modifier_stat - 10)//2
    final_damage = damage_dice + modifier
    print(final_damage)
    return final_damage
