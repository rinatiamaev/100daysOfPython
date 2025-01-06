import random
hangman_stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ==========
    """,  # 0 live
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    ==========
    """,  # 1 live
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |
    ==========
    """,  # 2 lives
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |
    ==========
    """,  # 3 lives
    """
     ------
     |    |
     |    O
     |    |
     |    
     |
    ==========
    """,  # 4 lives
    """
     ------
     |    |
     |    
     |    
     |    
     |
    ==========
    """  # 5 lives
]


words = ["hello", "mouse", "banana", "super", "good", "debagging", "hive"]
print("Welcome to hungman game!")
game_word = random.choice(words)

game_word_len = len(game_word)
word_to_char = list(game_word)
word_display = ["_"] * game_word_len

lives = 5
while lives > 0:
    print(hangman_stages[lives])
    print(word_display)
    char_guess = input("guess a letter: ").lower()
    if char_guess in word_to_char:
        for index, char in enumerate(word_to_char):
            if char_guess == char:
                word_display[index] = char
                
        if '_' not in word_display:
            print(word_display)
            print("You are win!")
            break
    else:
        lives -= 1
if lives == 0:
    print(hangman_stages[0])  
    print(f"Game over! Word was: {game_word}")
    






