from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(text, shift, operation):
    result = ""
    for letter in text:
        if letter not in alphabet:
            result += letter
            continue
        elif operation == 'encode':
            index_in_alphabet_shifted = alphabet.index(letter) + shift
        elif operation == 'decode':
            index_in_alphabet_shifted = alphabet.index(letter) - shift
        index_in_alphabet_shifted %= 26
        result += alphabet[index_in_alphabet_shifted]
    print(f"The {operation}d text is {result}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, operation=direction)
    wantToContinueGame = input("Type 'yes' if you want to go again. Otherwise type 'No' \n").lower()
    if wantToContinueGame == 'no':
        print("Good Bye")
        break
    elif wantToContinueGame == 'yes':
        caesar(text=text, shift=shift, operation=direction)
