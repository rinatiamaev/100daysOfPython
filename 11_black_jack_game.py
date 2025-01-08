import random

import random

def draw_card(value, suit):
    """Рисует одну карту в ASCII-арте"""
    card = f"""
    +-------+
|   {value: <2}  |
|       |
|   {suit}   |
|       |
|  {value: >2}   |
+-------+
    """
    return card.strip().split('\n')

# Список мастей
suits = ["♠", "♣", "♦", "♥"]

# Список значений карт
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

cost = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

random_valueComp = random.sample(values, 2)
random_suitComp = random.sample(suits, 2)
costComp = [cost[values.index(value)] for value in random_valueComp]

card1comp = draw_card(random_valueComp[0], random_suitComp[0])
card2comp = draw_card(random_valueComp[1], random_suitComp[1])

# Случайный выбор карт для игрока
random_valuePlayer = random.sample(values, 2)
random_suitPlayer = random.sample(suits, 2)
costPlayer = [cost[values.index(value)] for value in random_valuePlayer]

# Отображение карт игрока
print(f"Your cards: {random_valuePlayer[0]} {random_suitPlayer[0]} cost: {costPlayer[0]} and {random_valuePlayer[1]} {random_suitPlayer[1]} cost: {costPlayer[1]}")

# Рисуем карты игрока
card1 = draw_card(random_valuePlayer[0], random_suitPlayer[0])
card2 = draw_card(random_valuePlayer[1], random_suitPlayer[1])
for line1, line2 in zip(card1, card2):
    print(f"{line1}    {line2}")

player_res = costPlayer[0] + costPlayer[1]
comp_res = costComp[0] + costComp[1]

take_more = True

while take_more:
    more = input("Do you want take more card? Type y/n: ").lower()
    if more == "y":
        
        random_valuePlayerNext = random.choice(values)
        random_suitPlayerNext = random.choice(suits)
        costPlayerNext = cost[values.index(random_valuePlayerNext)]
        cardNext = draw_card(random_valuePlayerNext, random_suitPlayerNext)
        for line1, line2, line3 in zip(card1, card2, cardNext):
            print(f"{line1}    {line2}    {line3}")
        player_res += costPlayerNext
        take_more = False
if (player_res > comp_res and player_res < 22) or (player_res < 22 and comp_res > 21) :
    for line1, line2 in zip(card1comp, card2comp):
        print(f"{line1}    {line2}")
    print(f"Player res: {player_res}, Comp res: {comp_res}. Player Win!")
elif (comp_res > player_res and comp_res < 22) or (comp_res < 22 and player_res > 21):
    for line1, line2 in zip(card1comp, card2comp):
        print(f"{line1}    {line2}")
    print(f"Player res: {player_res}, Comp res: {comp_res}. Comp Win!")
else:
    for line1, line2 in zip(card1comp, card2comp):
        print(f"{line1}    {line2}")
    print(f"Player res: {player_res}, Comp res: {comp_res}. Tie!")


# Вывод карт для каждой масти и значения
# for value, suit in cards:
#     print(draw_card(value, suit))

print()
