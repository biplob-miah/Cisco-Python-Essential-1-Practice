#this program shows how to make our work easy using functions
#first of all we create functions then we call the function and then the code
#in a function works
print("Hi")
def user_input(): #we don't need to keep functions always at the top of our code
    print("Enter a value :")
user_input() #calling functions
a = int(input())
user_input()
b = int(input())
user_input()
c= int(input())

#creating functions with parameter and arguments

def hello(name):
    print("Hello", name)
name = input("Enter your name :")
hello(name)
