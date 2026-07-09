# Random Password Generator

## Description
This is a Python-based Random Password Generator that creates secure passwords based on the user's selected password type and desired length. The user selects any two password categories, and the program generates a random password using the combined character set.

## Features
- Generates random passwords of user-defined length.
- Allows users to choose any two password categories:
  - Alphabetic Password
  - Numeric Password
  - Alphanumeric Password
  - Alphanumeric Password with Special Characters
- Enforces a minimum password length of 8 characters.
- Validates user input.
- Handles invalid input using exception handling.
- Rejects invalid menu choices.
- Allows users to generate another password without restarting the program.

## Inputs
The program takes the following inputs from the user:
- Password Length (minimum 8 characters)
- First Character Set Category (1–4)
- Second Character set Category (1–4)

### Password Categories
1. Alphabetic Password
2. Numeric Password
3. Alphanumeric Password
4. Alphanumeric Password with Special Characters

## Output
The program displays:
- A randomly generated password based on the selected categories.

## Technologies Used
- Python 3
- random module
- string module

## How to Run
1. Run the Python file.
2. Enter the desired password length (minimum 8).
3. Select any two password categories from the menu.
4. The program generates a password using the selected character sets.
5. Choose whether to generate another password or exit.

## Example

Input:

Password Length: 12

First Choice: 1

Second Choice: 4

Output:

Generated Password: Ab@9Xk!Lm2Qr