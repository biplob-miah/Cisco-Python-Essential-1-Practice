#if return appears in a program without expression it stops the function when it's conditions becomes true
#return without expression = stop button of function
def happy_new_year(wishes = True):
    print("Three")
    print("Two")
    print("One")
    if not wishes:
        return
    print("Happy new year")
happy_new_year(False)
def num(x= False):
    if not x: #if x = not false = true then return(stop) and don't print anything
        return
    print("Hi")
num()
