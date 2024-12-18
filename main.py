# Morse Code Converter | Houlaymatou B. | @code_techhb

# _______________________________Morse dictionary_________________________________________
from morse import morse_dict, logo
reversed_morse_dict = {value: key for key, value in morse_dict.items()}


# _______________________________Functions_________________________________________
def toMorse(plaintext):
    """Takes in one string argument. Convert plain text to Morse code and print result."""
    morseText = ""
    for letter in plaintext:
        if letter == " ":
            morseText += "/"
        else:
            morseText += morse_dict.get(letter.lower(), letter) + " "
    print(f"Morse Text: {morseText}")


def toPlaintext(morsetext):
    """Takes in one string argument. Converts plain text into Morse code and print result. Words are separated by
    '/'."""
    plainText = ""
    for word in morsetext.split("/"):
        for letter in word.split(" "):
            plainText += reversed_morse_dict.get(letter, letter)
        plainText += " "
    print(f"Plain Text: {plainText}")


#_______________________________Main code_________________________________________
print(logo)

while True:
    # Get user choice
    while True:
        try:
            direction = int(input("\nPress 1️⃣ for plain text to Morse or 2️⃣ for Morse to text: "))
            if direction not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("🚨 Invalid input! Please enter 1 or 2.")

    # Process the user choice
    if direction == 1:
        userText = input("\nEnter your plain text: ").strip()
        toMorse(userText)
    else:
        print("\n⚠️ Note: For correct conversion:")
        print("   - Letters must be separated by a single space.")
        print("   - Words must be separated by '/'.")
        morseCode = input("Enter your Morse code: ").strip()
        toPlaintext(morseCode)

    # should continue?
    go_again = input("\nWould you like to continue? Press Y for yes or any other key for No: ").lower()
    if go_again != "y":
        print("\nSee you next time - ... . . / -.-- --- ..- / -. . -..- - / - .. -- . 🤓")
        break
