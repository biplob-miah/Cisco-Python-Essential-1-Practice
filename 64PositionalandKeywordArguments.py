#if the arguments of parameters setted inside the function call is called keyword arg passing
#like intro (first_name = "Rahim", last_name = "Miah") is called keyword passing
#use positional arguments then the keyword arguments

def adding(a,b,c):
    print(a, "+", b,  "+", c, "=", a+b+c)
adding(1,2,3) #pure argument passing example


adding(c=3, b=9, a=7) #we are using a, b, c as pure keyword to call the function

adding(7, c=3, b=9) #using positinal argument passing and keyword arguments mixed
