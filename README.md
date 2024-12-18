# ⚞ Text Morse Converter ⚟

Welcome to the **Text Morse Converter** repo! This project allows you to convert plain text to Morse code and vice 
versa. It is a simple command-line tool that takes user input, converts it between two formats, and handles different edge cases.

## Features ✨

- Convert **plain text to Morse code**.
- Convert **Morse code to plain text**.
- Supports **letters**, **numbers**, and **punctuation**.
- Preserves characters like **emojis** and other symbols.
- Includes **error handling** to ensure robust input validation.


## Key Concepts Practiced 👩🏽‍💻

- **Error Handling**: The program uses `try` and `except` blocks to handle errors such as invalid input (non-numeric input when selecting the conversion type).
  
- **Docstrings**: Clear and concise docstrings explain the purpose of functions and parameters, ensuring that the code is understandable for anyone who reads it.
  
- **Modular Program**: Functions like `toMorse()` and `toPlaintext()` handle specific tasks, promoting reusability and 
  separation of concerns.

## How It Works 🛠️

The program operates through a simple interface where the user can select the type of conversion they would like:

1. **Plain Text to Morse Code**: The program takes user input (plain text), and converts each character into its Morse code equivalent.
2. **Morse Code to Plain Text**: The program takes Morse code input, converts each Morse character back into the corresponding plain text character.

#### Example 🤓

- **Plain text to Morse**:
  - Input: `Thank you for visiting my repo!`
  - Output: `- .... .- -. -.- /-.-- --- ..- /..-. --- .-. /...- .. ... .. - .. -. --. /-- -.-- /.-. . .--. --- -.-.--`

- **Morse to Plain text**:
  - Input: `.. /.-- . .-.. -.-. --- -- . /-.-- --- ..- .-. /..-. . . -.. -... .- -.-. -.- /.- -. -.. /... ..- --. --. . ... - .. --- -. ... /- --- /.. -- .--. .-. --- ...- . /-- -.-- /-.-. --- -.. . -.-.-- `
  - Output: `i welcome your feedback and suggestions to improve my code!`

## Files in the Project

- **`main.py`**: The main Python script that contains the logic for both conversions (plain text to Morse and vice versa).
- **`morse.py`**: A separate file containing the logo displayed when the program starts and the dictionary that maps 
  letters, numbers, and punctuation to their corresponding Morse code equivalents.


