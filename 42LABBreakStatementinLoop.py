#guesing game using while loop, if statement and break statement
secret_word = "chupacabra"
user_word = input("Enter a word to to guess my secret word :")
while user_word != secret_word:
    user_word = input("Your are worng, guess again:")
    if user_word == secret_word:
        break
print(user_word,"You've successfully left the loop.")
