from src.char_stat_roll import stat_roller
from src.select_stat import all_stats


def char_name():
    name = input("please input the characters name. ")
    return name

def stats():
    stat_array = {"STR":0, "DEX":0, "CON":0, "WIS":0, "INT":0,"CHA":0}
    stats = stat_roller()
    stat_index = 0
    stat_style = 0
    while stat_style != "1" or stat_style != "2":
        stat_style = input("Do you wish to select what dice roll you want in each stat(1) or do you want stats added as rolled(2)? ")
        if stat_style == "1":
            all_stats(stats, stat_array)
            break
        elif stat_style == "2":
            for key, value in stat_array.items():
                stat_array[key] = stats[stat_index]
                stat_index += 1
            break
        else:
            print("invalid input")
    return stat_array
