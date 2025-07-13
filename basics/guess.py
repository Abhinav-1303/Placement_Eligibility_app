secret_word = "lion"
guess = ""
guess_count = 0
guess_limit = 3
outofguess = False
while guess != secret_word and not(outofguess):
    if guess_count < guess_limit:
        guess = input ("Enter the guess: ")
        guess_count += 1
    else:
        outofguess = True
if outofguess:
    print("Out of guesses")
else:
    print("You Won!!")