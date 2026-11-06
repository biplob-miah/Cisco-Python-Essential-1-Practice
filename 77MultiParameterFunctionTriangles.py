#this program checks three sides of given lengths can build a triangle or not

def is_a_triangle(a,b,c):
    #first two sides should be greater than third side
    return a + b <= c and b + c <= a and c + a <= b #if we don't wanna use if we can then use return

def is_a_right_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    if c > a and c> b:
        return c **2 == a**2 + b**2 #pythagorean theorem
    if a> b and a >c :
        return a **2 == b**2 + c **2

    
print(is_a_right_triangle(5,3,4))
print(is_a_triangle(1,3,4))



