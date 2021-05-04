from random import randint
def roll_dice(modifier = 0, number_of_dice = 1, sides_of_dice = 20):
    #xdy - x > number of dice, and y > number of sides
    #1d20 -> 1 20 sided die
    #3d6 -> 3 6 sided die
    total = 0

    for i in range(0,number_of_dice):
        total += randint(1, sides_of_dice)
    return total

def character_stat_roll():
    return roll_dice(number_of_dice = 3, sides_of_dice = 6)

stats = ['str', 'con', 'dex', 'int', 'cha', 'wis']
character = {}

for stat in stats:
    character[stat] = character_stat_roll()

print(character)
