def translator(phrase):
    translation = "" 
    for letter in phrase: #loop through each letter
        if letter in "AEIOUaeiou": #if any letter is of the vowel
            if letter.isupper():
                translation = translation + "G" #that word will be converted to G, here each word is checked one by one.
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translator(input("Enter a phrase: ")))