# Author:Tony Quinn
# Date: 25-8-19
# Description: App that uses all of the material covered in the course, so far
# This code is hanging,  not working as it should.
# Stopped at the start of the FOR LOOP Tutorial(2:32)

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess:")
    guess_count  += 1
else:
    out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, You Lose")
else:
    print("You win")
