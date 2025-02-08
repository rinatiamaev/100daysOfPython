import pandas

data = pandas.read_csv("alpha.txt")
# print(data)

format_data = {row.letter : row.code for index, row in data.iterrows() }
def gen_phonetic():
    word = input("type your word: ").upper()
    try:
        new_word = [format_data[letter] for letter in word]
    except KeyError:
        print("Just letter was accepted")
        gen_phonetic()
    else:
        print(new_word)

gen_phonetic()