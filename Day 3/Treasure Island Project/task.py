import sys

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_action = input("Do you want to go to the left, or to the right?")
if first_action.lower() != "left":
    print("You fall into a hole. Game Over")
    sys.exit()

print("You've chosen the correct path.")
second_action = input("Now do you want to swim, or wait?")
if second_action.lower() != "wait":
    print("You are attacked by trout. Game Over")
    sys.exit()

print("Your action was correct.")
color_of_door = input("Now you have to choose which door you want to enter: red, yellow or blue")
if color_of_door.lower() == "red":
    print("You were burned by fire. Game Over")
    sys.exit()
elif color_of_door.lower() == "blue":
    print("You were eaten by beasts. Game over")
    sys.exit()
elif color_of_door.lower() == "yellow":
    print("You win!")
    sys.exit()
else:
    print("Game Over")
    sys.exit()

