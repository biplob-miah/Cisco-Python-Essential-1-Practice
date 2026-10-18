#this program eats vowel in user word using for loop and continue, if-elif-else statement
user_word = input("Enter a word to play the vowel eater game :")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
    
