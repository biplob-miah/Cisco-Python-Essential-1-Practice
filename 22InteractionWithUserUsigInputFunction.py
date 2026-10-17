#program of getting user input and printing it on the screen
''' print("Tell me anything")
anything = input()
print("Hmm...",anything,"...Really?") '''

#program of getting user input smartly
'''
anything = input("Tell me your about yourself.")
print("Wow, you said",anything, "That's really impressive.")
'''
#program of calculation of square, root and cube of a number from user input using type casting or type conversion

'''x=float(input("Enter the number :"))
square=x**2.0
root=x**0.5
cube=x**3.0
print(x,"'s square is" ,square, "|", x,'s root is', root, "|", x,'s cube is', cube)
'''
'''
#example of user typed conversion into int then powered by float results float value
x=int(input("Enter any number :"))
square=x**2.0
print(x,"'s square is :",square)
'''

#program for calculation of a hypo using only print function

first_l=float(input("Enter the first length :"))
second_l=float(input("Enter the second length :"))
print(first_l, "and", second_l,'s Hypo length is', round((first_l**2+second_l**2)**0.5, 2))
