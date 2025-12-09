from familiar.familiar import dice_roll, get_modifier, roll_character_stats


def test_dice_roll():
    roll = dice_roll(2, 6, 0)
    print(roll)
    assert roll <= 12


def test_get_modifier():
    mod = get_modifier(12)
    assert mod == 1


def test_get_modifier_big_int():
    mod = get_modifier(18)
    assert mod == 4


def test_negative_get_modifier():
    mod = get_modifier(8)
    assert mod == -1


def test_negative_get_modifier_on_big_int():
    mod = get_modifier(4)
    assert mod == -3


def test_roll_character_stats_returns_dict():
    stats = roll_character_stats()
    assert isinstance(stats, dict)
    assert len(stats) == 6
    expected_keys = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    assert list(stats.keys()) == expected_keys


def test_roll_character_stats_values_in_valid_range():
    stats = roll_character_stats()
    for stat_name, value in stats.items():
        assert 3 <= value <= 18, f"{stat_name} value {value} is out of valid range (3-18)"


def test_roll_character_stats_array_mode():
    stats = roll_character_stats(assign_stats=False)
    assert isinstance(stats, list)
    assert len(stats) == 6
    for value in stats:
        assert 3 <= value <= 18, f"Stat value {value} is out of valid range (3-18)"
