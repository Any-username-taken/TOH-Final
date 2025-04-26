# File name-init_fights.py

import time
import random
import pyautogui
from TOH.Classes import *


with open("txt files/shop_buy.txt", "r") as items:
    items = items.read().split("|")

items.pop(0)

shop_f2 = items[0].split("\n").pop(0)
shop_f4 = items[1].split("\n").pop(0)


r_loot = ["Strength Potion [s]", "Strength Potion [m]", "Strength Potion [l]", "Health Potion [s]", "Health Potion [m]",
          "Health Potion [l]", "Health Potion [XL]", "Tome of Power", "Antidote", "Suspicious Stew [p]",
          "Suspicious Stew [r++]", "Enchiridion of Forbidden Power", "Regen Potion [s]", "Tome of Vitality",
          "Mana Potion [s]", "Sturdy Potion [s]", "Sturdy Potion [m]"]
f1_lootPool = ["Strength Potion [s]", "Mana Potion [s]", "Regen Potion [s]"]
f2_lootPool = ["Strength Potion [s]", "Health Potion [s]", "Mana Potion [s]"]
f3_lootPool = ["Health Potion [s]", "Mana Potion [s]", "Suspicious Stew [r++]", "Health Potion [s]", "Mana Potion [s]"]
f4_lootPool = ["Antidote", "Suspicious Stew [p]", "Health Potion [m]"]
loot = {0: f1_lootPool, 1: f2_lootPool, 2: f3_lootPool, 3: f3_lootPool, 4: f4_lootPool, 5: r_loot}


def tutorial():
    n = input("Please enter your name:\n")
    spells = []
    loop = True
    while loop:
        w = input("Choose your weapon:\n[1] Wooden Sword\n[2] Wooden Shield\n[3] Rusty Dagger\n[4] Bow\n")#[5] Magic Stick\n")

        if w.upper() == "WOODEN SWORD" or w.upper() == "1":
            print("Wooden Sword unlocks PATH OF THE KNIGHT, which is an all rounded class.")
            time.sleep(1)
            print("You will not be able to change your choice later...")
            time.sleep(1)
            while True:
                ans = input("Are you sure you want to choose the Wooden Sword?\n")
                if ans.upper() == "YES":
                    weapon, type_p, type_c, maxh, defense, base_dmg, dodge, will, mana = ('wooden sword', ["normal"],
                                                                                          '\033[1mKNIGHT\033[0m ', 50, 0,
                                                                                          0, 5, 100, 50)
                    loop = False
                    break
                elif ans.upper() != "NO":
                    print("Please enter yes or no.")
                else:
                    break

        elif w.upper() == "WOODEN SHIELD" or w.upper() == "2":
            print("Wooden Shield unlocks PATH OF THE PALADIN, which is a tanky class.")
            time.sleep(1)
            print("You will not be able to change your choice later...")
            time.sleep(1)
            while True:
                ans = input("Are you sure you want to choose the Wooden Shield?\n")
                if ans.upper() == "YES":
                    weapon, type_p, type_c, maxh, defense, base_dmg, dodge, will, mana, spells = ('wooden shield', ["holy",
                                                                                                            "light"],
                                                                                          '\033[1mPALADIN\033[0m ', 75,
                                                                                          3, 0, 5, 150, 50, ["holy circle"])
                    loop = False
                    break
                elif ans.upper() != "NO":
                    print("Please enter yes or no.")
                else:
                    break

        elif w.upper() == "RUSTY DAGGER" or w.upper() == "3":
            print("Rusty Dagger unlocks PATH OF THE ASSASSIN, which is a light class.")
            time.sleep(1)
            print("You will not be able to change your choice later...")
            time.sleep(1)
            while True:
                ans = input("Are you sure you want to choose the Rusty Dagger?\n")
                if ans.upper() == "YES":
                    weapon, type_p, type_c, maxh, defense, base_dmg, dodge, will, mana, spells = ('rusty dagger', ["trickster"],
                                                                                          '\033[1mASSASSIN\033[0m ', 35,
                                                                                          0, 0, 25, 100, 50, ["shadow step"])
                    loop = False
                    break
                elif ans.upper() != "NO":
                    print("Please enter yes or no.")
                else:
                    break

        elif w.upper() == "BOW" or w.upper() == "4":
            print("Bow unlocks PATH OF THE ARCHER, which is a speedy class.")
            time.sleep(1)
            print("You will not be able to change your choice later...")
            time.sleep(1)
            while True:
                ans = input("Are you sure you want to choose the Bow?\n")
                if ans.upper() == "YES":
                    weapon, type_p, type_c, maxh, defense, base_dmg, dodge, will, mana, spells = ('bow', ["life"],
                                                                                          '\033[1mARCHER\033[0m ', 35,
                                                                                          0, 0, 12, 75, 50, ["flaming arrow"])
                    loop = False
                    break
                elif ans.upper() != "NO":
                    print("Please enter yes or no.")
                else:
                    break

    if not spells:
        spells = []

    player = Player(n, type_p, type_c, maxh, defense, base_dmg, dodge, will, mana, "", "", 0, weapon, spells)
    return player


def get_mimic(form):
    with open("txt files/enemy.txt", "r") as mimic:
        mimic = mimic.read().split("|")
    mimic = mimic[0].split("\n")

    for i in range(len(mimic)):
        if form in mimic[i]:
            mimic = mimic[i]
            break

    lines = mimic.split("/")

    if lines[2] == "none":
        type2 = ""
    else:
        type2 = lines[2] + " "

    mimic = Monster(lines[0], lines[1].split("-"), type2, lines[3], lines[4], lines[5], lines[6], lines[7],
                    lines[8], lines[9].split("-"), lines[10], lines[11])

    return mimic


def get_enemy(map_num):
    with open("txt files/enemy.txt", "r") as choose:
        lines = choose.read().split("|")
    lines.pop(0)

    for i in range(len(lines)):
        if str(map_num) == lines[i].split("\n")[0]:
            lines = lines[i]
            break

    lines = lines.split("\n")
    lines.pop(len(lines) - 1)
    lines.pop(len(lines) - 1)
    lines.pop(0)

    lines = random.choice(lines)

    lines = lines.split("/")

    if lines[2] == "none":
        type2 = ""
    else:
        type2 = lines[2] + " "

    monster = Monster(lines[0], lines[1].split("-"), type2, lines[3], lines[4], lines[5], lines[6], lines[7],
                      lines[8], lines[9].split("-"), lines[10], lines[11])

    return monster


def get_boss(map_num):
    with open("txt files/enemy.txt", "r") as choose:
        lines = choose.read().split("|")
    lines.pop(0)

    for i in range(len(lines)):
        if str(map_num) == lines[i].split("\n")[0]:
            lines = lines[i]
            print("Found BOSS")
            break

    lines = lines.split("\n")
    lines.pop(len(lines) - 1)
    lines.pop(0)

    lines = lines[len(lines) - 1]

    lines = lines.split("/")

    type2 = lines[2] + " "

    monster = Monster(lines[0], lines[1].split("-"), type2, lines[3], lines[4], lines[5], lines[6], lines[7],
                      lines[8], lines[9].split("-"), lines[10], lines[11])

    return monster


def mock_fight(enemy, player):
    # come back later
    player.reset_survive()
    print(f"{enemy.name} appears!")
    time.sleep(1)
    enemy.find_weakness()
    player.find_weakness()
    run = False
    skip = False
    turns = 0

    # Main loop
    while enemy.is_alive() and player.is_alive() and not run:
        turns += 1
        player.reset()
        player.inflict_status()
        if turns > 1:
            input(">")
        pyautogui.hotkey("shift", "c")
        # -- Visuals --
        enemy.show_health()

        print("\n\n")

        player.show_health()

        # -- Main Player Loop __
        while True:
            if skip:
                skip = False
                break
            if run:
                break
            print("[FIGHT]   [ACTION]\n[ITEM]    [SPELLS]")
            action = input()

            # -- Action Section --
            if action.upper() == "FIGHT" or action.upper() == "F":
                if player.get_moves(enemy) == "c":
                    break

            elif action.upper() == "ACTION" or action.upper() == "A":
                while True:
                    ans = input("[INFO]   [RUN]\n[BACK]    [DEFEND]\n")

                    if ans.upper() == "INFO" or ans.upper() == "I":
                        print(f"Name: {enemy.name} Health: {enemy.h}")
                        time.sleep(1)
                        skip = True
                        break

                    elif ans.upper() == "RUN" or ans.upper() == "R":
                        ran = random.randint(0, 100)

                        if ran <= player.dc:
                            run = True
                            print("You ran from the fight...")
                            time.sleep(1)
                            break
                        else:
                            print("You couldn't run from the fight!")
                            time.sleep(1)
                            skip = True
                            break

                    elif ans.upper() == "DEFEND" or ans.upper() == "D":
                        player.temp_d += 5
                        print(f"{player.name} defended!")
                        skip = True
                        break

                    elif ans.upper() == "BACK" or ans.upper() == "B":
                        break

                    else:
                        print("Please enter one of the choices.")

            elif action.upper() == "ITEM" or action.upper() == "I":
                if player.inventory_check_use() == "c":
                    break

            elif action.upper() == "SPELLS" or action.upper() == "S":
                if player.spells:
                    if player.show_spells(enemy) == "c":
                        break
                else:
                    print("You don't know any spells!")
                    time.sleep(1)

            # --COME BACK FOR SPELLS--
            else:
                print("Please enter one of the choices...")
                time.sleep(1)

        input(">")
        enemy.inflict_status()

        if enemy.is_alive() and not run:
            enemy.reset()
            ran = random.randint(1, 20)
            if ran < 18:
                enemy.enemy_move(player)
            elif ran < 19:
                print(f"{enemy.name} defended!")
                time.sleep(1)
                enemy.temp_d += 3
            else:
                enemy.heal(int((enemy.mh / 3)))
        elif not run:
            print(f"{player.name} defeated {enemy.name}!")
            player.will += int(enemy.gold * 2.5)
            player.inventory_add(enemy.give_item())
            if enemy.gold > 1:
                print(f"{player.name} got \033[93m{enemy.gold} gold\033[0m.")
                player.gold += enemy.gold


def get_loot(floor):
    return random.choice(loot[floor])


def rest_room(player):
    print("You found a place to rest...")
    time.sleep(1)
    player.heal(9999)
    # Save progress here


def chest_room(player, type_mim):
    print("You stumbled onto a \033[93mTreasure Room\033[0m!")
    time.sleep(2)
    print("There is a large \033[93mtreasure chest\033[0m in the center of the room.")
    time.sleep(2)
    while True:
        ask = input("Do you want to open the \033[93mchest\033[0m?\n")

        match ask.upper().split():
            case ["YES" | "Y"]:
                ran = random.randint(1, 100)

                if ran <= 20:
                    enemy = get_mimic("Chest Mimic")
                    mock_fight(enemy, player)
                    return
                else:
                    player.inventory_add(random.choice(r_loot))
                    return
            case ["NO" | "N"]:
                return

            case _:
                print("Please enter yes or no.")
                time.sleep(1)


def shop(player, floor):
    if floor == 2:
        use = shop_f2
    elif floor == 4:
        use = shop_f4
    else:
        use = None

    print("You found a \033[93mshop\033[0m!")
    time.sleep(1)

    if use:
        gold = player.gold
        while True:
            return
    else:
        print("Something went wrong, this shop doesn't exist...")
        time.sleep(1)