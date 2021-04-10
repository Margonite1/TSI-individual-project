import random
import data.is_testing
def roll_die(sides):
    sides = int(sides)
    roll = random.randint(1,sides)
    testing = data.is_testing.is_testing()
    if testing == True:
        roll = sides
    return roll

def roll_dice(number, sides):
    total = 0
    while number > 0:
        roll = roll_die(sides)
        total += roll
        number -= 1
    return total
