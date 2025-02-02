import pandas

data = pandas.read_csv("alpha.txt")
# print(data)

format_data = {row.letter : row.code for index, row in data.iterrows() }

word = input("type your word: ").upper()

new_word = [format_data[letter] for letter in word]

print(new_word)
