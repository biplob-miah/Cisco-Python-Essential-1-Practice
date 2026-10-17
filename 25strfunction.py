#this program converts string to number using str() function

a= float(input("Enter the first length :"))
b= float(input("Enter the second length :"))
print("The Hypo is " +str(round((a**2+b**2)**0.5, 2)))
