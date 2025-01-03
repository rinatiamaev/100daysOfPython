import sys
import winsound
def treasure_chest():
    art = """
       ______
      /      \\
     /        \\
    /__________\\
    ||--------||
    ||  GOLD  ||
    ||________||
    ||--------||
    ||________||
    ||        ||
    ||________||
    """
    print(art)

treasure_chest()

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
crossroad1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ")
if crossroad1 == 'right':
    print("NOOOOO! Fall into a hole!!!\nGame Over.")
    sys.exit()
else:
    print("You have reached a river. What are you going to do?\nSwim or wait?: ")
    crossroad2 = input("Type 'swim' or 'wait': ")
    if crossroad2 == 'swim':
        print("You are attacked by a trout. Game Over.")
        sys.exit()
    else:
        print("You have arrived at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich color do you choose?")
        crossroad3 = input("Type 'red', 'yellow' or 'green': ")
        if crossroad3 == 'red':
            print("Burned by fire. Game Over.")
            sys.exit()
        elif crossroad3 == 'green':
            print("You found the treasure! You win!")
            winsound.Beep(1000, 500)
            sys.exit()
        else:
            print("Eaten by beasts. Game Over.")
            sys.exit()