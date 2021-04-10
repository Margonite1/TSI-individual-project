from data.database_stub import database_weapons
def weapons_spell_list():
    weapons_and_spells = database_weapons()
    weapons_and_spells_list = list(weapons_and_spells.keys())
    return weapons_and_spells_list