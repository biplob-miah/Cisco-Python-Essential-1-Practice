#where a function invokes/calls itself is called recursion
#we use recursive function to write clean, elegant and divide into smaller, organized chunks in python
#but recursive calls consume a lot of memory
def show(n):
    if n == 0: #base case
        return
    print(n)
    show(n -1) #recursion case
show(3)
