print("abc\ndef")
print("x\" y")

phrase = "Hello"
print(phrase + " world")


phrase = "Lion"
print(phrase.upper())
print(phrase.lower())

phrase = "tiger"
print(phrase.isupper())
print(phrase.islower())

phrase = "wolf"
print(phrase.upper().islower())
print(phrase.upper().isupper())

phrase = "Black"
print(len(phrase))
print(phrase[3])
print(phrase.index("a"))

phrase = "Steel Black"
print(phrase.replace("Black","White"))