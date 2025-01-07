alphabet = list('abcdefghijklmnopqrstuvwxyz')
a = True
def encryprt(text, shift):
    cipher_text = ""
    shift %= len(alphabet)
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index_char = (alphabet.index(char) + shift) % len(alphabet)
            new_char = alphabet[index_char]
            cipher_text += new_char.upper() if is_upper else new_char
        else:
            cipher_text += char
    print(f"encrypted text: {cipher_text}")
def decryprt(text, shift):
    cipher_text = ""
    shift %= len(alphabet)
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index_char = (alphabet.index(char) - shift) % len(alphabet)
            new_char = alphabet[index_char]
            cipher_text += new_char.upper() if is_upper else new_char
        else:
            cipher_text += char
    print(f"decrypted text: {cipher_text}")




while a == True:
    direction = input("Type 'encrypt' if you want encrypt message, and 'decrypt' if want to decrypt\n").lower()
    cipher = int(input("type number to encoding/decoding: "))
    if direction == "encrypt":
        text_input = input("Type text what you want encrypt: ")
        encryprt(text_input, cipher)
        again = input("Do you want go again? Type (y/n): ")
        

    else:
        text_input = input("Type text what you want decrypt: ")
        decryprt(text_input, cipher)
        again = input("Do you want go again? Type (y/n): ")
    if again.lower() != "y":
        a = False
