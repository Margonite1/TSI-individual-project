from src.dice import roll_dice, roll_die

def stat_roller():
    stats = []
    char_roller = input("Do you wish to roll using 3d6(1) or 4d6 drop the lowest(2) " )
    if char_roller == "1":
        for number in range(6):
            character_stat = roll_dice(3,6)
            stats.append(character_stat)
        return stats
    elif char_roller == "2":
         for number in range(6):
            four_dice = []
            for another_number in range(4):
                four_die = roll_die(6)
                four_dice.append(four_die)
            four_dice.sort()
            del four_dice[0]
            character_stat = sum(four_dice)
            stats.append(character_stat)
         return stats
    else:
        print("invalid input")
        stat_roller()
