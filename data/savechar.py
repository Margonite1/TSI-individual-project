import json

def save(character):
    name = character[0]
    path = "../save_data\\"
    extention = ".json"
    stats = character[1]
    filepath = path + name + extention
    with open(filepath, 'w') as char_save:
        json.dump(stats, char_save)

