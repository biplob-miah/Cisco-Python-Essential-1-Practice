#this program reads two integer, compares them and finds which is the larger
''' num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
if num1>num2:
    print(num1, "is large number")
else:
    print(num2, "is large number") '''

#this program reads three integer, compares them and finds which is the larger
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))

large_num = num1

if num2>large_num:
    large_num = num2
    
if num3>large_num:
    large_num= num3
    
print(large_num, "is large number")
