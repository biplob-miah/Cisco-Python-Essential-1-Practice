#this program shows how return gives value to the function and we can reuse it by assigining it in a new variable
#we can ignore the return value as well but our result will be lost

def boring_function():
    return 123
x = boring_function()
print("The boring function has returned ", x)
