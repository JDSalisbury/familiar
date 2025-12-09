from . import settings


def dice_roll(number_of_dice, dice_sides, mod):
    import random
    total = 0
    for i in range(1, number_of_dice + 1):
        total += random.randint(1, dice_sides)
    return total + mod


def get_modifier(stat):
    mod = stat - 10
    mod = mod / 2
    return round(mod)


def roll_character_stats(assign_stats=True):
    import random
    stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    stat_values = []

    for _ in range(6):
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        stat_values.append(sum(rolls))

    if assign_stats:
        return dict(zip(stats, stat_values))
    else:
        return stat_values


def get_game_version():
    return settings.VERSION

