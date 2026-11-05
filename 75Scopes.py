#this program shows the local scope(function scope)
#when a variable created inside a function it's called local scope
def student():
    name = "Karim"
    print(name)
student()
#we can not call a varibale which going outside of a function when variable is inside in a function
def student_two():
    name = "Rahim"
student_two()
print(name) #called the variable going outside of the function so python won't find so raises nameerro

#Global scope
name = "Foden" #a variable outside a function is called global variable
def student_three():
    print(name) #we can call the variable inside a functin
student_three()
print(name) #also going outside of a function

#if we want to change the value of a global var using the local var condition
#we should use global keyword
x = 10
def change():
    global x #local var x =20 er maddhome global keyword use kore global var x= 10 k change kore x = 30 kora hoyeche
    x = 30
change()
print(x)

