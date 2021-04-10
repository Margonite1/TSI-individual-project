from data import savechar, is_testing
from src import load_adapter, name_adapt
from src.char_gen import stats
from src.roll_weapon import roll_damage

def options():
    option = input("do you wish to load a character(1) or make a new one(2)")
    return option

def load_or_new(options):
    testing = is_testing.is_testing()
    load_vs_new = options
    if load_vs_new == "1":
        character = load_adapter.load_adapt()
        return character
    elif load_vs_new == "2":
        character = [name_adapt.name(), stats()]
        print(character)
        if testing == True:
            if_save = "NO"
        else:
            if_save = input("do you wish to save your character?(Yes/No)")
            if_save = if_save.upper()
        if if_save == "YES":
            savechar.save(character)
            print("character saved")
        else:
            print("character not saved")
        return character
    else:
        print("Please select valid option")
        load_or_new(load_vs_new)
