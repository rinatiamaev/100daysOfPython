import lower_higher_logo
import lower_higher_data
import random
lower_higher_logo.higher_lower_logo()
wrong = True
counter = 0
while wrong:
    first = random.choice(lower_higher_data.data)
    second = random.choice(lower_higher_data.data)
    if counter > 0:
        print(f"You are right, current score is {counter}")
    print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}\n")
    lower_higher_logo.versus()
    print(f"Compare B: {second['name']}, {second['description']}, from {second['country']}\n")
    user_in = input("Who has more followers in Instagram? Type A or B: ").upper()
    if first['follower_count'] > second['follower_count'] and user_in == 'A':
        counter += 1
    elif first['follower_count'] < second['follower_count'] and user_in == 'B':
        counter += 1
    else:
        wrong = False
        print(f"You are wrong, your score is {counter}. GAME OVER")