#this program shows how a functions can be parameterized with it's argument
def intro(first_name, last_name = "Smith"):
    print("Hello, my name is :", first_name, last_name)
intro("Biplob", "Miah")#if i didn't put my last name here our predefined last name Smith would print here
intro("Biplob")
