# File name-Base game.py

import random
import time
from Classes import *
from init_fights import *


def get_time(start, text):
    # Gets final time and calculates time passed
    time_end = time.time()
    time_sec = int(time_end - start)

    m, s = divmod(time_sec, 60)

    print(text.format(minutes=m, seconds=s))


def show_map(player_pos, visualizer):
    # -- Shows the map --
    y_pos = visualizer[player_pos[1]].split("-")
    if "P" in y_pos[player_pos[0]]:
        y_pos[player_pos[0]] = y_pos[player_pos[0]].replace("P", "\033[94m*\033[0m")
    else:
        y_pos[player_pos[0]] = y_pos[player_pos[0]].replace(" ", "\033[94m*\033[0m")
    player = ""
    for i in range(len(y_pos)):
        if i != 0 and i != len(y_pos):
            player = player + "-" + y_pos[i]
        else:
            player = player + y_pos[i]
    visualizer[player_pos[1]] = player

    for i in range(len(visualizer)):
        print(visualizer[i])


def check_move(player_pos, visualizer, map_number, keys):
    # -- Checks the space the Player is going to --
    # - This part is for battles/items -
    with open("txt files/map2.txt", "r") as maps:
        line_2 = maps.read().split("|")
    vis = line_2[map_number].split("\n")
    y = vis[player_pos[1] + 1].split("-")

    y_pos = visualizer[player_pos[1]].split("-")
    if "x" in y_pos[player_pos[0]]:
        return "wall"
    elif "N" in y_pos[player_pos[0]]:
        if "B" in y[player_pos[0]]:
            remove_char(y, player_pos, vis, map_number, "B")

            return "boss"
        else:
            return "up"
    elif "P" in y_pos[player_pos[0]]:
        return "down"
    else:
        if "E" in y[player_pos[0]]:
            remove_char(y, player_pos, vis, map_number, "E")

            return "monster"

        elif "F" in y[player_pos[0]]:
            replace_char(y, player_pos, vis, map_number, "F", "E")

            return "monster"

        elif "I" in y[player_pos[0]]:
            remove_char(y, player_pos, vis, map_number, "I")

            return "item"
        elif "2" in y[player_pos[0]]:
            replace_char(y, player_pos, vis, map_number, "2", "I")

            return "item"

        elif "S" in y[player_pos[0]]:

            return "shop"

        elif "CR" in y[player_pos[0]]:
            remove_char(y, player_pos, vis, map_number, "CR")

            return "chest"

        elif "R" in y[player_pos[0]]:
            remove_char(y, player_pos, vis, map_number, "R")

            return "rest"

        elif "D" in y[player_pos[0]]:
            if keys == 0:
                print("A mysterious barrier blocks your path...")
                time.sleep(1)
                print("[1] Key needed")
                time.sleep(1)

                return "wall"

            else:
                print("Key used to open barrier!")
                time.sleep(1)

                remove_char(y, player_pos, vis, map_number, "D")

                return "decrease"

        elif "K" in y[player_pos[0]]:
            print("You found a key!")
            time.sleep(1)

            remove_char(y, player_pos, vis, map_number, "K")

            return "increase"
        else:
            return " "


def remove_char(y, player_pos, vis, map_num, char):
    y[player_pos[0]] = y[player_pos[0]].replace(char, " ")
    player = ""
    for i in range(len(y)):
        if i != 0 and i != len(y):
            player = player + "-" + y[i]
        else:
            player = player + y[i]
    vis[player_pos[1] + 1] = player
    player = ""
    for i in range(len(vis)):
        if i != 0 and i != len(vis):
            player = player + "\n" + vis[i]
        else:
            player = player + vis[i]

    with open("txt files/map2.txt", "r") as map_test:
        lines = map_test.read().split("|")

    lines.insert(map_num, player)
    lines.pop(map_num + 1)
    player = ""

    for i in range(len(lines)):
        if i != 0 and i != len(lines):
            player = player + "|" + lines[i]
        else:
            player = player + lines[i]

    var = open("txt files/map2.txt", "w")
    var.write(player)
    var.close()


def replace_char(y, player_pos, vis, map_num, old, new):
    y[player_pos[0]] = y[player_pos[0]].replace(old, new)
    player = ""
    for i in range(len(y)):
        if i != 0 and i != len(y):
            player = player + "-" + y[i]
        else:
            player = player + y[i]
    vis[player_pos[1] + 1] = player
    player = ""
    for i in range(len(vis)):
        if i != 0 and i != len(vis):
            player = player + "\n" + vis[i]
        else:
            player = player + vis[i]

    with open("txt files/map2.txt", "r") as map_test:
        lines = map_test.read().split("|")

    lines.insert(map_num, player)
    lines.pop(map_num + 1)
    player = ""

    for i in range(len(lines)):
        if i != 0 and i != len(lines):
            player = player + "|" + lines[i]
        else:
            player = player + lines[i]

    var = open("txt files/map2.txt", "w")
    var.write(player)
    var.close()


def refresh_map(map_number):
    # -- Resets the map or else the player will appear on all previous spots --
    with open("txt files/map.txt", "r") as maps:
        lines = maps.read().split("|")
    visualizer = lines[map_number].split("\n")
    visualizer.pop(0)
    visualizer.pop(0)
    return visualizer


def choose_path(map_number, player):
    # -- Opens .txt file --
    with open("txt files/map.txt", "r") as maps:
        lines = maps.read().split("|")
    # I don't like looking at this, but it is necessary for it to work.
    visualizer = lines[map_number].split("\n")
    player_pos = visualizer[1].split(" ")
    player_pos[0] = int(player_pos[0])
    player_pos[1] = int(player_pos[1])
    dimensions = visualizer[0].split(" ")
    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])
    visualizer.pop(0)
    visualizer.pop(0)
    keys = 0
    print(f"Which way do you want to go? (controls: W) up, S) down, A) left, D) right, i) Inventory\n[F{map_number}]")
    show_map(player_pos, visualizer)
    while True and player.h > 0:
        # -- Resets Map --
        visualizer = refresh_map(map_number)
        # -- Controls --
        check = "Nan"
        ask = input(">")
        pyautogui.hotkey("shift", "c")

        if ask.upper() == "W":
            if player_pos[1] > 0:
                check = check_move((int(player_pos[0]), (int(player_pos[1]) - 1)), visualizer, map_number, keys)
                if check == "up" or check == "down" or check == " " or check == "monster" or check == "item" or check == "boss" or check == "increase" or check == "decrease" or check == "chest" or check == "rest" or check == "shop":
                    player_pos[1] -= 1
                else:
                    print("Can't move here...")
                    time.sleep(1)
            else:
                print("Can't move here...")
                time.sleep(1)

        elif ask.upper() == "S":
            if player_pos[1] < dimensions[1]:
                check = check_move((int(player_pos[0]), (int(player_pos[1]) + 1)), visualizer, map_number, keys)
                if check == "up" or check == "down" or check == " " or check == "monster" or check == "item" or check == "boss" or check == "increase" or check == "decrease" or check == "chest" or check == "rest" or check == "shop":
                    player_pos[1] += 1
                else:
                    print("Can't move here...")
                    time.sleep(1)
            else:
                print("Can't move here...")
                time.sleep(1)

        elif ask.upper() == "A":
            if player_pos[0] > 0:
                check = check_move(((int(player_pos[0]) - 1), int(player_pos[1])), visualizer, map_number, keys)
                if check == "up" or check == "down" or check == " " or check == "monster" or check == "item" or check == "boss" or check == "increase" or check == "decrease" or check == "chest" or check == "rest" or check == "shop":
                    player_pos[0] -= 1
                else:
                    print("Can't move here...")
                    time.sleep(1)
            else:
                print("Can't move here...")
                time.sleep(1)

        elif ask.upper() == "D":
            if player_pos[0] < dimensions[0]:
                check = check_move(((int(player_pos[0]) + 1), int(player_pos[1])), visualizer, map_number, keys)
                if check == "up" or check == "down" or check == " " or check == "monster" or check == "item" or check == "boss" or check == "increase" or check == "decrease" or check == "chest" or check == "rest" or check == "shop":
                    player_pos[0] += 1
                else:
                    print("Can't move here...")
                    time.sleep(1)
            else:
                print("Can't move here...")
                time.sleep(1)

        elif ask.upper() == "INVENTORY" or ask.upper() == "I":
            player.inventory_check_use()

        else:
            match ask.upper().split(" "):
                case ["COMMAND", command]:
                    match command:
                        case ["GIVE", item]:
                            player.inventory_add(item.lower())
                        case ["HEAL", num]:
                            player.heal(int(num))
                        case ["INFLICT", status]:
                            player.activate_status(status.lower(), 5)

            print("Please enter one of the actions. (controls: W) up, S) down, A) left, D) right)")

        # -- Shows Map/Exits Loop --
        if check == "up":
            return "up"
        elif check == "down":
            return "down"
        else:
            if check == "monster":
                enemy = get_enemy(map_number)
                mock_fight(enemy, player)
                print(f"[F{map_number}]")
                show_map(player_pos, visualizer)
            elif check == "item":
                player.inventory_add(get_loot(map_number))
                print(f"[F{map_number}]")
                show_map(player_pos, visualizer)
            elif check == "boss":
                enemy = get_boss(map_number)
                mock_fight(enemy, player)
                print("BOSS")
                return "up"
            elif check == "rest":
                rest_room(player)
            elif check == "chest":
                chest_room(player, "Chest Mimic")
            elif check == "shop":
                shop(player, map_number)
            else:
                if check == "increase":
                    keys += 1
                elif check == "decrease":
                    keys -= 1
                print(f"[F{map_number}]")
                show_map(player_pos, visualizer)


def main(player):
    # -- Controls # of floor
    with open("txt files/map.txt", "r") as thing:
        maps = thing.read().split("|")
    floor = 0
    while floor < len(maps) and player.h > 0:
        traverse = choose_path(floor, player)
        if traverse == "up":
            floor += 1
        else:
            floor -= 1
    return floor


with open("txt files/map2save.txt", "r") as save:
    lines = save.read()
reset = open("txt files/map2.txt", "w")
reset.write(lines)
reset.close()

# -- Player set-up --

player = tutorial()


def thing():
    print("Welcome to the Tower of Hostility!")
    time.sleep(2)
    print("You will be able to move through rooms to fight enemies!")
    time.sleep(2)
    print("You will be marked with a \033[96m*\033[0m on the map.")
    print("[ ]-[ ]-[\033[96m*\033[0m]-[ ]")
    print("  Player ^")
    time.sleep(2.5)
    print("You will also be unable to move into tiles with an [x] inside.")
    time.sleep(2)
    print("Your goal will be to reach the [N] tile!")
    time.sleep(2)
    print("You will also be able to go back to floors you have cleared previously by moving to a [P] tile!")
    time.sleep(2)
    print("You will also be able to have access to your inventory at any time by typing 'Inventory' or 'I'!")
    time.sleep(2)
    print("Good luck!")
    time.sleep(1)


# -- Starts main loop --
time_check = "Final Time: {minutes} min and {seconds} seconds."
time_start = time.time()

while True:
    ask = input("Do you want the tutorial?\n")

    if ask.upper() == "YES":
        thing()
        break
    elif ask.upper() == "NO":
        break
    else:
        print("Please enter yes or no.")
        time.sleep(1)

f = main(player)
time.sleep(1)
if player.h < 1:
    print("You died :(")
    time.sleep(1)
    print(f"Died on floor [{f}]")
    time.sleep(1)
    get_time(time_start, time_check)
else:
    print("Congratulations on reaching the peak of the tower(so far)!")
