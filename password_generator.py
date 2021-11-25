# Welcome to day 5 of the 100 days of code challenge. In this challenge I build
# a password generator, one that generates passwords based on a randomized
# number of characters that are determined by the user.

# Import all modules needed
import random

# Welcome Statement
print("Welcome to the password generator!\n")

# Input statements taken from the user for numbers of characters
letter_input = int(input("How many letters do you want to use in your password?\n"))
number_input = int(input("How many numbers do you want to use in your password?\n"))
symbol_input = int(input("How many symbols do you want to use in your password?\n"))

# List for each character type available for use in most passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Choosing a random set of characters based on the number input from the user
# and placing them into lists
choice_letters = random.choices(letters, k = letter_input)
choice_numbers = random.choices(numbers, k = number_input)
choice_symbols = random.choices(symbols, k = symbol_input)

# Concatenating the lists together
total_pass = choice_letters + choice_numbers + choice_symbols

# Randomizing the password
total_pass_random = random.sample(total_pass, len(total_pass))

# Looping through the list to turn it into a string. Other methods are known,
# however this is in line with what was learned in todays course.
pass_string = ''
for str in total_pass_random:
    pass_string += '' + str

# Print the password back to the user
print(f"Your new pass word is: {pass_string}")
