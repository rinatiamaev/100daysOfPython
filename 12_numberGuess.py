import random
logo = '''


          _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\                /::\    \                /::\    \                /::\    \        
       /::::\    \              /:::/    /               /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /:::/    /               /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \        /:::/    /               /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/    \:::\    \      /:::/    /               /::::\   \:::\    \       \:::\   \:::\    \       \:::\   \:::\    \   
  /:::/    / \:::\    \    /:::/    /      _____    /::::::\   \:::\    \    ___\:::\   \:::\    \    ___\:::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/____/      /\    \  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \  /\   \:::\   \:::\    \ 
/:::/____/  ___\:::|    ||:::|    /      /::\____\/:::/__\:::\   \:::\____\/::\   \:::\   \:::\____\/::\   \:::\   \:::\____\
\:::\    \ /\  /:::|____||:::|____\     /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /
 \:::\    /::\ \::/    /  \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/ 
  \:::\   \:::\ \/____/    \:::\    \ /:::/    /    \:::\   \:::\    \       \:::\   \:::\    \       \:::\   \:::\    \     
   \:::\   \:::\____\       \:::\    /:::/    /      \:::\   \:::\____\       \:::\   \:::\____\       \:::\   \:::\____\    
    \:::\  /:::/    /        \:::\__/:::/    /        \:::\   \::/    /        \:::\  /:::/    /        \:::\  /:::/    /    
     \:::\/:::/    /          \::::::::/    /          \:::\   \/____/          \:::\/:::/    /          \:::\/:::/    /     
      \::::::/    /            \::::::/    /            \:::\    \               \::::::/    /            \::::::/    /      
       \::::/    /              \::::/    /              \:::\____\               \::::/    /              \::::/    /       
        \::/____/                \::/____/                \::/    /                \::/    /                \::/    /        
                                  ~~                       \/____/                  \/____/                  \/____/         
                                                                                                                             

'''
print(logo)
print("Walcome to Number Guess game!")
random_nb = random.randint(0, 101)
while True:
    user_in = input("Select game difficult (1 - Easy, 2 - Medium, 3 - Hard): ")
    if user_in.isnumeric() and int(user_in) in {1, 2, 3}:
        user_in = int(user_in)
        break
    else:
        print("Invalid input")
if user_in == 1:
    lives = 11
elif user_in == 2:
    lives = 8
elif user_in == 3:
    lives = 5

print(random_nb)
while lives > 0:
    user_guess = input("You select Easy game: Please guess a number from 0 to 100: ")
    user_guess_nb = int(user_guess)
    if user_guess_nb > random_nb:
        print("Too big")
        lives -= 1
        if lives != 0:
            print(f"You have {lives} lives")
    elif user_guess_nb < random_nb:
        print("Too low")
        lives -= 1
        if lives != 0:
            print(f"You have {lives} lives")
    elif user_guess_nb == random_nb:
        print("You are right, WIN!")
        break
if lives == 0:
    print("You are lose :(")
