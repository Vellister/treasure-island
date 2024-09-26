print('''
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
print("Your mission is to find the Golden Monkey before kobolds or Rafaam find it first.")
direction = input("You're at a cross road. There is dim light. Where do you want to go? \n Type \"left\" or \"right\". \n ") #We can put the lower() function after the ")" so any input will be recognised as lower caps.
if direction == "left" or direction == "Left" or direction == "LEFT":
        swim_or_not = input("It seems you took the right path. You've come to a "
                            "lake full of gems and candles around it. There is a mysterious island in the middle of the lake. \n Type \"wait\" to wait for a boat. Type \"swim\" to swim across \n ")
        if swim_or_not == "wait" or swim_or_not == "Wait" or swim_or_not == "WAIT":
            chest = input("Good for you, you waited the boat. It is strange.. there is no boatman.. You arrive at the island unharmed. There are 3 treasure chests. \n The first one is red, covered by gems, \n emeralds and other precious ores. \n The second is yellow, covered in wax from the candles around it \n and the third one is blue with a strange ooze and stench. \n  Which treasure chest do you choose? \n ")
            if chest == "yellow" or chest == "Yellow" or chest == "YELLOW":
                print("You found the Golden Monkey! All your cards in your Hearthstone deck, that your grandpa gave you, are LEGENDARY! You win!")
            elif chest == "Red" or chest == "RED" or chest == "red":
                print("Wait.. You have unleashed the Memory of the Firelord. You have been purged by Firelord Ragnaros. Game Over.")
            elif chest == "Blue" or chest == "BLUE" or chest == "blue":
                print("A strange shadow attacked you and trapped your soul. Game Over.")
            else:
                print("The Rafaam using the kobolds, stole your treasure. Game over.")
        else:
            print("You have been attacked by angry Gorlocks. Game Over.")
else:
    print("You have been caught in the sticky webs of the nerubians. Game over.")

    
