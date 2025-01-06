import random
print("Welcome to stone, paperm siccors game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock:", rock)
print("Paper:", paper)
print("Scissors:", scissors)

while True:
    player_choice = int(input("Please choose 0 for ROCK, 1 for PAPER, 2 for SCISSORS: "))
    comp_choice = random.randint(0, 2)

    if player_choice == 0:
        print("Player: ", rock)
    if player_choice == 1:
        print("Player: ", paper)
    if player_choice == 2:
        print("Player: ", scissors)
    if comp_choice == 0:
        print("COMPUTER: ", rock)
    if comp_choice == 1:
        print("COMPUTER: ", paper)
    if comp_choice == 2:
        print("COMPUTER: ", scissors)
    if player_choice == 0 and comp_choice == 0:
        print("TIE!")
    if player_choice == 1 and comp_choice == 1:
        print("TIE!")
    if player_choice == 2 and comp_choice == 2:
        print("TIE!")
    if player_choice == 0 and comp_choice == 1:
        print("COMPUTER WIN")
    if player_choice == 0 and comp_choice == 2:
        print("Player WIN")
    if player_choice == 1 and comp_choice == 0:
        print("Player WIN")
    if player_choice == 1 and comp_choice == 2:
        print("COMPUTER WIN")
    if player_choice == 2 and comp_choice == 0:
        print("COMPUTER WIN")
    if player_choice == 2 and comp_choice == 1:
        print("Player WIN")
    again = input("Do you want play again (y/n): ")
    if again != "y":
        print("Thank you for playing, BYE!")
        break