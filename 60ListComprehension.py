#we can create new list from a list easily and shortly without so many code
num =[4,3,5,6,34,65]
new_num = [n*n for n in num]
print(new_num)

#we can use if else in list comprehension also
num =[4,3,5,6,34,65]
even_check = [n for n in num if n % 2 == 0 ]
odd_check = [n for n in num if n % 2 != 0 ]
print("Even num :",even_check)
print("Odd num :", odd_check)

#if else

num =[4,3,5,6,34,65]
result = [n if n>3 else 0 for n in num]
print("Using else :", result)
