from Classes import *


def set1(call):
    # tutorial monsters
    if call == 1:
        monster = Monster("Training dummy", "normal", '', 20, 1, 0, 0, 15, 42, ('standing still',
                                                                                'lifeless stare',
                                                                                'the fact that it is '
                                                                                'a dummy to stand still'), (0, 0, 0), )

    if call == 2:
        monster = Monster("Slime (s)")
        return monster


def set2(call):
    # F1 monsters
    if call == 1:
        monster = Monster()
        return monster

    elif call == 2:
        monster = Monster()
        return monster

    elif call == 3:
        monster = Monster()
        return monster

    elif call == 4:
        monster = Monster()
        return monster

