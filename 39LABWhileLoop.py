#guessing game using while loop
secret_number = 10
number = int(input("Welcome to the Game! Guess what number I have picked for you:"))
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number =int(input("Enter the number again"))
print("Well done, muggle! You are free now.")
    
    
