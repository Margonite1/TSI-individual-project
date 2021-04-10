def load(name):
    if name == "Zug":
        return {"STR": 12, "DEX": 8, "CON": 9, "WIS": 13, "INT": 12, "CHA": 10}
    elif name == "Samson":
        return {'STR': 10, 'DEX': 18, 'CON': 9, 'WIS': 13, 'INT': 16, 'CHA': 12}
    elif name == "Panic":
        return {'STR': 10, 'DEX': 15, 'CON':14, 'WIS': 13, 'INT': 10, 'CHA': 18}
    else:
        return {'STR': 'test', 'DEX': 'test', 'CON': 'test', 'WIS': 'test', 'INT': 'test', 'CHA': 'test'}