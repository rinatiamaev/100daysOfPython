import pandas

data_alpha = pandas.read_csv("alpha.csv")



format_data_alpha = {row.letter:row.code for (index, row) in data_alpha.iterrows()}
# print(format_data_alpha)

word = input("Enter your word: ").upper()

splitted_word = [format_data_alpha[letter] for letter in word]
print(splitted_word)
