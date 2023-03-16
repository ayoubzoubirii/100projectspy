print(f'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print(f'''Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go? Type "left" or "right"''')
l_or_r = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
if l_or_r == "left" : 
    swim_or_wait = input(f''' You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.''')
    if swim_or_wait == "wait" : 
       colr = input(f''' You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ''')
       if colr == "yellow" : 
           print("You found the treasure! You Win!")
       elif colr == "red" : 
           print("Game overright")
       elif colr == "bleu" : 
           print("Game over")
    elif swim_or_wait == "swim" : 
           print("Game over")
elif l_or_r == "right" : 
           print("You fell into a hole. Game Over.")
