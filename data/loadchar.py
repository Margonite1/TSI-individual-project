import json
import os
from data import is_testing, loadfake


def load(file=0):
    testing = is_testing.is_testing()
    if file == 0:
        saved_data = os.listdir('../save_data')
        print(saved_data)
        name_of_file = input("select a file to load (extension not needed) ")
    else:
        name_of_file = file
    path = "../save_data\\"
    extension = ".json"
    filepath = path + name_of_file + extension
    if testing == True:
        load_data = loadfake.load(file)
        character = [name_of_file, load_data]
        return character
    try:
        with open(filepath) as char_load:
            load_data = json.load(char_load)
        character = [name_of_file, load_data]
        return character
    except FileNotFoundError:
        print("there is no such file, please select an actual file")
        load()
