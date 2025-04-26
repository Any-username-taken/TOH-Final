# TOH-Final

REQUIRED ADD-ONS: Pyautogui

REQUIRED KEYBINDS: shift + c (on clear console)

Path: Settings> Keymap> Other> Clear all

Please remember to remove any previous keybinds using shift + c. (Also trying to capitalize c without using caps lock will clear the screen instead.)

It is recommended to review tutorial before begining the game.

-Tutorial-

You will be able to move through rooms to fight enemies!
You will be marked with a * on the map
[ ]-[ ]-[*]-[ ]
  Player ^

You can move around the map with WASD.

Tiles you can move into:
[ ]-[N]-[P]

Tiles you can't move into:
[X]-[ ] (note: these are invisible barriers that require a key to pass through)

FIGHTS:

Battles will look similar to this:

Enemy (normal)
[//////]


KNIGHT Player (normal)
[///////////]
[FIGHT]    [ACTION]
[ITEM]     [SPELLS]

-The player can choose any option by either typing out the full name of the action, or the first letter.

Ex:

>f
Enter the number of the attack or back to exit.
Will: 100

slash Atk: 4 Cost: 3 [1]
bash Atk: 3 Cost: 1 [2]
stab Atk: 3-6 Cost: 5 [3]

-If they choose fight, the text above will appear.

Will is like action points used for basic moves. You can regain will by either defeating enemies, taking potions, or having certain status effects active.

MOVES:
The moves that the player has is determined by what weapon they have equipped. The information goes as follows:

Name Atk: Damage dealt to enemy (disregarding traits) Cost: Amount of will/mana taken [index + 1]

The player can enter one of two things here, either the Index of an attack, or back to return to the previous screen.
Entering back does not loose a turn.

[FIGHT]    [ACTION]
[ITEM]     [SPELLS]

>s

-Spells work the same way as regular moves, except using mana instead of will, and having the ability to learn new spells from items

[FIGHT]    [ACTION]
[ITEM]     [SPELLS]

>a

-Choosing action will send them to a different screen.
[INFO]    [RUN]
[BACK]    [DEFEND]

-INFO:
-Displays enemy name & enemy health as an integer
-Using this action does use a turn

-RUN:
-Successfuly running from a fight grants no rewards.
-Chances are based off of the player's dodge chance. Some classes have higher dodge chance than others.
-Failing to run results in turn being wasted

-DEFEND:
-Adds defense to player. Currently in a 'broken' state. Choosing this option results nothing, except the player's turn being wasted

[FIGHT]    [ACTION]
[ITEM]     [SPELLS]

>i

-Choosing items will show the player their inventory, unless there are 0 items in their inventory.

Old:
Please enter the number of the item or back to exit.

[1] Heath Potion [s] 

[2] Heath Potion [s] 

[3] Heath Potion [s] 

[4] Strength Potion [s]

[5] Health Potion [s]

New:
Please enter the number of the item or back to exit.
[1] Health Potion [s] 4x
[2] Strength Potion [s] 1x

-Note: List starts from 1 instead of 0

///

One last thing, when attempting to move on a seemingly empty tile, and it says you can't move there, you need to find the key for the barrier somewhere on the map.
