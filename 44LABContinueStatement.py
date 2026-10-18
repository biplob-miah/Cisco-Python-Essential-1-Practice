#this is a pretty vowel eater game that concates the consonents from the word and vowel was eaten
user_word = input("Enter any word to play pretty vowel eater game :")
user_word = user_word.upper()
word_without_vowels = ""
for letter in user_word:
    if  letter == "A":
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
        word_without_vowels += letter

print(word_without_vowels)
